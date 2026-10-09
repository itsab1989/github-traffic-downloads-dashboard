#!/usr/bin/env python3
"""
Tests for the user-estimate additions (2026-10-09):

- Homebrew downloads ("_homebrew" assets) are their own category, never macOS
- the app total leaves out files that are not the app (demo projects, screenshots)
- the stable/beta split, and its rebuild from git history
- the migration of a stored downloads section to the app-only total
- rolling 30/90-day windows over all releases, their trend, and release curves
- the traffic API's own 14-day unique counts, kept per day
- one repository failing to fetch does not stop the others
- recorded traffic older than a year is kept

Run with:  python -m unittest discover -s tests -v
"""

import os
import sys
import unittest
from datetime import datetime, timedelta, timezone

ROOT = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

from classify import classify_platform, classify_arch  # noqa: E402
from fetch_traffic import (  # noqa: E402
    aggregate_downloads, aggregate_release, fetch_all, FetchError, build_traffic_data,
    load_repos,
)
from merge_history import (  # noqa: E402
    merge_downloads, migrate_downloads, merge_release_daily, merge_window_14d,
    zero_fill_daily_data, DOWNLOADS_SCHEMA, RELEASE_DAILY_TRACKING_DAYS,
)
import generate_dashboard as gd  # noqa: E402
import backfill_from_git as bf  # noqa: E402


def _day(offset):
    return (datetime.now(timezone.utc).date() + timedelta(days=offset)).strftime('%Y-%m-%d')


def _release(tag, assets, prerelease=False, published='2026-10-01T10:00:00Z'):
    return {'tag_name': tag, 'published_at': published, 'prerelease': prerelease,
            'assets': [{'name': n, 'download_count': c} for n, c in assets]}


CHROMIQ_ASSETS = [
    ('ChromIQ-macOS-arm64_v4.3.3.dmg', 10),
    ('ChromIQ-macOS-arm64_v4.3.3_homebrew.dmg', 4),
    ('ChromIQ-macOS-x86_64_v4.3.3.dmg', 3),
    ('ChromIQ-macOS-x86_64_v4.3.3_homebrew.dmg', 1),
    ('ChromIQ-macOS-universal_v4.3.3.dmg', 2),
    ('ChromIQ-Windows-x64_v4.3.3.zip', 7),
    ('ChromIQ-Windows-arm64_v4.3.3.zip', 1),
    ('ChromIQ-Linux-x86_64_v4.3.3.tar.gz', 2),
    ('ChromIQ-Linux-aarch64_v4.3.3.tar.gz', 1),
    ('ChromIQ-Demo-Projects_v4.3.3.zip', 5),
]


class TestClassification(unittest.TestCase):

    def test_every_chromiq_asset_name(self):
        expected = {
            'ChromIQ-macOS-arm64_v4.3.3.dmg': ('macos', 'arm64'),
            'ChromIQ-macOS-arm64_v4.3.3_homebrew.dmg': ('homebrew', 'arm64'),
            'ChromIQ-macOS-x86_64_v4.3.3.dmg': ('macos', 'x86_64'),
            'ChromIQ-macOS-x86_64_v4.3.3_homebrew.dmg': ('homebrew', 'x86_64'),
            'ChromIQ-macOS-universal_v4.3.3.dmg': ('macos', 'universal'),
            'ChromIQ-Windows-x64_v4.3.3.zip': ('windows', 'x86_64'),
            'ChromIQ-Windows-arm64_v4.3.3.zip': ('windows', 'arm64'),
            'ChromIQ-Linux-x86_64_v4.3.3.tar.gz': ('linux', 'x86_64'),
            'ChromIQ-Linux-aarch64_v4.3.3.tar.gz': ('linux', 'arm64'),
            'ChromIQ-macOS-arm64_v4.3.3-beta.17_homebrew.dmg': ('homebrew', 'arm64'),
        }
        for name, (platform, arch) in expected.items():
            self.assertEqual(classify_platform(name), platform, name)
            self.assertEqual(classify_arch(name), arch, name)

    def test_files_that_are_not_the_app(self):
        for name in ['ChromIQ-Demo-Projects_v4.3.3.zip', 'ChromIQ-demo-projects.zip',
                     'ChromIQ-Report-Limit-Demos.zip', '01-main-window.png',
                     'MacReplica-1.0.4.dmg.sha256', 'icon.icns']:
            self.assertIsNone(classify_platform(name), name)

    def test_homebrew_only_as_a_suffix(self):
        # a word "homebrew" elsewhere in the name is not the Homebrew copy
        self.assertEqual(classify_platform('homebrew-notes-macos.dmg'), 'macos')


class TestAggregation(unittest.TestCase):

    def test_homebrew_is_not_counted_again_under_macos(self):
        row = aggregate_release(_release('v4.3.3', CHROMIQ_ASSETS))
        self.assertEqual(row['macos'], 15)       # 10 + 3 + 2, no _homebrew
        self.assertEqual(row['homebrew'], 5)
        self.assertEqual(row['windows'], 8)
        self.assertEqual(row['linux'], 3)
        self.assertEqual(row['other'], 5)        # the demo projects
        self.assertEqual(row['downloads'], 31)   # app only
        self.assertFalse(row['prerelease'])

    def test_channels_follow_the_prerelease_flag(self):
        agg = aggregate_downloads([
            _release('v4.3.3', CHROMIQ_ASSETS),
            _release('v4.3.4-beta.1', [('ChromIQ-macOS-arm64_v4.3.4-beta.1_homebrew.dmg', 2),
                                       ('ChromIQ-Windows-x64_v4.3.4-beta.1.zip', 1)],
                     prerelease=True),
        ])
        self.assertEqual(agg['cumulative_total'], 34)
        self.assertEqual(agg['cumulative_stable_total'], 31)
        self.assertEqual(agg['cumulative_beta_total'], 3)
        self.assertEqual(agg['cumulative_beta_homebrew'], 2)
        self.assertEqual(agg['cumulative_homebrew'], 7)
        self.assertEqual(agg['cumulative_other'], 5)
        self.assertEqual(agg['by_arch']['homebrew'], {'arm64': 6, 'x86_64': 1})
        for k in ('total', 'windows', 'macos', 'linux', 'homebrew'):
            self.assertEqual(agg[f'cumulative_{k}'],
                             agg[f'cumulative_stable_{k}'] + agg[f'cumulative_beta_{k}'], k)


class TestFetchResilience(unittest.TestCase):

    def test_one_failing_repo_does_not_stop_the_others(self):
        def fetch(repo, token):
            if repo == 'o/broken':
                raise FetchError('TF001', 'HTTP 403')
            return {'clones': {'clones': [], 'count': 3, 'uniques': 2}, 'views': {'views': []},
                    'referrers': [], 'releases': []}
        raw, errors = fetch_all(['o/a', 'o/broken', 'o/b'], 'tok', fetch=fetch)
        self.assertEqual([r for r, _ in raw], ['o/a', 'o/b'])
        self.assertIn('o/broken', errors)
        data = build_traffic_data(raw, fetch_errors=errors)
        self.assertIn('o/broken', data['metadata']['fetch_errors'])
        self.assertEqual(data['repositories']['o/a']['window_14d']['clones_unique_14d'], 2)

    def test_the_workflow_fails_the_run_after_committing_when_a_repo_failed(self):
        with open(os.path.join(ROOT, '.github', 'workflows', 'main.yml')) as f:
            wf = f.read()
        commit = wf.index('- name: Commit changes')
        report = wf.index('- name: Report repositories that could not be fetched')
        self.assertLess(commit, report)
        self.assertIn('fetch_errors', wf[report:])

    def test_repos_txt_tracks_the_tap_and_macreplica(self):
        repos = load_repos([])
        self.assertIn('itsab1989/homebrew-chromiq', repos)
        self.assertIn('itsab1989/MacReplica', repos)
        self.assertIn('itsab1989/homebrew-chromiq', gd.REPO_NOTES)
        note = gd.REPO_NOTES['itsab1989/homebrew-chromiq']
        self.assertIn('rough indicator', note)
        self.assertIn('not a download count', note)


class TestMigration(unittest.TestCase):

    def schema1(self):
        return {'daily_data': [
            {'date': '2026-10-01', 'cumulative_total': 110, 'cumulative_windows': 30,
             'cumulative_macos': 60, 'cumulative_linux': 10},
            {'date': '2026-10-02', 'cumulative_total': 125, 'cumulative_windows': 35,
             'cumulative_macos': 68, 'cumulative_linux': 11},
        ], 'by_release_daily': {'v1': {'published_at': '2026-10-01T00:00:00Z', 'snapshots': [
            {'date': '2026-10-01', 'downloads': 12, 'windows': 3, 'macos': 6, 'linux': 1}]}}}

    def test_total_becomes_app_only_and_the_rest_other(self):
        m = migrate_downloads(self.schema1())
        self.assertEqual(m['schema'], DOWNLOADS_SCHEMA)
        self.assertEqual(m['daily_data'][0]['cumulative_total'], 100)
        self.assertEqual(m['daily_data'][0]['cumulative_other'], 10)
        self.assertEqual(m['daily_data'][1]['cumulative_total'], 114)
        self.assertEqual(m['by_release_daily']['v1']['snapshots'][0]['downloads'], 10)
        # idempotent
        self.assertEqual(migrate_downloads(m), m)

    def test_no_drop_on_the_day_the_meaning_changes(self):
        new = {'date': '2026-10-03', 'last_fetched': '2026-10-03T08:00:00Z',
               'cumulative_total': 120, 'cumulative_windows': 37, 'cumulative_macos': 70,
               'cumulative_linux': 11, 'cumulative_homebrew': 2, 'cumulative_other': 16,
               'cumulative_stable_total': 100, 'cumulative_beta_total': 20}
        out = merge_downloads(self.schema1(), new)
        last = out['daily_data'][-1]
        self.assertEqual(last['downloads_total'], 6)     # 120 - 114, not clamped to 0
        self.assertEqual(last['downloads_homebrew'], 2)
        # a series recorded for the first time books nothing on its first day
        self.assertEqual(last['downloads_stable_total'], 0)
        self.assertNotIn('cumulative_stable_total', out['daily_data'][0])


class TestHistoryKeepsItsPast(unittest.TestCase):

    def test_traffic_older_than_a_year_is_kept(self):
        old = {'date': _day(-400), 'clones_total': 5, 'clones_unique': 1,
               'views_total': 2, 'views_unique': 1}
        filled = zero_fill_daily_data([old, {'date': _day(0), 'clones_total': 1,
                                             'clones_unique': 1, 'views_total': 0,
                                             'views_unique': 0}])
        self.assertEqual(filled[0], old)
        self.assertEqual(len(filled), 401)

    def test_window_14d_is_one_entry_per_day(self):
        s = merge_window_14d([], {'date': '2026-10-08', 'clones_unique_14d': 3})
        s = merge_window_14d(s, {'date': '2026-10-09', 'clones_unique_14d': 4})
        s = merge_window_14d(s, {'date': '2026-10-09', 'clones_unique_14d': 5})
        self.assertEqual([(e['date'], e['clones_unique_14d']) for e in s],
                         [('2026-10-08', 3), ('2026-10-09', 5)])


class TestReleaseSeries(unittest.TestCase):

    def rel(self, n, prerelease=False):
        return {'tag': 'v1.0.0', 'published_at': '2026-07-01T10:00:00Z', 'downloads': n,
                'windows': n, 'macos': 0, 'linux': 0, 'homebrew': 0, 'prerelease': prerelease}

    def test_kept_for_ninety_days_and_only_on_change(self):
        self.assertEqual(RELEASE_DAILY_TRACKING_DAYS, 90)
        s = merge_release_daily({}, [self.rel(3)], '2026-07-01')
        s = merge_release_daily(s, [self.rel(3)], '2026-07-02')
        s = merge_release_daily(s, [self.rel(5)], '2026-07-03')
        s = merge_release_daily(s, [self.rel(5)], '2026-09-20')   # day 81
        e = s['v1.0.0']
        self.assertEqual([x['date'] for x in e['snapshots']], ['2026-07-01', '2026-07-03'])
        self.assertEqual(e['last_seen'], '2026-09-20')
        self.assertFalse(e['prerelease'])
        s = merge_release_daily(s, [self.rel(5)], '2026-10-05')   # day 96: aged out
        self.assertNotIn('v1.0.0', s)

    def test_curves_by_day_since_publish(self):
        brd = {
            'v1': {'published_at': '2026-07-01T10:00:00Z', 'last_seen': '2026-07-06',
                   'snapshots': [{'date': '2026-07-02', 'downloads': 4},
                                 {'date': '2026-07-04', 'downloads': 9}]},
            # tracking began long after publish: the early days are unknown
            'v0': {'published_at': '2026-06-01T10:00:00Z', 'last_seen': '2026-07-06',
                   'snapshots': [{'date': '2026-06-20', 'downloads': 30}]},
            'v2-beta': {'published_at': '2026-07-05T10:00:00Z', 'last_seen': '2026-07-06',
                        'prerelease': True,
                        'snapshots': [{'date': '2026-07-05', 'downloads': 1}]},
        }
        curves = {c['tag']: c for c in gd.compute_release_curves(brd, 30)}
        self.assertEqual(curves['v1']['points'], [0, 4, 4, 9, 9, 9])
        self.assertEqual(curves['v0']['points'][:19], [None] * 19)
        self.assertEqual(curves['v0']['points'][19], 30)
        self.assertEqual(len(curves['v0']['points']), 31)   # capped at the horizon
        self.assertTrue(curves['v2-beta']['prerelease'])

    def test_reception_keeps_to_the_first_fortnight(self):
        brd = {'old': {'published_at': '2026-07-01T00:00:00Z', 'last_seen': '2026-08-01',
                       'snapshots': [{'date': '2026-07-01', 'downloads': 4}]},
               'new': {'published_at': '2026-07-25T00:00:00Z', 'last_seen': '2026-08-01',
                       'snapshots': [{'date': '2026-07-25', 'downloads': 2, 'homebrew': 1}]}}
        rows = gd.compute_release_reception(brd)
        self.assertEqual([r['tag'] for r in rows], ['new'])
        self.assertEqual(rows[0]['age_days'], 8)
        self.assertEqual(rows[0]['accrued_homebrew'], 1)


def _daily(n_days, per_day, start_offset=None, channels=True):
    """n_days of downloads entries ending today, `per_day` downloads each."""
    start_offset = -(n_days - 1) if start_offset is None else start_offset
    out = []
    for i in range(n_days):
        e = {'date': _day(start_offset + i), 'cumulative_total': per_day * i,
             'downloads_total': per_day if i else 0, 'cumulative_windows': per_day * i,
             'downloads_windows': per_day if i else 0}
        if channels:
            e.update({'cumulative_stable_total': per_day * i,
                      'downloads_stable_total': per_day if i else 0,
                      'cumulative_beta_total': 0, 'downloads_beta_total': 0})
        out.append(e)
    return out


class TestRolling(unittest.TestCase):

    def test_thirty_days_means_thirty_days(self):
        r = gd.compute_rolling_downloads(_daily(120, 2), 30)
        self.assertEqual(r['all']['total'], 60)
        self.assertEqual(r['stable']['total'], 60)
        self.assertEqual(r['beta']['total'], 0)
        self.assertEqual(r['covered_days'], 30)
        traffic = [{'date': _day(-i), 'clones_total': 1, 'clones_unique': 1,
                    'views_total': 1, 'views_unique': 1} for i in range(60)]
        self.assertEqual(gd.calculate_period_stats(traffic, 30)['clones_total'], 30)
        self.assertEqual(gd.calculate_downloads_period_stats(_daily(120, 2), 30)['total'], 60)

    def test_a_window_reaching_before_tracking_says_so(self):
        r = gd.compute_rolling_downloads(_daily(10, 1), 30)
        self.assertEqual(r['covered_days'], 9)   # the first day has no baseline
        self.assertIn('9 days tracked', gd.render_estimate_md(_daily(10, 1)))

    def test_trend_only_where_the_whole_window_is_tracked(self):
        rs = gd.compute_rolling_series(_daily(40, 1), 30)
        self.assertEqual(len(rs['dates']), 10)
        self.assertEqual(set(rs['total']), {30})
        self.assertEqual(rs['dates'][-1], _day(0))

    def test_page_and_readme_carry_the_explanations(self):
        notes = ' '.join(gd.ESTIMATE_NOTES)
        for needle in ('two computers', 'never update', 'Betas are mostly testers',
                       'Homebrew', 'not counted again under macOS', 'Clones'):
            self.assertIn(needle, notes)
        for n in gd.ESTIMATE_NOTES:
            self.assertNotIn('—', n)
        md = gd.render_estimate_md(_daily(120, 2))
        self.assertIn('| 30 days | stable |', md)
        self.assertIn('| 90 days | beta |', md)
        with open(os.path.join(ROOT, 'dashboard.html'), encoding='utf-8') as f:
            page = f.read()
        for needle in ('estimate_notes', 'Release curves: first 30 days',
                       'Release curves: first 90 days', 'Rolling 30-day downloads',
                       'Different cloners in the last 14 days', "key: 'homebrew'"):
            self.assertIn(needle, page)


class TestBackfill(unittest.TestCase):

    def test_deleted_releases_leave_published_ones_carry(self):
        rows = {'2026-07-01': {'v1': {'downloads': 5, 'windows': 5, 'macos': 0, 'linux': 0, 'homebrew': 0},
                               'gone': {'downloads': 2, 'windows': 2, 'macos': 0, 'linux': 0, 'homebrew': 0}},
                '2026-07-02': {}}
        values = bf.fill_values(rows, {'v1'})
        self.assertEqual(set(values['2026-07-02']), {'v1'})

    def test_channel_sums_and_flags(self):
        values = {'2026-07-01': {
            'v1.0.0': {'downloads': 5, 'windows': 5, 'macos': 0, 'linux': 0, 'homebrew': 0},
            'v1.1.0-beta.1': {'downloads': 2, 'windows': 0, 'macos': 2, 'linux': 0, 'homebrew': 0}}}
        ch = bf.channel_series(values, {})
        self.assertEqual(ch['2026-07-01']['cumulative_stable_total'], 5)
        self.assertEqual(ch['2026-07-01']['cumulative_beta_macos'], 2)
        # GitHub's own flag wins over the tag's look
        ch = bf.channel_series(values, {'v1.0.0': True})
        self.assertEqual(ch['2026-07-01']['cumulative_beta_total'], 7)

    def test_rows_before_the_platform_split_count_all(self):
        self.assertEqual(bf.app_counts({'downloads': 9})['downloads'], 9)
        self.assertEqual(bf.app_counts({'downloads': 9, 'windows': 2, 'macos': 3,
                                        'linux': 1})['downloads'], 6)
        self.assertEqual(set(bf.rows_by_tag([{'tag': 'screenshots-2026', 'downloads': 3},
                                             {'tag': 'v1.0', 'downloads': 1}])), {'v1.0'})

    def test_a_day_before_the_platform_split_has_no_channel_platforms(self):
        """Writing 0 there booked every platform's lifetime count as the next
        day's downloads (ChromIQ, 2026-05-25: 510 'stable macOS' in a day)."""
        rows = {'2026-05-24': {'v1.0.0': bf.app_counts({'downloads': 9})},
                '2026-05-25': {'v1.0.0': bf.app_counts({'downloads': 10, 'windows': 4,
                                                        'macos': 5, 'linux': 1})}}
        ch = bf.channel_series(bf.fill_values(rows, {'v1.0.0'}), {})
        self.assertEqual(ch['2026-05-24'], {'cumulative_stable_total': 9,
                                            'cumulative_beta_total': 0})
        self.assertEqual(ch['2026-05-25']['cumulative_stable_macos'], 5)
        daily = [dict({'date': d, 'cumulative_total': v['cumulative_stable_total']}, **v)
                 for d, v in sorted(ch.items())]
        merged = merge_downloads({'daily_data': daily}, {})['daily_data']
        self.assertEqual(merged[1]['downloads_stable_total'], 1)
        self.assertEqual(merged[1]['downloads_stable_macos'], 0)

    def test_a_split_and_an_unsplit_row_of_one_tag_add_up(self):
        out = bf.rows_by_tag([{'tag': 'v1.0', 'downloads': 3},
                              {'tag': 'v1.0', 'downloads': 2, 'windows': 2, 'macos': 0, 'linux': 0}])
        self.assertEqual(out['v1.0']['downloads'], 5)


class TestAllIncludesHomebrew(unittest.TestCase):
    """Basti, 2026-10-09: one number for normal and Homebrew downloads together."""

    def test_the_total_counts_homebrew_once(self):
        agg = aggregate_downloads([_release('v4.3.3', CHROMIQ_ASSETS)])
        self.assertEqual(agg['cumulative_homebrew'], 5)
        self.assertEqual(agg['cumulative_macos'], 15)       # the copies are not in here
        self.assertEqual(agg['cumulative_total'], agg['cumulative_windows']
                         + agg['cumulative_macos'] + agg['cumulative_linux']
                         + agg['cumulative_homebrew'])
        self.assertEqual(agg['cumulative_total'], 31)       # demo ZIP left out
        self.assertEqual(agg['cumulative_other'], 5)

    def test_rolling_all_includes_homebrew(self):
        daily = merge_downloads({}, {'date': _day(-1), 'cumulative_total': 0, 'cumulative_macos': 0,
                                     'cumulative_homebrew': 0})
        daily = merge_downloads(daily, {'date': _day(0), 'cumulative_total': 7, 'cumulative_macos': 4,
                                        'cumulative_homebrew': 3})['daily_data']
        r = gd.compute_rolling_downloads(daily, 30)
        self.assertEqual((r['all']['total'], r['all']['macos'], r['all']['homebrew']), (7, 4, 3))

    def test_labelled_on_the_page_the_readme_and_the_badge(self):
        with open(os.path.join(ROOT, 'dashboard.html'), encoding='utf-8') as f:
            page = f.read()
        self.assertIn('<th>All downloads (incl. Homebrew)</th>', page)
        self.assertIn('All downloads (incl. Homebrew), lifetime:', page)
        self.assertIn('est.lifetime', page)
        md = gd.render_estimate_md(_daily(40, 1))
        self.assertIn('| Window | Channel | All downloads (incl. Homebrew) |', md)
        self.assertEqual(gd.ALL_LABEL, 'All downloads (incl. Homebrew)')
        badges = gd.render_badges('itsab1989/ChromIQ', {'total': 9}, {}, 1)
        self.assertIn('downloads%20incl.%20Homebrew-9-', badges)
        self.assertIn('![downloads](', gd.render_badges('someone/else', {'total': 9}, {}, 1))

    def test_the_chart_data_carries_the_lifetime_totals(self):
        daily = _daily(40, 1)
        history = {'metadata': {'repositories': ['itsab1989/ChromIQ']},
                   'repositories': {'itsab1989/ChromIQ': {
                       'daily_data': [], 'downloads': {'daily_data': daily,
                                                       'by_release': [{'tag': 'v1', 'downloads': 1}]}}}}
        est = gd.build_chart_data(history)['repositories'][0]['downloads']['estimate']
        self.assertEqual(est['lifetime']['total'], daily[-1]['cumulative_total'])


if __name__ == '__main__':
    unittest.main()
