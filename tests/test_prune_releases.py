#!/usr/bin/env python3
"""
Tests for scripts/prune_releases.py - the one-shot repair that removes
file-sharing pseudo-releases from history.json and un-inflates the
cumulative download series.

Run with:  python -m unittest discover -s tests -v
"""

import os
import sys
import unittest

SCRIPTS = os.path.join(os.path.dirname(__file__), '..', 'scripts')
sys.path.insert(0, SCRIPTS)

from prune_releases import prune_repo_downloads  # noqa: E402


def _daily(date, total, windows=0):
    entry = {'date': date}
    for p, cum in (('total', total), ('windows', windows), ('macos', 0), ('linux', 0)):
        entry[f'cumulative_{p}'] = cum
        entry[f'downloads_{p}'] = 0  # deltas are recomputed by the prune
    return entry


class TestPruneRepoDownloads(unittest.TestCase):

    def _downloads(self):
        # Day 1: only v1.0.0 (10 dl). Day 2: mockup release appears with 100 dl.
        # Day 3: mockup grows to 150, v1.0.0 to 12.
        return {
            'daily_data': [
                _daily('2026-07-01', 10, windows=10),
                _daily('2026-07-02', 110, windows=10),
                _daily('2026-07-03', 162, windows=12),
            ],
            'metadata': {'last_fetched': 'x', 'cumulative_total': 162,
                         'cumulative_windows': 12, 'cumulative_macos': 0,
                         'cumulative_linux': 0},
            'by_release': [
                {'tag': 'v1.0.0', 'downloads': 12, 'windows': 12, 'macos': 0,
                 'linux': 0, 'published_at': '2026-06-30T00:00:00Z'},
                {'tag': 'ui-mockups-2026-07-02', 'downloads': 150, 'windows': 0,
                 'macos': 0, 'linux': 0, 'published_at': '2026-07-02T00:00:00Z'},
            ],
            'by_release_daily': {
                'ui-mockups-2026-07-02': {
                    'published_at': '2026-07-02T00:00:00Z',
                    'snapshots': [
                        {'date': '2026-07-02', 'downloads': 100, 'windows': 0,
                         'macos': 0, 'linux': 0},
                        {'date': '2026-07-03', 'downloads': 150, 'windows': 0,
                         'macos': 0, 'linux': 0},
                    ],
                },
            },
        }

    def test_prunes_tables_and_repairs_daily_series(self):
        downloads = self._downloads()
        pruned = prune_repo_downloads(downloads)

        self.assertEqual(pruned, ['ui-mockups-2026-07-02'])
        self.assertEqual([r['tag'] for r in downloads['by_release']], ['v1.0.0'])
        self.assertEqual(downloads['by_release_daily'], {})

        totals = [e['cumulative_total'] for e in downloads['daily_data']]
        self.assertEqual(totals, [10, 10, 12])
        deltas = [e['downloads_total'] for e in downloads['daily_data']]
        self.assertEqual(deltas, [0, 0, 2])
        self.assertEqual(downloads['metadata']['cumulative_total'], 12)
        # Platform buckets were never inflated, so they are untouched
        self.assertEqual(downloads['metadata']['cumulative_windows'], 12)

    def test_deleted_pseudo_release_stops_contributing_after_last_snapshot(self):
        downloads = self._downloads()
        # Simulate the mockup release having been deleted from GitHub after
        # 07-02: it is gone from by_release, and its 100 downloads already left
        # the recorded cumulative totals on 07-03.
        downloads['by_release'] = downloads['by_release'][:1]
        downloads['by_release_daily']['ui-mockups-2026-07-02']['snapshots'] = [
            {'date': '2026-07-02', 'downloads': 100, 'windows': 0, 'macos': 0,
             'linux': 0}]
        downloads['daily_data'][2] = _daily('2026-07-03', 12, windows=12)

        pruned = prune_repo_downloads(downloads)
        self.assertEqual(pruned, ['ui-mockups-2026-07-02'])
        totals = [e['cumulative_total'] for e in downloads['daily_data']]
        self.assertEqual(totals, [10, 10, 12])

    def test_no_snapshots_falls_back_to_publish_date(self):
        downloads = self._downloads()
        del downloads['by_release_daily']['ui-mockups-2026-07-02']
        pruned = prune_repo_downloads(downloads)
        self.assertEqual(pruned, ['ui-mockups-2026-07-02'])
        # Full lifetime count (150) subtracted from its publish date onward
        totals = [e['cumulative_total'] for e in downloads['daily_data']]
        self.assertEqual(totals, [10, 0, 12])

    def test_clean_history_untouched(self):
        downloads = self._downloads()
        downloads['by_release'] = downloads['by_release'][:1]
        downloads['by_release_daily'] = {}
        before = [dict(e) for e in downloads['daily_data']]
        self.assertEqual(prune_repo_downloads(downloads), [])
        self.assertEqual(downloads['daily_data'], before)
        self.assertEqual(downloads['metadata']['cumulative_total'], 162)


if __name__ == '__main__':
    unittest.main()
