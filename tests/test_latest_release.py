#!/usr/bin/env python3
"""
Unit tests for get_latest_release() in scripts/generate_dashboard.py.

The "Latest Release" callout always surfaces the most recently published
release - even one with zero downloads - which the count-sorted "Top Releases"
table would otherwise hide. These tests lock in that behavior:

- newest release is chosen by published_at, not by download count
- input order does not matter (newest still wins when the list is shuffled)
- a brand-new release at 0 downloads is still returned
- entries missing published_at sort last but never crash
- an empty list returns None

Run with:  python -m unittest discover -s tests -v
"""

import os
import sys
import unittest

# Make scripts/ importable regardless of where the tests are run from
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from generate_dashboard import get_latest_release  # noqa: E402


class TestGetLatestRelease(unittest.TestCase):

    def _releases(self):
        """A typical by_release list: newest first, newest has 0 downloads."""
        return [
            {'tag': 'v3.7.37', 'downloads': 0, 'published_at': '2026-05-24T16:54:37Z'},
            {'tag': 'v3.7.36', 'downloads': 1, 'published_at': '2026-05-24T13:51:58Z'},
            {'tag': 'v1.0.0', 'downloads': 9, 'published_at': '2026-04-20T05:38:40Z'},
        ]

    def test_picks_most_recently_published(self):
        """The newest release by published_at wins, regardless of download count."""
        latest = get_latest_release(self._releases())
        self.assertEqual(latest['tag'], 'v3.7.37')
        self.assertEqual(latest['downloads'], 0)

    def test_ignores_input_order(self):
        """Even if the list is not pre-sorted, the newest release is returned."""
        shuffled = list(reversed(self._releases()))
        self.assertEqual(get_latest_release(shuffled)['tag'], 'v3.7.37')

    def test_zero_download_release_is_returned(self):
        """A freshly published release with no downloads is still the latest."""
        latest = get_latest_release(self._releases())
        self.assertEqual(latest['downloads'], 0)

    def test_missing_published_at_sorts_last_but_returns(self):
        """Entries without a timestamp never win over dated ones, but don't crash."""
        releases = [
            {'tag': 'no-date', 'downloads': 5},
            {'tag': 'v2.0.0', 'downloads': 1, 'published_at': '2026-01-01T00:00:00Z'},
        ]
        self.assertEqual(get_latest_release(releases)['tag'], 'v2.0.0')

    def test_only_undated_release_still_returned(self):
        """If no entry has a timestamp, a usable release is still returned."""
        self.assertEqual(get_latest_release([{'tag': 'x', 'downloads': 2}])['tag'], 'x')

    def test_empty_list_returns_none(self):
        """No releases yields None so callers can skip the callout."""
        self.assertIsNone(get_latest_release([]))


if __name__ == '__main__':
    unittest.main()
