See full Reference and Usage Guide at:
https://itsab1989.github.io/github-traffic-downloads-dashboard/

> This is a modified version of the original [github-traffic-dashboard](https://github.com/soul-traveller/github-traffic-dashboard), extended with platform-specific download statistics (Windows / macOS / Linux).

# 📊 GitHub Traffic & Downloads Dashboard

This dashboard tracks historical traffic data (clones, views, and release downloads) for GitHub repositories.

**Last Updated:** 2026-10-31T00:53:45.500483Z

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

![downloads incl. Homebrew](https://img.shields.io/badge/downloads%20incl.%20Homebrew-8752-212121) ![clones](https://img.shields.io/badge/clones-37839-2196F3) ![views](https://img.shields.io/badge/views-9470-4CAF50) ![releases](https://img.shields.io/badge/releases-923-6f42c1) ![latest stable v4.3.20](https://img.shields.io/badge/latest%20stable%20v4.3.20-58-212121 "Downloads of the latest stable release, all platforms incl. Homebrew") ![latest beta v4.3.10-beta.1](https://img.shields.io/badge/latest%20beta%20v4.3.10--beta.1-13-757575 "Downloads of the latest beta release, all platforms incl. Homebrew")

*Tracking since **2026-05-02** (181 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~181 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 251 | 4858 | ▼ -94.8% |
| Views | 309 | 245 | ▲ +26.1% |
| Downloads | 5130 | 191 | ▲ +2585.9% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 6776 | 807 |
| Last 90 Days | 19394 | 5737 |
| Lifetime | 37839 | 9798 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 6776 | 807 | 5969 | 88.1% |
| Last 90 Days | 19394 | 5737 | 13657 | 70.4% |
| Lifetime | 37839 | 9798 | 28041 | 74.1% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1709 | 522 |
| Last 90 Days | 5187 | 1431 |
| Lifetime | 9470 | 2455 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 522 | — |
| 🗅️ Unique cloners | 807 | 154.6% |
| 📥 Downloads | 5698 | 1091.6% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 10

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| aocr.org | 73 | 73 |
| Google | 44 | 32 |
| search.brave.com | 29 | 5 |
| yandex.ru | 21 | 8 |
| itsab1989.github.io | 16 | 13 |
| away.vk.ru | 16 | 3 |
| printerknowledge.com | 14 | 8 |
| github.com | 8 | 7 |
| dpreview.com | 5 | 3 |
| hub.displaycal.net | 2 | 2 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 1709 | 522 | 1187 | 69.5% |
| Last 90 Days | 5187 | 1431 | 3756 | 72.4% |
| Lifetime | 9470 | 2455 | 7015 | 74.1% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 1727 | 2063 | 2631 |
| 🍎 macOS | 2324 | 2719 | 4297 |
| 🐧 Linux | 1451 | 1515 | 1628 |
| 🍺 Homebrew | 196 | 196 | 196 |
| **All downloads (incl. Homebrew)** | **5698** | **6492** | **8752** |

*ℹ️ Not counted above: 174 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days | all | **5698** | 1727 | 2324 | 1451 | 196 |
| 30 days | stable | **1592** | 559 | 561 | 327 | 145 |
| 30 days | beta | **4151** | 1179 | 1797 | 1124 | 51 |
| 90 days | all | **6492** | 2063 | 2719 | 1515 | 196 |
| 90 days | stable | **2035** | 779 | 763 | 350 | 145 |
| 90 days | beta | **4502** | 1296 | 1991 | 1165 | 51 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-05-25** on; the stable/beta split from **2026-05-25**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v4.3.20` - **58** downloads (published 2026-10-29)

<details>
<summary><strong>📦 Per-version downloads</strong> (923 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v4.3.20 | 30 | 12 | 5 | 11 | **58** |
| v4.3.19 | 44 | 10 | 6 | 10 | **70** |
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
| v4.3.3-beta.2 *(beta)* | 2 | 6 | 3 | 0 | **11** |
| v4.3.3-beta.1 *(beta)* | 3 | 12 | 6 | 0 | **21** |
| v4.3.2 | 56 | 56 | 7 | 0 | **119** |
| v4.3.1 | 3 | 7 | 2 | 0 | **12** |
| v4.3.0 | 4 | 7 | 3 | 0 | **14** |
| v4.3.0-beta.49 *(beta)* | 4 | 5 | 2 | 0 | **11** |
| v4.3.0-beta.48 *(beta)* | 3 | 6 | 3 | 0 | **12** |
| v4.3.0-beta.47 *(beta)* | 4 | 5 | 2 | 0 | **11** |
| v4.3.0-beta.46 *(beta)* | 3 | 7 | 2 | 0 | **12** |
| v4.3.0-beta.45 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v4.3.0-beta.44 *(beta)* | 4 | 8 | 2 | 0 | **14** |
| v4.3.0-beta.43 *(beta)* | 3 | 6 | 2 | 0 | **11** |
| v4.3.0-beta.42 *(beta)* | 4 | 6 | 2 | 0 | **12** |
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
| v4.3.0-beta.28 *(beta)* | 2 | 5 | 1 | 0 | **8** |
| v4.3.0-beta.27 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.3.0-beta.26 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v4.3.0-beta.25 *(beta)* | 2 | 4 | 4 | 0 | **10** |
| v4.3.0-beta.24 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v4.3.0-beta.23 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.3.0-beta.22 *(beta)* | 2 | 5 | 4 | 0 | **11** |
| v4.3.0-beta.21 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v4.3.0-beta.20 *(beta)* | 2 | 4 | 4 | 0 | **10** |
| v4.3.0-beta.19 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.3.0-beta.18 *(beta)* | 6 | 5 | 2 | 0 | **13** |
| v4.3.0-beta.17 *(beta)* | 5 | 7 | 3 | 0 | **15** |
| v4.3.0-beta.16 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v4.3.0-beta.15 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.3.0-beta.14 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v4.3.0-beta.13 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v4.3.0-beta.12 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v4.3.0-beta.11 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.3.0-beta.10 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v4.3.0-beta.9 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v4.3.0-beta.8 *(beta)* | 2 | 6 | 3 | 0 | **11** |
| v4.3.0-beta.7 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v4.3.0-beta.6 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v4.3.0-beta.5 *(beta)* | 4 | 5 | 4 | 0 | **13** |
| v4.2.7 | 57 | 49 | 8 | 0 | **114** |
| v4.2.6 | 5 | 3 | 3 | 0 | **11** |
| v4.3.0-beta.4 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v4.2.5 | 5 | 7 | 3 | 0 | **15** |
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
| v4.1.5-beta.9 *(beta)* | 7 | 11 | 8 | 0 | **26** |
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
| v4.1.3-beta.21 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.3-beta.20 *(beta)* | 6 | 4 | 2 | 0 | **12** |
| v4.1.3-beta.19 *(beta)* | 5 | 2 | 2 | 0 | **9** |
| v4.1.3-beta.18 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v4.1.3-beta.17 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.3-beta.16 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.3-beta.15 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.3-beta.14 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.3-beta.13 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.3-beta.12 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v4.1.3-beta.11 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v4.1.3-beta.10 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.3-beta.9 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.3-beta.8 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.3-beta.7 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.3-beta.6 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v4.1.3-beta.5 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v4.1.3-beta.4 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.3-beta.3 *(beta)* | 2 | 5 | 3 | 0 | **10** |
| v4.1.3-beta.2 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.3-beta.1 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.2 | 19 | 22 | 3 | 0 | **44** |
| v4.1.2-beta.10 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.2-beta.9 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.1.2-beta.8 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.2-beta.7 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v4.1.2-beta.6 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.1.2-beta.5 *(beta)* | 3 | 3 | 1 | 0 | **7** |
| v4.1.2-beta.4 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v4.1.2-beta.3 *(beta)* | 3 | 2 | 2 | 0 | **7** |
| v4.1.2-beta.2 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v4.1.2-beta.1 *(beta)* | 2 | 4 | 3 | 0 | **9** |
| v4.1.1 | 31 | 16 | 2 | 0 | **49** |
| v4.1.0 | 15 | 10 | 4 | 0 | **29** |
| v4.0.2-beta.12 *(beta)* | 1 | 4 | 2 | 0 | **7** |
| v4.0.2-beta.11 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.0.2-beta.10 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v4.0.2-beta.9 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.0.2-beta.8 *(beta)* | 1 | 4 | 2 | 0 | **7** |
| v4.0.2-beta.7 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.0.2-beta.6 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v4.0.2-beta.5 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.0.2-beta.4 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.0.2-beta.3 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v4.0.2-beta.2 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.0.2-beta.1 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v4.0.1 | 4 | 8 | 2 | 0 | **14** |
| v4.0.0 | 5 | 10 | 2 | 0 | **17** |
| v4.0.0-beta.5 *(beta)* | 2 | 5 | 1 | 0 | **8** |
| v4.0.0-beta.4 *(beta)* | 2 | 4 | 1 | 0 | **7** |
| v4.0.0-beta.3 *(beta)* | 3 | 3 | 1 | 0 | **7** |
| v4.0.0-beta.2 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v4.0.0-beta.1 *(beta)* | 4 | 5 | 2 | 0 | **11** |
| v3.14.8-beta.222 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.221 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.220 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.219 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.218 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.217 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.216 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.215 *(beta)* | 3 | 2 | 2 | 0 | **7** |
| v3.14.8-beta.214 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.213 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.212 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.211 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.210 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.207 *(beta)* | 5 | 3 | 2 | 0 | **10** |
| v3.14.8-beta.206 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.14.8-beta.205 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.204 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.203 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.202 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.14.8-beta.201 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.200 *(beta)* | 1 | 2 | 2 | 0 | **5** |
| v3.14.8-beta.199 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.198 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.197 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.196 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.195 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.194 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.193 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.192 *(beta)* | 3 | 6 | 4 | 0 | **13** |
| v3.14.8-beta.191 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.14.8-beta.190 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.14.8-beta.189 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.14.8-beta.188 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.187 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.186 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.185 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.184 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.183 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.14.8-beta.182 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.14.8-beta.181 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.180 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.179 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.178 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.177 *(beta)* | 1 | 2 | 1 | 0 | **4** |
| v3.14.8-beta.176 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.175 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.14.8-beta.174 *(beta)* | 3 | 5 | 4 | 0 | **12** |
| v3.14.8-beta.173 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.14.8-beta.172 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.14.8-beta.171 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.170 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.14.8-beta.165 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.14.8-beta.162 *(beta)* | 3 | 2 | 1 | 0 | **6** |
| v3.14.8-beta.160 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.14.8-beta.159 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.158 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.14.8-beta.157 *(beta)* | 1 | 2 | 1 | 0 | **4** |
| v3.14.8-beta.156 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.155 *(beta)* | 4 | 7 | 4 | 0 | **15** |
| v3.14.8-beta.154 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.153 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.152 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.151 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.150 *(beta)* | 1 | 4 | 2 | 0 | **7** |
| v3.14.8-beta.149 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.14.8-beta.148 *(beta)* | 3 | 4 | 1 | 0 | **8** |
| v3.14.8-beta.147 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.146 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.14.8-beta.145 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.144 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.143 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.142 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.141 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.140 *(beta)* | 2 | 4 | 1 | 0 | **7** |
| v3.14.8-beta.139 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.14.8-beta.138 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.137 *(beta)* | 3 | 4 | 1 | 0 | **8** |
| v3.14.8-beta.136 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.135 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.134 *(beta)* | 3 | 3 | 1 | 0 | **7** |
| v3.14.8-beta.133 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.132 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.131 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.130 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.129 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.128 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.127 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.126 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.125 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.14.8-beta.124 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.123 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.122 *(beta)* | 3 | 2 | 2 | 0 | **7** |
| v3.14.8-beta.121 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.120 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.119 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.118 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.14.8-beta.117 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.116 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.115 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.114 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.113 *(beta)* | 3 | 2 | 2 | 0 | **7** |
| v3.14.8-beta.112 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.111 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.110 *(beta)* | 2 | 1 | 2 | 0 | **5** |
| v3.14.8-beta.109 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.108 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.107 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.106 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.105 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.104 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.103 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.102 *(beta)* | 1 | 4 | 2 | 0 | **7** |
| v3.14.8-beta.101 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.100 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.14.8-beta.99 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.98 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.97 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.96 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.95 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.94 *(beta)* | 5 | 3 | 2 | 0 | **10** |
| v3.14.8-beta.93 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.92 *(beta)* | 3 | 3 | 1 | 0 | **7** |
| v3.14.8-beta.91 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.90 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.89 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.88 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.87 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.86 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.85 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.84 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.83 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.82 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.81 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.80 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.79 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.78 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.77 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.76 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.75 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.74 *(beta)* | 6 | 3 | 2 | 0 | **11** |
| v3.14.8-beta.73 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.72 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.71 *(beta)* | 1 | 4 | 2 | 0 | **7** |
| v3.14.8-beta.70 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.69 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.68 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.67 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.66 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.65 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.64 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.63 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.62 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.61 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.60 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.59 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.58 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.57 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.14.8-beta.56 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.55 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.14.8-beta.54 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.53 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.52 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.51 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.50 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.49 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.48 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.47 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.46 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.14.8-beta.45 *(beta)* | 4 | 5 | 3 | 0 | **12** |
| v3.14.8-beta.44 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.43 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.42 *(beta)* | 4 | 7 | 4 | 0 | **15** |
| v3.14.8-beta.41 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.14.8-beta.40 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.39 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.38 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.37 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.36 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.14.8-beta.35 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.14.8-beta.34 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.33 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.32 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.31 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.30 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.29 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.28 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.14.8-beta.27 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.26 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.25 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.24 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.23 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.14.8-beta.22 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.14.8-beta.21 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.20 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.19 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.18 *(beta)* | 1 | 4 | 2 | 0 | **7** |
| v3.14.8-beta.17 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.16 *(beta)* | 2 | 3 | 3 | 0 | **8** |
| v3.14.8-beta.15 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.14 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v3.14.8-beta.13 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.12 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.10 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.9 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.14.8-beta.8 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.14.8-beta.7 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.14.8-beta.6 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.5 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.4 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.3 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.14.8-beta.2 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.1 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.7 | 29 | 33 | 6 | 0 | **68** |
| v3.14.6 | 3 | 3 | 2 | 0 | **8** |
| v3.14.5 | 3 | 4 | 1 | 0 | **8** |
| v3.14.4 | 6 | 10 | 3 | 0 | **19** |
| v3.14.3 | 7 | 12 | 5 | 0 | **24** |
| v3.14.2 | 4 | 5 | 2 | 0 | **11** |
| v3.14.1 | 3 | 5 | 2 | 0 | **10** |
| v3.14.0 | 4 | 6 | 2 | 0 | **12** |
| v3.13.12-beta.35 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v3.13.12-beta.34 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.33 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.12-beta.32 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.13.12-beta.31 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.30 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.29 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.28 *(beta)* | 1 | 4 | 2 | 0 | **7** |
| v3.13.12-beta.27 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.26 *(beta)* | 4 | 5 | 2 | 0 | **11** |
| v3.13.12-beta.25 *(beta)* | 5 | 6 | 3 | 0 | **14** |
| v3.13.12-beta.24 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.12-beta.23 *(beta)* | 6 | 7 | 3 | 0 | **16** |
| v3.13.12-beta.22 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.13.12-beta.21 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.13.12-beta.20 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.12-beta.19 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.13.12-beta.18 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.17 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.16 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.15 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.12-beta.14 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.13 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.12 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.12-beta.11 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.12-beta.10 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.9 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.13.12-beta.8 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.12-beta.7 *(beta)* | 3 | 3 | 2 | 0 | **8** |
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
| v3.13.7-beta.3 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.13.7-beta.2 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.7-beta.1 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.13.6 | 9 | 9 | 3 | 0 | **21** |
| v3.13.6-beta.4 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.6-beta.3 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.6-beta.2 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.6-beta.1 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.5 | 7 | 12 | 2 | 0 | **21** |
| v3.13.4 | 6 | 7 | 2 | 0 | **15** |
| v3.13.4-beta.11 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.4-beta.10 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.4-beta.9 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.4-beta.8 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.4-beta.7 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.4-beta.6 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.4-beta.5 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.4-beta.4 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.4-beta.3 *(beta)* | 1 | 5 | 2 | 0 | **8** |
| v3.13.4-beta.2 *(beta)* | 1 | 2 | 2 | 0 | **5** |
| v3.13.4-beta.1 *(beta)* | 1 | 3 | 0 | 0 | **4** |
| v3.13.3 | 7 | 7 | 3 | 0 | **17** |
| v3.13.2 | 2 | 5 | 2 | 0 | **9** |
| v3.13.1 | 6 | 5 | 3 | 0 | **14** |
| v3.13.0 | 1 | 9 | 1 | 0 | **11** |
| v3.13.0-beta.143 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.13.0-beta.142 *(beta)* | 1 | 3 | 1 | 0 | **5** |
| v3.13.0-beta.141 *(beta)* | 1 | 3 | 1 | 0 | **5** |
| v3.13.0-beta.140 *(beta)* | 1 | 3 | 1 | 0 | **5** |
| v3.13.0-beta.139 *(beta)* | 1 | 3 | 1 | 0 | **5** |
| v3.13.0-beta.138 *(beta)* | 0 | 4 | 2 | 0 | **6** |
| v3.13.0-beta.137 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.13.0-beta.136 *(beta)* | 3 | 8 | 1 | 0 | **12** |
| v3.13.0-beta.135 *(beta)* | 1 | 2 | 1 | 0 | **4** |
| v3.13.0-beta.134 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.13.0-beta.133 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v3.13.0-beta.132 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.131 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.13.0-beta.130 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.129 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.128 *(beta)* | 2 | 5 | 1 | 0 | **8** |
| v3.13.0-beta.127 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.126 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.125 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.124 *(beta)* | 2 | 6 | 2 | 0 | **10** |
| v3.13.0-beta.123 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.122 *(beta)* | 3 | 9 | 2 | 0 | **14** |
| v3.13.0-beta.121 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.120 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.119 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.118 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.117 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.13.0-beta.116 *(beta)* | 3 | 3 | 1 | 0 | **7** |
| v3.13.0-beta.115 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.114 *(beta)* | 3 | 4 | 1 | 0 | **8** |
| v3.13.0-beta.113 *(beta)* | 3 | 9 | 2 | 0 | **14** |
| v3.13.0-beta.112 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.111 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.110 *(beta)* | 3 | 7 | 2 | 0 | **12** |
| v3.13.0-beta.109 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.108 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.107 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.106 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.105 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.13.0-beta.104 *(beta)* | 4 | 7 | 4 | 0 | **15** |
| v3.13.0-beta.103 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.102 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.101 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.100 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.99 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.13.0-beta.98 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.97 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.96 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.95 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.0-beta.94 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.0-beta.93 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.92 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.91 *(beta)* | 7 | 11 | 6 | 0 | **24** |
| v3.13.0-beta.90 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.89 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.88 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.87 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.86 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.13.0-beta.85 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.13.0-beta.84 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.83 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.82 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.81 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.80 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.79 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.78 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.77 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.76 *(beta)* | 2 | 2 | 2 | 0 | **6** |
| v3.13.0-beta.75 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.74 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.73 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.72 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.13.0-beta.71 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.70 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.13.0-beta.69 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.13.0-beta.68 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.67 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.13.0-beta.66 *(beta)* | 2 | 4 | 1 | 0 | **7** |
| v3.13.0-beta.65 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.13.0-beta.64 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.63 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.62 *(beta)* | 4 | 6 | 2 | 0 | **12** |
| v3.13.0-beta.60 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.59 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.58 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.57 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.56 *(beta)* | 3 | 2 | 2 | 0 | **7** |
| v3.13.0-beta.55 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.0-beta.54 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.53 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.52 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.51 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.50 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.49 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.13.0-beta.48 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.47 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.46 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.13.0-beta.45 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.44 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.43 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.42 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.41 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.40 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.39 *(beta)* | 8 | 13 | 7 | 0 | **28** |
| v3.13.0-beta.38 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.37 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.13.0-beta.36 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.35 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.34 *(beta)* | 4 | 5 | 4 | 0 | **13** |
| v3.13.0-beta.33 *(beta)* | 4 | 7 | 4 | 0 | **15** |
| v3.13.0-beta.32 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.31 *(beta)* | 6 | 9 | 6 | 0 | **21** |
| v3.13.0-beta.30 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.29 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.28 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.13.0-beta.27 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.26 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.25 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.24 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.13.0-beta.23 *(beta)* | 2 | 2 | 1 | 0 | **5** |
| v3.13.0-beta.22 *(beta)* | 4 | 4 | 2 | 0 | **10** |
| v3.13.0-beta.21 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.20 *(beta)* | 3 | 2 | 2 | 0 | **7** |
| v3.13.0-beta.19 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.0-beta.18 *(beta)* | 1 | 4 | 2 | 0 | **7** |
| v3.13.0-beta.17 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.16 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.15 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.13.0-beta.14 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.13 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v3.13.0-beta.12 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.11 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.10 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.9 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.8 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.13.0-beta.7 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.6 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.5 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.4 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.3 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.2 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.12.1 | 31 | 25 | 3 | 0 | **59** |
| v3.13.0-beta.1 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.12.1-beta.1 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.12.0 | 7 | 8 | 2 | 0 | **17** |
| v3.12.0-beta.18 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.12.0-beta.17 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.12.0-beta.16 *(beta)* | 2 | 5 | 2 | 0 | **9** |
| v3.12.0-beta.15 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.12.0-beta.14 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.12.0-beta.13 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.12 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.12.0-beta.11 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.10 *(beta)* | 2 | 3 | 1 | 0 | **6** |
| v3.12.0-beta.9 *(beta)* | 3 | 4 | 1 | 0 | **8** |
| v3.12.0-beta.8 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.12.0-beta.7 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.12.0-beta.6 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.5 *(beta)* | 3 | 4 | 2 | 0 | **9** |
| v3.12.0-beta.4 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.12.0-beta.3 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.12.0-beta.2 *(beta)* | 2 | 4 | 1 | 0 | **7** |
| v3.12.0-beta.1 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.11.25 | 9 | 8 | 2 | 0 | **19** |
| v3.11.24 | 3 | 7 | 2 | 0 | **12** |
| v3.11.23 | 7 | 5 | 2 | 0 | **14** |
| v3.11.22 | 0 | 3 | 2 | 0 | **5** |
| v3.11.21 | 3 | 4 | 2 | 0 | **9** |
| v3.11.20 | 3 | 5 | 2 | 0 | **10** |
| v3.11.19 | 3 | 5 | 2 | 0 | **10** |
| v3.11.18 | 10 | 8 | 2 | 0 | **20** |
| v3.11.17 | 2 | 3 | 2 | 0 | **7** |
| v3.11.16 | 3 | 2 | 2 | 0 | **7** |
| v3.11.15 | 2 | 3 | 2 | 0 | **7** |
| v3.11.14 | 2 | 3 | 2 | 0 | **7** |
| v3.11.13 | 3 | 3 | 2 | 0 | **8** |
| v3.11.12 | 2 | 2 | 2 | 0 | **6** |
| v3.11.11 | 8 | 7 | 2 | 0 | **17** |
| v3.11.10 | 2 | 5 | 2 | 0 | **9** |
| v3.11.9 | 3 | 5 | 2 | 0 | **10** |
| v3.11.8 | 3 | 8 | 2 | 0 | **13** |
| v3.11.7 | 4 | 4 | 2 | 0 | **10** |
| v3.11.6 | 4 | 5 | 2 | 0 | **11** |
| v3.11.5 | 2 | 4 | 2 | 0 | **8** |
| v3.11.4 | 4 | 4 | 2 | 0 | **10** |
| v3.11.3 | 3 | 6 | 2 | 0 | **11** |
| v3.11.2 | 2 | 5 | 2 | 0 | **9** |
| v3.11.1 | 2 | 5 | 2 | 0 | **9** |
| v3.11.0 | 5 | 5 | 2 | 0 | **12** |
| v3.10.28 | 3 | 3 | 2 | 0 | **8** |
| v3.10.27 | 2 | 3 | 2 | 0 | **7** |
| v3.10.26 | 4 | 5 | 2 | 0 | **11** |
| v3.10.25 | 2 | 3 | 2 | 0 | **7** |
| v3.10.24 | 3 | 5 | 2 | 0 | **10** |
| v3.10.23 | 2 | 5 | 1 | 0 | **8** |
| v3.10.22 | 2 | 3 | 2 | 0 | **7** |
| v3.10.21 | 3 | 5 | 2 | 0 | **10** |
| v3.10.20 | 2 | 5 | 2 | 0 | **9** |
| v3.10.19 | 3 | 5 | 2 | 0 | **10** |
| v3.10.18 | 3 | 6 | 2 | 0 | **11** |
| v3.10.17 | 1 | 3 | 2 | 0 | **6** |
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
| v3.9.31 | 2 | 2 | 2 | 0 | **6** |
| v3.9.30 | 2 | 4 | 2 | 0 | **8** |
| v3.9.29 | 4 | 6 | 2 | 0 | **12** |
| v3.9.28 | 3 | 5 | 2 | 0 | **10** |
| v3.9.27 | 2 | 4 | 2 | 0 | **8** |
| v3.9.26 | 2 | 5 | 2 | 0 | **9** |
| v3.9.25 | 2 | 4 | 2 | 0 | **8** |
| v3.9.24 | 1 | 5 | 1 | 0 | **7** |
| v3.9.23 | 3 | 5 | 2 | 0 | **10** |
| v3.9.22 | 2 | 3 | 2 | 0 | **7** |
| v3.9.21 | 5 | 5 | 2 | 0 | **12** |
| v3.9.20 | 2 | 4 | 1 | 0 | **7** |
| v3.9.19 | 4 | 3 | 2 | 0 | **9** |
| v3.9.18 | 2 | 5 | 2 | 0 | **9** |
| v3.9.17 | 3 | 4 | 2 | 0 | **9** |
| v3.9.16 | 4 | 6 | 1 | 0 | **11** |
| v3.9.15 | 3 | 4 | 2 | 0 | **9** |
| v3.9.14 | 2 | 3 | 2 | 0 | **7** |
| v3.9.13 | 3 | 5 | 2 | 0 | **10** |
| v3.9.12 | 1 | 4 | 2 | 0 | **7** |
| v3.9.11 | 2 | 3 | 2 | 0 | **7** |
| v3.9.10 | 1 | 4 | 1 | 0 | **6** |
| v3.9.9 | 2 | 1 | 2 | 0 | **5** |
| v3.9.8 | 2 | 3 | 2 | 0 | **7** |
| v3.9.7 | 2 | 3 | 1 | 0 | **6** |
| v3.9.6 | 3 | 4 | 1 | 0 | **8** |
| v3.9.5 | 2 | 3 | 2 | 0 | **7** |
| v3.9.4 | 0 | 3 | 1 | 0 | **4** |
| v3.9.3 | 3 | 1 | 2 | 0 | **6** |
| v3.9.2 | 2 | 2 | 2 | 0 | **6** |
| v3.9.1 | 3 | 4 | 1 | 0 | **8** |
| v3.9.0 | 2 | 1 | 1 | 0 | **4** |
| v3.8.19 | 5 | 7 | 2 | 0 | **14** |
| v3.8.18 | 3 | 5 | 2 | 0 | **10** |
| v3.8.17 | 3 | 8 | 4 | 0 | **15** |
| v3.8.16 | 6 | 11 | 3 | 0 | **20** |
| v3.8.15 | 3 | 3 | 2 | 0 | **8** |
| v3.8.14 | 1 | 4 | 2 | 0 | **7** |
| v3.8.13 | 2 | 6 | 1 | 0 | **9** |
| v3.8.12 | 6 | 2 | 0 | 0 | **8** |
| v3.8.11 | 4 | 1 | 0 | 0 | **5** |
| v3.8.10 | 0 | 3 | 0 | 0 | **3** |
| v3.8.9 | 2 | 1 | 0 | 0 | **3** |
| v3.8.8 | 4 | 7 | 0 | 0 | **11** |
| v3.8.7 | 0 | 0 | 0 | 0 | **0** |
| v3.8.6 | 2 | 2 | 0 | 0 | **4** |
| v3.8.5 | 2 | 4 | 0 | 0 | **6** |
| v3.8.4 | 16 | 4 | 0 | 0 | **20** |
| v3.8.3 | 12 | 2 | 0 | 0 | **14** |
| v3.8.2 | 2 | 2 | 0 | 0 | **4** |
| v3.8.1 | 1 | 1 | 0 | 0 | **2** |
| v3.8.0 | 13 | 7 | 2 | 0 | **22** |
| v3.8.0-beta.31 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.8.0-beta.30 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.8.0-beta.29 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.8.0-beta.28 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.8.0-beta.27 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.8.0-beta.26 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v3.8.0-beta.25 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.24 *(beta)* | 7 | 10 | 6 | 0 | **23** |
| v3.8.0-beta.23 *(beta)* | 6 | 9 | 6 | 0 | **21** |
| v3.8.0-beta.22 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.8.0-beta.21 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.8.0-beta.20 *(beta)* | 4 | 3 | 2 | 0 | **9** |
| v3.8.0-beta.19 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.18 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.17 *(beta)* | 0 | 1 | 1 | 0 | **2** |
| v3.8.0-beta.16 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.8.0-beta.15 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.8.0-beta.14 *(beta)* | 6 | 1 | 0 | 0 | **7** |
| v3.8.0-beta.13 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.12 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.11 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.8.0-beta.10 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.8.0-beta.9 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.7.42 | 13 | 3 | 0 | 0 | **16** |
| v3.8.0-beta.8 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.6 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.7.41 | 1 | 1 | 0 | 0 | **2** |
| v3.8.0-beta.5 *(beta)* | 4 | 8 | 4 | 0 | **16** |
| v3.8.0-beta.4 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.7.40 | 2 | 1 | 0 | 0 | **3** |
| v3.7.39 | 1 | 2 | 0 | 0 | **3** |
| v3.8.0-beta.3 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.2 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.8.0-beta.1 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.7.38 | 1 | 28 | 0 | 0 | **29** |
| v3.7.37 | 1 | 10 | 0 | 0 | **11** |
| v3.7.36 | 1 | 3 | 0 | 0 | **4** |
| v3.7.35 | 0 | 3 | 0 | 0 | **3** |
| v3.7.34 | 0 | 3 | 0 | 0 | **3** |
| v3.7.33 | 1 | 4 | 0 | 0 | **5** |
| v3.7.32 | 1 | 4 | 0 | 0 | **5** |
| v3.7.31 | 1 | 3 | 0 | 0 | **4** |
| v3.7.30 | 0 | 3 | 0 | 0 | **3** |
| v3.7.29 | 0 | 3 | 0 | 0 | **3** |
| v3.7.28 | 0 | 4 | 0 | 0 | **4** |
| v3.7.27 | 3 | 7 | 2 | 0 | **12** |
| v3.7.26 | 2 | 5 | 2 | 0 | **9** |
| v3.7.25 | 2 | 3 | 0 | 0 | **5** |
| v3.7.24 | 2 | 3 | 0 | 0 | **5** |
| v3.7.23 | 0 | 4 | 0 | 0 | **4** |
| v3.7.22 | 2 | 7 | 2 | 0 | **11** |
| v3.7.21 | 1 | 5 | 0 | 0 | **6** |
| v3.7.20 | 0 | 4 | 0 | 0 | **4** |
| v3.7.19 | 4 | 5 | 0 | 0 | **9** |
| v3.7.18 | 0 | 4 | 0 | 0 | **4** |
| v3.7.17 | 1 | 4 | 0 | 0 | **5** |
| v3.7.16 | 0 | 3 | 0 | 0 | **3** |
| v3.7.15 | 1 | 6 | 0 | 0 | **7** |
| v3.7.14 | 3 | 5 | 0 | 0 | **8** |
| v3.7.13 | 0 | 5 | 0 | 0 | **5** |
| v3.7.12 | 0 | 4 | 0 | 0 | **4** |
| v3.7.11 | 3 | 7 | 2 | 0 | **12** |
| v3.7.10 | 2 | 7 | 0 | 0 | **9** |
| v3.7.9 | 0 | 10 | 0 | 0 | **10** |
| v3.7.8 | 0 | 10 | 0 | 0 | **10** |
| v3.7.7 | 0 | 4 | 0 | 0 | **4** |
| v3.7.6 | 0 | 6 | 0 | 0 | **6** |
| v3.7.5 | 5 | 7 | 1 | 0 | **13** |
| v3.7.4 | 1 | 8 | 0 | 0 | **9** |
| v3.7.3 | 0 | 8 | 0 | 0 | **8** |
| v3.7.2 | 3 | 7 | 2 | 0 | **12** |
| v3.7.1 | 0 | 40 | 2 | 0 | **42** |
| v3.7.0 | 3 | 35 | 3 | 0 | **41** |
| v3.6.7 | 3 | 42 | 3 | 0 | **48** |
| v3.6.6 | 4 | 32 | 2 | 0 | **38** |
| v3.6.5 | 3 | 42 | 3 | 0 | **48** |
| v3.6.4 | 3 | 48 | 3 | 0 | **54** |
| v3.6.3 | 0 | 4 | 0 | 0 | **4** |
| v3.6.2 | 0 | 3 | 0 | 0 | **3** |
| v3.6.1 | 0 | 6 | 0 | 0 | **6** |
| v3.6.0 | 3 | 9 | 4 | 0 | **16** |
| v3.5.13 | 1 | 4 | 3 | 0 | **8** |
| v3.5.12 | 0 | 4 | 0 | 0 | **4** |
| v3.5.11 | 0 | 3 | 0 | 0 | **3** |
| v3.5.10 | 1 | 3 | 0 | 0 | **4** |
| v3.5.9 | 2 | 3 | 0 | 0 | **5** |
| v3.5.8 | 1 | 5 | 0 | 0 | **6** |
| v3.5.7 | 1 | 3 | 0 | 0 | **4** |
| v3.5.6 | 0 | 3 | 0 | 0 | **3** |
| v3.5.5 | 0 | 6 | 0 | 0 | **6** |
| v3.5.4 | 0 | 3 | 0 | 0 | **3** |
| v3.5.3 | 0 | 4 | 0 | 0 | **4** |
| v3.5.2 | 1 | 4 | 0 | 0 | **5** |
| v3.5.1 | 0 | 5 | 0 | 0 | **5** |
| v3.5.0 | 1 | 7 | 1 | 0 | **9** |
| v3.5.0-beta.6 *(beta)* | 0 | 4 | 1 | 0 | **5** |
| v3.5.0-beta.5 *(beta)* | 0 | 3 | 2 | 0 | **5** |
| v3.2.9 | 3 | 4 | 0 | 0 | **7** |
| v3.5.0-beta.4 *(beta)* | 0 | 5 | 1 | 0 | **6** |
| v3.5.0-beta.3 *(beta)* | 0 | 3 | 0 | 0 | **3** |
| v3.5.0-beta.2 *(beta)* | 0 | 5 | 0 | 0 | **5** |
| v3.5.0-beta.1 *(beta)* | 0 | 3 | 0 | 0 | **3** |
| v3.2.8 | 3 | 8 | 0 | 0 | **11** |
| v3.2.7 | 0 | 6 | 0 | 0 | **6** |
| v3.2.6 | 0 | 3 | 0 | 0 | **3** |
| v3.2.5 | 0 | 3 | 0 | 0 | **3** |
| v3.2.4 | 0 | 3 | 0 | 0 | **3** |
| v3.2.3 | 0 | 2 | 0 | 0 | **2** |
| v3.2.2 | 0 | 3 | 0 | 0 | **3** |
| v3.2.1 | 0 | 2 | 0 | 0 | **2** |
| v3.2.0 | 0 | 3 | 0 | 0 | **3** |
| v3.2.0-beta.3 *(beta)* | 1 | 4 | 0 | 0 | **5** |
| v3.2.0-beta.2 *(beta)* | 0 | 4 | 0 | 0 | **4** |
| v3.2.0-beta.1 *(beta)* | 2 | 5 | 0 | 0 | **7** |
| v3.1.4 | 0 | 3 | 0 | 0 | **3** |
| v3.1.3 | 0 | 4 | 0 | 0 | **4** |
| v3.1.2 | 0 | 3 | 0 | 0 | **3** |
| v3.1.1 | 1 | 5 | 0 | 0 | **6** |
| v3.1.0 | 3 | 5 | 0 | 0 | **8** |
| v3.0.2 | 2 | 5 | 0 | 0 | **7** |
| v3.0.1 | 1 | 2 | 0 | 0 | **3** |
| v3.0.0 | 5 | 8 | 0 | 0 | **13** |
| v3.0.0-beta.10 *(beta)* | 3 | 17 | 0 | 0 | **20** |
| v3.0.0-beta.9 *(beta)* | 0 | 3 | 0 | 0 | **3** |
| v3.0.0-beta.8 *(beta)* | 2 | 3 | 0 | 0 | **5** |
| v3.0.0-beta.7 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v3.0.0-beta.6 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v3.0.0-beta.5 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.0.0-beta.4 *(beta)* | 1 | 3 | 0 | 0 | **4** |
| v3.0.0-beta.3 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v3.0.0-beta.2 *(beta)* | 5 | 2 | 0 | 0 | **7** |
| v3.0.0-beta.1 *(beta)* | 8 | 2 | 0 | 0 | **10** |
| v2.11.0 | 0 | 4 | 0 | 0 | **4** |
| v2.10.3 | 0 | 4 | 0 | 0 | **4** |
| v2.10.2 | 0 | 7 | 0 | 0 | **7** |
| v2.10.1 | 0 | 6 | 0 | 0 | **6** |
| v2.10.0 | 0 | 3 | 0 | 0 | **3** |
| v2.9.4 | 0 | 4 | 0 | 0 | **4** |
| v2.9.3 | 0 | 3 | 0 | 0 | **3** |
| v2.9.2 | 0 | 3 | 0 | 0 | **3** |
| v2.9.1 | 0 | 2 | 0 | 0 | **2** |
| v2.9.0 | 0 | 9 | 0 | 0 | **9** |
| v2.8.1 | 0 | 5 | 0 | 0 | **5** |
| v2.8.0 | 0 | 3 | 0 | 0 | **3** |
| v2.7.0 | 0 | 4 | 0 | 0 | **4** |
| v2.6.0 | 0 | 4 | 0 | 0 | **4** |
| v2.5.0 | 0 | 4 | 0 | 0 | **4** |
| v2.4.1 | 0 | 9 | 0 | 0 | **9** |
| v2.4.0 | 0 | 2 | 0 | 0 | **2** |
| v2.3.3 | 0 | 3 | 0 | 0 | **3** |
| v2.3.2 | 0 | 2 | 0 | 0 | **2** |
| v2.3.1 | 0 | 2 | 0 | 0 | **2** |
| v2.3.0 | 0 | 1 | 0 | 0 | **1** |
| v2.2.3 | 0 | 12 | 0 | 0 | **12** |
| v2.2.2 | 0 | 9 | 0 | 0 | **9** |
| v2.2.1 | 0 | 3 | 0 | 0 | **3** |
| v2.2.0 | 0 | 6 | 0 | 0 | **6** |
| v2.1.4 | 0 | 2 | 0 | 0 | **2** |
| v2.1.2 | 0 | 10 | 0 | 0 | **10** |
| v2.1.1 | 0 | 7 | 0 | 0 | **7** |
| v2.1.0 | 0 | 3 | 0 | 0 | **3** |
| v2.0.9 | 0 | 8 | 0 | 0 | **8** |
| v2.0.8 | 0 | 2 | 0 | 0 | **2** |
| v2.0.7 | 0 | 3 | 0 | 0 | **3** |
| v2.0.6 | 0 | 3 | 0 | 0 | **3** |
| v2.0.5 | 0 | 5 | 0 | 0 | **5** |
| v2.0.4 | 0 | 7 | 0 | 0 | **7** |
| v2.0.3 | 0 | 6 | 0 | 0 | **6** |
| v2.0.2 | 0 | 2 | 0 | 0 | **2** |
| v2.0.1 | 0 | 1 | 0 | 0 | **1** |
| v2.0.0 | 0 | 4 | 0 | 0 | **4** |
| v1.7.1 | 0 | 6 | 0 | 0 | **6** |
| v1.7.0 | 0 | 3 | 0 | 0 | **3** |
| v1.6.1 | 0 | 3 | 0 | 0 | **3** |
| v1.6.0 | 0 | 3 | 0 | 0 | **3** |
| v1.5.2 | 0 | 3 | 0 | 0 | **3** |
| v1.5.1 | 0 | 5 | 0 | 0 | **5** |
| v1.5.0 | 0 | 3 | 0 | 0 | **3** |
| v1.4.0 | 0 | 3 | 0 | 0 | **3** |
| v1.3.1 | 0 | 5 | 0 | 0 | **5** |
| v1.3.0 | 0 | 3 | 0 | 0 | **3** |
| v1.2.0 | 0 | 3 | 0 | 0 | **3** |
| v1.1.6 | 0 | 4 | 0 | 0 | **4** |
| v1.1.5 | 0 | 2 | 0 | 0 | **2** |
| v1.1.3 | 0 | 9 | 0 | 0 | **9** |
| v1.1.2 | 0 | 3 | 0 | 0 | **3** |
| v1.1.1 | 0 | 2 | 0 | 0 | **2** |
| v1.1.0 | 0 | 2 | 0 | 0 | **2** |
| v1.0.3 | 0 | 4 | 0 | 0 | **4** |
| v1.0.2 | 0 | 4 | 0 | 0 | **4** |
| v1.0.1 | 0 | 4 | 0 | 0 | **4** |
| v1.0.0 | 0 | 1 | 0 | 0 | **1** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | arm64 | x86_64 | universal | Total |
|----------|-------|-------|-------|-------|
| 🪟 Windows | 829 | 1802 | 0 | **2631** |
| 🍎 macOS | 2111 | 1111 | 1075 | **4297** |
| 🐧 Linux | 789 | 839 | 0 | **1628** |
| 🍺 Homebrew | 138 | 58 | 0 | **196** |

*💡 Low-volume builds (<2% of lifetime downloads), candidates to stop shipping: 🍺 Homebrew arm64 (138, 1.6%); 🍺 Homebrew x86_64 (58, 0.7%).*

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v4.3.2 | 119 | 2026-09-28 |
| v4.2.7 | 114 | 2026-09-12 |
| v4.3.4 | 108 | 2026-10-10 |
| v4.1.4 | 74 | 2026-08-28 |
| v4.3.19 | 70 | 2026-10-28 |
| v3.14.7 | 68 | 2026-07-22 |
| v3.12.1 | 59 | 2026-06-25 |
| v4.3.20 | 58 | 2026-10-29 |
| v3.6.4 | 54 | 2026-05-17 |
| v4.3.7 | 49 | 2026-10-18 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear. 🍺 is Homebrew (its own copies of the Mac file, not counted again under 🍎); releases without Homebrew copies show 0.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | 🍺 | All downloads (incl. Homebrew) |
|---------|-----------|-----|----|----|----|----|------------------------------|
| v4.3.20 | 2026-10-29 | 3d | 30 | 12 | 5 | 11 | **58** |
| v4.3.19 | 2026-10-28 | 4d | 44 | 10 | 6 | 10 | **70** |
| v4.3.18 | 2026-10-27 | 5d | 8 | 5 | 4 | 5 | **22** |
| v4.3.17 | 2026-10-27 | 5d | 12 | 13 | 5 | 5 | **35** |
| v4.3.16 | 2026-10-26 | 6d | 13 | 6 | 3 | 9 | **31** |
| v4.3.15 | 2026-10-25 | 7d | 8 | 9 | 5 | 4 | **26** |
| v4.3.14 | 2026-10-25 | 7d | 6 | 4 | 2 | 5 | **17** |
| v4.3.13 | 2026-10-24 | 8d | 11 | 8 | 2 | 4 | **25** |
| v4.3.12 | 2026-10-24 | 8d | 8 | 1 | 2 | 8 | **19** |
| v4.3.11 | 2026-10-24 | 8d | 4 | 5 | 2 | 4 | **15** |
| v4.3.10 | 2026-10-23 | 9d | 9 | 5 | 3 | 6 | **23** |
| v4.3.10-beta.1 | 2026-10-22 | 10d | 4 | 3 | 2 | 4 | **13** |
| v4.3.9 | 2026-10-21 | 11d | 17 | 7 | 2 | 19 | **45** |
| v4.3.8 | 2026-10-21 | 11d | 6 | 5 | 3 | 4 | **18** |
| v4.3.8-beta.3 | 2026-10-21 | 11d | 3 | 3 | 3 | 5 | **14** |
| v4.3.8-beta.2 | 2026-10-20 | 12d | 5 | 3 | 2 | 4 | **14** |
| v4.3.8-beta.1 | 2026-10-20 | 12d | 3 | 4 | 2 | 3 | **12** |
| v4.3.7 | 2026-10-18 | 14d | 30 | 7 | 4 | 8 | **49** |
| v4.3.6 | 2026-10-18 | 14d | 5 | 8 | 2 | 5 | **20** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq)**

---

# ChromIQ-Patches

![downloads](https://img.shields.io/badge/downloads-46-212121) ![clones](https://img.shields.io/badge/clones-390-2196F3) ![views](https://img.shields.io/badge/views-132-4CAF50) ![releases](https://img.shields.io/badge/releases-5-6f42c1) ![latest stable v1.2.1](https://img.shields.io/badge/latest%20stable%20v1.2.1-23-212121 "Downloads of the latest stable release, all platforms incl. Homebrew")

*Tracking since **2026-07-02** (120 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~120 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 5 | 11 | ▼ -54.5% |
| Views | 11 | 0 | — |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 35 | 33 |
| Last 90 Days | 71 | 68 |
| Lifetime | 390 | 215 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 35 | 33 | 2 | 5.7% |
| Last 90 Days | 71 | 68 | 3 | 4.2% |
| Lifetime | 390 | 215 | 175 | 44.9% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 19 | 13 |
| Last 90 Days | 54 | 32 |
| Lifetime | 132 | 63 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 13 | — |
| 🗅️ Unique cloners | 33 | 253.8% |
| 📥 Downloads | 1 | 7.7% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 4

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| aocr.org | 3 | 3 |
| github.com | 3 | 3 |
| Bing | 1 | 1 |
| itsab1989.github.io | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 19 | 13 | 6 | 31.6% |
| Last 90 Days | 54 | 32 | 22 | 40.7% |
| Lifetime | 132 | 63 | 69 | 52.3% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 1 | 6 | 19 |
| 🍎 macOS | 0 | 3 | 24 |
| 🐧 Linux | 0 | 0 | 3 |
| **All downloads (incl. Homebrew)** | **1** | **9** | **46** |

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days | all | **1** | 1 | 0 | 0 | 0 |
| 30 days | stable | **1** | 1 | 0 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days | all | **9** | 6 | 3 | 0 | 0 |
| 90 days | stable | **9** | 6 | 3 | 0 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-07-03** on; the stable/beta split from **2026-07-03**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v1.2.1` - **23** downloads (published 2026-07-07)

<details>
<summary><strong>📦 Per-version downloads</strong> (5 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v1.2.1 | 10 | 12 | 1 | 0 | **23** |
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
| 🍎 macOS | 18 | 3 | 3 | **24** |
| 🐧 Linux | 0 | 3 | 0 | **3** |

**Top 5 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.2.1 | 23 | 2026-07-07 |
| v1.2.0 | 14 | 2026-07-03 |
| v1.0.1 | 4 | 2026-07-02 |
| v1.0.0 | 4 | 2026-07-02 |
| v1.1.0 | 1 | 2026-07-02 |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq-patches)**

---

# ChromIQ-Gamut-Viewer

![downloads](https://img.shields.io/badge/downloads-39-212121) ![clones](https://img.shields.io/badge/clones-2502-2196F3) ![views](https://img.shields.io/badge/views-73-4CAF50) ![releases](https://img.shields.io/badge/releases-96-6f42c1) ![latest stable v2.54.0](https://img.shields.io/badge/latest%20stable%20v2.54.0-5-212121 "Downloads of the latest stable release, all platforms incl. Homebrew")

*Tracking since **2026-08-13** (78 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~78 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 1 | 2 | ▼ -50.0% |
| Views | 9 | 0 | — |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 11 | 11 |
| Last 90 Days | 2502 | 526 |
| Lifetime | 2502 | 526 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 11 | 11 | 0 | 0.0% |
| Last 90 Days | 2502 | 526 | 1976 | 79.0% |
| Lifetime | 2502 | 526 | 1976 | 79.0% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 9 | 1 |
| Last 90 Days | 73 | 18 |
| Lifetime | 73 | 18 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 1 | — |
| 🗅️ Unique cloners | 11 | 1100.0% |
| 📥 Downloads | 1 | 100.0% |

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
| Last 30 Days | 9 | 1 | 8 | 88.9% |
| Last 90 Days | 73 | 18 | 55 | 75.3% |
| Lifetime | 73 | 18 | 55 | 75.3% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 0 | 9 | 10 |
| 🍎 macOS | 1 | 19 | 23 |
| 🐧 Linux | 0 | 4 | 6 |
| **All downloads (incl. Homebrew)** | **1** | **32** | **39** |

*ℹ️ Not counted above: 11 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days | all | **1** | 0 | 1 | 0 | 0 |
| 30 days | stable | **1** | 0 | 1 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days (78 days tracked) | all | **32** | 9 | 19 | 4 | 0 |
| 90 days | stable | **32** | 9 | 19 | 4 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-08-15** on; the stable/beta split from **2026-08-15**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v2.54.0` - **5** downloads (published 2026-08-31)

<details>
<summary><strong>📦 Per-version downloads</strong> (96 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v2.54.0 | 1 | 4 | 0 | 0 | **5** |
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
| 🍎 macOS | 18 | 5 | **23** |
| 🐧 Linux | 3 | 3 | **6** |

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v2.50.1 | 6 | 2026-08-21 |
| v2.54.0 | 5 | 2026-08-31 |
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

![downloads](https://img.shields.io/badge/downloads-0-212121) ![clones](https://img.shields.io/badge/clones-8878-2196F3) ![views](https://img.shields.io/badge/views-39-4CAF50) ![releases](https://img.shields.io/badge/releases-0-6f42c1)

*Tracking since **2026-07-30** (92 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~92 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 247 | 402 | ▼ -38.6% |
| Views | 7 | 0 | — |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1327 | 523 |
| Last 90 Days | 8699 | 5009 |
| Lifetime | 8878 | 5050 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 1327 | 523 | 804 | 60.6% |
| Last 90 Days | 8699 | 5009 | 3690 | 42.4% |
| Lifetime | 8878 | 5050 | 3828 | 43.1% |

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
| 🗅️ Unique cloners | 523 | 6537.5% |
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
| 90 days (79 days tracked) | all | **0** | 0 | 0 | 0 | 0 |
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

**Different cloners in the last 14 days:** 144 (as of 2026-10-31; GitHub's own 14-day count, recorded daily from 2026-10-09 on)

![downloads](https://img.shields.io/badge/downloads-0-212121) ![clones](https://img.shields.io/badge/clones-535-2196F3) ![views](https://img.shields.io/badge/views-1-4CAF50) ![releases](https://img.shields.io/badge/releases-0-6f42c1)

*Tracking since **2026-10-09** (21 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~21 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 134 | 180 | ▼ -25.6% |
| Views | 1 | 0 | — |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 535 | 298 |
| Last 90 Days | 535 | 298 |
| Lifetime | 535 | 298 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 535 | 298 | 237 | 44.3% |
| Last 90 Days | 535 | 298 | 237 | 44.3% |
| Lifetime | 535 | 298 | 237 | 44.3% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1 | 1 |
| Last 90 Days | 1 | 1 |
| Lifetime | 1 | 1 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 1 | — |
| 🗅️ Unique cloners | 298 | 29800.0% |
| 📥 Downloads | 0 | 0.0% |

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
| Last 30 Days | 1 | 1 | 0 | 0.0% |
| Last 90 Days | 1 | 1 | 0 | 0.0% |
| Lifetime | 1 | 1 | 0 | 0.0% |

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
| 30 days (22 days tracked) | all | **0** | 0 | 0 | 0 | 0 |
| 30 days | stable | **0** | 0 | 0 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days (22 days tracked) | all | **0** | 0 | 0 | 0 | 0 |
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

![downloads](https://img.shields.io/badge/downloads-42-212121) ![clones](https://img.shields.io/badge/clones-1924-2196F3) ![views](https://img.shields.io/badge/views-105-4CAF50) ![releases](https://img.shields.io/badge/releases-20-6f42c1) ![latest stable v1.1.11](https://img.shields.io/badge/latest%20stable%20v1.1.11-3-212121 "Downloads of the latest stable release, all platforms incl. Homebrew")

*Tracking since **2026-10-02** (28 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~28 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 9 | 640 | ▼ -98.6% |
| Views | 0 | 39 | ▼ -100.0% |
| Downloads | 0 | 12 | ▼ -100.0% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1924 | 663 |
| Last 90 Days | 1924 | 663 |
| Lifetime | 1924 | 663 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 1924 | 663 | 1261 | 65.5% |
| Last 90 Days | 1924 | 663 | 1261 | 65.5% |
| Lifetime | 1924 | 663 | 1261 | 65.5% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 105 | 31 |
| Last 90 Days | 105 | 31 |
| Lifetime | 105 | 31 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 31 | — |
| 🗅️ Unique cloners | 663 | 2138.7% |
| 📥 Downloads | 28 | 90.3% |

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
| Last 30 Days | 105 | 31 | 74 | 70.5% |
| Last 90 Days | 105 | 31 | 74 | 70.5% |
| Lifetime | 105 | 31 | 74 | 70.5% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 0 | 0 | 0 |
| 🍎 macOS | 28 | 28 | 42 |
| 🐧 Linux | 0 | 0 | 0 |
| **All downloads (incl. Homebrew)** | **28** | **28** | **42** |

*ℹ️ Not counted above: 7 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days (22 days tracked) | all | **28** | 0 | 28 | 0 | 0 |
| 30 days | stable | **28** | 0 | 28 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days (22 days tracked) | all | **28** | 0 | 28 | 0 | 0 |
| 90 days | stable | **28** | 0 | 28 | 0 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-10-10** on; the stable/beta split from **2026-10-10**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v1.1.11` - **3** downloads (published 2026-10-20)

<details>
<summary><strong>📦 Per-version downloads</strong> (20 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v1.1.11 | 0 | 3 | 0 | 0 | **3** |
| v1.1.10 | 0 | 1 | 0 | 0 | **1** |
| v1.1.9 | 0 | 1 | 0 | 0 | **1** |
| v1.1.8 | 0 | 3 | 0 | 0 | **3** |
| v1.1.7 | 0 | 1 | 0 | 0 | **1** |
| v1.1.6 | 0 | 1 | 0 | 0 | **1** |
| v1.1.5 | 0 | 1 | 0 | 0 | **1** |
| v1.1.4 | 0 | 1 | 0 | 0 | **1** |
| v1.1.3 | 0 | 2 | 0 | 0 | **2** |
| v1.1.2 | 0 | 1 | 0 | 0 | **1** |
| v1.1.1 | 0 | 1 | 0 | 0 | **1** |
| v1.1.0 | 0 | 4 | 0 | 0 | **4** |
| v1.0.7 | 0 | 2 | 0 | 0 | **2** |
| v1.0.6 | 0 | 1 | 0 | 0 | **1** |
| v1.0.5 | 0 | 3 | 0 | 0 | **3** |
| v1.0.4 | 0 | 6 | 0 | 0 | **6** |
| v1.0.3 | 0 | 1 | 0 | 0 | **1** |
| v1.0.2 | 0 | 2 | 0 | 0 | **2** |
| v1.0.1 | 0 | 3 | 0 | 0 | **3** |
| v1.0.0 | 0 | 4 | 0 | 0 | **4** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | other | Total |
|----------|-------|-------|
| 🪟 Windows | 0 | **0** |
| 🍎 macOS | 42 | **42** |
| 🐧 Linux | 0 | **0** |

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.0.4 | 6 | 2026-10-04 |
| v1.1.0 | 4 | 2026-10-15 |
| v1.0.0 | 4 | 2026-10-02 |
| v1.1.11 | 3 | 2026-10-20 |
| v1.1.8 | 3 | 2026-10-19 |
| v1.0.5 | 3 | 2026-10-13 |
| v1.0.1 | 3 | 2026-10-03 |
| v1.1.3 | 2 | 2026-10-17 |
| v1.0.7 | 2 | 2026-10-14 |
| v1.0.2 | 2 | 2026-10-04 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear. 🍺 is Homebrew (its own copies of the Mac file, not counted again under 🍎); releases without Homebrew copies show 0.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | 🍺 | All downloads (incl. Homebrew) |
|---------|-----------|-----|----|----|----|----|------------------------------|
| v1.1.11 | 2026-10-20 | 12d | 0 | 3 | 0 | 0 | **3** |
| v1.1.10 | 2026-10-20 | 12d | 0 | 1 | 0 | 0 | **1** |
| v1.1.9 | 2026-10-20 | 12d | 0 | 1 | 0 | 0 | **1** |
| v1.1.8 | 2026-10-19 | 13d | 0 | 3 | 0 | 0 | **3** |
| v1.1.7 | 2026-10-18 | 14d | 0 | 1 | 0 | 0 | **1** |
| v1.1.6 | 2026-10-18 | 14d | 0 | 1 | 0 | 0 | **1** |
| v1.1.5 | 2026-10-18 | 14d | 0 | 1 | 0 | 0 | **1** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#macreplica)**

---

# neolume

![downloads](https://img.shields.io/badge/downloads-65-212121) ![clones](https://img.shields.io/badge/clones-272-2196F3) ![views](https://img.shields.io/badge/views-5-4CAF50) ![releases](https://img.shields.io/badge/releases-9-6f42c1) ![latest stable v1.0.8](https://img.shields.io/badge/latest%20stable%20v1.0.8-7-212121 "Downloads of the latest stable release, all platforms incl. Homebrew")

*Tracking since **2026-10-27** (3 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~3 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 272 | 0 | — |
| Views | 5 | 0 | — |
| Downloads | 65 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 272 | 42 |
| Last 90 Days | 272 | 42 |
| Lifetime | 272 | 42 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 272 | 42 | 230 | 84.6% |
| Last 90 Days | 272 | 42 | 230 | 84.6% |
| Lifetime | 272 | 42 | 230 | 84.6% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 5 | 2 |
| Last 90 Days | 5 | 2 |
| Lifetime | 5 | 2 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 2 | — |
| 🗅️ Unique cloners | 42 | 2100.0% |
| 📥 Downloads | 65 | 3250.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 1

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| itsab1989.github.io | 2 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 5 | 2 | 3 | 60.0% |
| Last 90 Days | 5 | 2 | 3 | 60.0% |
| Lifetime | 5 | 2 | 3 | 60.0% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 20 | 20 | 20 |
| 🍎 macOS | 24 | 24 | 24 |
| 🐧 Linux | 21 | 21 | 21 |
| **All downloads (incl. Homebrew)** | **65** | **65** | **65** |

*ℹ️ Not counted above: 22 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All downloads (incl. Homebrew) | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|--------------------------------|---------|-------|-------|----------|
| 30 days (4 days tracked) | all | **65** | 20 | 24 | 21 | 0 |
| 30 days | stable | **65** | 20 | 24 | 21 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days (4 days tracked) | all | **65** | 20 | 24 | 21 | 0 |
| 90 days | stable | **65** | 20 | 24 | 21 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-10-28** on; the stable/beta split from **2026-10-28**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. The Stable rows are the closer ones to users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS, and the "All downloads (incl. Homebrew)" figures include them. For ChromIQ the copies start with 4.3.3-beta.17: brew installs of earlier versions fetched the normal file and count under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v1.0.8` - **7** downloads (published 2026-10-30)

<details>
<summary><strong>📦 Per-version downloads</strong> (9 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
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
| 🪟 Windows | 10 | 10 | **20** |
| 🍎 macOS | 13 | 11 | **24** |
| 🐧 Linux | 10 | 11 | **21** |

**Top 9 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.0.3 | 9 | 2026-10-27 |
| v1.0.7 | 8 | 2026-10-30 |
| v1.0.5 | 8 | 2026-10-28 |
| v1.0.8 | 7 | 2026-10-30 |
| v1.0.6 | 7 | 2026-10-29 |
| v1.0.2 | 7 | 2026-10-27 |
| v1.0.0 | 7 | 2026-10-27 |
| v1.0.4 | 6 | 2026-10-27 |
| v1.0.1 | 6 | 2026-10-27 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear. 🍺 is Homebrew (its own copies of the Mac file, not counted again under 🍎); releases without Homebrew copies show 0.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | 🍺 | All downloads (incl. Homebrew) |
|---------|-----------|-----|----|----|----|----|------------------------------|
| v1.0.8 | 2026-10-30 | 2d | 2 | 2 | 3 | 0 | **7** |
| v1.0.7 | 2026-10-30 | 2d | 3 | 3 | 2 | 0 | **8** |
| v1.0.6 | 2026-10-29 | 3d | 2 | 3 | 2 | 0 | **7** |
| v1.0.5 | 2026-10-28 | 4d | 3 | 2 | 3 | 0 | **8** |
| v1.0.4 | 2026-10-27 | 5d | 2 | 2 | 2 | 0 | **6** |
| v1.0.3 | 2026-10-27 | 5d | 2 | 5 | 2 | 0 | **9** |
| v1.0.2 | 2026-10-27 | 5d | 2 | 2 | 3 | 0 | **7** |
| v1.0.1 | 2026-10-27 | 5d | 2 | 2 | 2 | 0 | **6** |
| v1.0.0 | 2026-10-27 | 5d | 2 | 3 | 2 | 0 | **7** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#neolume)**

---

*This dashboard is automatically updated daily using GitHub Actions.*
