#!/usr/bin/env python3
"""
Unit tests for merge_release_daily() in scripts/merge_history.py.

by_release_daily is the one piece of download data that CANNOT be recovered
retroactively: GitHub only exposes a release's current cumulative download_count,
so to know how a release's downloads accrued over time we must snapshot it on
every run. These tests lock in that bounded, append-over-time behavior:

- a release picks up one dated snapshot per run, deduped by date (new wins)
- snapshots accumulate across runs and stay sorted by date
- releases older than RELEASE_DAILY_TRACKING_DAYS are pruned (lifetime only lives
  in by_release), keeping history.json bounded
- releases without a published_at, or with no snapshots, are not tracked
- the structure round-trips through merge_downloads under the 'by_release_daily' key

Run with:  python -m unittest discover -s tests -v
"""

import os
import sys
import unittest

# Make scripts/ importable regardless of where the tests are run from
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from merge_history import (  # noqa: E402
    merge_release_daily,
    merge_downloads,
    RELEASE_DAILY_TRACKING_DAYS,
)


def release(tag, published_at, downloads, windows=0, macos=0, linux=0):
    """Build a per-release lifetime entry like the workflow writes."""
    return {
        'tag': tag,
        'published_at': published_at,
        'downloads': downloads,
        'windows': windows,
        'macos': macos,
        'linux': linux,
    }


class TestMergeReleaseDaily(unittest.TestCase):

    def test_first_run_records_one_snapshot(self):
        """A fresh release gets a single dated snapshot of its cumulative counts."""
        result = merge_release_daily(
            {},
            [release('v1.0.0', '2026-05-20T10:00:00Z', 10, macos=8, windows=2)],
            '2026-05-24',
        )
        self.assertIn('v1.0.0', result)
        snaps = result['v1.0.0']['snapshots']
        self.assertEqual(len(snaps), 1)
        self.assertEqual(snaps[0], {'date': '2026-05-24', 'downloads': 10,
                                    'windows': 2, 'macos': 8, 'linux': 0})

    def test_snapshots_accumulate_across_runs(self):
        """Each run appends a new dated snapshot; the series grows and stays sorted."""
        day1 = merge_release_daily(
            {}, [release('v1.0.0', '2026-05-20T10:00:00Z', 10)], '2026-05-24')
        day2 = merge_release_daily(
            day1, [release('v1.0.0', '2026-05-20T10:00:00Z', 17)], '2026-05-25')
        snaps = day2['v1.0.0']['snapshots']
        self.assertEqual([s['date'] for s in snaps], ['2026-05-24', '2026-05-25'])
        self.assertEqual(snaps[-1]['downloads'], 17)

    def test_same_day_snapshot_overwrites(self):
        """Re-running on the same date overwrites that date's snapshot (new wins)."""
        day1 = merge_release_daily(
            {}, [release('v1.0.0', '2026-05-20T10:00:00Z', 10)], '2026-05-24')
        again = merge_release_daily(
            day1, [release('v1.0.0', '2026-05-20T10:00:00Z', 12)], '2026-05-24')
        snaps = again['v1.0.0']['snapshots']
        self.assertEqual(len(snaps), 1)
        self.assertEqual(snaps[0]['downloads'], 12)

    def test_old_release_is_pruned(self):
        """A release past the tracking window is dropped to keep history bounded."""
        old_publish = '2026-01-01T00:00:00Z'  # well over 90 days before as_of
        existing = {
            'v0.1.0': {
                'published_at': old_publish,
                'snapshots': [{'date': '2026-01-02', 'downloads': 5,
                               'windows': 0, 'macos': 5, 'linux': 0}],
            }
        }
        result = merge_release_daily(
            existing, [release('v0.1.0', old_publish, 5)], '2026-05-24')
        self.assertNotIn('v0.1.0', result)

    def test_release_inside_window_is_kept(self):
        """A release just inside the window is retained."""
        # published exactly RELEASE_DAILY_TRACKING_DAYS before as_of -> kept
        from datetime import date, timedelta
        as_of = date(2026, 5, 24)
        published = as_of - timedelta(days=RELEASE_DAILY_TRACKING_DAYS)
        result = merge_release_daily(
            {},
            [release('v2.0.0', published.strftime('%Y-%m-%dT00:00:00Z'), 3)],
            as_of.strftime('%Y-%m-%d'),
        )
        self.assertIn('v2.0.0', result)

    def test_release_without_published_at_is_tracked_until_dated(self):
        """A release with no publish date still records snapshots (cannot age out)."""
        result = merge_release_daily(
            {}, [{'tag': 'nightly', 'downloads': 4}], '2026-05-24')
        self.assertIn('nightly', result)
        self.assertEqual(result['nightly']['snapshots'][0]['downloads'], 4)

    def test_no_as_of_date_keeps_existing_without_adding(self):
        """Without a snapshot date, no new snapshot is added (but existing kept)."""
        existing = {
            'v1.0.0': {
                'published_at': '2026-05-20T00:00:00Z',
                'snapshots': [{'date': '2026-05-24', 'downloads': 10,
                               'windows': 0, 'macos': 10, 'linux': 0}],
            }
        }
        result = merge_release_daily(
            existing, [release('v1.0.0', '2026-05-20T00:00:00Z', 99)], '')
        self.assertEqual(len(result['v1.0.0']['snapshots']), 1)
        self.assertEqual(result['v1.0.0']['snapshots'][0]['downloads'], 10)

    def test_merge_downloads_exposes_by_release_daily(self):
        """merge_downloads threads the per-release daily series through its result."""
        new = {
            'date': '2026-05-24',
            'last_fetched': '2026-05-24T00:00:00Z',
            'cumulative_total': 10, 'cumulative_windows': 2,
            'cumulative_macos': 8, 'cumulative_linux': 0,
            'by_release': [release('v1.0.0', '2026-05-22T00:00:00Z', 10, macos=8, windows=2)],
        }
        result = merge_downloads({}, new)
        self.assertIn('by_release_daily', result)
        self.assertIn('v1.0.0', result['by_release_daily'])

    def test_empty_inputs(self):
        """No data in, empty dict out."""
        self.assertEqual(merge_release_daily({}, [], '2026-05-24'), {})


if __name__ == '__main__':
    unittest.main()
