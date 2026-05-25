#!/usr/bin/env python3
"""
Unit tests for get_release_breakdown() in scripts/generate_dashboard.py.

The collapsible "Per-version downloads" table lists every release (newest
first) split into Windows / macOS / Linux / Total. These tests lock in:

- releases are ordered by published_at, newest first
- per-platform fields default to 0 for releases fetched before per-release
  platform tracking existed, while 'total' comes from 'downloads'
- 'published' is the date portion of published_at
- an empty list yields no rows

Run with:  python -m unittest discover -s tests -v
"""

import os
import sys
import unittest

# Make scripts/ importable regardless of where the tests are run from
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from generate_dashboard import get_release_breakdown  # noqa: E402


class TestGetReleaseBreakdown(unittest.TestCase):

    def test_orders_newest_first(self):
        """Rows are sorted by published_at descending, regardless of input order."""
        releases = [
            {'tag': 'v1.0.0', 'downloads': 9, 'published_at': '2026-04-20T05:38:40Z'},
            {'tag': 'v3.7.38', 'downloads': 0, 'published_at': '2026-05-24T18:00:00Z'},
            {'tag': 'v2.0.0', 'downloads': 4, 'published_at': '2026-05-01T00:00:00Z'},
        ]
        tags = [row['tag'] for row in get_release_breakdown(releases)]
        self.assertEqual(tags, ['v3.7.38', 'v2.0.0', 'v1.0.0'])

    def test_per_platform_split_passed_through(self):
        """When a release carries per-platform counts, they appear in the row."""
        releases = [{
            'tag': 'v2.0.0', 'downloads': 30,
            'windows': 5, 'macos': 20, 'linux': 5,
            'published_at': '2026-05-01T00:00:00Z',
        }]
        row = get_release_breakdown(releases)[0]
        self.assertEqual((row['windows'], row['macos'], row['linux']), (5, 20, 5))
        self.assertEqual(row['total'], 30)

    def test_missing_platform_fields_default_to_zero(self):
        """Legacy releases without per-platform fields show 0, but keep their total."""
        releases = [{'tag': 'v1.0.0', 'downloads': 9, 'published_at': '2026-04-20T05:38:40Z'}]
        row = get_release_breakdown(releases)[0]
        self.assertEqual((row['windows'], row['macos'], row['linux']), (0, 0, 0))
        self.assertEqual(row['total'], 9)

    def test_published_is_date_only(self):
        """The published field is the YYYY-MM-DD prefix of published_at."""
        releases = [{'tag': 'v1.0.0', 'downloads': 1, 'published_at': '2026-04-20T05:38:40Z'}]
        self.assertEqual(get_release_breakdown(releases)[0]['published'], '2026-04-20')

    def test_empty_list_yields_no_rows(self):
        """No releases yields an empty list so the callout can be skipped."""
        self.assertEqual(get_release_breakdown([]), [])


if __name__ == '__main__':
    unittest.main()
