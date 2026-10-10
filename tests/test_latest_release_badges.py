#!/usr/bin/env python3
"""
Unit tests for the latest-stable / latest-beta badges in render_badges().

Every repo's badge row ends with the downloads of its newest stable release and
its newest beta (GitHub pre-release flag). These tests lock in:

- the newest release of each channel is picked by published_at, not by count
- the count is the release's 'downloads' figure (all platforms + Homebrew,
  never the 'other' files such as demo projects), as in the per-version table
- a newer stable release does not hide the older newest beta, and vice versa
- a repo with only stable releases gets no beta badge (and the reverse); a repo
  without releases gets neither
- the tag in the label survives shields' '-' / '_' field separators

Run with:  python -m unittest discover -s tests -v
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import generate_dashboard as gd  # noqa: E402

STABLE = ('latest stable', gd.LATEST_STABLE_BADGE_COLOR)
BETA = ('latest beta', gd.LATEST_BETA_BADGE_COLOR)


def _row(tag, downloads, published, prerelease=False, other=0, homebrew=0):
    return {'tag': tag, 'downloads': downloads, 'homebrew': homebrew, 'other': other,
            'prerelease': prerelease, 'published_at': published}


def _badges(releases):
    return gd.render_badges('itsab1989/ChromIQ', {'total': 1}, {}, len(releases), releases)


class TestLatestReleaseBadges(unittest.TestCase):

    def releases(self):
        return [
            _row('v4.3.2', 300, '2026-09-01T10:00:00Z'),
            _row('v4.3.3-beta.16', 16, '2026-10-09T14:01:37Z', prerelease=True),
            # Homebrew is inside 'downloads'; 'other' (demo projects) is not.
            _row('v4.3.3', 10, '2026-10-10T04:28:07Z', other=7, homebrew=3),
            _row('v4.3.3-beta.17', 5, '2026-10-10T01:44:02Z', prerelease=True, homebrew=3),
        ]

    def test_newest_of_each_channel_with_its_app_downloads(self):
        md = _badges(self.releases())
        self.assertIn('![latest stable v4.3.3](https://img.shields.io/badge/'
                      'latest%20stable%20v4.3.3-10-212121', md)
        self.assertIn('![latest beta v4.3.3-beta.17](https://img.shields.io/badge/'
                      'latest%20beta%20v4.3.3--beta.17-5-757575', md)

    def test_channel_pick_ignores_download_count(self):
        latest = gd.get_latest_release_in_channel(self.releases(), prerelease=False)
        self.assertEqual(latest['tag'], 'v4.3.3')
        latest = gd.get_latest_release_in_channel(self.releases(), prerelease=True)
        self.assertEqual(latest['tag'], 'v4.3.3-beta.17')

    def test_new_releases_come_after_the_existing_badges(self):
        md = _badges(self.releases())
        self.assertLess(md.index('![releases]'), md.index('![latest stable'))
        self.assertLess(md.index('![latest stable'), md.index('![latest beta'))
        self.assertTrue(md.endswith('\n\n'))
        self.assertEqual(md.count('\n'), 2, 'the row stays a single markdown line')

    def test_stable_only_repo_has_no_beta_badge(self):
        md = _badges([_row('v1.0.4', 4, '2026-10-04T18:13:01Z')])
        self.assertIn('latest%20stable%20v1.0.4-4-', md)
        self.assertNotIn('latest beta', md)

    def test_beta_only_repo_has_no_stable_badge(self):
        md = _badges([_row('v0.1.0-beta.1', 2, '2026-10-04T18:13:01Z', prerelease=True)])
        self.assertIn('latest%20beta%20v0.1.0--beta.1-2-', md)
        self.assertNotIn('latest stable', md)

    def test_no_releases_no_latest_badges(self):
        for releases in ([], None):
            md = gd.render_badges('a/b', {'total': 0}, {}, 0, releases)
            self.assertNotIn('latest', md)

    def test_older_call_without_releases_keeps_old_row(self):
        md = gd.render_badges('a/b', {'total': 3}, {'clones_total': 2, 'views_total': 1}, 0)
        self.assertEqual(md, '![downloads](https://img.shields.io/badge/downloads-3-212121) '
                             '![clones](https://img.shields.io/badge/clones-2-2196F3) '
                             '![views](https://img.shields.io/badge/views-1-4CAF50) '
                             '![releases](https://img.shields.io/badge/releases-0-6f42c1)\n\n')

    def test_underscore_in_tag_is_escaped(self):
        md = _badges([_row('v1_2', 1, '2026-01-01T00:00:00Z')])
        self.assertIn('latest%20stable%20v1__2-1-', md)


if __name__ == '__main__':
    unittest.main()
