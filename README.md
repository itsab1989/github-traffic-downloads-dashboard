See full Reference and Usage Guide at:
https://itsab1989.github.io/github-traffic-downloads-dashboard/

> This is a modified version of the original [github-traffic-dashboard](https://github.com/soul-traveller/github-traffic-dashboard), extended with platform-specific download statistics (Windows / macOS / Linux).

# 📊 GitHub Traffic & Downloads Dashboard

This dashboard tracks historical traffic data (clones, views, and release downloads) for GitHub repositories.

**Last Updated:** 2026-11-06T00:59:14.760018Z

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

![downloads incl. Homebrew](https://img.shields.io/badge/downloads%20incl.%20Homebrew-10488-212121) ![clones](https://img.shields.io/badge/clones-37942-2196F3) ![views](https://img.shields.io/badge/views-9801-4CAF50) ![releases](https://img.shields.io/badge/releases-928-6f42c1) ![latest stable v4.3.25](https://img.shields.io/badge/latest%20stable%20v4.3.25-18-212121 "Downloads of the latest stable release, all platforms incl. Homebrew") ![latest beta v4.3.10-beta.1](https://img.shields.io/badge/latest%20beta%20v4.3.10--beta.1-13-757575 "Downloads of the latest beta release, all platforms incl. Homebrew")

*Tracking since **2026-05-02** (187 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~187 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 87 | 342 | ▼ -74.6% |
| Views | 277 | 456 | ▼ -39.3% |
| Downloads | 1995 | 4904 | ▼ -59.3% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 5983 | 491 |
| Last 90 Days | 18623 | 5585 |
| Lifetime | 37942 | 9827 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 5983 | 491 | 5492 | 91.8% |
| Last 90 Days | 18623 | 5585 | 13038 | 70.0% |
| Lifetime | 37942 | 9827 | 28115 | 74.1% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1608 | 569 |
| Last 90 Days | 5220 | 1518 |
| Lifetime | 9801 | 2593 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 569 | — |
| 🗅️ Unique cloners | 491 | 86.3% |
| 📥 Downloads | 7336 | 1289.3% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 10

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| aocr.org | 83 | 83 |
| Google | 47 | 25 |
| itsab1989.github.io | 30 | 22 |
| search.brave.com | 24 | 5 |
| yandex.ru | 18 | 6 |
| github.com | 16 | 10 |
| printerknowledge.com | 7 | 5 |
| dpreview.com | 5 | 2 |
| hub.displaycal.net | 3 | 3 |
| forum.luminous-landscape.com | 2 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 1608 | 569 | 1039 | 64.6% |
| Last 90 Days | 5220 | 1518 | 3702 | 70.9% |
| Lifetime | 9801 | 2593 | 7208 | 73.5% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 2210 | 2552 | 3159 |
| 🍎 macOS | 3069 | 3464 | 5092 |
| 🐧 Linux | 1838 | 1894 | 2018 |
| 🍺 Homebrew | 219 | 219 | 219 |
| **All downloads (incl. Homebrew)** | **7336** | **8128** | **10488** |

*ℹ️ Not counted above: 179 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days | all | **7336** | 2210 | 3069 | 1838 | 219 |
| 30 days | stable | **2579** | 842 | 1028 | 541 | 168 |
| 30 days | beta | **4802** | 1379 | 2075 | 1297 | 51 |
| 90 days | all | **8128** | 2552 | 3464 | 1894 | 219 |
| 90 days | stable | **3059** | 1088 | 1240 | 565 | 168 |
| 90 days | beta | **5114** | 1476 | 2259 | 1329 | 51 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-05-25** on; the stable/beta split from **2026-05-25**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v4.3.25` - **18** downloads (published 2026-11-04)

<details>
<summary><strong>📦 Per-version downloads</strong> (928 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v4.3.25 | 8 | 2 | 3 | 5 | **18** |
| v4.3.24 | 5 | 8 | 2 | 3 | **18** |
| v4.3.23 | 6 | 7 | 2 | 4 | **19** |
| v4.3.22 | 10 | 4 | 3 | 3 | **20** |
| v4.3.21 | 10 | 7 | 2 | 5 | **24** |
| v4.3.20 | 75 | 16 | 6 | 13 | **110** |
| v4.3.19 | 44 | 11 | 6 | 11 | **72** |
| v4.3.18 | 8 | 5 | 4 | 5 | **22** |
| v4.3.17 | 12 | 13 | 5 | 5 | **35** |
| v4.3.16 | 13 | 6 | 3 | 9 | **31** |
| v4.3.15 | 8 | 9 | 5 | 4 | **26** |
| v4.3.14 | 6 | 4 | 2 | 5 | **17** |
| v4.3.13 | 11 | 8 | 2 | 4 | **25** |
| v4.3.12 | 8 | 1 | 2 | 8 | **19** |
| v4.3.11 | 4 | 5 | 2 | 4 | **15** |
| v4.3.10 | 9 | 5 | 3 | 6 | **23** |
| v4.3.10-beta.1 *(beta)* | 4 | 3 | 2 | 4 | **13** |
| v4.3.9 | 17 | 7 | 2 | 19 | **45** |
| v4.3.8 | 6 | 5 | 3 | 4 | **18** |
| v4.3.8-beta.3 *(beta)* | 3 | 3 | 3 | 5 | **14** |
| v4.3.8-beta.2 *(beta)* | 5 | 3 | 2 | 4 | **14** |
| v4.3.8-beta.1 *(beta)* | 3 | 4 | 2 | 3 | **12** |
| v4.3.7 | 30 | 7 | 4 | 8 | **49** |
| v4.3.6 | 5 | 8 | 2 | 5 | **20** |
| v4.3.5 | 9 | 7 | 4 | 9 | **29** |
| v4.3.5-beta.9 *(beta)* | 7 | 3 | 4 | 3 | **17** |
| v4.3.5-beta.8 *(beta)* | 6 | 4 | 4 | 3 | **17** |
| v4.3.5-beta.7 *(beta)* | 6 | 4 | 2 | 3 | **15** |
| v4.3.5-beta.6 *(beta)* | 3 | 3 | 2 | 3 | **11** |
| v4.3.5-beta.5 *(beta)* | 2 | 6 | 2 | 3 | **13** |
| v4.3.5-beta.4 *(beta)* | 3 | 5 | 2 | 4 | **14** |
| v4.3.5-beta.3 *(beta)* | 8 | 9 | 2 | 3 | **22** |
| v4.3.5-beta.2 *(beta)* | 4 | 5 | 2 | 3 | **14** |
| v4.3.5-beta.1 *(beta)* | 3 | 2 | 2 | 5 | **12** |
| v4.3.4 | 45 | 31 | 8 | 24 | **108** |
| v4.3.3 | 7 | 10 | 6 | 5 | **28** |
| v4.3.3-beta.17 *(beta)* | 5 | 7 | 4 | 5 | **21** |
| v4.3.3-beta.16 *(beta)* | 5 | 21 | 4 | 0 | **30** |
| v4.3.3-beta.15 *(beta)* | 5 | 11 | 4 | 0 | **20** |
| v4.3.3-beta.14 *(beta)* | 3 | 6 | 2 | 0 | **11** |
| v4.3.3-beta.13 *(beta)* | 5 | 5 | 2 | 0 | **12** |
| v4.3.3-beta.12 *(beta)* | 5 | 8 | 5 | 0 | **18** |
| v4.3.3-beta.11 *(beta)* | 7 | 10 | 3 | 0 | **20** |
| v4.3.3-beta.10 *(beta)* | 5 | 5 | 2 | 0 | **12** |
| v4.3.3-beta.9 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v4.3.3-beta.8 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v4.3.3-beta.7 *(beta)* | 5 | 6 | 3 | 0 | **14** |
| v4.3.3-beta.6 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v4.3.3-beta.5 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v4.3.3-beta.4 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v4.3.3-beta.3 *(beta)* | 4 | 7 | 4 | 0 | **15** |
| v4.3.3-beta.2 *(beta)* | 2 | 6 | 4 | 0 | **12** |
| v4.3.3-beta.1 *(beta)* | 3 | 12 | 6 | 0 | **21** |
| v4.3.2 | 57 | 56 | 7 | 0 | **120** |
| v4.3.1 | 3 | 8 | 2 | 0 | **13** |
| v4.3.0 | 4 | 7 | 4 | 0 | **15** |
| v4.3.0-beta.49 *(beta)* | 4 | 5 | 2 | 0 | **11** |
| v4.3.0-beta.48 *(beta)* | 3 | 6 | 3 | 0 | **12** |
| v4.3.0-beta.47 *(beta)* | 4 | 5 | 2 | 0 | **11** |
| v4.3.0-beta.46 *(beta)* | 3 | 7 | 2 | 0 | **12** |
| v4.3.0-beta.45 *(beta)* | 4 | 5 | 2 | 0 | **11** |
| v4.3.0-beta.44 *(beta)* | 4 | 8 | 2 | 0 | **14** |
| v4.3.0-beta.43 *(beta)* | 3 | 6 | 2 | 0 | **11** |
| v4.3.0-beta.42 *(beta)* | 5 | 6 | 2 | 0 | **13** |
| v4.3.0-beta.41 *(beta)* | 4 | 7 | 2 | 0 | **13** |
| v4.3.0-beta.40 *(beta)* | 4 | 7 | 2 | 0 | **13** |
| v4.3.0-beta.39 *(beta)* | 2 | 7 | 2 | 0 | **11** |
| v4.3.0-beta.38 *(beta)* | 3 | 6 | 2 | 0 | **11** |
| v4.3.0-beta.37 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v4.3.0-beta.36 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v4.3.0-beta.35 *(beta)* | 4 | 5 | 2 | 0 | **11** |
| v4.3.0-beta.34 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v4.3.0-beta.33 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v4.3.0-beta.32 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.3.0-beta.31 *(beta)* | 3 | 6 | 2 | 0 | **11** |
| v4.3.0-beta.30 *(beta)* | 2 | 7 | 2 | 0 | **11** |
| v4.3.0-beta.29 *(beta)* | 4 | 7 | 2 | 0 | **13** |
| v4.3.0-beta.28 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v4.3.0-beta.27 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.3.0-beta.26 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v4.3.0-beta.25 *(beta)* | 2 | 4 | 4 | 0 | **10** |
| v4.3.0-beta.24 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v4.3.0-beta.23 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.3.0-beta.22 *(beta)* | 2 | 5 | 4 | 0 | **11** |
| v4.3.0-beta.21 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v4.3.0-beta.20 *(beta)* | 2 | 4 | 6 | 0 | **12** |
| v4.3.0-beta.19 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.3.0-beta.18 *(beta)* | 6 | 5 | 2 | 0 | **13** |
| v4.3.0-beta.17 *(beta)* | 5 | 8 | 3 | 0 | **16** |
| v4.3.0-beta.16 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v4.3.0-beta.15 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.3.0-beta.14 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v4.3.0-beta.13 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v4.3.0-beta.12 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v4.3.0-beta.11 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.3.0-beta.10 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v4.3.0-beta.9 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v4.3.0-beta.8 *(beta)* | 2 | 6 | 3 | 0 | **11** |
| v4.3.0-beta.7 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v4.3.0-beta.6 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v4.3.0-beta.5 *(beta)* | 4 | 5 | 4 | 0 | **13** |
| v4.2.7 | 57 | 49 | 8 | 0 | **114** |
| v4.2.6 | 5 | 3 | 3 | 0 | **11** |
| v4.3.0-beta.4 *(beta)* | 3 | 6 | 2 | 0 | **11** |
| v4.2.5 | 5 | 8 | 3 | 0 | **16** |
| v4.3.0-beta.3 *(beta)* | 3 | 7 | 2 | 0 | **12** |
| v4.2.4 | 4 | 5 | 2 | 0 | **11** |
| v4.2.3 | 8 | 4 | 2 | 0 | **14** |
| v4.3.0-beta.2 *(beta)* | 7 | 4 | 2 | 0 | **13** |
| v4.2.2 | 3 | 7 | 4 | 0 | **14** |
| v4.3.0-beta.1 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v4.2.1 | 5 | 6 | 2 | 0 | **13** |
| v4.2.0 | 20 | 14 | 5 | 0 | **39** |
| v4.1.5-beta.11 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v4.1.5-beta.10 *(beta)* | 5 | 5 | 2 | 0 | **12** |
| v4.1.5-beta.9 *(beta)* | 8 | 11 | 8 | 0 | **27** |
| v4.1.5-beta.8 *(beta)* | 7 | 12 | 8 | 0 | **27** |
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
| v3.14.8-beta.182 *(beta)* | 5 | 7 | 4 | 0 | **16** |
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
| v3.13.0-beta.91 *(beta)* | 7 | 11 | 6 | 0 | **24** |
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
| v3.13.0-beta.39 *(beta)* | 8 | 13 | 8 | 0 | **29** |
| v3.13.0-beta.38 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.37 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.36 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.35 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v3.13.0-beta.34 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.13.0-beta.33 *(beta)* | 4 | 7 | 4 | 0 | **15** |
| v3.13.0-beta.32 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.31 *(beta)* | 6 | 10 | 6 | 0 | **22** |
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
| v3.8.0-beta.24 *(beta)* | 9 | 13 | 8 | 0 | **30** |
| v3.8.0-beta.23 *(beta)* | 8 | 12 | 8 | 0 | **28** |
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
| v3.8.0-beta.5 *(beta)* | 6 | 11 | 6 | 0 | **23** |
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
| v3.7.27 | 5 | 10 | 4 | 0 | **19** |
| v3.7.26 | 4 | 8 | 4 | 0 | **16** |
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
| v3.7.11 | 5 | 10 | 4 | 0 | **19** |
| v3.7.10 | 4 | 10 | 2 | 0 | **16** |
| v3.7.9 | 2 | 13 | 2 | 0 | **17** |
| v3.7.8 | 2 | 13 | 2 | 0 | **17** |
| v3.7.7 | 2 | 7 | 2 | 0 | **11** |
| v3.7.6 | 2 | 9 | 2 | 0 | **13** |
| v3.7.5 | 7 | 10 | 3 | 0 | **20** |
| v3.7.4 | 3 | 11 | 2 | 0 | **16** |
| v3.7.3 | 2 | 11 | 2 | 0 | **15** |
| v3.7.2 | 5 | 10 | 4 | 0 | **19** |
| v3.7.1 | 2 | 43 | 4 | 0 | **49** |
| v3.7.0 | 5 | 38 | 5 | 0 | **48** |
| v3.6.7 | 5 | 45 | 5 | 0 | **55** |
| v3.6.6 | 6 | 35 | 4 | 0 | **45** |
| v3.6.5 | 5 | 45 | 5 | 0 | **55** |
| v3.6.4 | 5 | 51 | 5 | 0 | **61** |
| v3.6.3 | 2 | 7 | 2 | 0 | **11** |
| v3.6.2 | 2 | 6 | 2 | 0 | **10** |
| v3.6.1 | 2 | 9 | 2 | 0 | **13** |
| v3.6.0 | 5 | 12 | 6 | 0 | **23** |
| v3.5.13 | 3 | 7 | 5 | 0 | **15** |
| v3.5.12 | 2 | 7 | 2 | 0 | **11** |
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
| v3.5.0-beta.6 *(beta)* | 2 | 7 | 3 | 0 | **12** |
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
| v3.2.0-beta.3 *(beta)* | 3 | 7 | 0 | 0 | **10** |
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
| v1.0.0 | 0 | 2 | 0 | 0 | **2** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | arm64 | x86_64 | universal | Total |
|----------|-------|-------|-------|-------|
| 🪟 Windows | 1052 | 2107 | 0 | **3159** |
| 🍎 macOS | 2420 | 1322 | 1350 | **5092** |
| 🐧 Linux | 988 | 1030 | 0 | **2018** |
| 🍺 Homebrew | 161 | 58 | 0 | **219** |

*💡 Low-volume builds (<2% of lifetime downloads), candidates to stop shipping: 🍺 Homebrew arm64 (161, 1.5%); 🍺 Homebrew x86_64 (58, 0.6%).*

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v4.3.2 | 120 | 2026-09-28 |
| v4.2.7 | 114 | 2026-09-12 |
| v4.3.20 | 110 | 2026-10-29 |
| v4.3.4 | 108 | 2026-10-10 |
| v4.1.4 | 74 | 2026-08-28 |
| v4.3.19 | 72 | 2026-10-28 |
| v3.14.7 | 68 | 2026-07-22 |
| v3.6.4 | 61 | 2026-05-17 |
| v3.12.1 | 60 | 2026-06-25 |
| v3.6.7 | 55 | 2026-05-18 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear. 🍺 is Homebrew (its own copies of the Mac file, not counted again under 🍎); releases without Homebrew copies show 0.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | 🍺 | All downloads (incl. Homebrew) |
|---------|-----------|-----|----|----|----|----|------------------------------|
| v4.3.25 | 2026-11-04 | 3d | 8 | 2 | 3 | 5 | **18** |
| v4.3.24 | 2026-11-04 | 3d | 5 | 8 | 2 | 3 | **18** |
| v4.3.23 | 2026-11-03 | 4d | 6 | 7 | 2 | 4 | **19** |
| v4.3.22 | 2026-11-03 | 4d | 10 | 4 | 3 | 3 | **20** |
| v4.3.21 | 2026-11-02 | 5d | 10 | 7 | 2 | 5 | **24** |
| v4.3.20 | 2026-10-29 | 9d | 75 | 16 | 6 | 13 | **110** |
| v4.3.19 | 2026-10-28 | 10d | 44 | 11 | 6 | 11 | **72** |
| v4.3.18 | 2026-10-27 | 11d | 8 | 5 | 4 | 5 | **22** |
| v4.3.17 | 2026-10-27 | 11d | 12 | 13 | 5 | 5 | **35** |
| v4.3.16 | 2026-10-26 | 12d | 13 | 6 | 3 | 9 | **31** |
| v4.3.15 | 2026-10-25 | 13d | 8 | 9 | 5 | 4 | **26** |
| v4.3.14 | 2026-10-25 | 13d | 6 | 4 | 2 | 5 | **17** |
| v4.3.13 | 2026-10-24 | 14d | 11 | 8 | 2 | 4 | **25** |
| v4.3.12 | 2026-10-24 | 14d | 8 | 1 | 2 | 8 | **19** |
| v4.3.11 | 2026-10-24 | 14d | 4 | 5 | 2 | 4 | **15** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq)**

---

# ChromIQ-Patches

![downloads](https://img.shields.io/badge/downloads-47-212121) ![clones](https://img.shields.io/badge/clones-396-2196F3) ![views](https://img.shields.io/badge/views-141-4CAF50) ![releases](https://img.shields.io/badge/releases-5-6f42c1) ![latest stable v1.2.1](https://img.shields.io/badge/latest%20stable%20v1.2.1-24-212121 "Downloads of the latest stable release, all platforms incl. Homebrew")

*Tracking since **2026-07-02** (125 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~125 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 6 | 6 | ▬ 0% |
| Views | 7 | 13 | ▼ -46.2% |
| Downloads | 1 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 38 | 35 |
| Last 90 Days | 73 | 69 |
| Lifetime | 396 | 220 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 38 | 35 | 3 | 7.9% |
| Last 90 Days | 73 | 69 | 4 | 5.5% |
| Lifetime | 396 | 220 | 176 | 44.4% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 28 | 21 |
| Last 90 Days | 62 | 39 |
| Lifetime | 141 | 71 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 21 | — |
| 🗅️ Unique cloners | 35 | 166.7% |
| 📥 Downloads | 2 | 9.5% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 4

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 7 | 4 |
| aocr.org | 4 | 4 |
| Bing | 1 | 1 |
| itsab1989.github.io | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 28 | 21 | 7 | 25.0% |
| Last 90 Days | 62 | 39 | 23 | 37.1% |
| Lifetime | 141 | 71 | 70 | 49.6% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 1 | 6 | 19 |
| 🍎 macOS | 1 | 4 | 25 |
| 🐧 Linux | 0 | 0 | 3 |
| **All downloads (incl. Homebrew)** | **2** | **10** | **47** |

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days | all | **2** | 1 | 1 | 0 | 0 |
| 30 days | stable | **2** | 1 | 1 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days | all | **10** | 6 | 4 | 0 | 0 |
| 90 days | stable | **10** | 6 | 4 | 0 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-07-03** on; the stable/beta split from **2026-07-03**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v1.2.1` - **24** downloads (published 2026-07-07)

<details>
<summary><strong>📦 Per-version downloads</strong> (5 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v1.2.1 | 10 | 13 | 1 | 0 | **24** |
| v1.2.0 | 5 | 7 | 2 | 0 | **14** |
| v1.1.0 | 0 | 1 | 0 | 0 | **1** |
| v1.0.1 | 1 | 3 | 0 | 0 | **4** |
| v1.0.0 | 3 | 1 | 0 | 0 | **4** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | arm64 | x86_64 | universal | Total |
|----------|-------|-------|-------|-------|
| 🪟 Windows | 0 | 19 | 0 | **19** |
| 🍎 macOS | 18 | 3 | 4 | **25** |
| 🐧 Linux | 0 | 3 | 0 | **3** |

**Top 5 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.2.1 | 24 | 2026-07-07 |
| v1.2.0 | 14 | 2026-07-03 |
| v1.0.1 | 4 | 2026-07-02 |
| v1.0.0 | 4 | 2026-07-02 |
| v1.1.0 | 1 | 2026-07-02 |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq-patches)**

---

# ChromIQ-Gamut-Viewer

![downloads](https://img.shields.io/badge/downloads-41-212121) ![clones](https://img.shields.io/badge/clones-2504-2196F3) ![views](https://img.shields.io/badge/views-77-4CAF50) ![releases](https://img.shields.io/badge/releases-96-6f42c1) ![latest stable v2.54.0](https://img.shields.io/badge/latest%20stable%20v2.54.0-7-212121 "Downloads of the latest stable release, all platforms incl. Homebrew")

*Tracking since **2026-08-13** (83 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~83 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 1 | 2 | ▼ -50.0% |
| Views | 3 | 10 | ▼ -70.0% |
| Downloads | 2 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 9 | 9 |
| Last 90 Days | 2504 | 528 |
| Lifetime | 2504 | 528 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 9 | 9 | 0 | 0.0% |
| Last 90 Days | 2504 | 528 | 1976 | 78.9% |
| Lifetime | 2504 | 528 | 1976 | 78.9% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 13 | 4 |
| Last 90 Days | 77 | 21 |
| Lifetime | 77 | 21 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 4 | — |
| 🗅️ Unique cloners | 9 | 225.0% |
| 📥 Downloads | 3 | 75.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 2

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 2 | 2 |
| aocr.org | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 13 | 4 | 9 | 69.2% |
| Last 90 Days | 77 | 21 | 56 | 72.7% |
| Lifetime | 77 | 21 | 56 | 72.7% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 0 | 9 | 10 |
| 🍎 macOS | 3 | 21 | 25 |
| 🐧 Linux | 0 | 4 | 6 |
| **All downloads (incl. Homebrew)** | **3** | **34** | **41** |

*ℹ️ Not counted above: 11 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days | all | **3** | 0 | 3 | 0 | 0 |
| 30 days | stable | **3** | 0 | 3 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days (84 days tracked) | all | **34** | 9 | 21 | 4 | 0 |
| 90 days | stable | **34** | 9 | 21 | 4 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-08-15** on; the stable/beta split from **2026-08-15**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v2.54.0` - **7** downloads (published 2026-08-31)

<details>
<summary><strong>📦 Per-version downloads</strong> (96 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v2.54.0 | 1 | 6 | 0 | 0 | **7** |
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
| 🪟 Windows | 1 | 9 | **10** |
| 🍎 macOS | 19 | 6 | **25** |
| 🐧 Linux | 3 | 3 | **6** |

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v2.54.0 | 7 | 2026-08-31 |
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

![downloads](https://img.shields.io/badge/downloads-0-212121) ![clones](https://img.shields.io/badge/clones-9108-2196F3) ![views](https://img.shields.io/badge/views-39-4CAF50) ![releases](https://img.shields.io/badge/releases-0-6f42c1)

*Tracking since **2026-07-30** (98 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~98 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 189 | 395 | ▼ -52.2% |
| Views | 0 | 7 | ▼ -100.0% |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1334 | 512 |
| Last 90 Days | 8523 | 4985 |
| Lifetime | 9108 | 5133 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 1334 | 512 | 822 | 61.6% |
| Last 90 Days | 8523 | 4985 | 3538 | 41.5% |
| Lifetime | 9108 | 5133 | 3975 | 43.6% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 8 | 8 |
| Last 90 Days | 38 | 21 |
| Lifetime | 39 | 22 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 8 | — |
| 🗅️ Unique cloners | 512 | 6400.0% |
| 📥 Downloads | 0 | 0.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 1

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| aocr.org | 5 | 5 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 8 | 8 | 0 | 0.0% |
| Last 90 Days | 38 | 21 | 17 | 44.7% |
| Lifetime | 39 | 22 | 17 | 43.6% |

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
| 90 days (85 days tracked) | all | **0** | 0 | 0 | 0 | 0 |
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

**Different cloners in the last 14 days:** 98 (as of 2026-11-06; GitHub's own 14-day count, recorded daily from 2026-10-09 on)

![downloads](https://img.shields.io/badge/downloads-0-212121) ![clones](https://img.shields.io/badge/clones-574-2196F3) ![views](https://img.shields.io/badge/views-2-4CAF50) ![releases](https://img.shields.io/badge/releases-0-6f42c1)

*Tracking since **2026-10-09** (27 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~27 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 31 | 180 | ▼ -82.8% |
| Views | 1 | 1 | ▬ 0% |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 574 | 319 |
| Last 90 Days | 574 | 319 |
| Lifetime | 574 | 319 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 574 | 319 | 255 | 44.4% |
| Last 90 Days | 574 | 319 | 255 | 44.4% |
| Lifetime | 574 | 319 | 255 | 44.4% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 2 | 2 |
| Last 90 Days | 2 | 2 |
| Lifetime | 2 | 2 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 2 | — |
| 🗅️ Unique cloners | 319 | 15950.0% |
| 📥 Downloads | 0 | 0.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 1

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 2 | 2 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 2 | 2 | 0 | 0.0% |
| Last 90 Days | 2 | 2 | 0 | 0.0% |
| Lifetime | 2 | 2 | 0 | 0.0% |

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
| 30 days (28 days tracked) | all | **0** | 0 | 0 | 0 | 0 |
| 30 days | stable | **0** | 0 | 0 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days (28 days tracked) | all | **0** | 0 | 0 | 0 | 0 |
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

![downloads](https://img.shields.io/badge/downloads-77-212121) ![clones](https://img.shields.io/badge/clones-2169-2196F3) ![views](https://img.shields.io/badge/views-149-4CAF50) ![releases](https://img.shields.io/badge/releases-25-6f42c1) ![latest stable v1.1.16](https://img.shields.io/badge/latest%20stable%20v1.1.16-2-212121 "Downloads of the latest stable release, all platforms incl. Homebrew")

*Tracking since **2026-10-02** (34 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~34 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 244 | 11 | ▲ +2118.2% |
| Views | 44 | 3 | ▲ +1366.7% |
| Downloads | 35 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1578 | 497 |
| Last 90 Days | 2169 | 709 |
| Lifetime | 2169 | 709 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 1578 | 497 | 1081 | 68.5% |
| Last 90 Days | 2169 | 709 | 1460 | 67.3% |
| Lifetime | 2169 | 709 | 1460 | 67.3% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 114 | 27 |
| Last 90 Days | 149 | 35 |
| Lifetime | 149 | 35 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 27 | — |
| 🗅️ Unique cloners | 497 | 1840.7% |
| 📥 Downloads | 63 | 233.3% |

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
| Last 30 Days | 114 | 27 | 87 | 76.3% |
| Last 90 Days | 149 | 35 | 114 | 76.5% |
| Lifetime | 149 | 35 | 114 | 76.5% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 0 | 0 | 0 |
| 🍎 macOS | 63 | 63 | 77 |
| 🐧 Linux | 0 | 0 | 0 |
| **All downloads (incl. Homebrew)** | **63** | **63** | **77** |

*ℹ️ Not counted above: 33 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days (28 days tracked) | all | **63** | 0 | 63 | 0 | 0 |
| 30 days | stable | **63** | 0 | 63 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days (28 days tracked) | all | **63** | 0 | 63 | 0 | 0 |
| 90 days | stable | **63** | 0 | 63 | 0 | 0 |
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
| v1.1.3 | 0 | 3 | 0 | 0 | **3** |
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
| 🍎 macOS | 77 | **77** |
| 🐧 Linux | 0 | **0** |

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.0.4 | 7 | 2026-10-04 |
| v1.1.11 | 5 | 2026-10-20 |
| v1.1.0 | 5 | 2026-10-15 |
| v1.0.0 | 5 | 2026-10-02 |
| v1.1.8 | 4 | 2026-10-19 |
| v1.0.5 | 4 | 2026-10-13 |
| v1.0.1 | 4 | 2026-10-03 |
| v1.1.12 | 3 | 2026-11-03 |
| v1.1.9 | 3 | 2026-10-20 |
| v1.1.7 | 3 | 2026-10-18 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear. 🍺 is Homebrew (its own copies of the Mac file, not counted again under 🍎); releases without Homebrew copies show 0.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | 🍺 | All downloads (incl. Homebrew) |
|---------|-----------|-----|----|----|----|----|------------------------------|
| v1.1.16 | 2026-11-04 | 3d | 0 | 2 | 0 | 0 | **2** |
| v1.1.15 | 2026-11-04 | 3d | 0 | 2 | 0 | 0 | **2** |
| v1.1.14 | 2026-11-04 | 3d | 0 | 2 | 0 | 0 | **2** |
| v1.1.13 | 2026-11-03 | 4d | 0 | 2 | 0 | 0 | **2** |
| v1.1.12 | 2026-11-03 | 4d | 0 | 3 | 0 | 0 | **3** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#macreplica)**

---

# neolume

![downloads](https://img.shields.io/badge/downloads-145-212121) ![clones](https://img.shields.io/badge/clones-817-2196F3) ![views](https://img.shields.io/badge/views-8-4CAF50) ![releases](https://img.shields.io/badge/releases-19-6f42c1) ![latest stable v1.0.18](https://img.shields.io/badge/latest%20stable%20v1.0.18-6-212121 "Downloads of the latest stable release, all platforms incl. Homebrew")

*Tracking since **2026-10-27** (9 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~9 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 415 | 402 | ▲ +3.2% |
| Views | 3 | 5 | ▼ -40.0% |
| Downloads | 80 | 65 | ▲ +23.1% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 817 | 153 |
| Last 90 Days | 817 | 153 |
| Lifetime | 817 | 153 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 817 | 153 | 664 | 81.3% |
| Last 90 Days | 817 | 153 | 664 | 81.3% |
| Lifetime | 817 | 153 | 664 | 81.3% |

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
| 🗅️ Unique cloners | 153 | 3060.0% |
| 📥 Downloads | 145 | 2900.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 2

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| itsab1989.github.io | 2 | 1 |
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
| 🪟 Windows | 46 | 46 | 46 |
| 🍎 macOS | 52 | 52 | 52 |
| 🐧 Linux | 47 | 47 | 47 |
| **All downloads (incl. Homebrew)** | **145** | **145** | **145** |

*ℹ️ Not counted above: 42 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days (10 days tracked) | all | **145** | 46 | 52 | 47 | 0 |
| 30 days | stable | **145** | 46 | 52 | 47 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days (10 days tracked) | all | **145** | 46 | 52 | 47 | 0 |
| 90 days | stable | **145** | 46 | 52 | 47 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-10-28** on; the stable/beta split from **2026-10-28**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v1.0.18` - **6** downloads (published 2026-11-05)

<details>
<summary><strong>📦 Per-version downloads</strong> (19 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v1.0.18 | 2 | 2 | 2 | 0 | **6** |
| v1.0.17 | 2 | 2 | 2 | 0 | **6** |
| v1.0.16 | 2 | 2 | 2 | 0 | **6** |
| v1.0.15 | 4 | 7 | 4 | 0 | **15** |
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
| 🪟 Windows | 23 | 23 | **46** |
| 🍎 macOS | 27 | 25 | **52** |
| 🐧 Linux | 22 | 25 | **47** |

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.0.12 | 17 | 2026-11-03 |
| v1.0.15 | 15 | 2026-11-04 |
| v1.0.3 | 9 | 2026-10-27 |
| v1.0.7 | 8 | 2026-10-30 |
| v1.0.5 | 8 | 2026-10-28 |
| v1.0.8 | 7 | 2026-10-30 |
| v1.0.6 | 7 | 2026-10-29 |
| v1.0.2 | 7 | 2026-10-27 |
| v1.0.0 | 7 | 2026-10-27 |
| v1.0.18 | 6 | 2026-11-05 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear. 🍺 is Homebrew (its own copies of the Mac file, not counted again under 🍎); releases without Homebrew copies show 0.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | 🍺 | All downloads (incl. Homebrew) |
|---------|-----------|-----|----|----|----|----|------------------------------|
| v1.0.18 | 2026-11-05 | 2d | 2 | 2 | 2 | 0 | **6** |
| v1.0.17 | 2026-11-05 | 2d | 2 | 2 | 2 | 0 | **6** |
| v1.0.16 | 2026-11-04 | 3d | 2 | 2 | 2 | 0 | **6** |
| v1.0.15 | 2026-11-04 | 3d | 4 | 7 | 4 | 0 | **15** |
| v1.0.14 | 2026-11-04 | 3d | 2 | 2 | 2 | 0 | **6** |
| v1.0.13 | 2026-11-04 | 3d | 2 | 2 | 2 | 0 | **6** |
| v1.0.12 | 2026-11-03 | 4d | 6 | 5 | 6 | 0 | **17** |
| v1.0.11 | 2026-11-02 | 5d | 2 | 2 | 2 | 0 | **6** |
| v1.0.10 | 2026-11-01 | 6d | 2 | 2 | 2 | 0 | **6** |
| v1.0.9 | 2026-10-31 | 7d | 2 | 2 | 2 | 0 | **6** |
| v1.0.8 | 2026-10-30 | 8d | 2 | 2 | 3 | 0 | **7** |
| v1.0.7 | 2026-10-30 | 8d | 3 | 3 | 2 | 0 | **8** |
| v1.0.6 | 2026-10-29 | 9d | 2 | 3 | 2 | 0 | **7** |
| v1.0.5 | 2026-10-28 | 10d | 3 | 2 | 3 | 0 | **8** |
| v1.0.4 | 2026-10-27 | 11d | 2 | 2 | 2 | 0 | **6** |
| v1.0.3 | 2026-10-27 | 11d | 2 | 5 | 2 | 0 | **9** |
| v1.0.2 | 2026-10-27 | 11d | 2 | 2 | 3 | 0 | **7** |
| v1.0.1 | 2026-10-27 | 11d | 2 | 2 | 2 | 0 | **6** |
| v1.0.0 | 2026-10-27 | 11d | 2 | 3 | 2 | 0 | **7** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#neolume)**

---

*This dashboard is automatically updated daily using GitHub Actions.*
