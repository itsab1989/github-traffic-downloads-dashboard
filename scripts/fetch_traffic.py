#!/usr/bin/env python3
"""
Fetch GitHub traffic + release-download data and write traffic_data.json.

This replaces the ~250-line bash+jq fetch step that used to live inline in the
workflow. It produces a traffic_data.json with exactly the structure
merge_history.py expects, so the rest of the pipeline is unchanged.

Why Python: the bash step was the only untested stage and the most failure-prone
(network, pagination, asset classification). The pure data-shaping here is unit
tested (test_fetch_traffic.py), and the asset matching lives in classify.py.

Repositories are read from a single source - repos.txt at the repo root (one
"owner/name" per line; blank lines and #comments ignored) - or from argv after
the output path. Auth + API config come from the environment:
  TRAFFIC_ACTION_TOKEN  (required)  - token with 'repo' scope
  GITHUB_API_BASE_URL   (optional)  - default https://api.github.com
  GITHUB_API_VERSION    (optional)  - default 2022-11-28

GitHub's traffic API returns the last 14 days; release download_count is a
cumulative all-time counter (snapshotted here, diffed later by merge_history).

Usage:
    python scripts/fetch_traffic.py [output_path] [owner/repo ...]

Error codes (kept from the original step):
  TF001 clones  TF002 views  TF003 referrers  TF004 releases
  JV001-004     invalid JSON for the above
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

# scripts/ on path so this works whether run as a script or imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify import classify_platform, classify_arch  # noqa: E402

DEFAULT_OUTPUT = "traffic_data.json"
REPOS_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "repos.txt")
API_BASE = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
API_VERSION = os.environ.get("GITHUB_API_VERSION", "2022-11-28")
# App-download categories. 'homebrew' is the copy of a Mac DMG a Homebrew cask
# downloads (classify.py); it is never counted again under 'macos'.
PLATFORMS = ["windows", "macos", "linux", "homebrew"]
# Release channels: GitHub's own pre-release flag decides. Betas are mostly
# testers, so the dashboard keeps them apart from stable releases.
CHANNELS = ["stable", "beta"]

# Only releases whose tag looks like a version number count toward download
# statistics: "v1.2.3", "1.0", "v3.14.8-beta.221", "2.0-rc1", ... Tracked repos
# sometimes carry ad-hoc releases used purely to share files (design mockups,
# test data, screenshots); their asset fetches would otherwise inflate the
# download totals. Draft releases are excluded for the same reason.
RELEASE_TAG_PATTERN = re.compile(r"^v?\d+(\.\d+)*([-+.].*)?$")


class FetchError(Exception):
    """Raised with a stable error code so the workflow log stays diagnosable."""
    def __init__(self, code, message):
        super().__init__(f"ERROR_CODE: {code} - {message}")


def _utc_now_iso():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def _utc_today():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d')


# --------------------------------------------------------------------------- #
# Pure data shaping (unit tested) - no network here.
# --------------------------------------------------------------------------- #

def build_daily_data(clones, views):
    """
    Merge clones and views arrays (GitHub traffic API shape) into daily entries.

    Each clone/view item looks like {"timestamp": "2026-05-25T00:00:00Z",
    "count": N, "uniques": M}. Output entries are keyed by the YYYY-MM-DD date
    with clones_total/clones_unique/views_total/views_unique, date-sorted.
    """
    by_date = {}
    for c in clones or []:
        ts = (c.get('timestamp') or '')[:10]
        if not ts:
            continue
        e = by_date.setdefault(ts, {})
        e['clones_total'] = c.get('count', 0)
        e['clones_unique'] = c.get('uniques', 0)
    for v in views or []:
        ts = (v.get('timestamp') or '')[:10]
        if not ts:
            continue
        e = by_date.setdefault(ts, {})
        e['views_total'] = v.get('count', 0)
        e['views_unique'] = v.get('uniques', 0)
    out = []
    for date in sorted(by_date):
        e = by_date[date]
        out.append({
            'date': date,
            'clones_total': e.get('clones_total', 0),
            'clones_unique': e.get('clones_unique', 0),
            'views_total': e.get('views_total', 0),
            'views_unique': e.get('views_unique', 0),
        })
    return out


def is_countable_release(release):
    """True if the release is a real, published release (version-like tag, not a draft)."""
    if release.get('draft'):
        return False
    return bool(RELEASE_TAG_PATTERN.match(release.get('tag_name') or ''))


def filter_releases(releases):
    """Drop drafts and file-sharing pseudo-releases (non-version tags) from the list."""
    return [r for r in releases or [] if is_countable_release(r)]


def release_channel(release):
    """'beta' for a GitHub pre-release, 'stable' otherwise."""
    return 'beta' if release.get('prerelease') else 'stable'


def aggregate_release(release):
    """
    Per-release lifetime totals split by platform (matching the by_release shape).

    'downloads' counts APP downloads only: assets matched to a platform or to
    Homebrew. Anything else (demo projects, screenshots, checksums, icons) goes
    to 'other', so a demo ZIP never reads as somebody installing the app.
    """
    counts = {'downloads': 0, 'other': 0}
    counts.update({p: 0 for p in PLATFORMS})
    for asset in release.get('assets') or []:
        dc = asset.get('download_count', 0) or 0
        platform = classify_platform(asset.get('name'))
        if platform:
            counts[platform] += dc
            counts['downloads'] += dc
        else:
            counts['other'] += dc
    row = {'tag': release.get('tag_name', ''), 'downloads': counts['downloads']}
    for p in PLATFORMS:
        row[p] = counts[p]
    row['other'] = counts['other']
    row['prerelease'] = bool(release.get('prerelease'))
    row['published_at'] = release.get('published_at')
    return row


def aggregate_downloads(releases):
    """
    Aggregate all releases into cumulative totals, per-release, and per-arch.

    'cumulative_total' counts app downloads only (the platform buckets plus
    Homebrew); assets that match no platform are summed in 'cumulative_other'.
    'cumulative_stable_<key>' and 'cumulative_beta_<key>' split the same totals
    by release channel (GitHub's pre-release flag).

    Drafts and non-version tags are dropped first (see filter_releases), and
    releases sharing a tag (e.g. a re-created release whose failed first attempt
    left an asset-less duplicate) are merged into a single by_release row.
    """
    keys = ['total'] + PLATFORMS
    cumulative = {k: 0 for k in keys + ['other']}
    channel = {c: {k: 0 for k in keys} for c in CHANNELS}
    by_arch = {p: {} for p in PLATFORMS}
    by_release = []
    by_tag = {}
    for release in filter_releases(releases):
        rel = aggregate_release(release)
        merged = by_tag.get(rel['tag'])
        if merged:
            merged['downloads'] += rel['downloads']
            merged['other'] += rel['other']
            for p in PLATFORMS:
                merged[p] += rel[p]
            # ISO timestamps compare lexicographically; keep the earliest publish
            if rel['published_at'] and (not merged['published_at']
                                        or rel['published_at'] < merged['published_at']):
                merged['published_at'] = rel['published_at']
        else:
            by_tag[rel['tag']] = rel
            by_release.append(rel)
        cumulative['total'] += rel['downloads']
        cumulative['other'] += rel['other']
        ch = channel[release_channel(release)]
        ch['total'] += rel['downloads']
        for p in PLATFORMS:
            cumulative[p] += rel[p]
            ch[p] += rel[p]
        for asset in release.get('assets') or []:
            platform = classify_platform(asset.get('name'))
            if not platform:
                continue
            arch = classify_arch(asset.get('name'))
            dc = asset.get('download_count', 0) or 0
            by_arch[platform][arch] = by_arch[platform].get(arch, 0) + dc
    out = {f'cumulative_{k}': cumulative[k] for k in keys + ['other']}
    for c in CHANNELS:
        for k in keys:
            out[f'cumulative_{c}_{k}'] = channel[c][k]
    out['by_release'] = by_release
    out['by_arch'] = by_arch
    return out


def build_window_totals(clones_raw, views_raw, today):
    """
    The traffic API's own 14-day totals, as one dated snapshot.

    Next to the per-day arrays, /traffic/clones and /traffic/views return
    'count' and 'uniques' for the whole 14-day window. That 'uniques' is the
    number of distinct cloners (or visitors) over the 14 days, which summing
    the per-day uniques cannot give: one person on five days counts once here
    and five times in the sum.
    """
    clones_raw = clones_raw or {}
    views_raw = views_raw or {}
    return {
        'date': today,
        'clones_14d': int(clones_raw.get('count', 0) or 0),
        'clones_unique_14d': int(clones_raw.get('uniques', 0) or 0),
        'views_14d': int(views_raw.get('count', 0) or 0),
        'views_unique_14d': int(views_raw.get('uniques', 0) or 0),
    }


def build_repo_payload(clones, views, referrers, releases, fetch_date=None, today=None,
                       clones_raw=None, views_raw=None):
    """Assemble the per-repository object stored under repositories[repo]."""
    fetch_date = fetch_date or _utc_now_iso()
    today = today or _utc_today()
    daily = build_daily_data(clones, views)
    downloads = aggregate_downloads(releases)
    downloads.update({'date': today, 'last_fetched': fetch_date})
    return {
        'window_14d': build_window_totals(clones_raw, views_raw, today),
        'daily_data': daily,
        'referrers': referrers or [],
        'metadata': {
            'last_fetched': fetch_date,
            'clones_total': sum(d['clones_total'] for d in daily),
            'clones_unique_total': sum(d['clones_unique'] for d in daily),
            'views_total': sum(d['views_total'] for d in daily),
            'views_unique_total': sum(d['views_unique'] for d in daily),
        },
        'downloads': downloads,
    }


def build_traffic_data(repos_raw, generated_at=None, fetch_errors=None):
    """
    Build the full traffic_data.json structure from raw per-repo API responses.

    Args:
        repos_raw: ordered list of (repo_name, {clones, views, referrers, releases})
        generated_at: optional timestamp; defaults to now (UTC)

    Returns:
        {'metadata': {generated_at, repositories: [...]}, 'repositories': {...}}
    """
    generated_at = generated_at or _utc_now_iso()
    fetch_date = _utc_now_iso()
    today = _utc_today()
    repositories = {}
    order = []
    for repo, raw in repos_raw:
        repositories[repo] = build_repo_payload(
            raw.get('clones', {}).get('clones', []),
            raw.get('views', {}).get('views', []),
            raw.get('referrers', []),
            raw.get('releases', []),
            fetch_date=fetch_date, today=today,
            clones_raw=raw.get('clones', {}), views_raw=raw.get('views', {}),
        )
        order.append(repo)
    metadata = {'generated_at': generated_at, 'repositories': order}
    if fetch_errors:
        metadata['fetch_errors'] = dict(fetch_errors)
    return {'metadata': metadata, 'repositories': repositories}


# --------------------------------------------------------------------------- #
# Network layer.
# --------------------------------------------------------------------------- #

def http_get_json(url, token, fetch_code, validate_code, expect_array=False):
    """GET a URL and parse JSON, raising FetchError with stable codes on failure."""
    req = urllib.request.Request(url, headers={
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {token}',
        'X-GitHub-Api-Version': API_VERSION,
        'User-Agent': 'github-traffic-dashboard',
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            body = resp.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        raise FetchError(fetch_code, f"HTTP {e.code} for {url}")
    except urllib.error.URLError as e:
        raise FetchError(fetch_code, f"request failed for {url}: {e.reason}")
    if status != 200:
        raise FetchError(fetch_code, f"HTTP {status} for {url}")
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        raise FetchError(validate_code, f"invalid JSON from {url}")
    if expect_array and not isinstance(data, list):
        raise FetchError(validate_code, f"expected JSON array from {url}")
    return data


def fetch_releases(repo, token):
    """Fetch all releases, following pagination (100/page)."""
    releases = []
    page = 1
    while True:
        url = f"{API_BASE}/repos/{repo}/releases?per_page=100&page={page}"
        chunk = http_get_json(url, token, 'TF004', 'JV004', expect_array=True)
        releases.extend(chunk)
        if len(chunk) < 100:
            break
        page += 1
    return releases


def fetch_repo(repo, token):
    """Fetch all raw API responses for a single repository."""
    return {
        'clones': http_get_json(f"{API_BASE}/repos/{repo}/traffic/clones", token, 'TF001', 'JV001'),
        'views': http_get_json(f"{API_BASE}/repos/{repo}/traffic/views", token, 'TF002', 'JV002'),
        'referrers': http_get_json(f"{API_BASE}/repos/{repo}/traffic/popular/referrers", token, 'TF003', 'JV003'),
        'releases': fetch_releases(repo, token),
    }


def fetch_all(repos, token, fetch=None):
    """
    Fetch every repo; one that fails does not stop the others.

    Before, the first failing repo (say a new entry in repos.txt the token
    cannot read) ended the whole run, so no repo was updated at all. Now the
    failure is recorded, printed as a GitHub error annotation, and returned;
    the workflow's last step fails the run AFTER the others are committed, so a
    broken repo is still impossible to miss.

    Returns (repos_raw, errors): [(repo, raw) ...] and {repo: message}.
    """
    fetch = fetch or fetch_repo
    repos_raw, errors = [], {}
    for repo in repos:
        print(f"  - {repo}")
        try:
            repos_raw.append((repo, fetch(repo, token)))
        except FetchError as e:
            errors[repo] = str(e)
            print(f"::error::{repo}: {e}", file=sys.stderr)
    return repos_raw, errors


def load_repos(extra_args):
    """Repos from CLI args if given, else from repos.txt (comments/blanks ignored)."""
    if extra_args:
        return extra_args
    repos = []
    if os.path.exists(REPOS_FILE):
        with open(REPOS_FILE) as f:
            for line in f:
                line = line.split('#', 1)[0].strip()
                if line:
                    repos.append(line)
    return repos


def main():
    output = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    repos = load_repos(sys.argv[2:])
    if not repos:
        print("ERROR_CODE: TF000 - no repositories configured (repos.txt empty?)", file=sys.stderr)
        sys.exit(1)

    token = os.environ.get('TRAFFIC_ACTION_TOKEN', '')
    if not token:
        print("ERROR_CODE: TF000 - TRAFFIC_ACTION_TOKEN is not set", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching traffic for {len(repos)} repository(ies): {', '.join(repos)}")
    repos_raw, errors = fetch_all(repos, token)
    if not repos_raw:
        print("ERROR_CODE: TF000 - no repository could be fetched", file=sys.stderr)
        sys.exit(1)

    # The repo order in metadata is the configured order (repos.txt), so a repo
    # that failed this run keeps its place and its history; merge_history keeps
    # its existing data untouched.
    data = build_traffic_data(repos_raw, fetch_errors=errors)
    data['metadata']['repositories'] = list(repos)
    with open(output, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {output}")


if __name__ == '__main__':
    main()
