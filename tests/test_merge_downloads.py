#!/usr/bin/env python3
"""
Unit tests for the release-download merge logic in scripts/merge_history.py.

merge_downloads() is the trickiest part of the pipeline: GitHub's download_count
is a cumulative all-time counter, so per-day downloads are derived by diffing
consecutive daily snapshots. These tests lock in that behavior:

- first snapshot has a daily delta of 0 (no prior baseline)
- subsequent snapshots produce correct per-platform deltas
- gaps between snapshots are carry-forward filled (cumulative flat, delta 0)
- negative deltas (deleted release/asset) are clamped to 0
- lifetime metadata reflects the latest cumulative totals
- by_release / by_arch breakdowns pass through (new wins, else existing)

Run with:  python -m unittest discover -s tests -v
"""

import os
import sys
import unittest

# Make scripts/ importable regardless of where the tests are run from
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from merge_history import merge_downloads  # noqa: E402


def snapshot(date, total, windows, macos, linux, **extra):
    """Build a fetched-snapshot dict like the workflow writes to traffic_data.json."""
    snap = {
        'date': date,
        'last_fetched': date + 'T00:00:00Z',
        'cumulative_total': total,
        'cumulative_windows': windows,
        'cumulative_macos': macos,
        'cumulative_linux': linux,
    }
    snap.update(extra)
    return snap


class TestMergeDownloads(unittest.TestCase):

    def test_first_snapshot_has_zero_daily(self):
        """The very first snapshot has no baseline, so all daily deltas are 0."""
        result = merge_downloads({}, snapshot('2026-05-24', 599, 89, 479, 31))
        self.assertEqual(len(result['daily_data']), 1)
        entry = result['daily_data'][0]
        self.assertEqual(entry['cumulative_total'], 599)
        self.assertEqual(entry['downloads_total'], 0)
        self.assertEqual(entry['downloads_windows'], 0)

    def test_delta_between_two_snapshots(self):
        """A later snapshot yields per-platform deltas from the previous cumulative."""
        existing = merge_downloads({}, snapshot('2026-05-19', 580, 85, 465, 30))
        result = merge_downloads(existing, snapshot('2026-05-24', 599, 89, 479, 31))

        # Series spans 05-19 .. 05-24 (6 days) with carry-forward in the gap
        self.assertEqual(len(result['daily_data']), 6)

        last = result['daily_data'][-1]
        self.assertEqual(last['date'], '2026-05-24')
        self.assertEqual(last['downloads_total'], 19)
        self.assertEqual(last['downloads_windows'], 4)
        self.assertEqual(last['downloads_macos'], 14)
        self.assertEqual(last['downloads_linux'], 1)

    def test_gap_days_carry_forward_with_zero_delta(self):
        """Days with no snapshot hold cumulative flat and record a 0 delta."""
        existing = merge_downloads({}, snapshot('2026-05-19', 580, 85, 465, 30))
        result = merge_downloads(existing, snapshot('2026-05-24', 599, 89, 479, 31))

        # 05-20 .. 05-23 are gap-filled
        for entry in result['daily_data'][1:-1]:
            self.assertEqual(entry['cumulative_total'], 580)
            self.assertEqual(entry['downloads_total'], 0)

    def test_negative_delta_is_clamped(self):
        """If cumulative drops (deleted release/asset), the daily delta clamps to 0."""
        existing = merge_downloads({}, snapshot('2026-05-23', 600, 90, 480, 30))
        result = merge_downloads(existing, snapshot('2026-05-24', 595, 88, 478, 29))
        last = result['daily_data'][-1]
        self.assertEqual(last['downloads_total'], 0)
        self.assertEqual(last['downloads_windows'], 0)
        # Cumulative still reflects the (lower) reality
        self.assertEqual(last['cumulative_total'], 595)

    def test_metadata_reflects_latest_cumulative(self):
        """Lifetime metadata equals the most recent cumulative snapshot."""
        existing = merge_downloads({}, snapshot('2026-05-19', 580, 85, 465, 30))
        result = merge_downloads(existing, snapshot('2026-05-24', 599, 89, 479, 31))
        meta = result['metadata']
        self.assertEqual(meta['cumulative_total'], 599)
        self.assertEqual(meta['cumulative_macos'], 479)

    def test_same_day_snapshot_overwrites(self):
        """A new snapshot for an existing date overwrites it (new data wins)."""
        existing = merge_downloads({}, snapshot('2026-05-24', 590, 88, 472, 30))
        result = merge_downloads(existing, snapshot('2026-05-24', 599, 89, 479, 31))
        self.assertEqual(len(result['daily_data']), 1)
        self.assertEqual(result['daily_data'][0]['cumulative_total'], 599)

    def test_breakdowns_pass_through_new_wins(self):
        """by_release / by_arch take the new snapshot's values when present."""
        new = snapshot(
            '2026-05-24', 599, 89, 479, 31,
            by_release=[{'tag': 'v3.6.4', 'downloads': 54, 'published_at': '2026-05-17T21:00:29Z'}],
            by_arch={'macos': {'arm64': 305, 'x86_64': 124, 'universal': 50}},
        )
        result = merge_downloads({}, new)
        self.assertEqual(result['by_release'][0]['tag'], 'v3.6.4')
        self.assertEqual(result['by_arch']['macos']['arm64'], 305)

    def test_breakdowns_fall_back_to_existing(self):
        """If a new snapshot omits breakdowns, the previous ones are retained."""
        existing = {
            'daily_data': [],
            'metadata': {},
            'by_release': [{'tag': 'v1.0.0', 'downloads': 5}],
            'by_arch': {'linux': {'x86_64': 23}},
        }
        result = merge_downloads(existing, snapshot('2026-05-24', 599, 89, 479, 31))
        self.assertEqual(result['by_release'][0]['tag'], 'v1.0.0')
        self.assertEqual(result['by_arch']['linux']['x86_64'], 23)

    def test_empty_inputs(self):
        """No existing data and no new snapshot yields an empty, well-formed result."""
        result = merge_downloads({}, {})
        self.assertEqual(result['daily_data'], [])
        self.assertEqual(result['metadata'], {})
        self.assertEqual(result['by_release'], [])
        self.assertEqual(result['by_arch'], {})


if __name__ == '__main__':
    unittest.main()
