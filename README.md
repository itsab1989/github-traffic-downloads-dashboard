See full Reference and Usage Guide at:
https://itsab1989.github.io/github-traffic-downloads-dashboard/

> This is a modified version of the original [github-traffic-dashboard](https://github.com/soul-traveller/github-traffic-dashboard), extended with platform-specific download statistics (Windows / macOS / Linux).

# 📊 GitHub Traffic & Downloads Dashboard

This dashboard tracks historical traffic data (clones, views, and release downloads) for GitHub repositories.

**Last Updated:** 2026-11-14T09:32:28.644839Z

## 📋 How Metrics Are Calculated

This dashboard uses GitHub Traffic API data to calculate the following metrics:

### 📊 Core Metrics

**Views:**
- Counted when someone visits the repository page
- Includes page views from web browsers
- Does not include visits via command-line tools or APIs

**Clones:**
- Counted when someone clones the repository
- Includes clones via `git clone`, GitHub Desktop, download ZIP, and API
- Can occur without a corresponding view event

**Release Downloads:**
- Counted when someone downloads a pre-compiled release asset (binary/installer)
- Split by platform from the asset file name (Windows, macOS, Linux, Homebrew); **All downloads (incl. Homebrew)** is the combined total, with each download counted once
- This is a **separate metric** from Clones - cloning the source is not a release download
- **Lifetime** totals reflect all-time downloads (GitHub's cumulative `download_count`) and are accurate immediately
- **Per-day** figures are derived by diffing daily snapshots, so they only accrue from the first tracked day onward

**Important:** Views and Clones are **independent metrics**. Users can:
- View without cloning
- Clone without viewing (e.g., via `git clone` command)
- Both view and clone

### 🔢 Calculation Formulas

**For any time period (short-term, medium-term, lifetime):**

**Total Metrics:**
- Total Views = Sum of daily views for the period
- Total Clones = Sum of daily clones for the period

**Unique Metrics:**
- Unique Views = Sum of daily unique views for the period
- Unique Clones = Sum of daily unique clones for the period
  - Note: This sums daily unique counts, which may count the same user on multiple days

**Repeat Metrics:**
- Repeat Views = Total Views - Unique Views
- Repeat Clones = Total Clones - Unique Clones
- Repeat Percentage = (Repeat / Total) × 100

**Example:**
```
If a repository has:
- Total Views: 100
- Unique Views: 20
Then:
- Repeat Views = 100 - 20 = 80
- Repeat Percentage = (80 / 100) × 100 = 80%
```

### 📈 Graph Data Aggregation

**Daily Graphs:**
- Shows raw daily data points
- Each point represents one day's activity

**Weekly Graphs:**
- Aggregates daily data into 7-day periods
- Each point represents the sum of 7 consecutive days

**Bi-Weekly Graphs:**
- Aggregates daily data into 14-day periods
- Each point represents the sum of 14 consecutive days

**Cumulative Graphs:**
- Shows running totals over time
- Each point represents the sum of all previous days plus current day

## 📋 Table of Contents

Quick navigation to repository statistics:

- [ChromIQ](#chromiq)
- [ChromIQ-Patches](#chromiq-patches)
- [ChromIQ-Gamut-Viewer](#chromiq-gamut-viewer)
- [github-traffic-downloads-dashboard](#github-traffic-downloads-dashboard)
- [homebrew-chromiq](#homebrew-chromiq)
- [MacReplica](#macreplica)
- [neolume](#neolume)

# ChromIQ

![downloads incl. Homebrew](https://img.shields.io/badge/downloads%20incl.%20Homebrew-10904-212121) ![clones](https://img.shields.io/badge/clones-38372-2196F3) ![views](https://img.shields.io/badge/views-10403-4CAF50) ![releases](https://img.shields.io/badge/releases-938-6f42c1) ![latest stable v4.3.35](https://img.shields.io/badge/latest%20stable%20v4.3.35-0-212121 "Downloads of the latest stable release, all platforms incl. Homebrew") ![latest beta v4.3.10-beta.1](https://img.shields.io/badge/latest%20beta%20v4.3.10--beta.1-13-757575 "Downloads of the latest beta release, all platforms incl. Homebrew")

*Tracking since **2026-05-02** (196 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~196 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 326 | 172 | ▲ +89.5% |
| Views | 280 | 569 | ▼ -50.8% |
| Downloads | 350 | 187 | ▲ +87.2% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 5700 | 341 |
| Last 90 Days | 13028 | 2066 |
| Lifetime | 38372 | 9960 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 5700 | 341 | 5359 | 94.0% |
| Last 90 Days | 13028 | 2066 | 10962 | 84.1% |
| Lifetime | 38372 | 9960 | 28412 | 74.0% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1673 | 800 |
| Last 90 Days | 5290 | 1780 |
| Lifetime | 10403 | 2963 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 800 | — |
| 🗅️ Unique cloners | 341 | 42.6% |
| 📥 Downloads | 7531 | 941.4% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 10

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| aocr.org | 185 | 185 |
| Google | 46 | 22 |
| itsab1989.github.io | 29 | 23 |
| github.com | 18 | 14 |
| dpreview.com | 11 | 9 |
| yandex.ru | 11 | 1 |
| forum.luminous-landscape.com | 9 | 5 |
| printerknowledge.com | 9 | 4 |
| hub.displaycal.net | 4 | 4 |
| search.brave.com | 2 | 2 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 1673 | 800 | 873 | 52.2% |
| Last 90 Days | 5290 | 1780 | 3510 | 66.4% |
| Lifetime | 10403 | 2963 | 7440 | 71.5% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 2246 | 2634 | 3268 |
| 🍎 macOS | 3062 | 3495 | 5175 |
| 🐧 Linux | 1990 | 2039 | 2178 |
| 🍺 Homebrew | 233 | 283 | 283 |
| **All downloads (incl. Homebrew)** | **7531** | **8451** | **10904** |

*ℹ️ Not counted above: 179 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days | all | **7531** | 2246 | 3062 | 1990 | 233 |
| 30 days | stable | **2808** | 908 | 1083 | 607 | 210 |
| 30 days | beta | **4723** | 1338 | 1979 | 1383 | 23 |
| 90 days | all | **8451** | 2634 | 3495 | 2039 | 283 |
| 90 days | stable | **3360** | 1191 | 1303 | 634 | 232 |
| 90 days | beta | **5136** | 1455 | 2226 | 1405 | 51 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-05-25** on; the stable/beta split from **2026-05-25**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v4.3.35` - **0** downloads (published 2026-11-14)

<details>
<summary><strong>📦 Per-version downloads</strong> (938 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v4.3.35 | 0 | 0 | 0 | 0 | **0** |
| v4.3.34 | 3 | 3 | 2 | 6 | **14** |
| v4.3.33 | 14 | 8 | 3 | 8 | **33** |
| v4.3.32 | 10 | 8 | 2 | 8 | **28** |
| v4.3.31 | 5 | 3 | 4 | 6 | **18** |
| v4.3.30 | 14 | 11 | 3 | 6 | **34** |
| v4.3.29 | 7 | 4 | 3 | 4 | **18** |
| v4.3.28 | 20 | 8 | 2 | 8 | **38** |
| v4.3.27 | 6 | 3 | 2 | 2 | **13** |
| v4.3.26 | 3 | 3 | 2 | 1 | **9** |
| v4.3.25 | 20 | 10 | 3 | 7 | **40** |
| v4.3.24 | 5 | 8 | 2 | 3 | **18** |
| v4.3.23 | 8 | 10 | 3 | 6 | **27** |
| v4.3.22 | 13 | 8 | 6 | 6 | **33** |
| v4.3.21 | 12 | 10 | 3 | 6 | **31** |
| v4.3.20 | 78 | 20 | 11 | 15 | **124** |
| v4.3.19 | 46 | 17 | 10 | 15 | **88** |
| v4.3.18 | 9 | 7 | 7 | 6 | **29** |
| v4.3.17 | 12 | 13 | 6 | 5 | **36** |
| v4.3.16 | 13 | 6 | 4 | 9 | **32** |
| v4.3.15 | 8 | 9 | 6 | 4 | **27** |
| v4.3.14 | 6 | 4 | 3 | 5 | **18** |
| v4.3.13 | 11 | 8 | 3 | 4 | **26** |
| v4.3.12 | 8 | 1 | 3 | 8 | **20** |
| v4.3.11 | 4 | 5 | 3 | 4 | **16** |
| v4.3.10 | 9 | 5 | 4 | 6 | **24** |
| v4.3.10-beta.1 *(beta)* | 4 | 3 | 2 | 4 | **13** |
| v4.3.9 | 17 | 7 | 3 | 19 | **46** |
| v4.3.8 | 6 | 5 | 4 | 4 | **19** |
| v4.3.8-beta.3 *(beta)* | 3 | 3 | 4 | 5 | **15** |
| v4.3.8-beta.2 *(beta)* | 5 | 3 | 3 | 4 | **15** |
| v4.3.8-beta.1 *(beta)* | 3 | 4 | 3 | 3 | **13** |
| v4.3.7 | 30 | 7 | 5 | 8 | **50** |
| v4.3.6 | 5 | 8 | 3 | 5 | **21** |
| v4.3.5 | 9 | 7 | 5 | 9 | **30** |
| v4.3.5-beta.9 *(beta)* | 7 | 3 | 5 | 3 | **18** |
| v4.3.5-beta.8 *(beta)* | 6 | 4 | 5 | 3 | **18** |
| v4.3.5-beta.7 *(beta)* | 6 | 4 | 3 | 3 | **16** |
| v4.3.5-beta.6 *(beta)* | 3 | 3 | 3 | 3 | **12** |
| v4.3.5-beta.5 *(beta)* | 2 | 6 | 3 | 3 | **14** |
| v4.3.5-beta.4 *(beta)* | 3 | 5 | 3 | 4 | **15** |
| v4.3.5-beta.3 *(beta)* | 8 | 9 | 3 | 3 | **23** |
| v4.3.5-beta.2 *(beta)* | 4 | 5 | 3 | 3 | **15** |
| v4.3.5-beta.1 *(beta)* | 3 | 2 | 3 | 5 | **13** |
| v4.3.4 | 45 | 31 | 9 | 24 | **109** |
| v4.3.3 | 7 | 10 | 7 | 5 | **29** |
| v4.3.3-beta.17 *(beta)* | 5 | 7 | 7 | 5 | **24** |
| v4.3.3-beta.16 *(beta)* | 5 | 21 | 5 | 0 | **31** |
| v4.3.3-beta.15 *(beta)* | 5 | 11 | 5 | 0 | **21** |
| v4.3.3-beta.14 *(beta)* | 3 | 6 | 3 | 0 | **12** |
| v4.3.3-beta.13 *(beta)* | 5 | 5 | 3 | 0 | **13** |
| v4.3.3-beta.12 *(beta)* | 5 | 8 | 6 | 0 | **19** |
| v4.3.3-beta.11 *(beta)* | 7 | 10 | 4 | 0 | **21** |
| v4.3.3-beta.10 *(beta)* | 5 | 5 | 3 | 0 | **13** |
| v4.3.3-beta.9 *(beta)* | 3 | 5 | 3 | 0 | **11** |
| v4.3.3-beta.8 *(beta)* | 3 | 5 | 3 | 0 | **11** |
| v4.3.3-beta.7 *(beta)* | 5 | 6 | 4 | 0 | **15** |
| v4.3.3-beta.6 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v4.3.3-beta.5 *(beta)* | 2 | 6 | 3 | 0 | **11** |
| v4.3.3-beta.4 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v4.3.3-beta.3 *(beta)* | 4 | 7 | 5 | 0 | **16** |
| v4.3.3-beta.2 *(beta)* | 2 | 6 | 5 | 0 | **13** |
| v4.3.3-beta.1 *(beta)* | 3 | 12 | 7 | 0 | **22** |
| v4.3.2 | 57 | 56 | 8 | 0 | **121** |
| v4.3.1 | 3 | 8 | 2 | 0 | **13** |
| v4.3.0 | 4 | 7 | 5 | 0 | **16** |
| v4.3.0-beta.49 *(beta)* | 4 | 5 | 3 | 0 | **12** |
| v4.3.0-beta.48 *(beta)* | 3 | 6 | 4 | 0 | **13** |
| v4.3.0-beta.47 *(beta)* | 4 | 5 | 3 | 0 | **12** |
| v4.3.0-beta.46 *(beta)* | 3 | 7 | 3 | 0 | **13** |
| v4.3.0-beta.45 *(beta)* | 4 | 5 | 3 | 0 | **12** |
| v4.3.0-beta.44 *(beta)* | 4 | 8 | 3 | 0 | **15** |
| v4.3.0-beta.43 *(beta)* | 3 | 6 | 3 | 0 | **12** |
| v4.3.0-beta.42 *(beta)* | 5 | 6 | 3 | 0 | **14** |
| v4.3.0-beta.41 *(beta)* | 4 | 7 | 3 | 0 | **14** |
| v4.3.0-beta.40 *(beta)* | 4 | 7 | 3 | 0 | **14** |
| v4.3.0-beta.39 *(beta)* | 2 | 7 | 3 | 0 | **12** |
| v4.3.0-beta.38 *(beta)* | 3 | 6 | 3 | 0 | **12** |
| v4.3.0-beta.37 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v4.3.0-beta.36 *(beta)* | 4 | 4 | 3 | 0 | **11** |
| v4.3.0-beta.35 *(beta)* | 4 | 5 | 3 | 0 | **12** |
| v4.3.0-beta.34 *(beta)* | 4 | 4 | 3 | 0 | **11** |
| v4.3.0-beta.33 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v4.3.0-beta.32 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v4.3.0-beta.31 *(beta)* | 3 | 6 | 3 | 0 | **12** |
| v4.3.0-beta.30 *(beta)* | 2 | 7 | 3 | 0 | **12** |
| v4.3.0-beta.29 *(beta)* | 4 | 7 | 3 | 0 | **14** |
| v4.3.0-beta.28 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v4.3.0-beta.27 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v4.3.0-beta.26 *(beta)* | 3 | 5 | 3 | 0 | **11** |
| v4.3.0-beta.25 *(beta)* | 2 | 4 | 5 | 0 | **11** |
| v4.3.0-beta.24 *(beta)* | 2 | 4 | 4 | 0 | **10** |
| v4.3.0-beta.23 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v4.3.0-beta.22 *(beta)* | 2 | 5 | 5 | 0 | **12** |
| v4.3.0-beta.21 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v4.3.0-beta.20 *(beta)* | 2 | 4 | 7 | 0 | **13** |
| v4.3.0-beta.19 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v4.3.0-beta.18 *(beta)* | 6 | 5 | 4 | 0 | **15** |
| v4.3.0-beta.17 *(beta)* | 5 | 8 | 4 | 0 | **17** |
| v4.3.0-beta.16 *(beta)* | 3 | 4 | 4 | 0 | **11** |
| v4.3.0-beta.15 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v4.3.0-beta.14 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v4.3.0-beta.13 *(beta)* | 2 | 6 | 3 | 0 | **11** |
| v4.3.0-beta.12 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v4.3.0-beta.11 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v4.3.0-beta.10 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v4.3.0-beta.9 *(beta)* | 3 | 5 | 3 | 0 | **11** |
| v4.3.0-beta.8 *(beta)* | 2 | 6 | 4 | 0 | **12** |
| v4.3.0-beta.7 *(beta)* | 4 | 4 | 3 | 0 | **11** |
| v4.3.0-beta.6 *(beta)* | 2 | 3 | 4 | 0 | **9** |
| v4.3.0-beta.5 *(beta)* | 4 | 5 | 5 | 0 | **14** |
| v4.2.7 | 57 | 49 | 9 | 0 | **115** |
| v4.2.6 | 5 | 3 | 4 | 0 | **12** |
| v4.3.0-beta.4 *(beta)* | 3 | 6 | 3 | 0 | **12** |
| v4.2.5 | 5 | 8 | 4 | 0 | **17** |
| v4.3.0-beta.3 *(beta)* | 3 | 7 | 3 | 0 | **13** |
| v4.2.4 | 4 | 5 | 3 | 0 | **12** |
| v4.2.3 | 8 | 4 | 3 | 0 | **15** |
| v4.3.0-beta.2 *(beta)* | 7 | 4 | 3 | 0 | **14** |
| v4.2.2 | 3 | 7 | 5 | 0 | **15** |
| v4.3.0-beta.1 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v4.2.1 | 5 | 6 | 3 | 0 | **14** |
| v4.2.0 | 22 | 14 | 6 | 0 | **42** |
| v4.1.5-beta.11 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v4.1.5-beta.10 *(beta)* | 5 | 5 | 2 | 0 | **12** |
| v4.1.5-beta.9 *(beta)* | 8 | 11 | 8 | 0 | **27** |
| v4.1.5-beta.8 *(beta)* | 7 | 12 | 9 | 0 | **28** |
| v4.1.5-beta.7 *(beta)* | 5 | 8 | 4 | 0 | **17** |
| v4.1.5-beta.6 *(beta)* | 6 | 7 | 5 | 0 | **18** |
| v4.1.5-beta.5 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v4.1.5-beta.4 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.5-beta.3 *(beta)* | 4 | 3 | 3 | 0 | **10** |
| v4.1.5-beta.2 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v4.1.5-beta.1 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v4.1.4 | 35 | 32 | 7 | 0 | **74** |
| v4.1.3 | 5 | 15 | 2 | 0 | **22** |
| v4.1.3-beta.21 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v4.1.3-beta.20 *(beta)* | 6 | 4 | 2 | 0 | **12** |
| v4.1.3-beta.19 *(beta)* | 5 | 3 | 2 | 0 | **10** |
| v4.1.3-beta.18 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v4.1.3-beta.17 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.3-beta.16 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.3-beta.15 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.3-beta.14 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v4.1.3-beta.13 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.3-beta.12 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v4.1.3-beta.11 *(beta)* | 3 | 4 | 4 | 0 | **11** |
| v4.1.3-beta.10 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v4.1.3-beta.9 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.3-beta.8 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.3-beta.7 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.3-beta.6 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v4.1.3-beta.5 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v4.1.3-beta.4 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v4.1.3-beta.3 *(beta)* | 2 | 5 | 4 | 0 | **11** |
| v4.1.3-beta.2 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.3-beta.1 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.2 | 19 | 22 | 3 | 0 | **44** |
| v4.1.2-beta.10 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.2-beta.9 *(beta)* | 3 | 3 | 3 | 0 | **9** |
| v4.1.2-beta.8 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.2-beta.7 *(beta)* | 3 | 3 | 3 | 0 | **9** |
| v4.1.2-beta.6 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v4.1.2-beta.5 *(beta)* | 3 | 3 | 3 | 0 | **9** |
| v4.1.2-beta.4 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.2-beta.3 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v4.1.2-beta.2 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v4.1.2-beta.1 *(beta)* | 2 | 4 | 4 | 0 | **10** |
| v4.1.1 | 31 | 17 | 2 | 0 | **50** |
| v4.1.0 | 16 | 10 | 4 | 0 | **30** |
| v4.0.2-beta.12 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v4.0.2-beta.11 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v4.0.2-beta.10 *(beta)* | 3 | 3 | 3 | 0 | **9** |
| v4.0.2-beta.9 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.0.2-beta.8 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.0.2-beta.7 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.0.2-beta.6 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.0.2-beta.5 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.0.2-beta.4 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.0.2-beta.3 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v4.0.2-beta.2 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.0.2-beta.1 *(beta)* | 2 | 5 | 4 | 0 | **11** |
| v4.0.1 | 4 | 10 | 2 | 0 | **16** |
| v4.0.0 | 5 | 10 | 2 | 0 | **17** |
| v4.0.0-beta.5 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v4.0.0-beta.4 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v4.0.0-beta.3 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v4.0.0-beta.2 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.0.0-beta.1 *(beta)* | 4 | 5 | 2 | 0 | **11** |
| v3.14.8-beta.222 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.14.8-beta.221 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v3.14.8-beta.220 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.219 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v3.14.8-beta.218 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.217 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.216 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.215 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.214 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.213 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.212 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.211 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.210 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.207 *(beta)* | 5 | 3 | 4 | 0 | **12** |
| v3.14.8-beta.206 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.205 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.204 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.203 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.202 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.14.8-beta.201 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.200 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.199 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.198 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.197 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.196 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.195 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.194 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.193 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.192 *(beta)* | 3 | 6 | 4 | 0 | **13** |
| v3.14.8-beta.191 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.190 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.189 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.188 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.187 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.186 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.185 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.14.8-beta.184 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.183 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.14.8-beta.182 *(beta)* | 5 | 7 | 5 | 0 | **17** |
| v3.14.8-beta.181 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.180 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.179 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.178 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.177 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.176 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.175 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.14.8-beta.174 *(beta)* | 4 | 7 | 4 | 0 | **15** |
| v3.14.8-beta.173 *(beta)* | 4 | 7 | 4 | 0 | **15** |
| v3.14.8-beta.172 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.14.8-beta.171 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v3.14.8-beta.170 *(beta)* | 0 | 3 | 0 | 0 | **3** |
| v3.14.8-beta.165 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.14.8-beta.162 *(beta)* | 3 | 3 | 1 | 0 | **7** |
| v3.14.8-beta.160 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.14.8-beta.159 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.158 *(beta)* | 3 | 1 | 0 | 0 | **4** |
| v3.14.8-beta.157 *(beta)* | 1 | 2 | 1 | 0 | **4** |
| v3.14.8-beta.156 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.155 *(beta)* | 4 | 7 | 4 | 0 | **15** |
| v3.14.8-beta.154 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.153 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.152 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.151 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.150 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.149 *(beta)* | 5 | 7 | 4 | 0 | **16** |
| v3.14.8-beta.148 *(beta)* | 3 | 5 | 3 | 0 | **11** |
| v3.14.8-beta.147 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.146 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.145 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.14.8-beta.144 *(beta)* | 4 | 5 | 2 | 0 | **11** |
| v3.14.8-beta.143 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.142 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.14.8-beta.141 *(beta)* | 4 | 4 | 3 | 0 | **11** |
| v3.14.8-beta.140 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.139 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.14.8-beta.138 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.137 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.136 *(beta)* | 3 | 5 | 3 | 0 | **11** |
| v3.14.8-beta.135 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.134 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.133 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.14.8-beta.132 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.131 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.130 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.129 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.128 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v3.14.8-beta.127 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.126 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.125 *(beta)* | 3 | 5 | 3 | 0 | **11** |
| v3.14.8-beta.124 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.123 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.122 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.14.8-beta.121 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.120 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.119 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.118 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.14.8-beta.117 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.116 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.115 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.114 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v3.14.8-beta.113 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.112 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.111 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.110 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.109 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.14.8-beta.108 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.14.8-beta.107 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v3.14.8-beta.106 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.105 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.104 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.103 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.102 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.101 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.100 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v3.14.8-beta.99 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.98 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.97 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.96 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.95 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.94 *(beta)* | 5 | 3 | 2 | 0 | **10** |
| v3.14.8-beta.93 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.92 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.91 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.90 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.89 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.88 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.87 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.86 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.85 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.84 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.83 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.82 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.81 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.80 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v3.14.8-beta.79 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.78 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.77 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.76 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v3.14.8-beta.75 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.74 *(beta)* | 6 | 3 | 2 | 0 | **11** |
| v3.14.8-beta.73 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.72 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.71 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.70 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v3.14.8-beta.69 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.68 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.67 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.66 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.65 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.64 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.63 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.62 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.14.8-beta.61 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.60 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.59 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.58 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.57 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.56 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.55 *(beta)* | 4 | 5 | 2 | 0 | **11** |
| v3.14.8-beta.54 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.53 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.52 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.51 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.50 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.49 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.48 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.47 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.46 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.14.8-beta.45 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.14.8-beta.44 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.43 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.42 *(beta)* | 4 | 7 | 4 | 0 | **15** |
| v3.14.8-beta.41 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.40 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.39 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.38 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.37 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.36 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.35 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.34 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.14.8-beta.33 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.32 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.31 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.30 *(beta)* | 3 | 3 | 3 | 0 | **9** |
| v3.14.8-beta.29 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.28 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.27 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.26 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.25 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.24 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.23 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.22 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.21 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.20 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.19 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.18 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.17 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.16 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v3.14.8-beta.15 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.14 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v3.14.8-beta.13 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.12 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.10 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.9 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.14.8-beta.8 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.14.8-beta.7 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.6 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.5 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.4 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.3 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.2 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.1 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.7 | 29 | 33 | 6 | 0 | **68** |
| v3.14.6 | 4 | 3 | 2 | 0 | **9** |
| v3.14.5 | 3 | 4 | 2 | 0 | **9** |
| v3.14.4 | 6 | 10 | 3 | 0 | **19** |
| v3.14.3 | 8 | 12 | 5 | 0 | **25** |
| v3.14.2 | 5 | 6 | 2 | 0 | **13** |
| v3.14.1 | 3 | 5 | 3 | 0 | **11** |
| v3.14.0 | 4 | 6 | 2 | 0 | **12** |
| v3.13.12-beta.35 *(beta)* | 4 | 7 | 2 | 0 | **13** |
| v3.13.12-beta.34 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.33 *(beta)* | 2 | 6 | 3 | 0 | **11** |
| v3.13.12-beta.32 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v3.13.12-beta.31 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.12-beta.30 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.29 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.12-beta.28 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.12-beta.27 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.12-beta.26 *(beta)* | 5 | 5 | 2 | 0 | **12** |
| v3.13.12-beta.25 *(beta)* | 5 | 6 | 4 | 0 | **15** |
| v3.13.12-beta.24 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.12-beta.23 *(beta)* | 6 | 7 | 3 | 0 | **16** |
| v3.13.12-beta.22 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.21 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.13.12-beta.20 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.12-beta.19 *(beta)* | 4 | 5 | 3 | 0 | **12** |
| v3.13.12-beta.18 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.12-beta.17 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.12-beta.16 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.15 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.12-beta.14 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.13 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.12 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.12-beta.11 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.12-beta.10 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.9 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.13.12-beta.8 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.7 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.13.12-beta.6 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.5 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.13.12-beta.4 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.12-beta.3 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.12-beta.2 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.12-beta.1 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.11 | 6 | 14 | 2 | 0 | **22** |
| v3.13.10 | 3 | 5 | 2 | 0 | **10** |
| v3.13.9 | 16 | 7 | 4 | 0 | **27** |
| v3.13.8 | 3 | 8 | 2 | 0 | **13** |
| v3.13.7 | 3 | 4 | 2 | 0 | **9** |
| v3.13.7-beta.5 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.7-beta.4 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.7-beta.3 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v3.13.7-beta.2 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.7-beta.1 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.13.6 | 10 | 9 | 3 | 0 | **22** |
| v3.13.6-beta.4 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.6-beta.3 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.6-beta.2 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.6-beta.1 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.5 | 7 | 12 | 2 | 0 | **21** |
| v3.13.4 | 6 | 7 | 2 | 0 | **15** |
| v3.13.4-beta.11 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.4-beta.10 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.4-beta.9 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.4-beta.8 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.4-beta.7 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.4-beta.6 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.4-beta.5 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.4-beta.4 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.4-beta.3 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v3.13.4-beta.2 *(beta)* | 2 | 5 | 4 | 0 | **11** |
| v3.13.4-beta.1 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.3 | 8 | 9 | 5 | 0 | **22** |
| v3.13.2 | 4 | 8 | 4 | 0 | **16** |
| v3.13.1 | 7 | 8 | 5 | 0 | **20** |
| v3.13.0 | 3 | 12 | 3 | 0 | **18** |
| v3.13.0-beta.143 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v3.13.0-beta.142 *(beta)* | 3 | 5 | 3 | 0 | **11** |
| v3.13.0-beta.141 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v3.13.0-beta.140 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.13.0-beta.139 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.13.0-beta.138 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.137 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.136 *(beta)* | 4 | 9 | 3 | 0 | **16** |
| v3.13.0-beta.135 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.13.0-beta.134 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.133 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.132 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.131 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.0-beta.130 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.129 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.128 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v3.13.0-beta.127 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.126 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.125 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.124 *(beta)* | 3 | 6 | 2 | 0 | **11** |
| v3.13.0-beta.123 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.122 *(beta)* | 3 | 10 | 2 | 0 | **15** |
| v3.13.0-beta.121 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.120 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.119 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v3.13.0-beta.118 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.117 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.13.0-beta.116 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.115 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.114 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.13.0-beta.113 *(beta)* | 4 | 9 | 2 | 0 | **15** |
| v3.13.0-beta.112 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v3.13.0-beta.111 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.110 *(beta)* | 3 | 8 | 2 | 0 | **13** |
| v3.13.0-beta.109 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.108 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.107 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.106 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v3.13.0-beta.105 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.13.0-beta.104 *(beta)* | 4 | 7 | 4 | 0 | **15** |
| v3.13.0-beta.103 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.102 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.101 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.100 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.99 *(beta)* | 5 | 3 | 2 | 0 | **10** |
| v3.13.0-beta.98 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.13.0-beta.97 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.96 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.95 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.0-beta.94 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.0-beta.93 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.92 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.91 *(beta)* | 7 | 11 | 7 | 0 | **25** |
| v3.13.0-beta.90 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.89 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.88 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.87 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.86 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.85 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.84 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.83 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.82 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.81 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.80 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.79 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.78 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.77 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.76 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.75 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.0-beta.74 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.73 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.72 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.13.0-beta.71 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.70 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.69 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.13.0-beta.68 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.67 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.66 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.65 *(beta)* | 5 | 6 | 4 | 0 | **15** |
| v3.13.0-beta.64 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.13.0-beta.63 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.62 *(beta)* | 4 | 6 | 2 | 0 | **12** |
| v3.13.0-beta.60 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.59 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.58 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.57 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.56 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.0-beta.55 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.0-beta.54 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.53 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.52 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.51 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.50 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.49 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.48 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.47 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.46 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.45 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.44 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.43 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.42 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.41 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.40 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v3.13.0-beta.39 *(beta)* | 8 | 13 | 9 | 0 | **30** |
| v3.13.0-beta.38 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.37 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.36 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.35 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v3.13.0-beta.34 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.13.0-beta.33 *(beta)* | 4 | 7 | 4 | 0 | **15** |
| v3.13.0-beta.32 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.31 *(beta)* | 6 | 10 | 7 | 0 | **23** |
| v3.13.0-beta.30 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.29 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.28 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.27 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.26 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.25 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v3.13.0-beta.24 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.13.0-beta.23 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.22 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.13.0-beta.21 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.20 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.0-beta.19 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.0-beta.18 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.17 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.16 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v3.13.0-beta.15 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v3.13.0-beta.14 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.13 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.13.0-beta.12 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.11 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.10 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v3.13.0-beta.9 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.8 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.7 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.6 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v3.13.0-beta.5 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.4 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v3.13.0-beta.3 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.2 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.12.1 | 32 | 25 | 3 | 0 | **60** |
| v3.13.0-beta.1 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.12.1-beta.1 *(beta)* | 4 | 3 | 3 | 0 | **10** |
| v3.12.0 | 7 | 10 | 2 | 0 | **19** |
| v3.12.0-beta.18 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v3.12.0-beta.17 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.16 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v3.12.0-beta.15 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.14 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.13 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.12 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v3.12.0-beta.11 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.10 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.12.0-beta.9 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.12.0-beta.8 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v3.12.0-beta.7 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.6 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.5 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.12.0-beta.4 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.3 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.12.0-beta.2 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.1 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.11.25 | 9 | 9 | 2 | 0 | **20** |
| v3.11.24 | 3 | 9 | 2 | 0 | **14** |
| v3.11.23 | 7 | 5 | 2 | 0 | **14** |
| v3.11.22 | 2 | 3 | 2 | 0 | **7** |
| v3.11.21 | 3 | 4 | 2 | 0 | **9** |
| v3.11.20 | 3 | 5 | 2 | 0 | **10** |
| v3.11.19 | 3 | 5 | 2 | 0 | **10** |
| v3.11.18 | 10 | 8 | 2 | 0 | **20** |
| v3.11.17 | 2 | 4 | 2 | 0 | **8** |
| v3.11.16 | 3 | 4 | 2 | 0 | **9** |
| v3.11.15 | 2 | 3 | 2 | 0 | **7** |
| v3.11.14 | 2 | 3 | 2 | 0 | **7** |
| v3.11.13 | 3 | 3 | 3 | 0 | **9** |
| v3.11.12 | 2 | 3 | 2 | 0 | **7** |
| v3.11.11 | 8 | 8 | 2 | 0 | **18** |
| v3.11.10 | 2 | 6 | 2 | 0 | **10** |
| v3.11.9 | 3 | 5 | 2 | 0 | **10** |
| v3.11.8 | 3 | 8 | 2 | 0 | **13** |
| v3.11.7 | 4 | 4 | 2 | 0 | **10** |
| v3.11.6 | 5 | 6 | 2 | 0 | **13** |
| v3.11.5 | 2 | 4 | 2 | 0 | **8** |
| v3.11.4 | 4 | 5 | 2 | 0 | **11** |
| v3.11.3 | 3 | 6 | 2 | 0 | **11** |
| v3.11.2 | 2 | 5 | 2 | 0 | **9** |
| v3.11.1 | 2 | 5 | 2 | 0 | **9** |
| v3.11.0 | 5 | 5 | 2 | 0 | **12** |
| v3.10.28 | 3 | 3 | 2 | 0 | **8** |
| v3.10.27 | 2 | 3 | 2 | 0 | **7** |
| v3.10.26 | 4 | 5 | 2 | 0 | **11** |
| v3.10.25 | 2 | 3 | 2 | 0 | **7** |
| v3.10.24 | 3 | 5 | 2 | 0 | **10** |
| v3.10.23 | 2 | 5 | 2 | 0 | **9** |
| v3.10.22 | 2 | 3 | 2 | 0 | **7** |
| v3.10.21 | 3 | 5 | 2 | 0 | **10** |
| v3.10.20 | 2 | 5 | 2 | 0 | **9** |
| v3.10.19 | 4 | 5 | 2 | 0 | **11** |
| v3.10.18 | 3 | 6 | 2 | 0 | **11** |
| v3.10.17 | 2 | 3 | 2 | 0 | **7** |
| v3.10.16 | 2 | 7 | 2 | 0 | **11** |
| v3.10.15 | 5 | 5 | 2 | 0 | **12** |
| v3.10.14 | 3 | 4 | 2 | 0 | **9** |
| v3.10.13 | 2 | 5 | 2 | 0 | **9** |
| v3.10.12 | 2 | 3 | 2 | 0 | **7** |
| v3.10.11 | 2 | 3 | 2 | 0 | **7** |
| v3.10.10 | 2 | 7 | 2 | 0 | **11** |
| v3.10.9 | 3 | 5 | 2 | 0 | **10** |
| v3.10.8 | 2 | 7 | 2 | 0 | **11** |
| v3.10.7 | 2 | 4 | 2 | 0 | **8** |
| v3.10.6 | 2 | 3 | 2 | 0 | **7** |
| v3.10.5 | 6 | 9 | 6 | 0 | **21** |
| v3.10.4 | 2 | 5 | 2 | 0 | **9** |
| v3.10.3 | 2 | 4 | 2 | 0 | **8** |
| v3.10.2 | 9 | 10 | 4 | 0 | **23** |
| v3.10.1 | 2 | 3 | 2 | 0 | **7** |
| v3.10.0 | 3 | 4 | 2 | 0 | **9** |
| v3.9.31 | 2 | 3 | 2 | 0 | **7** |
| v3.9.30 | 3 | 4 | 2 | 0 | **9** |
| v3.9.29 | 4 | 7 | 2 | 0 | **13** |
| v3.9.28 | 3 | 5 | 2 | 0 | **10** |
| v3.9.27 | 2 | 4 | 2 | 0 | **8** |
| v3.9.26 | 2 | 6 | 2 | 0 | **10** |
| v3.9.25 | 2 | 4 | 3 | 0 | **9** |
| v3.9.24 | 2 | 5 | 2 | 0 | **9** |
| v3.9.23 | 3 | 5 | 2 | 0 | **10** |
| v3.9.22 | 2 | 3 | 2 | 0 | **7** |
| v3.9.21 | 6 | 7 | 2 | 0 | **15** |
| v3.9.20 | 2 | 5 | 2 | 0 | **9** |
| v3.9.19 | 4 | 3 | 2 | 0 | **9** |
| v3.9.18 | 2 | 6 | 3 | 0 | **11** |
| v3.9.17 | 3 | 4 | 2 | 0 | **9** |
| v3.9.16 | 4 | 6 | 2 | 0 | **12** |
| v3.9.15 | 3 | 5 | 2 | 0 | **10** |
| v3.9.14 | 3 | 3 | 2 | 0 | **8** |
| v3.9.13 | 4 | 5 | 4 | 0 | **13** |
| v3.9.12 | 2 | 5 | 2 | 0 | **9** |
| v3.9.11 | 2 | 5 | 2 | 0 | **9** |
| v3.9.10 | 2 | 4 | 3 | 0 | **9** |
| v3.9.9 | 3 | 3 | 2 | 0 | **8** |
| v3.9.8 | 2 | 3 | 2 | 0 | **7** |
| v3.9.7 | 2 | 4 | 2 | 0 | **8** |
| v3.9.6 | 3 | 5 | 2 | 0 | **10** |
| v3.9.5 | 3 | 4 | 2 | 0 | **9** |
| v3.9.4 | 2 | 3 | 2 | 0 | **7** |
| v3.9.3 | 3 | 3 | 2 | 0 | **8** |
| v3.9.2 | 2 | 3 | 3 | 0 | **8** |
| v3.9.1 | 4 | 4 | 2 | 0 | **10** |
| v3.9.0 | 2 | 3 | 3 | 0 | **8** |
| v3.8.19 | 6 | 7 | 3 | 0 | **16** |
| v3.8.18 | 3 | 5 | 3 | 0 | **11** |
| v3.8.17 | 5 | 9 | 4 | 0 | **18** |
| v3.8.16 | 6 | 12 | 4 | 0 | **22** |
| v3.8.15 | 3 | 4 | 3 | 0 | **10** |
| v3.8.14 | 3 | 5 | 3 | 0 | **11** |
| v3.8.13 | 2 | 7 | 2 | 0 | **11** |
| v3.8.12 | 9 | 5 | 3 | 0 | **17** |
| v3.8.11 | 7 | 5 | 3 | 0 | **15** |
| v3.8.10 | 3 | 6 | 2 | 0 | **11** |
| v3.8.9 | 4 | 4 | 2 | 0 | **10** |
| v3.8.8 | 6 | 11 | 3 | 0 | **20** |
| v3.8.7 | 2 | 4 | 2 | 0 | **8** |
| v3.8.6 | 5 | 7 | 2 | 0 | **14** |
| v3.8.5 | 4 | 8 | 2 | 0 | **14** |
| v3.8.4 | 18 | 7 | 3 | 0 | **28** |
| v3.8.3 | 14 | 5 | 2 | 0 | **21** |
| v3.8.2 | 4 | 5 | 3 | 0 | **12** |
| v3.8.1 | 3 | 5 | 3 | 0 | **11** |
| v3.8.0 | 15 | 11 | 5 | 0 | **31** |
| v3.8.0-beta.31 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.8.0-beta.30 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v3.8.0-beta.29 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.8.0-beta.28 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.8.0-beta.27 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.8.0-beta.26 *(beta)* | 3 | 6 | 2 | 0 | **11** |
| v3.8.0-beta.25 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.8.0-beta.24 *(beta)* | 9 | 13 | 9 | 0 | **31** |
| v3.8.0-beta.23 *(beta)* | 8 | 12 | 9 | 0 | **29** |
| v3.8.0-beta.22 *(beta)* | 3 | 5 | 3 | 0 | **11** |
| v3.8.0-beta.21 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.8.0-beta.20 *(beta)* | 7 | 6 | 4 | 0 | **17** |
| v3.8.0-beta.19 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.8.0-beta.18 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.8.0-beta.17 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v3.8.0-beta.16 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.8.0-beta.15 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.8.0-beta.14 *(beta)* | 8 | 5 | 2 | 0 | **15** |
| v3.8.0-beta.13 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.8.0-beta.12 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.8.0-beta.11 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.8.0-beta.10 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.8.0-beta.9 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.7.42 | 15 | 6 | 2 | 0 | **23** |
| v3.8.0-beta.8 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v3.8.0-beta.6 *(beta)* | 4 | 5 | 2 | 0 | **11** |
| v3.7.41 | 3 | 4 | 2 | 0 | **9** |
| v3.8.0-beta.5 *(beta)* | 6 | 11 | 7 | 0 | **24** |
| v3.8.0-beta.4 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.7.40 | 4 | 4 | 3 | 0 | **11** |
| v3.7.39 | 3 | 6 | 2 | 0 | **11** |
| v3.8.0-beta.3 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v3.8.0-beta.2 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.8.0-beta.1 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.7.38 | 4 | 31 | 2 | 0 | **37** |
| v3.7.37 | 3 | 13 | 2 | 0 | **18** |
| v3.7.36 | 4 | 6 | 2 | 0 | **12** |
| v3.7.35 | 2 | 6 | 2 | 0 | **10** |
| v3.7.34 | 3 | 6 | 2 | 0 | **11** |
| v3.7.33 | 3 | 7 | 3 | 0 | **13** |
| v3.7.32 | 3 | 7 | 2 | 0 | **12** |
| v3.7.31 | 3 | 6 | 3 | 0 | **12** |
| v3.7.30 | 2 | 6 | 2 | 0 | **10** |
| v3.7.29 | 2 | 8 | 2 | 0 | **12** |
| v3.7.28 | 2 | 7 | 2 | 0 | **11** |
| v3.7.27 | 5 | 10 | 5 | 0 | **20** |
| v3.7.26 | 4 | 8 | 5 | 0 | **17** |
| v3.7.25 | 4 | 6 | 2 | 0 | **12** |
| v3.7.24 | 4 | 6 | 2 | 0 | **12** |
| v3.7.23 | 2 | 7 | 2 | 0 | **11** |
| v3.7.22 | 4 | 10 | 4 | 0 | **18** |
| v3.7.21 | 3 | 8 | 2 | 0 | **13** |
| v3.7.20 | 2 | 7 | 2 | 0 | **11** |
| v3.7.19 | 6 | 8 | 2 | 0 | **16** |
| v3.7.18 | 2 | 7 | 2 | 0 | **11** |
| v3.7.17 | 3 | 7 | 2 | 0 | **12** |
| v3.7.16 | 2 | 6 | 2 | 0 | **10** |
| v3.7.15 | 3 | 9 | 2 | 0 | **14** |
| v3.7.14 | 5 | 8 | 2 | 0 | **15** |
| v3.7.13 | 2 | 8 | 2 | 0 | **12** |
| v3.7.12 | 2 | 7 | 2 | 0 | **11** |
| v3.7.11 | 5 | 10 | 5 | 0 | **20** |
| v3.7.10 | 4 | 10 | 2 | 0 | **16** |
| v3.7.9 | 2 | 13 | 2 | 0 | **17** |
| v3.7.8 | 2 | 13 | 2 | 0 | **17** |
| v3.7.7 | 2 | 7 | 2 | 0 | **11** |
| v3.7.6 | 2 | 9 | 2 | 0 | **13** |
| v3.7.5 | 7 | 10 | 3 | 0 | **20** |
| v3.7.4 | 3 | 11 | 2 | 0 | **16** |
| v3.7.3 | 2 | 11 | 2 | 0 | **15** |
| v3.7.2 | 5 | 10 | 5 | 0 | **20** |
| v3.7.1 | 2 | 43 | 4 | 0 | **49** |
| v3.7.0 | 5 | 38 | 5 | 0 | **48** |
| v3.6.7 | 5 | 45 | 5 | 0 | **55** |
| v3.6.6 | 6 | 35 | 4 | 0 | **45** |
| v3.6.5 | 5 | 45 | 5 | 0 | **55** |
| v3.6.4 | 5 | 51 | 5 | 0 | **61** |
| v3.6.3 | 2 | 7 | 3 | 0 | **12** |
| v3.6.2 | 2 | 6 | 2 | 0 | **10** |
| v3.6.1 | 2 | 9 | 2 | 0 | **13** |
| v3.6.0 | 5 | 12 | 6 | 0 | **23** |
| v3.5.13 | 3 | 7 | 5 | 0 | **15** |
| v3.5.12 | 2 | 7 | 3 | 0 | **12** |
| v3.5.11 | 2 | 6 | 2 | 0 | **10** |
| v3.5.10 | 3 | 6 | 3 | 0 | **12** |
| v3.5.9 | 4 | 6 | 2 | 0 | **12** |
| v3.5.8 | 3 | 8 | 2 | 0 | **13** |
| v3.5.7 | 3 | 7 | 2 | 0 | **12** |
| v3.5.6 | 2 | 7 | 2 | 0 | **11** |
| v3.5.5 | 2 | 9 | 2 | 0 | **13** |
| v3.5.4 | 2 | 6 | 2 | 0 | **10** |
| v3.5.3 | 2 | 7 | 2 | 0 | **11** |
| v3.5.2 | 3 | 7 | 2 | 0 | **12** |
| v3.5.1 | 2 | 8 | 2 | 0 | **12** |
| v3.5.0 | 3 | 10 | 3 | 0 | **16** |
| v3.5.0-beta.6 *(beta)* | 2 | 7 | 4 | 0 | **13** |
| v3.5.0-beta.5 *(beta)* | 2 | 6 | 4 | 0 | **12** |
| v3.2.9 | 5 | 7 | 0 | 0 | **12** |
| v3.5.0-beta.4 *(beta)* | 2 | 8 | 3 | 0 | **13** |
| v3.5.0-beta.3 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v3.5.0-beta.2 *(beta)* | 2 | 8 | 2 | 0 | **12** |
| v3.5.0-beta.1 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v3.2.8 | 5 | 11 | 0 | 0 | **16** |
| v3.2.7 | 2 | 9 | 0 | 0 | **11** |
| v3.2.6 | 2 | 6 | 0 | 0 | **8** |
| v3.2.5 | 2 | 5 | 0 | 0 | **7** |
| v3.2.4 | 2 | 5 | 0 | 0 | **7** |
| v3.2.3 | 2 | 4 | 0 | 0 | **6** |
| v3.2.2 | 2 | 5 | 0 | 0 | **7** |
| v3.2.1 | 2 | 4 | 0 | 0 | **6** |
| v3.2.0 | 2 | 5 | 0 | 0 | **7** |
| v3.2.0-beta.3 *(beta)* | 3 | 8 | 0 | 0 | **11** |
| v3.2.0-beta.2 *(beta)* | 2 | 6 | 0 | 0 | **8** |
| v3.2.0-beta.1 *(beta)* | 4 | 7 | 0 | 0 | **11** |
| v3.1.4 | 2 | 5 | 0 | 0 | **7** |
| v3.1.3 | 2 | 6 | 0 | 0 | **8** |
| v3.1.2 | 2 | 5 | 0 | 0 | **7** |
| v3.1.1 | 3 | 7 | 0 | 0 | **10** |
| v3.1.0 | 5 | 7 | 0 | 0 | **12** |
| v3.0.2 | 4 | 7 | 0 | 0 | **11** |
| v3.0.1 | 3 | 4 | 0 | 0 | **7** |
| v3.0.0 | 7 | 10 | 0 | 0 | **17** |
| v3.0.0-beta.10 *(beta)* | 5 | 19 | 0 | 0 | **24** |
| v3.0.0-beta.9 *(beta)* | 2 | 5 | 0 | 0 | **7** |
| v3.0.0-beta.8 *(beta)* | 4 | 5 | 0 | 0 | **9** |
| v3.0.0-beta.7 *(beta)* | 3 | 4 | 0 | 0 | **7** |
| v3.0.0-beta.6 *(beta)* | 3 | 4 | 0 | 0 | **7** |
| v3.0.0-beta.5 *(beta)* | 2 | 4 | 0 | 0 | **6** |
| v3.0.0-beta.4 *(beta)* | 3 | 5 | 0 | 0 | **8** |
| v3.0.0-beta.3 *(beta)* | 3 | 4 | 0 | 0 | **7** |
| v3.0.0-beta.2 *(beta)* | 7 | 4 | 0 | 0 | **11** |
| v3.0.0-beta.1 *(beta)* | 10 | 4 | 0 | 0 | **14** |
| v2.11.0 | 0 | 6 | 0 | 0 | **6** |
| v2.10.3 | 0 | 6 | 0 | 0 | **6** |
| v2.10.2 | 0 | 9 | 0 | 0 | **9** |
| v2.10.1 | 0 | 8 | 0 | 0 | **8** |
| v2.10.0 | 0 | 5 | 0 | 0 | **5** |
| v2.9.4 | 0 | 6 | 0 | 0 | **6** |
| v2.9.3 | 0 | 5 | 0 | 0 | **5** |
| v2.9.2 | 0 | 5 | 0 | 0 | **5** |
| v2.9.1 | 0 | 4 | 0 | 0 | **4** |
| v2.9.0 | 0 | 11 | 0 | 0 | **11** |
| v2.8.1 | 0 | 7 | 0 | 0 | **7** |
| v2.8.0 | 0 | 5 | 0 | 0 | **5** |
| v2.7.0 | 0 | 6 | 0 | 0 | **6** |
| v2.6.0 | 0 | 6 | 0 | 0 | **6** |
| v2.5.0 | 0 | 6 | 0 | 0 | **6** |
| v2.4.1 | 0 | 11 | 0 | 0 | **11** |
| v2.4.0 | 0 | 4 | 0 | 0 | **4** |
| v2.3.3 | 0 | 4 | 0 | 0 | **4** |
| v2.3.2 | 0 | 3 | 0 | 0 | **3** |
| v2.3.1 | 0 | 3 | 0 | 0 | **3** |
| v2.3.0 | 0 | 2 | 0 | 0 | **2** |
| v2.2.3 | 0 | 14 | 0 | 0 | **14** |
| v2.2.2 | 0 | 11 | 0 | 0 | **11** |
| v2.2.1 | 0 | 5 | 0 | 0 | **5** |
| v2.2.0 | 0 | 8 | 0 | 0 | **8** |
| v2.1.4 | 0 | 4 | 0 | 0 | **4** |
| v2.1.2 | 0 | 12 | 0 | 0 | **12** |
| v2.1.1 | 0 | 9 | 0 | 0 | **9** |
| v2.1.0 | 0 | 5 | 0 | 0 | **5** |
| v2.0.9 | 0 | 10 | 0 | 0 | **10** |
| v2.0.8 | 0 | 4 | 0 | 0 | **4** |
| v2.0.7 | 0 | 5 | 0 | 0 | **5** |
| v2.0.6 | 0 | 5 | 0 | 0 | **5** |
| v2.0.5 | 0 | 7 | 0 | 0 | **7** |
| v2.0.4 | 0 | 9 | 0 | 0 | **9** |
| v2.0.3 | 0 | 8 | 0 | 0 | **8** |
| v2.0.2 | 0 | 4 | 0 | 0 | **4** |
| v2.0.1 | 0 | 2 | 0 | 0 | **2** |
| v2.0.0 | 0 | 6 | 0 | 0 | **6** |
| v1.7.1 | 0 | 8 | 0 | 0 | **8** |
| v1.7.0 | 0 | 5 | 0 | 0 | **5** |
| v1.6.1 | 0 | 5 | 0 | 0 | **5** |
| v1.6.0 | 0 | 5 | 0 | 0 | **5** |
| v1.5.2 | 0 | 5 | 0 | 0 | **5** |
| v1.5.1 | 0 | 7 | 0 | 0 | **7** |
| v1.5.0 | 0 | 5 | 0 | 0 | **5** |
| v1.4.0 | 0 | 5 | 0 | 0 | **5** |
| v1.3.1 | 0 | 7 | 0 | 0 | **7** |
| v1.3.0 | 0 | 5 | 0 | 0 | **5** |
| v1.2.0 | 0 | 5 | 0 | 0 | **5** |
| v1.1.6 | 0 | 6 | 0 | 0 | **6** |
| v1.1.5 | 0 | 4 | 0 | 0 | **4** |
| v1.1.3 | 0 | 11 | 0 | 0 | **11** |
| v1.1.2 | 0 | 5 | 0 | 0 | **5** |
| v1.1.1 | 0 | 3 | 0 | 0 | **3** |
| v1.1.0 | 0 | 3 | 0 | 0 | **3** |
| v1.0.3 | 0 | 5 | 0 | 0 | **5** |
| v1.0.2 | 0 | 5 | 0 | 0 | **5** |
| v1.0.1 | 0 | 5 | 0 | 0 | **5** |
| v1.0.0 | 0 | 3 | 0 | 0 | **3** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | arm64 | x86_64 | universal | Total |
|----------|-------|-------|-------|-------|
| 🪟 Windows | 1071 | 2197 | 0 | **3268** |
| 🍎 macOS | 2459 | 1345 | 1371 | **5175** |
| 🐧 Linux | 1004 | 1174 | 0 | **2178** |
| 🍺 Homebrew | 209 | 74 | 0 | **283** |

*💡 Low-volume builds (<2% of lifetime downloads), candidates to stop shipping: 🍺 Homebrew arm64 (209, 1.9%); 🍺 Homebrew x86_64 (74, 0.7%).*

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v4.3.20 | 124 | 2026-10-29 |
| v4.3.2 | 121 | 2026-09-28 |
| v4.2.7 | 115 | 2026-09-12 |
| v4.3.4 | 109 | 2026-10-10 |
| v4.3.19 | 88 | 2026-10-28 |
| v4.1.4 | 74 | 2026-08-28 |
| v3.14.7 | 68 | 2026-07-22 |
| v3.6.4 | 61 | 2026-05-17 |
| v3.12.1 | 60 | 2026-06-25 |
| v3.6.7 | 55 | 2026-05-18 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear. 🍺 is Homebrew (its own copies of the Mac file, not counted again under 🍎); releases without Homebrew copies show 0.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | 🍺 | All downloads (incl. Homebrew) |
|---------|-----------|-----|----|----|----|----|------------------------------|
| v4.3.35 | 2026-11-14 | 1d | 0 | 0 | 0 | 0 | **0** |
| v4.3.34 | 2026-11-14 | 1d | 3 | 3 | 2 | 6 | **14** |
| v4.3.33 | 2026-11-13 | 2d | 14 | 8 | 3 | 8 | **33** |
| v4.3.32 | 2026-11-12 | 3d | 10 | 8 | 2 | 8 | **28** |
| v4.3.31 | 2026-11-11 | 4d | 5 | 3 | 4 | 6 | **18** |
| v4.3.30 | 2026-11-10 | 5d | 14 | 11 | 3 | 6 | **34** |
| v4.3.29 | 2026-11-09 | 6d | 7 | 4 | 3 | 4 | **18** |
| v4.3.28 | 2026-11-07 | 8d | 20 | 8 | 2 | 8 | **38** |
| v4.3.27 | 2026-11-07 | 8d | 6 | 3 | 2 | 2 | **13** |
| v4.3.26 | 2026-11-07 | 8d | 3 | 3 | 2 | 1 | **9** |
| v4.3.25 | 2026-11-04 | 11d | 20 | 10 | 3 | 7 | **40** |
| v4.3.24 | 2026-11-04 | 11d | 5 | 8 | 2 | 3 | **18** |
| v4.3.23 | 2026-11-03 | 12d | 8 | 10 | 3 | 6 | **27** |
| v4.3.22 | 2026-11-03 | 12d | 13 | 8 | 6 | 6 | **33** |
| v4.3.21 | 2026-11-02 | 13d | 12 | 10 | 3 | 6 | **31** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq)**

---

# ChromIQ-Patches

![downloads](https://img.shields.io/badge/downloads-59-212121) ![clones](https://img.shields.io/badge/clones-404-2196F3) ![views](https://img.shields.io/badge/views-149-4CAF50) ![releases](https://img.shields.io/badge/releases-5-6f42c1) ![latest stable v1.2.1](https://img.shields.io/badge/latest%20stable%20v1.2.1-36-212121 "Downloads of the latest stable release, all platforms incl. Homebrew")

*Tracking since **2026-07-02** (135 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~135 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 7 | 4 | ▲ +75.0% |
| Views | 8 | 5 | ▲ +60.0% |
| Downloads | 12 | 1 | ▲ +1100.0% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 32 | 30 |
| Last 90 Days | 75 | 72 |
| Lifetime | 404 | 228 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 32 | 30 | 2 | 6.2% |
| Last 90 Days | 75 | 72 | 3 | 4.0% |
| Lifetime | 404 | 228 | 176 | 43.6% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 31 | 19 |
| Last 90 Days | 67 | 40 |
| Lifetime | 149 | 74 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 19 | — |
| 🗅️ Unique cloners | 30 | 157.9% |
| 📥 Downloads | 13 | 68.4% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 2

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 6 | 4 |
| itsab1989.github.io | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 31 | 19 | 12 | 38.7% |
| Last 90 Days | 67 | 40 | 27 | 40.3% |
| Lifetime | 149 | 74 | 75 | 50.3% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 3 | 9 | 22 |
| 🍎 macOS | 5 | 8 | 29 |
| 🐧 Linux | 5 | 5 | 8 |
| **All downloads (incl. Homebrew)** | **13** | **22** | **59** |

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days | all | **13** | 3 | 5 | 5 | 0 |
| 30 days | stable | **13** | 3 | 5 | 5 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days | all | **22** | 9 | 8 | 5 | 0 |
| 90 days | stable | **22** | 9 | 8 | 5 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-07-03** on; the stable/beta split from **2026-07-03**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v1.2.1` - **36** downloads (published 2026-07-07)

<details>
<summary><strong>📦 Per-version downloads</strong> (5 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v1.2.1 | 13 | 17 | 6 | 0 | **36** |
| v1.2.0 | 5 | 7 | 2 | 0 | **14** |
| v1.1.0 | 0 | 1 | 0 | 0 | **1** |
| v1.0.1 | 1 | 3 | 0 | 0 | **4** |
| v1.0.0 | 3 | 1 | 0 | 0 | **4** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | arm64 | x86_64 | universal | Total |
|----------|-------|-------|-------|-------|
| 🪟 Windows | 1 | 21 | 0 | **22** |
| 🍎 macOS | 19 | 4 | 6 | **29** |
| 🐧 Linux | 1 | 7 | 0 | **8** |

*💡 Low-volume builds (<2% of lifetime downloads), candidates to stop shipping: 🪟 Windows arm64 (1, 1.7%); 🐧 Linux arm64 (1, 1.7%).*

**Top 5 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.2.1 | 36 | 2026-07-07 |
| v1.2.0 | 14 | 2026-07-03 |
| v1.0.1 | 4 | 2026-07-02 |
| v1.0.0 | 4 | 2026-07-02 |
| v1.1.0 | 1 | 2026-07-02 |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq-patches)**

---

# ChromIQ-Gamut-Viewer

![downloads](https://img.shields.io/badge/downloads-44-212121) ![clones](https://img.shields.io/badge/clones-2506-2196F3) ![views](https://img.shields.io/badge/views-84-4CAF50) ![releases](https://img.shields.io/badge/releases-96-6f42c1) ![latest stable v2.54.0](https://img.shields.io/badge/latest%20stable%20v2.54.0-10-212121 "Downloads of the latest stable release, all platforms incl. Homebrew")

*Tracking since **2026-08-13** (93 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~93 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 1 | 2 | ▼ -50.0% |
| Views | 7 | 3 | ▲ +133.3% |
| Downloads | 3 | 2 | ▲ +50.0% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 8 | 8 |
| Last 90 Days | 1716 | 350 |
| Lifetime | 2506 | 530 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 8 | 8 | 0 | 0.0% |
| Last 90 Days | 1716 | 350 | 1366 | 79.6% |
| Lifetime | 2506 | 530 | 1976 | 78.9% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 20 | 7 |
| Last 90 Days | 82 | 23 |
| Lifetime | 84 | 24 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 7 | — |
| 🗅️ Unique cloners | 8 | 114.3% |
| 📥 Downloads | 5 | 71.4% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 1

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 20 | 7 | 13 | 65.0% |
| Last 90 Days | 82 | 23 | 59 | 72.0% |
| Lifetime | 84 | 24 | 60 | 71.4% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 2 | 10 | 12 |
| 🍎 macOS | 3 | 22 | 26 |
| 🐧 Linux | 0 | 4 | 6 |
| **All downloads (incl. Homebrew)** | **5** | **36** | **44** |

*ℹ️ Not counted above: 14 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days | all | **5** | 2 | 3 | 0 | 0 |
| 30 days | stable | **5** | 2 | 3 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days | all | **36** | 10 | 22 | 4 | 0 |
| 90 days | stable | **36** | 10 | 22 | 4 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-08-15** on; the stable/beta split from **2026-08-15**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v2.54.0` - **10** downloads (published 2026-08-31)

<details>
<summary><strong>📦 Per-version downloads</strong> (96 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v2.54.0 | 3 | 7 | 0 | 0 | **10** |
| v2.53.2 | 0 | 1 | 0 | 0 | **1** |
| v2.53.1 | 0 | 1 | 0 | 0 | **1** |
| v2.53.0 | 0 | 1 | 0 | 0 | **1** |
| v2.52.1 | 1 | 4 | 0 | 0 | **5** |
| v2.52.0 | 0 | 0 | 0 | 0 | **0** |
| v2.51.0 | 0 | 0 | 0 | 0 | **0** |
| v2.50.5 | 0 | 0 | 0 | 0 | **0** |
| v2.50.4 | 0 | 0 | 0 | 0 | **0** |
| v2.50.3 | 0 | 0 | 0 | 0 | **0** |
| v2.50.2 | 0 | 0 | 0 | 0 | **0** |
| v2.50.1 | 2 | 2 | 2 | 0 | **6** |
| v2.50.0 | 0 | 0 | 0 | 0 | **0** |
| v2.49.0 | 0 | 0 | 0 | 0 | **0** |
| v2.48.0 | 0 | 0 | 0 | 0 | **0** |
| v2.47.0 | 0 | 0 | 0 | 0 | **0** |
| v2.46.0 | 0 | 0 | 0 | 0 | **0** |
| v2.45.1 | 0 | 0 | 0 | 0 | **0** |
| v2.45.0 | 0 | 0 | 0 | 0 | **0** |
| v2.44.0 | 0 | 0 | 0 | 0 | **0** |
| v2.43.1 | 1 | 0 | 0 | 0 | **1** |
| v2.43.0 | 0 | 2 | 0 | 0 | **2** |
| v2.42.0 | 0 | 0 | 0 | 0 | **0** |
| v2.41.0 | 0 | 0 | 0 | 0 | **0** |
| v2.40.2 | 0 | 0 | 0 | 0 | **0** |
| v2.40.1 | 0 | 0 | 0 | 0 | **0** |
| v2.40.0 | 0 | 0 | 0 | 0 | **0** |
| v2.39.6 | 0 | 0 | 0 | 0 | **0** |
| v2.39.5 | 0 | 0 | 0 | 0 | **0** |
| v2.39.4 | 0 | 0 | 0 | 0 | **0** |
| v2.39.3 | 0 | 0 | 0 | 0 | **0** |
| v2.39.2 | 0 | 0 | 0 | 0 | **0** |
| v2.39.1 | 0 | 0 | 0 | 0 | **0** |
| v2.39.0 | 1 | 1 | 0 | 0 | **2** |
| v2.38.0 | 1 | 0 | 0 | 0 | **1** |
| v2.37.0 | 0 | 0 | 0 | 0 | **0** |
| v2.36.0 | 0 | 0 | 0 | 0 | **0** |
| v2.35.0 | 0 | 0 | 0 | 0 | **0** |
| v2.34.0 | 0 | 0 | 0 | 0 | **0** |
| v2.33.0 | 0 | 0 | 0 | 0 | **0** |
| v2.32.0 | 0 | 0 | 0 | 0 | **0** |
| v2.31.0 | 0 | 0 | 0 | 0 | **0** |
| v2.30.0 | 0 | 0 | 0 | 0 | **0** |
| v2.29.0 | 0 | 0 | 0 | 0 | **0** |
| v2.28.0 | 0 | 0 | 0 | 0 | **0** |
| v2.27.0 | 0 | 0 | 0 | 0 | **0** |
| v2.26.0 | 0 | 0 | 0 | 0 | **0** |
| v2.25.0 | 0 | 0 | 0 | 0 | **0** |
| v2.24.0 | 0 | 1 | 0 | 0 | **1** |
| v2.23.0 | 0 | 0 | 0 | 0 | **0** |
| v2.22.0 | 0 | 0 | 0 | 0 | **0** |
| v2.21.0 | 1 | 2 | 2 | 0 | **5** |
| v2.20.2 | 0 | 0 | 0 | 0 | **0** |
| v2.20.0 | 0 | 0 | 0 | 0 | **0** |
| v2.19.0 | 0 | 0 | 0 | 0 | **0** |
| v2.18.0 | 0 | 0 | 0 | 0 | **0** |
| v2.17.0 | 0 | 0 | 0 | 0 | **0** |
| v2.16.0 | 0 | 0 | 0 | 0 | **0** |
| v2.15.1 | 0 | 0 | 0 | 0 | **0** |
| v2.15.0 | 0 | 0 | 0 | 0 | **0** |
| v2.14.0 | 0 | 0 | 0 | 0 | **0** |
| v2.13.0 | 0 | 0 | 0 | 0 | **0** |
| v2.12.0 | 0 | 0 | 0 | 0 | **0** |
| v2.11.0 | 0 | 0 | 0 | 0 | **0** |
| v2.10.0 | 0 | 0 | 0 | 0 | **0** |
| v2.9.0 | 0 | 0 | 0 | 0 | **0** |
| v2.8.0 | 0 | 0 | 0 | 0 | **0** |
| v2.7.0 | 0 | 0 | 0 | 0 | **0** |
| v2.6.0 | 0 | 0 | 0 | 0 | **0** |
| v2.5.0 | 0 | 0 | 0 | 0 | **0** |
| v2.4.0 | 0 | 0 | 0 | 0 | **0** |
| v2.3.0 | 0 | 0 | 0 | 0 | **0** |
| v2.2.1 | 1 | 0 | 0 | 0 | **1** |
| v2.2.0 | 0 | 0 | 0 | 0 | **0** |
| v2.1.0 | 0 | 0 | 0 | 0 | **0** |
| v2.0.1 | 0 | 0 | 0 | 0 | **0** |
| v2.0.0 | 0 | 0 | 0 | 0 | **0** |
| v1.9.6 | 0 | 0 | 0 | 0 | **0** |
| v1.9.2 | 0 | 0 | 0 | 0 | **0** |
| v1.9.1 | 0 | 0 | 0 | 0 | **0** |
| v1.9.0 | 0 | 0 | 0 | 0 | **0** |
| v1.8.0 | 0 | 0 | 0 | 0 | **0** |
| v1.7.1 | 0 | 0 | 0 | 0 | **0** |
| v1.7.0 | 0 | 0 | 0 | 0 | **0** |
| v1.6.1 | 0 | 0 | 0 | 0 | **0** |
| v1.6.0 | 0 | 0 | 0 | 0 | **0** |
| v1.5.2 | 0 | 2 | 0 | 0 | **2** |
| v1.5.1 | 0 | 0 | 0 | 0 | **0** |
| v1.5.0 | 0 | 0 | 0 | 0 | **0** |
| v1.4.0 | 0 | 0 | 0 | 0 | **0** |
| v1.3.1 | 0 | 0 | 0 | 0 | **0** |
| v1.3.0 | 0 | 0 | 0 | 0 | **0** |
| v1.2.0 | 0 | 0 | 0 | 0 | **0** |
| v1.1.0 | 0 | 0 | 0 | 0 | **0** |
| v1.0.1 | 0 | 0 | 0 | 0 | **0** |
| v1.0.0 | 1 | 2 | 2 | 0 | **5** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | arm64 | x86_64 | Total |
|----------|-------|-------|-------|
| 🪟 Windows | 1 | 11 | **12** |
| 🍎 macOS | 20 | 6 | **26** |
| 🐧 Linux | 3 | 3 | **6** |

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v2.54.0 | 10 | 2026-08-31 |
| v2.50.1 | 6 | 2026-08-21 |
| v2.52.1 | 5 | 2026-08-22 |
| v2.21.0 | 5 | 2026-08-17 |
| v1.0.0 | 5 | 2026-08-14 |
| v2.43.0 | 2 | 2026-08-20 |
| v2.39.0 | 2 | 2026-08-19 |
| v1.5.2 | 2 | 2026-08-14 |
| v2.53.2 | 1 | 2026-08-30 |
| v2.53.1 | 1 | 2026-08-30 |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq-gamut-viewer)**

---

# github-traffic-downloads-dashboard

![downloads](https://img.shields.io/badge/downloads-0-212121) ![clones](https://img.shields.io/badge/clones-9372-2196F3) ![views](https://img.shields.io/badge/views-43-4CAF50) ![releases](https://img.shields.io/badge/releases-0-6f42c1)

*Tracking since **2026-07-30** (107 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~107 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 172 | 246 | ▼ -30.1% |
| Views | 1 | 3 | ▼ -66.7% |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1254 | 475 |
| Last 90 Days | 4240 | 1443 |
| Lifetime | 9372 | 5239 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 1254 | 475 | 779 | 62.1% |
| Last 90 Days | 4240 | 1443 | 2797 | 66.0% |
| Lifetime | 9372 | 5239 | 4133 | 44.1% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 11 | 11 |
| Last 90 Days | 35 | 23 |
| Lifetime | 43 | 26 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 11 | — |
| 🗅️ Unique cloners | 475 | 4318.2% |
| 📥 Downloads | 0 | 0.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 1

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| aocr.org | 3 | 3 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 11 | 11 | 0 | 0.0% |
| Last 90 Days | 35 | 23 | 12 | 34.3% |
| Lifetime | 43 | 26 | 17 | 39.5% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 0 | 0 | 0 |
| 🍎 macOS | 0 | 0 | 0 |
| 🐧 Linux | 0 | 0 | 0 |
| **All downloads (incl. Homebrew)** | **0** | **0** | **0** |

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days | all | **0** | 0 | 0 | 0 | 0 |
| 30 days | stable | **0** | 0 | 0 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days | all | **0** | 0 | 0 | 0 | 0 |
| 90 days | stable | **0** | 0 | 0 | 0 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-08-14** on; the stable/beta split from **2026-10-10**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#github-traffic-downloads-dashboard)**

---

# homebrew-chromiq

> ℹ️ This is ChromIQ's Homebrew tap: it has no downloads of its own. Homebrew clones it when someone installs ChromIQ with brew and fetches it again on updates, so the number of different cloners in the last 14 days is a rough indicator of how many machines use the Homebrew install. It is not a download count, and machines that have not run brew lately do not show. ChromIQ's release workflow also clones it once per release. The Homebrew downloads themselves are counted under ChromIQ (Homebrew).

**Different cloners in the last 14 days:** 57 (as of 2026-11-14; GitHub's own 14-day count, recorded daily from 2026-10-09 on)

![downloads](https://img.shields.io/badge/downloads-0-212121) ![clones](https://img.shields.io/badge/clones-668-2196F3) ![views](https://img.shields.io/badge/views-3-4CAF50) ![releases](https://img.shields.io/badge/releases-0-6f42c1)

*Tracking since **2026-10-09** (36 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~36 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 69 | 55 | ▲ +25.5% |
| Views | 0 | 2 | ▼ -100.0% |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 476 | 263 |
| Last 90 Days | 668 | 373 |
| Lifetime | 668 | 373 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 476 | 263 | 213 | 44.7% |
| Last 90 Days | 668 | 373 | 295 | 44.2% |
| Lifetime | 668 | 373 | 295 | 44.2% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 3 | 3 |
| Last 90 Days | 3 | 3 |
| Lifetime | 3 | 3 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 3 | — |
| 🗅️ Unique cloners | 263 | 8766.7% |
| 📥 Downloads | 0 | 0.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 2

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| aocr.org | 1 | 1 |
| github.com | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 3 | 3 | 0 | 0.0% |
| Last 90 Days | 3 | 3 | 0 | 0.0% |
| Lifetime | 3 | 3 | 0 | 0.0% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 0 | 0 | 0 |
| 🍎 macOS | 0 | 0 | 0 |
| 🐧 Linux | 0 | 0 | 0 |
| **All downloads (incl. Homebrew)** | **0** | **0** | **0** |

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days | all | **0** | 0 | 0 | 0 | 0 |
| 30 days | stable | **0** | 0 | 0 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days (36 days tracked) | all | **0** | 0 | 0 | 0 | 0 |
| 90 days | stable | **0** | 0 | 0 | 0 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-10-10** on; the stable/beta split from **2026-10-10**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#homebrew-chromiq)**

---

# MacReplica

![downloads](https://img.shields.io/badge/downloads-78-212121) ![clones](https://img.shields.io/badge/clones-2191-2196F3) ![views](https://img.shields.io/badge/views-149-4CAF50) ![releases](https://img.shields.io/badge/releases-25-6f42c1) ![latest stable v1.1.16](https://img.shields.io/badge/latest%20stable%20v1.1.16-2-212121 "Downloads of the latest stable release, all platforms incl. Homebrew")

*Tracking since **2026-10-02** (43 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~43 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 14 | 252 | ▼ -94.4% |
| Views | 0 | 44 | ▼ -100.0% |
| Downloads | 1 | 35 | ▼ -97.1% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1143 | 333 |
| Last 90 Days | 2191 | 724 |
| Lifetime | 2191 | 724 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 1143 | 333 | 810 | 70.9% |
| Last 90 Days | 2191 | 724 | 1467 | 67.0% |
| Lifetime | 2191 | 724 | 1467 | 67.0% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 97 | 18 |
| Last 90 Days | 149 | 35 |
| Lifetime | 149 | 35 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 18 | — |
| 🗅️ Unique cloners | 333 | 1850.0% |
| 📥 Downloads | 52 | 288.9% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 2

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 6 | 2 |
| Bing | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 97 | 18 | 79 | 81.4% |
| Last 90 Days | 149 | 35 | 114 | 76.5% |
| Lifetime | 149 | 35 | 114 | 76.5% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 0 | 0 | 0 |
| 🍎 macOS | 52 | 64 | 78 |
| 🐧 Linux | 0 | 0 | 0 |
| **All downloads (incl. Homebrew)** | **52** | **64** | **78** |

*ℹ️ Not counted above: 33 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days | all | **52** | 0 | 52 | 0 | 0 |
| 30 days | stable | **52** | 0 | 52 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days (36 days tracked) | all | **64** | 0 | 64 | 0 | 0 |
| 90 days | stable | **64** | 0 | 64 | 0 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-10-10** on; the stable/beta split from **2026-10-10**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v1.1.16` - **2** downloads (published 2026-11-04)

<details>
<summary><strong>📦 Per-version downloads</strong> (25 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v1.1.16 | 0 | 2 | 0 | 0 | **2** |
| v1.1.15 | 0 | 2 | 0 | 0 | **2** |
| v1.1.14 | 0 | 2 | 0 | 0 | **2** |
| v1.1.13 | 0 | 2 | 0 | 0 | **2** |
| v1.1.12 | 0 | 3 | 0 | 0 | **3** |
| v1.1.11 | 0 | 5 | 0 | 0 | **5** |
| v1.1.10 | 0 | 2 | 0 | 0 | **2** |
| v1.1.9 | 0 | 3 | 0 | 0 | **3** |
| v1.1.8 | 0 | 4 | 0 | 0 | **4** |
| v1.1.7 | 0 | 3 | 0 | 0 | **3** |
| v1.1.6 | 0 | 3 | 0 | 0 | **3** |
| v1.1.5 | 0 | 2 | 0 | 0 | **2** |
| v1.1.4 | 0 | 2 | 0 | 0 | **2** |
| v1.1.3 | 0 | 4 | 0 | 0 | **4** |
| v1.1.2 | 0 | 2 | 0 | 0 | **2** |
| v1.1.1 | 0 | 2 | 0 | 0 | **2** |
| v1.1.0 | 0 | 5 | 0 | 0 | **5** |
| v1.0.7 | 0 | 3 | 0 | 0 | **3** |
| v1.0.6 | 0 | 2 | 0 | 0 | **2** |
| v1.0.5 | 0 | 4 | 0 | 0 | **4** |
| v1.0.4 | 0 | 7 | 0 | 0 | **7** |
| v1.0.3 | 0 | 2 | 0 | 0 | **2** |
| v1.0.2 | 0 | 3 | 0 | 0 | **3** |
| v1.0.1 | 0 | 4 | 0 | 0 | **4** |
| v1.0.0 | 0 | 5 | 0 | 0 | **5** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | other | Total |
|----------|-------|-------|
| 🪟 Windows | 0 | **0** |
| 🍎 macOS | 78 | **78** |
| 🐧 Linux | 0 | **0** |

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.0.4 | 7 | 2026-10-04 |
| v1.1.11 | 5 | 2026-10-20 |
| v1.1.0 | 5 | 2026-10-15 |
| v1.0.0 | 5 | 2026-10-02 |
| v1.1.8 | 4 | 2026-10-19 |
| v1.1.3 | 4 | 2026-10-17 |
| v1.0.5 | 4 | 2026-10-13 |
| v1.0.1 | 4 | 2026-10-03 |
| v1.1.12 | 3 | 2026-11-03 |
| v1.1.9 | 3 | 2026-10-20 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear. 🍺 is Homebrew (its own copies of the Mac file, not counted again under 🍎); releases without Homebrew copies show 0.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | 🍺 | All downloads (incl. Homebrew) |
|---------|-----------|-----|----|----|----|----|------------------------------|
| v1.1.16 | 2026-11-04 | 11d | 0 | 2 | 0 | 0 | **2** |
| v1.1.15 | 2026-11-04 | 11d | 0 | 2 | 0 | 0 | **2** |
| v1.1.14 | 2026-11-04 | 11d | 0 | 2 | 0 | 0 | **2** |
| v1.1.13 | 2026-11-03 | 12d | 0 | 2 | 0 | 0 | **2** |
| v1.1.12 | 2026-11-03 | 12d | 0 | 3 | 0 | 0 | **3** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#macreplica)**

---

# neolume

![downloads](https://img.shields.io/badge/downloads-185-212121) ![clones](https://img.shields.io/badge/clones-1154-2196F3) ![views](https://img.shields.io/badge/views-8-4CAF50) ![releases](https://img.shields.io/badge/releases-24-6f42c1) ![latest stable v1.0.23](https://img.shields.io/badge/latest%20stable%20v1.0.23-6-212121 "Downloads of the latest stable release, all platforms incl. Homebrew")

*Tracking since **2026-10-27** (18 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~18 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 94 | 588 | ▼ -84.0% |
| Views | 0 | 3 | ▼ -100.0% |
| Downloads | 19 | 101 | ▼ -81.2% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1154 | 212 |
| Last 90 Days | 1154 | 212 |
| Lifetime | 1154 | 212 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 1154 | 212 | 942 | 81.6% |
| Last 90 Days | 1154 | 212 | 942 | 81.6% |
| Lifetime | 1154 | 212 | 942 | 81.6% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 8 | 5 |
| Last 90 Days | 8 | 5 |
| Lifetime | 8 | 5 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 5 | — |
| 🗅️ Unique cloners | 212 | 4240.0% |
| 📥 Downloads | 185 | 3700.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 1

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 8 | 5 | 3 | 37.5% |
| Last 90 Days | 8 | 5 | 3 | 37.5% |
| Lifetime | 8 | 5 | 3 | 37.5% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 62 | 62 | 62 |
| 🍎 macOS | 64 | 64 | 64 |
| 🐧 Linux | 59 | 59 | 59 |
| **All downloads (incl. Homebrew)** | **185** | **185** | **185** |

*ℹ️ Not counted above: 73 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days (18 days tracked) | all | **185** | 62 | 64 | 59 | 0 |
| 30 days | stable | **185** | 62 | 64 | 59 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days (18 days tracked) | all | **185** | 62 | 64 | 59 | 0 |
| 90 days | stable | **185** | 62 | 64 | 59 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-10-28** on; the stable/beta split from **2026-10-28**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v1.0.23` - **6** downloads (published 2026-11-10)

<details>
<summary><strong>📦 Per-version downloads</strong> (24 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v1.0.23 | 2 | 2 | 2 | 0 | **6** |
| v1.0.22 | 2 | 2 | 2 | 0 | **6** |
| v1.0.21 | 2 | 2 | 2 | 0 | **6** |
| v1.0.20 | 3 | 3 | 2 | 0 | **8** |
| v1.0.19 | 1 | 1 | 1 | 0 | **3** |
| v1.0.18 | 2 | 2 | 2 | 0 | **6** |
| v1.0.17 | 2 | 2 | 2 | 0 | **6** |
| v1.0.16 | 2 | 2 | 2 | 0 | **6** |
| v1.0.15 | 10 | 9 | 7 | 0 | **26** |
| v1.0.14 | 2 | 2 | 2 | 0 | **6** |
| v1.0.13 | 2 | 2 | 2 | 0 | **6** |
| v1.0.12 | 6 | 5 | 6 | 0 | **17** |
| v1.0.11 | 2 | 2 | 2 | 0 | **6** |
| v1.0.10 | 2 | 2 | 2 | 0 | **6** |
| v1.0.9 | 2 | 2 | 2 | 0 | **6** |
| v1.0.8 | 2 | 2 | 3 | 0 | **7** |
| v1.0.7 | 3 | 3 | 2 | 0 | **8** |
| v1.0.6 | 2 | 3 | 2 | 0 | **7** |
| v1.0.5 | 3 | 2 | 3 | 0 | **8** |
| v1.0.4 | 2 | 2 | 2 | 0 | **6** |
| v1.0.3 | 2 | 5 | 2 | 0 | **9** |
| v1.0.2 | 2 | 2 | 3 | 0 | **7** |
| v1.0.1 | 2 | 2 | 2 | 0 | **6** |
| v1.0.0 | 2 | 3 | 2 | 0 | **7** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | arm64 | x86_64 | Total |
|----------|-------|-------|-------|
| 🪟 Windows | 31 | 31 | **62** |
| 🍎 macOS | 33 | 31 | **64** |
| 🐧 Linux | 28 | 31 | **59** |

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.0.15 | 26 | 2026-11-04 |
| v1.0.12 | 17 | 2026-11-03 |
| v1.0.3 | 9 | 2026-10-27 |
| v1.0.20 | 8 | 2026-11-06 |
| v1.0.7 | 8 | 2026-10-30 |
| v1.0.5 | 8 | 2026-10-28 |
| v1.0.8 | 7 | 2026-10-30 |
| v1.0.6 | 7 | 2026-10-29 |
| v1.0.2 | 7 | 2026-10-27 |
| v1.0.0 | 7 | 2026-10-27 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear. 🍺 is Homebrew (its own copies of the Mac file, not counted again under 🍎); releases without Homebrew copies show 0.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | 🍺 | All downloads (incl. Homebrew) |
|---------|-----------|-----|----|----|----|----|------------------------------|
| v1.0.23 | 2026-11-10 | 5d | 2 | 2 | 2 | 0 | **6** |
| v1.0.22 | 2026-11-08 | 7d | 2 | 2 | 2 | 0 | **6** |
| v1.0.21 | 2026-11-07 | 8d | 2 | 2 | 2 | 0 | **6** |
| v1.0.20 | 2026-11-06 | 9d | 3 | 3 | 2 | 0 | **8** |
| v1.0.19 | 2026-11-06 | 9d | 1 | 1 | 1 | 0 | **3** |
| v1.0.18 | 2026-11-05 | 10d | 2 | 2 | 2 | 0 | **6** |
| v1.0.17 | 2026-11-05 | 10d | 2 | 2 | 2 | 0 | **6** |
| v1.0.16 | 2026-11-04 | 11d | 2 | 2 | 2 | 0 | **6** |
| v1.0.15 | 2026-11-04 | 11d | 10 | 9 | 7 | 0 | **26** |
| v1.0.14 | 2026-11-04 | 11d | 2 | 2 | 2 | 0 | **6** |
| v1.0.13 | 2026-11-04 | 11d | 2 | 2 | 2 | 0 | **6** |
| v1.0.12 | 2026-11-03 | 12d | 6 | 5 | 6 | 0 | **17** |
| v1.0.11 | 2026-11-02 | 13d | 2 | 2 | 2 | 0 | **6** |
| v1.0.10 | 2026-11-01 | 14d | 2 | 2 | 2 | 0 | **6** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#neolume)**

---

*This dashboard is automatically updated daily using GitHub Actions.*
