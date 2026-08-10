#!/usr/bin/env python3
"""
Prune non-release entries (file-sharing uploads, test data, drafts) from
history.json and repair the download statistics they inflated.

fetch_traffic.py now filters these out at fetch time (see RELEASE_TAG_PATTERN),
but data collected before that filter existed still carries them. This one-shot
script removes every release whose tag is not version-like from:

  - downloads.by_release          (lifetime per-release table)
  - downloads.by_release_daily    (early-life snapshot series)

and subtracts their download counts from the cumulative daily series
(downloads.daily_data), then recomputes the per-day deltas and the metadata
totals - so charts and lifetime figures no longer include the junk.

How the per-day subtraction works: for each pruned tag we build its cumulative
contribution per date. Where by_release_daily snapshots exist they give the
exact step curve (carried forward across gaps). After the last snapshot the
final value carries forward if the release still exists in by_release, and
drops to 0 if it does not (the release was deleted, so its counts already left
the recorded cumulative totals). Tags with no snapshots fall back to their full
lifetime count from their publish date onward. Duplicate-tag rows in by_release
are merged the same way aggregate_downloads now does.

Usage:
    python scripts/prune_releases.py history.json            # rewrite in place
    python scripts/prune_releases.py history.json out.json   # write elsewhere
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_traffic import is_countable_release, PLATFORMS  # noqa: E402

FIELDS = ['downloads'] + PLATFORMS          # per-release count fields
DAILY_PLATFORMS = ['total'] + PLATFORMS     # daily_data field suffixes


def _is_junk_tag(tag):
    return not is_countable_release({'tag_name': tag})


def _contribution_curve(dates, snapshots, lifetime, published_at, still_exists):
    """
    Cumulative download contribution of one pruned release for each date.

    Returns {date: {field: count}} covering every date in `dates`.
    """
    curve = {}
    snaps = sorted(snapshots or [], key=lambda s: s['date'])
    published_date = (published_at or '')[:10]
    zero = {f: 0 for f in FIELDS}
    for date in dates:
        if snaps:
            value = zero
            for s in snaps:
                if s['date'] <= date:
                    value = {f: int(s.get(f, 0) or 0) for f in FIELDS}
                else:
                    break
            if date > snaps[-1]['date'] and not still_exists:
                value = zero  # deleted release: its counts left the totals too
        else:
            # No snapshot series: assume the lifetime total from publish onward.
            in_range = published_date and date >= published_date
            value = {f: int(lifetime.get(f, 0) or 0) for f in FIELDS} \
                if (in_range and still_exists) else zero
        curve[date] = value
    return curve


def _merge_by_tag(by_release):
    """Collapse duplicate-tag rows (same merge rule as aggregate_downloads)."""
    merged, order = {}, []
    for rel in by_release:
        tag = rel.get('tag', '')
        if tag in merged:
            m = merged[tag]
            for f in FIELDS:
                m[f] = int(m.get(f, 0) or 0) + int(rel.get(f, 0) or 0)
            pub = rel.get('published_at')
            if pub and (not m.get('published_at') or pub < m['published_at']):
                m['published_at'] = pub
        else:
            merged[tag] = dict(rel)
            order.append(tag)
    return [merged[t] for t in order]


def prune_repo_downloads(downloads):
    """Prune junk releases from one repo's downloads section, in place-ish."""
    by_release = _merge_by_tag(downloads.get('by_release', []))
    by_release_daily = downloads.get('by_release_daily', {}) or {}
    daily_data = downloads.get('daily_data', [])

    surviving_tags = {r['tag'] for r in by_release if not _is_junk_tag(r.get('tag', ''))}
    junk_lifetime = {r['tag']: r for r in by_release if _is_junk_tag(r.get('tag', ''))}
    junk_tags = set(junk_lifetime) | {t for t in by_release_daily if _is_junk_tag(t)}
    if not junk_tags:
        downloads['by_release'] = by_release
        return []

    dates = [e['date'] for e in daily_data]
    total_curve = {d: {f: 0 for f in FIELDS} for d in dates}
    for tag in sorted(junk_tags):
        curve = _contribution_curve(
            dates,
            (by_release_daily.get(tag) or {}).get('snapshots'),
            junk_lifetime.get(tag, {}),
            junk_lifetime.get(tag, {}).get('published_at')
            or (by_release_daily.get(tag) or {}).get('published_at'),
            still_exists=tag in junk_lifetime,
        )
        for d in dates:
            for f in FIELDS:
                total_curve[d][f] += curve[d][f]

    # Subtract from the cumulative series, then recompute per-day deltas the
    # same way merge_downloads does (first day 0, negatives clamped).
    prev = None
    for entry in daily_data:
        sub = total_curve[entry['date']]
        for p in DAILY_PLATFORMS:
            f = 'downloads' if p == 'total' else p
            key = f'cumulative_{p}'
            entry[key] = max(0, int(entry.get(key, 0) or 0) - sub[f])
        for p in DAILY_PLATFORMS:
            key = f'cumulative_{p}'
            entry[f'downloads_{p}'] = 0 if prev is None else max(0, entry[key] - prev[key])
        prev = {f'cumulative_{p}': entry[f'cumulative_{p}'] for p in DAILY_PLATFORMS}

    downloads['by_release'] = [r for r in by_release if r['tag'] in surviving_tags]
    downloads['by_release_daily'] = {
        t: info for t, info in by_release_daily.items() if not _is_junk_tag(t)}
    if daily_data:
        for p in DAILY_PLATFORMS:
            downloads.setdefault('metadata', {})[f'cumulative_{p}'] = \
                daily_data[-1][f'cumulative_{p}']
    return sorted(junk_tags)


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: prune_releases.py <history.json> [output.json]", file=sys.stderr)
        sys.exit(1)
    history_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) == 3 else history_file

    with open(history_file) as f:
        history = json.load(f)

    any_pruned = False
    for repo_name, repo in history.get('repositories', {}).items():
        pruned = prune_repo_downloads(repo.get('downloads', {}) or {})
        if pruned:
            any_pruned = True
            meta = repo.get('downloads', {}).get('metadata', {})
            print(f"{repo_name}: pruned {len(pruned)} pseudo-release(s), "
                  f"lifetime downloads now {meta.get('cumulative_total', '?')}")
            for tag in pruned:
                print(f"  - {tag}")
        else:
            print(f"{repo_name}: nothing to prune")

    if any_pruned or output_file != history_file:
        with open(output_file, 'w') as f:
            json.dump(history, f, indent=2)
        print(f"Wrote {output_file}")


if __name__ == '__main__':
    main()
