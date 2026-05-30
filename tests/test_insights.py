#!/usr/bin/env python3
"""
Unit tests for the derived-insight helpers in scripts/generate_dashboard.py:
tracking window, week-over-week momentum, engagement funnel, unclassified
downloads, and recent-release reception.

These power the "at a glance" and engagement sections. They are pure functions
so the dashboard can be reasoned about without rendering matplotlib.

Run with:  python -m unittest discover -s tests -v
"""

import os
import sys
import unittest
from datetime import datetime, timezone, timedelta

# Make scripts/ importable regardless of where the tests are run from
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from generate_dashboard import (  # noqa: E402
    compute_tracking_window,
    compute_momentum,
    compute_funnel,
    compute_unclassified,
    compute_release_reception,
)


def _day(offset):
    """A YYYY-MM-DD string `offset` days before today (UTC)."""
    return (datetime.now(timezone.utc) - timedelta(days=offset)).strftime('%Y-%m-%d')


class TestTrackingWindow(unittest.TestCase):

    def test_finds_first_active_day_through_zero_fill(self):
        """Leading zero-filled days are ignored; window starts at first activity."""
        data = [
            {'date': '2025-01-01', 'clones_total': 0, 'views_total': 0},
            {'date': '2025-01-02', 'clones_total': 0, 'views_total': 0},
            {'date': '2025-01-03', 'clones_total': 5, 'views_total': 0},
            {'date': '2025-01-07', 'clones_total': 1, 'views_total': 2},
        ]
        first, days = compute_tracking_window(data)
        self.assertEqual(first, '2025-01-03')
        self.assertEqual(days, 5)  # 01-03 .. 01-07 inclusive

    def test_no_activity_returns_none(self):
        """All-zero data means tracking hasn't really begun."""
        data = [{'date': '2025-01-01', 'clones_total': 0, 'views_total': 0}]
        self.assertEqual(compute_tracking_window(data), (None, 0))

    def test_empty(self):
        self.assertEqual(compute_tracking_window([]), (None, 0))


class TestMomentum(unittest.TestCase):

    def test_week_over_week_delta(self):
        """Current 7-day window vs the prior 7-day window, with % change."""
        data = []
        # prior week (days 13..7 ago): 1/day -> 7 total
        for off in range(7, 14):
            data.append({'date': _day(off), 'clones_total': 1, 'views_total': 0})
        # this week (days 6..0 ago): 2/day -> 14 total
        for off in range(0, 7):
            data.append({'date': _day(off), 'clones_total': 2, 'views_total': 0})
        mom = compute_momentum(data, 'clones_total')
        self.assertEqual(mom['current'], 14)
        self.assertEqual(mom['previous'], 7)
        self.assertEqual(mom['delta_pct'], 100.0)

    def test_no_baseline_gives_none_delta(self):
        """No prior-week data -> delta is None (avoids divide-by-zero)."""
        data = [{'date': _day(off), 'clones_total': 3, 'views_total': 0} for off in range(0, 7)]
        mom = compute_momentum(data, 'clones_total')
        self.assertEqual(mom['current'], 21)
        self.assertEqual(mom['previous'], 0)
        self.assertIsNone(mom['delta_pct'])


class TestFunnel(unittest.TestCase):

    def test_ratios(self):
        f = compute_funnel(views=100, clones=25, downloads=5)
        self.assertEqual(f['clone_rate'], 25.0)
        self.assertEqual(f['download_rate'], 20.0)

    def test_zero_denominators_are_none(self):
        f = compute_funnel(views=0, clones=0, downloads=0)
        self.assertIsNone(f['clone_rate'])
        self.assertIsNone(f['download_rate'])


class TestUnclassified(unittest.TestCase):

    def test_gap_between_total_and_platforms(self):
        """total minus matched platforms surfaces unclassified assets."""
        self.assertEqual(
            compute_unclassified({'total': 100, 'windows': 40, 'macos': 50, 'linux': 5}), 5)

    def test_never_negative(self):
        """If platforms somehow exceed total, clamp to 0 rather than report nonsense."""
        self.assertEqual(
            compute_unclassified({'total': 10, 'windows': 8, 'macos': 8, 'linux': 0}), 0)


class TestReleaseReception(unittest.TestCase):

    def test_accrued_downloads_since_first_tracked(self):
        """Reception = latest minus first observed snapshot, per platform."""
        brd = {
            'v1.0.0': {
                'published_at': '2026-05-20T00:00:00Z',
                'snapshots': [
                    {'date': '2026-05-20', 'downloads': 2, 'windows': 1, 'macos': 1, 'linux': 0},
                    {'date': '2026-05-24', 'downloads': 12, 'windows': 4, 'macos': 7, 'linux': 1},
                ],
            }
        }
        rows = compute_release_reception(brd)
        self.assertEqual(len(rows), 1)
        r = rows[0]
        self.assertEqual(r['accrued'], 10)
        self.assertEqual(r['accrued_windows'], 3)
        self.assertEqual(r['accrued_macos'], 6)
        self.assertEqual(r['accrued_linux'], 1)
        self.assertEqual(r['tracked_days'], 5)
        self.assertEqual(r['lifetime'], 12)

    def test_sorted_newest_first(self):
        brd = {
            'old': {'published_at': '2026-05-01T00:00:00Z',
                    'snapshots': [{'date': '2026-05-01', 'downloads': 1}]},
            'new': {'published_at': '2026-05-25T00:00:00Z',
                    'snapshots': [{'date': '2026-05-25', 'downloads': 1}]},
        }
        self.assertEqual([r['tag'] for r in compute_release_reception(brd)], ['new', 'old'])

    def test_empty(self):
        self.assertEqual(compute_release_reception({}), [])


if __name__ == '__main__':
    unittest.main()
