#!/usr/bin/env python3
"""
Rebuild per-release and per-channel download history from this repo's own git
history of history.json. One-shot; safe to run again.

Why this works: every collector run commits history.json, and each commit's
'by_release' holds every release's lifetime download_count, split by
platform. So the git log already contains a daily per-release record back to
the first run that stored the split (2026-05-25), long before the dashboard
kept per-release series of its own (it kept 14 days per release, then dropped
them). From it this script fills in:

  - downloads.daily_data: cumulative_stable_<key> and cumulative_beta_<key>
    (key = total, windows, macos, linux, homebrew) for every recorded day, so
    the stable/beta split is known from the first tracked day, not from the
    day this script ran;
  - downloads.by_release_daily: the daily snapshot series of every release
    published within RELEASE_DAILY_TRACKING_DAYS (90), for the 30- and 90-day
    release curves. Snapshots the collector already recorded win.

A day is read from the LAST commit of that UTC day (the same value the
collector itself keeps for a day: later runs overwrite earlier ones). The
release channel is GitHub's pre-release flag as stored in the current
by_release; a release that no longer exists counts as beta when its tag has a
pre-release suffix ("-beta.3"). A release missing from one day's commit but
still published keeps its last known count; one that was deleted counts 0
from the day it vanished (its downloads left GitHub's totals then too).

Usage:
    python scripts/backfill_from_git.py history.json            # in place
    python scripts/backfill_from_git.py history.json out.json
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_traffic import is_countable_release  # noqa: E402
from merge_history import (  # noqa: E402
    APP_KEYS, CHANNELS, RELEASE_DAILY_TRACKING_DAYS, RELEASE_SNAPSHOT_FIELDS,
    merge_downloads, migrate_downloads, _drop_unchanged,
)

PLATFORM_FIELDS = ['windows', 'macos', 'linux', 'homebrew']


def _git(repo_dir: str, *args: str) -> str:
    return subprocess.run(['git', '-C', repo_dir, *args], check=True,
                          capture_output=True, text=True).stdout


def app_counts(row: Dict[str, Any]) -> Dict[str, int]:
    """A by_release row's app downloads. Rows before the platform split count all."""
    out = {p: int(row.get(p, 0) or 0) for p in PLATFORM_FIELDS}
    if 'windows' in row:
        out['downloads'] = sum(out.values())
    else:
        out['downloads'] = int(row.get('downloads', 0) or 0)
        out['no_split'] = 1     # the platforms of this row are not known
    return out


def rows_by_tag(by_release: List[Dict[str, Any]]) -> Dict[str, Dict[str, int]]:
    """Countable releases only; rows sharing a tag are summed (as the fetch does)."""
    out: Dict[str, Dict[str, int]] = {}
    for row in by_release or []:
        tag = row.get('tag') or ''
        if not is_countable_release({'tag_name': tag}):
            continue
        counts = app_counts(row)
        if tag in out:
            out[tag] = {k: out[tag].get(k, 0) + counts.get(k, 0)
                        for k in set(out[tag]) | set(counts)}
        else:
            out[tag] = counts
    return out


def daily_rows_from_git(repo_dir: str, repo: str, path: str = 'history.json'
                        ) -> Dict[str, Dict[str, Dict[str, int]]]:
    """{date: {tag: counts}} from the last commit of each day that has the repo."""
    log = _git(repo_dir, 'log', '--reverse', '--format=%H %ct', '--', path).split('\n')
    last_of_day: Dict[str, str] = {}
    for line in log:
        if not line.strip():
            continue
        sha, when = line.split()
        when_utc = datetime.fromtimestamp(int(when), tz=timezone.utc)
        last_of_day[when_utc.strftime('%Y-%m-%d')] = sha
    out: Dict[str, Dict[str, Dict[str, int]]] = {}
    for day in sorted(last_of_day):
        try:
            data = json.loads(_git(repo_dir, 'show', f'{last_of_day[day]}:{path}'))
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            continue
        repos = data.get('repositories') if isinstance(data, dict) else None
        entry = repos.get(repo) if isinstance(repos, dict) else None   # older layouts: skip
        dl = entry.get('downloads') if isinstance(entry, dict) else None
        if not isinstance(dl, dict):
            continue
        if not dl.get('by_release'):
            continue
        fetched = (dl.get('metadata') or {}).get('last_fetched') or ''
        date = fetched[:10] if fetched[:10] else day
        out[date] = rows_by_tag(dl['by_release'])
    return out


def is_beta(tag: str, prerelease_of: Dict[str, bool]) -> bool:
    if tag in prerelease_of:
        return prerelease_of[tag]
    return '-' in tag.lstrip('v')


def fill_values(rows_by_date: Dict[str, Dict[str, Dict[str, int]]],
                still_published: set) -> Dict[str, Dict[str, Dict[str, int]]]:
    """Per day, every release's count: carried forward while it is still published."""
    known: Dict[str, Dict[str, int]] = {}
    out = {}
    for date in sorted(rows_by_date):
        today = rows_by_date[date]
        for tag in list(known):
            if tag not in today and tag not in still_published:
                del known[tag]          # deleted: its downloads left the totals
        known.update(today)
        out[date] = dict(known)
    return out


def channel_series(values_by_date: Dict[str, Dict[str, Dict[str, int]]],
                   prerelease_of: Dict[str, bool]) -> Dict[str, Dict[str, int]]:
    """{date: {'cumulative_stable_total': n, ...}} summed over the releases."""
    out = {}
    for date, values in values_by_date.items():
        sums = {f'cumulative_{c}_{k}': 0 for c in CHANNELS for k in APP_KEYS}
        for tag, counts in values.items():
            c = 'beta' if is_beta(tag, prerelease_of) else 'stable'
            sums[f'cumulative_{c}_total'] += counts['downloads']
            for p in PLATFORM_FIELDS:
                sums[f'cumulative_{c}_{p}'] += counts[p]
        # A day with a row from before the platform split has channel TOTALS
        # but no channel platforms: leave those out rather than write 0, which
        # would book every platform's lifetime count as the next day's downloads.
        if any(counts.get('no_split') for counts in values.values()):
            sums = {k: v for k, v in sums.items() if k.endswith('_total')}
        out[date] = sums
    return out


def release_series(values_by_date: Dict[str, Dict[str, Dict[str, int]]],
                   releases: Dict[str, Dict[str, Any]], as_of: str,
                   days: int = RELEASE_DAILY_TRACKING_DAYS) -> Dict[str, Any]:
    """by_release_daily entries for releases published within `days` of as_of."""
    as_of_d = datetime.strptime(as_of, '%Y-%m-%d').date()
    out: Dict[str, Any] = {}
    for tag, meta in releases.items():
        published = (meta.get('published_at') or '')[:10]
        if not published:
            continue
        pub_d = datetime.strptime(published, '%Y-%m-%d').date()
        if (as_of_d - pub_d).days > days:
            continue
        snaps, last_seen = [], ''
        for date in sorted(values_by_date):
            if date < published or tag not in values_by_date[date]:
                continue
            counts = values_by_date[date][tag]
            snaps.append({'date': date, **{f: counts.get(f, 0) for f in RELEASE_SNAPSHOT_FIELDS}})
            last_seen = date
        if snaps:
            out[tag] = {'published_at': meta.get('published_at', ''),
                        'prerelease': bool(meta.get('prerelease', False)),
                        'snapshots': _drop_unchanged(snaps), 'last_seen': last_seen}
    return out


def merge_release_entries(existing: Dict[str, Any], backfilled: Dict[str, Any]) -> Dict[str, Any]:
    """Union of both; on a date both have, the collector's own snapshot wins."""
    out = {}
    for tag in set(existing) | set(backfilled):
        old, new = existing.get(tag) or {}, backfilled.get(tag) or {}
        snaps = {s['date']: s for s in new.get('snapshots', [])}
        snaps.update({s['date']: s for s in old.get('snapshots', [])})
        entry = dict(new)
        entry.update({k: v for k, v in old.items() if k != 'snapshots'})
        if 'prerelease' in new:
            entry['prerelease'] = new['prerelease']
        entry['last_seen'] = max(old.get('last_seen', ''), new.get('last_seen', ''),
                                 max(snaps) if snaps else '')
        entry['snapshots'] = _drop_unchanged([snaps[d] for d in sorted(snaps)])
        out[tag] = entry
    return out


def backfill_repo(downloads: Dict[str, Any], rows_by_date, as_of: str) -> Dict[str, Any]:
    downloads = migrate_downloads(downloads)
    by_release = downloads.get('by_release', [])
    releases = {r['tag']: r for r in by_release if r.get('tag')}
    prerelease_of = {t: bool(r.get('prerelease')) for t, r in releases.items() if 'prerelease' in r}
    values = fill_values(rows_by_date, set(releases))
    channels = channel_series(values, prerelease_of)

    daily = []
    for entry in downloads.get('daily_data', []):
        e = dict(entry)
        # A day the collector itself recorded the split for keeps its own
        # values (it read them later in the day than the last commit did).
        if e['date'] in channels and 'cumulative_stable_total' not in e:
            e.update(channels[e['date']])
        daily.append(e)
    # The first recorded days may predate the first commit with a platform
    # split: leave those without a channel series rather than guess.
    downloads = dict(downloads, daily_data=daily)
    downloads['by_release_daily'] = merge_release_entries(
        downloads.get('by_release_daily', {}),
        release_series(values, {t: dict(r, prerelease=prerelease_of.get(t, is_beta(t, {})))
                                for t, r in releases.items()}, as_of))
    # Recompute every per-day delta from the cumulative series.
    return merge_downloads(downloads, {})


def main():
    if len(sys.argv) not in (2, 3):
        print(__doc__)
        sys.exit(2)
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) == 3 else src
    # The git history is this checkout's, wherever the file being filled is.
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(src) as f:
        history = json.load(f)
    as_of = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    for repo, data in history.get('repositories', {}).items():
        dl = data.get('downloads') or {}
        if not dl.get('by_release'):
            continue
        rows = daily_rows_from_git(repo_dir, repo)
        if not rows:
            continue
        data['downloads'] = backfill_repo(dl, rows, as_of)
        daily = data['downloads']['daily_data']
        mismatch = max((abs(e.get('cumulative_total', 0)
                            - e.get('cumulative_stable_total', 0)
                            - e.get('cumulative_beta_total', 0))
                        for e in daily if 'cumulative_stable_total' in e), default=0)
        first = next((e['date'] for e in daily if 'cumulative_stable_total' in e), None)
        print(f"{repo}: {len(rows)} days from git, channel split from {first}, "
              f"{len(data['downloads']['by_release_daily'])} releases with a daily series, "
              f"largest stable+beta vs total gap {mismatch}")
    with open(dst, 'w') as f:
        json.dump(history, f, indent=2)


if __name__ == '__main__':
    main()
