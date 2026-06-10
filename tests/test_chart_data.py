#!/usr/bin/env python3
"""
Unit tests for build_chart_data() in scripts/generate_dashboard.py.

build_chart_data() assembles the JSON payload that the interactive dashboard
(dashboard.html) renders client-side. These tests lock in the shape the
front-end depends on:

- one entry per repository, in metadata order, with a URL anchor
- traffic series (daily/weekly/biweekly/cumulative) each carry aligned
  dates/clones/views arrays
- download series carry per-platform arrays + release markers, and has_data
  reflects whether any download history exists

Run with:  python -m unittest discover -s tests -v
"""

import os
import sys
import unittest
from datetime import datetime, timezone, timedelta

# Make scripts/ importable regardless of where the tests are run from
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from generate_dashboard import build_chart_data  # noqa: E402


def _day(offset):
    return (datetime.now(timezone.utc) - timedelta(days=offset)).strftime('%Y-%m-%d')


def _history(with_downloads=True):
    daily = [
        {'date': _day(2), 'clones_total': 4, 'clones_unique': 3, 'views_total': 10, 'views_unique': 7},
        {'date': _day(1), 'clones_total': 6, 'clones_unique': 4, 'views_total': 12, 'views_unique': 8},
        {'date': _day(0), 'clones_total': 5, 'clones_unique': 3, 'views_total': 9, 'views_unique': 6},
    ]
    repo = {'daily_data': daily, 'referrers': [], 'metadata': {}}
    if with_downloads:
        repo['downloads'] = {
            'daily_data': [
                {'date': _day(1), 'cumulative_total': 10, 'downloads_total': 10,
                 'cumulative_windows': 3, 'downloads_windows': 3,
                 'cumulative_macos': 6, 'downloads_macos': 6,
                 'cumulative_linux': 1, 'downloads_linux': 1},
                {'date': _day(0), 'cumulative_total': 14, 'downloads_total': 4,
                 'cumulative_windows': 4, 'downloads_windows': 1,
                 'cumulative_macos': 8, 'downloads_macos': 2,
                 'cumulative_linux': 2, 'downloads_linux': 1},
            ],
            'by_release': [{'tag': 'v1.0.0', 'downloads': 14, 'published_at': _day(1) + 'T00:00:00Z'}],
            'by_release_daily': {
                'v1.0.0': {
                    'published_at': _day(1) + 'T00:00:00Z',
                    'snapshots': [
                        {'date': _day(1), 'downloads': 10, 'windows': 3, 'macos': 6, 'linux': 1},
                        {'date': _day(0), 'downloads': 14, 'windows': 4, 'macos': 8, 'linux': 2},
                    ],
                    'launch': [
                        {'time': _day(1) + 'T02:00:00Z', 'downloads': 4,
                         'windows': 1, 'macos': 2, 'linux': 1},
                        {'time': _day(1) + 'T08:30:00Z', 'downloads': 10,
                         'windows': 3, 'macos': 6, 'linux': 1},
                    ],
                },
            },
        }
    else:
        repo['downloads'] = {}
    return {
        'metadata': {'last_updated': '2026-05-31T00:00:00Z', 'repositories': ['owner/Repo']},
        'repositories': {'owner/Repo': repo},
    }


class TestBuildChartData(unittest.TestCase):

    def test_top_level_shape(self):
        data = build_chart_data(_history())
        self.assertIn('generated_at', data)
        self.assertEqual(len(data['repositories']), 1)
        repo = data['repositories'][0]
        self.assertEqual(repo['name'], 'owner/Repo')
        self.assertEqual(repo['display'], 'Repo')
        self.assertEqual(repo['anchor'], 'repo')

    def test_traffic_series_aligned(self):
        repo = build_chart_data(_history())['repositories'][0]
        for window in ('daily', 'weekly', 'biweekly', 'cumulative'):
            block = repo['traffic'][window]
            self.assertEqual(len(block['dates']), len(block['clones']))
            self.assertEqual(len(block['dates']), len(block['views']))

    def test_cumulative_is_monotonic(self):
        repo = build_chart_data(_history())['repositories'][0]
        cum = repo['traffic']['cumulative']['clones']
        self.assertEqual(cum, sorted(cum))  # running totals never decrease

    def test_downloads_present(self):
        repo = build_chart_data(_history(with_downloads=True))['repositories'][0]
        d = repo['downloads']
        self.assertTrue(d['has_data'])
        for key in ('total', 'windows', 'macos', 'linux'):
            self.assertIn(key, d['daily'])
            self.assertIn(key, d['cumulative'])
        self.assertEqual(d['releases'][0]['tag'], 'v1.0.0')

    def test_downloads_absent(self):
        repo = build_chart_data(_history(with_downloads=False))['repositories'][0]
        self.assertFalse(repo['downloads']['has_data'])

    def test_reception_rows(self):
        d = build_chart_data(_history())['repositories'][0]['downloads']
        self.assertEqual(len(d['reception']), 1)
        r = d['reception'][0]
        self.assertEqual(r['tag'], 'v1.0.0')
        # Latest cumulative counts, not a delta against the first snapshot
        self.assertEqual(r['total'], 14)
        self.assertEqual((r['windows'], r['macos'], r['linux']), (4, 8, 2))

    def test_launch_curves(self):
        d = build_chart_data(_history())['repositories'][0]['downloads']
        self.assertEqual(len(d['launch_curves']), 1)
        curve = d['launch_curves'][0]
        self.assertEqual(curve['tag'], 'v1.0.0')
        # Origin point plus one per recorded launch point, as publish offsets
        self.assertEqual(curve['points'][0], {'h': 0, 'downloads': 0})
        self.assertEqual([p['h'] for p in curve['points']], [0, 2.0, 8.5])
        self.assertEqual([p['downloads'] for p in curve['points']], [0, 4, 10])

    def test_respects_metadata_repo_order(self):
        h = _history()
        h['repositories']['owner/Second'] = h['repositories']['owner/Repo']
        h['metadata']['repositories'] = ['owner/Second', 'owner/Repo']
        names = [r['name'] for r in build_chart_data(h)['repositories']]
        self.assertEqual(names, ['owner/Second', 'owner/Repo'])


if __name__ == '__main__':
    unittest.main()
