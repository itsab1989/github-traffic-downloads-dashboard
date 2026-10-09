See full Reference and Usage Guide at:
https://itsab1989.github.io/github-traffic-downloads-dashboard/

> This is a modified version of the original [github-traffic-dashboard](https://github.com/soul-traveller/github-traffic-dashboard), extended with platform-specific download statistics (Windows / macOS / Linux).

# 📊 GitHub Traffic & Downloads Dashboard

This dashboard tracks historical traffic data (clones, views, and release downloads) for GitHub repositories.

**Last Updated:** 2026-10-09T15:49:53.680927Z

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
- Split by platform from the asset file name (Windows, macOS, Linux); **All** is the combined total
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

# ChromIQ

![downloads](https://img.shields.io/badge/downloads-3201-212121) ![clones](https://img.shields.io/badge/clones-32194-2196F3) ![views](https://img.shields.io/badge/views-8272-4CAF50) ![releases](https://img.shields.io/badge/releases-891-6f42c1)

*Tracking since **2026-05-02** (160 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~160 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 1066 | 2705 | ▼ -60.6% |
| Views | 376 | 486 | ▼ -22.6% |
| Downloads | 119 | 114 | ▲ +4.4% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 5432 | 1135 |
| Last 90 Days | 16645 | 5972 |
| Lifetime | 32194 | 9423 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 5432 | 1135 | 4297 | 79.1% |
| Last 90 Days | 16645 | 5972 | 10673 | 64.1% |
| Lifetime | 32194 | 9423 | 22771 | 70.7% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 2084 | 514 |
| Last 90 Days | 5142 | 1232 |
| Lifetime | 8272 | 2041 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 514 | — |
| 🗅️ Unique cloners | 1135 | 220.8% |
| 📥 Downloads | 480 | 93.4% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 10

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| Google | 46 | 31 |
| itsab1989.github.io | 36 | 25 |
| github.com | 29 | 12 |
| yandex.ru | 17 | 3 |
| hub.displaycal.net | 11 | 9 |
| dpreview.com | 11 | 6 |
| search.brave.com | 9 | 4 |
| printerknowledge.com | 8 | 5 |
| DuckDuckGo | 4 | 3 |
| druckerchannel.de | 3 | 3 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 2084 | 514 | 1570 | 75.3% |
| Last 90 Days | 5142 | 1232 | 3910 | 76.0% |
| Lifetime | 8272 | 2041 | 6231 | 75.3% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 190 | 533 | 960 |
| 🍎 macOS | 268 | 689 | 2061 |
| 🐧 Linux | 22 | 91 | 180 |
| 🍺 Homebrew | 0 | 0 | 0 |
| **All** | **480** | **1312** | **3201** |

*ℹ️ Not counted above: 97 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|-----|---------|-------|-------|----------|
| 30 days | all | **480** | 190 | 268 | 22 | 0 |
| 30 days | stable | **268** | 135 | 120 | 13 | 0 |
| 30 days | beta | **212** | 55 | 148 | 9 | 0 |
| 90 days | all | **1312** | 533 | 689 | 91 | 0 |
| 90 days | stable | **712** | 339 | 336 | 39 | 0 |
| 90 days | beta | **600** | 195 | 354 | 52 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-05-25** on; the stable/beta split from **2026-05-25**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. Read the stable column for users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v4.3.3-beta.16` - **13** downloads (published 2026-10-09)

<details>
<summary><strong>📦 Per-version downloads</strong> (891 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v4.3.3-beta.16 *(beta)* | 0 | 13 | 0 | 0 | **13** |
| v4.3.3-beta.15 *(beta)* | 1 | 3 | 0 | 0 | **4** |
| v4.3.3-beta.14 *(beta)* | 1 | 3 | 0 | 0 | **4** |
| v4.3.3-beta.13 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.3.3-beta.12 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v4.3.3-beta.11 *(beta)* | 3 | 4 | 0 | 0 | **7** |
| v4.3.3-beta.10 *(beta)* | 3 | 2 | 0 | 0 | **5** |
| v4.3.3-beta.9 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v4.3.3-beta.8 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v4.3.3-beta.7 *(beta)* | 1 | 3 | 0 | 0 | **4** |
| v4.3.3-beta.6 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v4.3.3-beta.5 *(beta)* | 0 | 3 | 0 | 0 | **3** |
| v4.3.3-beta.4 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.3-beta.3 *(beta)* | 1 | 3 | 0 | 0 | **4** |
| v4.3.3-beta.2 *(beta)* | 0 | 3 | 0 | 0 | **3** |
| v4.3.3-beta.1 *(beta)* | 0 | 9 | 2 | 0 | **11** |
| v4.3.2 | 53 | 51 | 5 | 0 | **109** |
| v4.3.1 | 1 | 3 | 0 | 0 | **4** |
| v4.3.0 | 2 | 4 | 0 | 0 | **6** |
| v4.3.0-beta.49 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v4.3.0-beta.48 *(beta)* | 0 | 3 | 0 | 0 | **3** |
| v4.3.0-beta.47 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v4.3.0-beta.46 *(beta)* | 0 | 3 | 0 | 0 | **3** |
| v4.3.0-beta.45 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v4.3.0-beta.44 *(beta)* | 2 | 5 | 0 | 0 | **7** |
| v4.3.0-beta.43 *(beta)* | 1 | 3 | 0 | 0 | **4** |
| v4.3.0-beta.42 *(beta)* | 1 | 3 | 0 | 0 | **4** |
| v4.3.0-beta.41 *(beta)* | 2 | 4 | 0 | 0 | **6** |
| v4.3.0-beta.40 *(beta)* | 0 | 3 | 0 | 0 | **3** |
| v4.3.0-beta.39 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v4.3.0-beta.38 *(beta)* | 1 | 3 | 0 | 0 | **4** |
| v4.3.0-beta.37 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v4.3.0-beta.36 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v4.3.0-beta.35 *(beta)* | 2 | 2 | 0 | 0 | **4** |
| v4.3.0-beta.34 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v4.3.0-beta.33 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.32 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.31 *(beta)* | 1 | 3 | 0 | 0 | **4** |
| v4.3.0-beta.30 *(beta)* | 0 | 3 | 0 | 0 | **3** |
| v4.3.0-beta.29 *(beta)* | 1 | 3 | 0 | 0 | **4** |
| v4.3.0-beta.28 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.27 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.3.0-beta.26 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v4.3.0-beta.25 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.24 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.23 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.22 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.21 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v4.3.0-beta.20 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.19 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.18 *(beta)* | 4 | 1 | 0 | 0 | **5** |
| v4.3.0-beta.17 *(beta)* | 3 | 1 | 0 | 0 | **4** |
| v4.3.0-beta.16 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v4.3.0-beta.15 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.14 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.3.0-beta.13 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.12 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v4.3.0-beta.11 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.3.0-beta.10 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.9 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v4.3.0-beta.8 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.7 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.3.0-beta.6 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.3.0-beta.5 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.2.7 | 55 | 45 | 6 | 0 | **106** |
| v4.2.6 | 3 | 0 | 0 | 0 | **3** |
| v4.3.0-beta.4 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v4.2.5 | 3 | 3 | 0 | 0 | **6** |
| v4.3.0-beta.3 *(beta)* | 1 | 3 | 0 | 0 | **4** |
| v4.2.4 | 2 | 2 | 0 | 0 | **4** |
| v4.2.3 | 4 | 1 | 0 | 0 | **5** |
| v4.3.0-beta.2 *(beta)* | 5 | 1 | 0 | 0 | **6** |
| v4.2.2 | 1 | 4 | 0 | 0 | **5** |
| v4.3.0-beta.1 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v4.2.1 | 3 | 3 | 0 | 0 | **6** |
| v4.2.0 | 18 | 11 | 3 | 0 | **32** |
| v4.1.5-beta.11 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.1.5-beta.10 *(beta)* | 3 | 2 | 0 | 0 | **5** |
| v4.1.5-beta.9 *(beta)* | 6 | 7 | 6 | 0 | **19** |
| v4.1.5-beta.8 *(beta)* | 5 | 8 | 6 | 0 | **19** |
| v4.1.5-beta.7 *(beta)* | 3 | 5 | 2 | 0 | **10** |
| v4.1.5-beta.6 *(beta)* | 3 | 4 | 3 | 0 | **10** |
| v4.1.5-beta.5 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v4.1.5-beta.4 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.5-beta.3 *(beta)* | 2 | 0 | 0 | 0 | **2** |
| v4.1.5-beta.2 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v4.1.5-beta.1 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v4.1.4 | 33 | 28 | 5 | 0 | **66** |
| v4.1.3 | 3 | 12 | 0 | 0 | **15** |
| v4.1.3-beta.21 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.3-beta.20 *(beta)* | 4 | 1 | 0 | 0 | **5** |
| v4.1.3-beta.19 *(beta)* | 2 | 0 | 0 | 0 | **2** |
| v4.1.3-beta.18 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v4.1.3-beta.17 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.1.3-beta.16 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.1.3-beta.15 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.1.3-beta.14 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.1.3-beta.13 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.1.3-beta.12 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.3-beta.11 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.3-beta.10 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.3-beta.9 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.1.3-beta.8 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.3-beta.7 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.3-beta.6 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.1.3-beta.5 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.1.3-beta.4 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.3-beta.3 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.1.3-beta.2 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.3-beta.1 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.1.2 | 17 | 19 | 1 | 0 | **37** |
| v4.1.2-beta.10 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.2-beta.9 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.2-beta.8 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.2-beta.7 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.2-beta.6 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.2-beta.5 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v4.1.2-beta.4 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.2-beta.3 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.2-beta.2 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.2-beta.1 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.1.1 | 29 | 13 | 0 | 0 | **42** |
| v4.1.0 | 12 | 6 | 2 | 0 | **20** |
| v4.0.2-beta.12 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.0.2-beta.11 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v4.0.2-beta.10 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.0.2-beta.9 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.0.2-beta.8 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.0.2-beta.7 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.0.2-beta.6 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.0.2-beta.5 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.0.2-beta.4 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.0.2-beta.3 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v4.0.2-beta.2 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v4.0.2-beta.1 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.0.1 | 2 | 5 | 0 | 0 | **7** |
| v4.0.0 | 3 | 6 | 0 | 0 | **9** |
| v4.0.0-beta.5 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v4.0.0-beta.4 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.0.0-beta.3 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v4.0.0-beta.2 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v4.0.0-beta.1 *(beta)* | 2 | 2 | 0 | 0 | **4** |
| v3.14.8-beta.222 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.221 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.220 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.219 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.218 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.217 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.216 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.215 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.214 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.213 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.212 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.211 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.210 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.207 *(beta)* | 3 | 0 | 0 | 0 | **3** |
| v3.14.8-beta.206 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.205 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.204 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.203 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.202 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.201 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.200 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.199 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.198 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.197 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.196 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.195 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.194 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.193 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.192 *(beta)* | 1 | 3 | 2 | 0 | **6** |
| v3.14.8-beta.191 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.190 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.189 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.188 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.187 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.186 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.185 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.184 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.183 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.182 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.181 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.180 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.179 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.178 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.177 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.176 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.175 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.174 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.173 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.172 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.171 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.170 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.165 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.162 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.160 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.159 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.158 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.157 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.156 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.155 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.154 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.153 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.152 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.151 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.150 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.149 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.148 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.147 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.146 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.145 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.144 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.14.8-beta.143 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.142 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.141 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.140 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.139 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.14.8-beta.138 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.137 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.136 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.135 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.134 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.133 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.132 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.131 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.130 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.129 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.128 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.127 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.126 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.125 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.14.8-beta.124 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.123 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.122 *(beta)* | 2 | 0 | 0 | 0 | **2** |
| v3.14.8-beta.121 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.120 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.119 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.118 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.14.8-beta.117 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.116 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.115 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.114 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.113 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.112 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.111 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.110 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.109 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.14.8-beta.108 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v3.14.8-beta.107 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.106 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.105 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.104 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.103 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.102 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.101 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.100 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.14.8-beta.99 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.98 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.97 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.96 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.95 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.94 *(beta)* | 3 | 0 | 0 | 0 | **3** |
| v3.14.8-beta.93 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.92 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.91 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.90 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.89 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.88 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.87 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.86 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.85 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.84 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.83 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.82 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.81 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.80 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.79 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.78 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.77 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.76 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.75 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.74 *(beta)* | 4 | 0 | 0 | 0 | **4** |
| v3.14.8-beta.73 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.72 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.71 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.70 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.69 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.68 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.67 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.66 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.65 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.64 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.63 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.62 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.61 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.60 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.59 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.58 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.57 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.56 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.55 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.14.8-beta.54 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.53 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.52 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.51 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.50 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.49 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.48 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.47 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.46 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.45 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.14.8-beta.44 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.43 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.42 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.14.8-beta.41 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.40 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.39 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.38 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.37 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.36 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.35 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.34 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.33 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.32 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.31 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.30 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.14.8-beta.29 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.28 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.27 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.26 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.25 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.24 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.23 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.22 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.21 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.20 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.19 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.18 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.17 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.16 *(beta)* | 0 | 0 | 1 | 0 | **1** |
| v3.14.8-beta.15 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.14 *(beta)* | 0 | 3 | 0 | 0 | **3** |
| v3.14.8-beta.13 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.12 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.10 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.9 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.8-beta.8 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.14.8-beta.7 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.6 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.5 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.4 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.3 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.14.8-beta.2 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.14.8-beta.1 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.14.7 | 27 | 30 | 4 | 0 | **61** |
| v3.14.6 | 1 | 0 | 0 | 0 | **1** |
| v3.14.5 | 1 | 1 | 0 | 0 | **2** |
| v3.14.4 | 4 | 7 | 1 | 0 | **12** |
| v3.14.3 | 6 | 9 | 3 | 0 | **18** |
| v3.14.2 | 3 | 2 | 0 | 0 | **5** |
| v3.14.1 | 1 | 2 | 0 | 0 | **3** |
| v3.14.0 | 2 | 3 | 0 | 0 | **5** |
| v3.13.12-beta.35 *(beta)* | 2 | 3 | 0 | 0 | **5** |
| v3.13.12-beta.34 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.33 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.12-beta.32 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.12-beta.31 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.30 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.29 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.12-beta.28 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.12-beta.27 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.26 *(beta)* | 2 | 2 | 0 | 0 | **4** |
| v3.13.12-beta.25 *(beta)* | 3 | 3 | 2 | 0 | **8** |
| v3.13.12-beta.24 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.13.12-beta.23 *(beta)* | 4 | 4 | 1 | 0 | **9** |
| v3.13.12-beta.22 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.21 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v3.13.12-beta.20 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.13.12-beta.19 *(beta)* | 2 | 2 | 0 | 0 | **4** |
| v3.13.12-beta.18 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.12-beta.17 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.16 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.15 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.12-beta.14 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.13 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.12 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.12-beta.11 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.12-beta.10 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.9 *(beta)* | 2 | 0 | 0 | 0 | **2** |
| v3.13.12-beta.8 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.7 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.13.12-beta.6 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.5 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.13.12-beta.4 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.12-beta.3 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.12-beta.2 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.12-beta.1 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.13.11 | 4 | 11 | 0 | 0 | **15** |
| v3.13.10 | 1 | 2 | 0 | 0 | **3** |
| v3.13.9 | 14 | 4 | 2 | 0 | **20** |
| v3.13.8 | 1 | 5 | 0 | 0 | **6** |
| v3.13.7 | 1 | 1 | 0 | 0 | **2** |
| v3.13.7-beta.5 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.7-beta.4 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.13.7-beta.3 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.7-beta.2 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.7-beta.1 *(beta)* | 2 | 0 | 0 | 0 | **2** |
| v3.13.6 | 8 | 6 | 1 | 0 | **15** |
| v3.13.6-beta.4 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.6-beta.3 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.6-beta.2 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.6-beta.1 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.5 | 5 | 9 | 0 | 0 | **14** |
| v3.13.4 | 4 | 4 | 0 | 0 | **8** |
| v3.13.4-beta.11 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.4-beta.10 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.4-beta.9 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.4-beta.8 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.4-beta.7 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.4-beta.6 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.4-beta.5 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.4-beta.4 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.4-beta.3 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.4-beta.2 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.4-beta.1 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.3 | 5 | 4 | 2 | 0 | **11** |
| v3.13.2 | 2 | 3 | 1 | 0 | **6** |
| v3.13.1 | 5 | 3 | 1 | 0 | **9** |
| v3.13.0 | 1 | 7 | 0 | 0 | **8** |
| v3.13.0-beta.143 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.0-beta.142 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.141 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.140 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.0-beta.139 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.0-beta.138 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.137 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.136 *(beta)* | 2 | 6 | 0 | 0 | **8** |
| v3.13.0-beta.135 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.134 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.133 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.132 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.131 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.130 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.129 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.0-beta.128 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.0-beta.127 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.126 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.125 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.124 *(beta)* | 0 | 3 | 0 | 0 | **3** |
| v3.13.0-beta.123 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.122 *(beta)* | 1 | 6 | 0 | 0 | **7** |
| v3.13.0-beta.121 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.120 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.0-beta.119 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.118 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.117 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.13.0-beta.116 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.13.0-beta.115 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.114 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v3.13.0-beta.113 *(beta)* | 1 | 6 | 0 | 0 | **7** |
| v3.13.0-beta.112 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.13.0-beta.111 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.110 *(beta)* | 1 | 4 | 0 | 0 | **5** |
| v3.13.0-beta.109 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.108 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.107 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.106 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.105 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.104 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.103 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.102 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.101 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.100 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.99 *(beta)* | 2 | 0 | 0 | 0 | **2** |
| v3.13.0-beta.98 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v3.13.0-beta.97 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.13.0-beta.96 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.13.0-beta.95 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.13.0-beta.94 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.13.0-beta.93 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.92 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.91 *(beta)* | 5 | 8 | 4 | 0 | **17** |
| v3.13.0-beta.90 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.89 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.88 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.87 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.86 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.85 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.84 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.83 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.82 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.81 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.80 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.79 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.13.0-beta.78 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.0-beta.77 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.76 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.75 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.74 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.73 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.0-beta.72 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.71 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.70 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.69 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.13.0-beta.68 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.67 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.66 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.65 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.64 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.13.0-beta.63 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.0-beta.62 *(beta)* | 2 | 3 | 0 | 0 | **5** |
| v3.13.0-beta.60 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.59 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.58 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.57 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.56 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.13.0-beta.55 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.13.0-beta.54 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.53 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.52 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.51 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.50 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.49 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.48 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.47 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.46 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.45 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.44 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.43 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.42 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.41 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.40 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.39 *(beta)* | 6 | 10 | 6 | 0 | **22** |
| v3.13.0-beta.38 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.37 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.13.0-beta.36 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.35 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.34 *(beta)* | 2 | 3 | 2 | 0 | **7** |
| v3.13.0-beta.33 *(beta)* | 2 | 4 | 2 | 0 | **8** |
| v3.13.0-beta.32 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.31 *(beta)* | 4 | 6 | 4 | 0 | **14** |
| v3.13.0-beta.30 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.13.0-beta.29 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.28 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.27 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.26 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.25 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.24 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.13.0-beta.23 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.22 *(beta)* | 2 | 1 | 0 | 0 | **3** |
| v3.13.0-beta.21 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.20 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.13.0-beta.19 *(beta)* | 1 | 0 | 0 | 0 | **1** |
| v3.13.0-beta.18 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.17 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.16 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.15 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.14 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.13 *(beta)* | 1 | 2 | 0 | 0 | **3** |
| v3.13.0-beta.12 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.11 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.10 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.0-beta.9 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.8 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.13.0-beta.7 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.6 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.5 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.4 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.3 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.2 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.12.1 | 29 | 22 | 1 | 0 | **52** |
| v3.13.0-beta.1 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.12.1-beta.1 *(beta)* | 2 | 0 | 0 | 0 | **2** |
| v3.12.0 | 5 | 5 | 0 | 0 | **10** |
| v3.12.0-beta.18 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.12.0-beta.17 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.12.0-beta.16 *(beta)* | 0 | 2 | 0 | 0 | **2** |
| v3.12.0-beta.15 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.12.0-beta.14 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.12.0-beta.13 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.12.0-beta.12 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.12.0-beta.11 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.12.0-beta.10 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.12.0-beta.9 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.12.0-beta.8 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.12.0-beta.7 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.12.0-beta.6 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.12.0-beta.5 *(beta)* | 1 | 1 | 0 | 0 | **2** |
| v3.12.0-beta.4 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.12.0-beta.3 *(beta)* | 0 | 0 | 0 | 0 | **0** |
| v3.12.0-beta.2 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.12.0-beta.1 *(beta)* | 0 | 1 | 0 | 0 | **1** |
| v3.11.25 | 7 | 6 | 0 | 0 | **13** |
| v3.11.24 | 1 | 5 | 0 | 0 | **6** |
| v3.11.23 | 5 | 2 | 0 | 0 | **7** |
| v3.11.22 | 0 | 0 | 0 | 0 | **0** |
| v3.11.21 | 1 | 1 | 0 | 0 | **2** |
| v3.11.20 | 2 | 2 | 0 | 0 | **4** |
| v3.11.19 | 1 | 2 | 0 | 0 | **3** |
| v3.11.18 | 8 | 5 | 0 | 0 | **13** |
| v3.11.17 | 0 | 0 | 0 | 0 | **0** |
| v3.11.16 | 1 | 0 | 0 | 0 | **1** |
| v3.11.15 | 0 | 0 | 0 | 0 | **0** |
| v3.11.14 | 0 | 0 | 0 | 0 | **0** |
| v3.11.13 | 1 | 0 | 0 | 0 | **1** |
| v3.11.12 | 0 | 0 | 0 | 0 | **0** |
| v3.11.11 | 6 | 5 | 0 | 0 | **11** |
| v3.11.10 | 0 | 2 | 0 | 0 | **2** |
| v3.11.9 | 1 | 2 | 0 | 0 | **3** |
| v3.11.8 | 1 | 5 | 0 | 0 | **6** |
| v3.11.7 | 2 | 1 | 0 | 0 | **3** |
| v3.11.6 | 2 | 2 | 0 | 0 | **4** |
| v3.11.5 | 0 | 1 | 0 | 0 | **1** |
| v3.11.4 | 2 | 1 | 0 | 0 | **3** |
| v3.11.3 | 1 | 3 | 0 | 0 | **4** |
| v3.11.2 | 0 | 2 | 0 | 0 | **2** |
| v3.11.1 | 0 | 2 | 0 | 0 | **2** |
| v3.11.0 | 3 | 2 | 0 | 0 | **5** |
| v3.10.28 | 1 | 0 | 0 | 0 | **1** |
| v3.10.27 | 0 | 0 | 0 | 0 | **0** |
| v3.10.26 | 2 | 2 | 0 | 0 | **4** |
| v3.10.25 | 0 | 0 | 0 | 0 | **0** |
| v3.10.24 | 1 | 3 | 0 | 0 | **4** |
| v3.10.23 | 0 | 2 | 0 | 0 | **2** |
| v3.10.22 | 0 | 0 | 0 | 0 | **0** |
| v3.10.21 | 1 | 2 | 0 | 0 | **3** |
| v3.10.20 | 0 | 2 | 0 | 0 | **2** |
| v3.10.19 | 1 | 2 | 0 | 0 | **3** |
| v3.10.18 | 1 | 3 | 0 | 0 | **4** |
| v3.10.17 | 0 | 0 | 0 | 0 | **0** |
| v3.10.16 | 0 | 4 | 0 | 0 | **4** |
| v3.10.15 | 3 | 2 | 0 | 0 | **5** |
| v3.10.14 | 1 | 1 | 0 | 0 | **2** |
| v3.10.13 | 0 | 2 | 0 | 0 | **2** |
| v3.10.12 | 0 | 0 | 0 | 0 | **0** |
| v3.10.11 | 0 | 0 | 0 | 0 | **0** |
| v3.10.10 | 0 | 4 | 0 | 0 | **4** |
| v3.10.9 | 1 | 2 | 0 | 0 | **3** |
| v3.10.8 | 0 | 4 | 0 | 0 | **4** |
| v3.10.7 | 0 | 1 | 0 | 0 | **1** |
| v3.10.6 | 0 | 0 | 0 | 0 | **0** |
| v3.10.5 | 4 | 6 | 4 | 0 | **14** |
| v3.10.4 | 0 | 2 | 0 | 0 | **2** |
| v3.10.3 | 0 | 1 | 0 | 0 | **1** |
| v3.10.2 | 7 | 7 | 2 | 0 | **16** |
| v3.10.1 | 0 | 0 | 0 | 0 | **0** |
| v3.10.0 | 1 | 1 | 0 | 0 | **2** |
| v3.9.31 | 0 | 0 | 0 | 0 | **0** |
| v3.9.30 | 0 | 1 | 0 | 0 | **1** |
| v3.9.29 | 2 | 3 | 0 | 0 | **5** |
| v3.9.28 | 1 | 2 | 0 | 0 | **3** |
| v3.9.27 | 0 | 1 | 0 | 0 | **1** |
| v3.9.26 | 0 | 2 | 0 | 0 | **2** |
| v3.9.25 | 0 | 1 | 0 | 0 | **1** |
| v3.9.24 | 0 | 2 | 0 | 0 | **2** |
| v3.9.23 | 1 | 2 | 0 | 0 | **3** |
| v3.9.22 | 0 | 0 | 0 | 0 | **0** |
| v3.9.21 | 3 | 3 | 0 | 0 | **6** |
| v3.9.20 | 0 | 2 | 0 | 0 | **2** |
| v3.9.19 | 2 | 0 | 0 | 0 | **2** |
| v3.9.18 | 0 | 2 | 0 | 0 | **2** |
| v3.9.17 | 1 | 1 | 0 | 0 | **2** |
| v3.9.16 | 2 | 3 | 0 | 0 | **5** |
| v3.9.15 | 1 | 1 | 0 | 0 | **2** |
| v3.9.14 | 0 | 0 | 0 | 0 | **0** |
| v3.9.13 | 2 | 2 | 0 | 0 | **4** |
| v3.9.12 | 0 | 2 | 0 | 0 | **2** |
| v3.9.11 | 0 | 0 | 0 | 0 | **0** |
| v3.9.10 | 0 | 1 | 0 | 0 | **1** |
| v3.9.9 | 0 | 0 | 0 | 0 | **0** |
| v3.9.8 | 0 | 0 | 0 | 0 | **0** |
| v3.9.7 | 0 | 0 | 0 | 0 | **0** |
| v3.9.6 | 1 | 2 | 0 | 0 | **3** |
| v3.9.5 | 0 | 0 | 0 | 0 | **0** |
| v3.9.4 | 0 | 0 | 0 | 0 | **0** |
| v3.9.3 | 1 | 0 | 0 | 0 | **1** |
| v3.9.2 | 0 | 0 | 0 | 0 | **0** |
| v3.9.1 | 1 | 1 | 0 | 0 | **2** |
| v3.9.0 | 0 | 0 | 0 | 0 | **0** |
| v3.8.19 | 4 | 4 | 0 | 0 | **8** |
| v3.8.18 | 1 | 2 | 0 | 0 | **3** |
| v3.8.17 | 2 | 5 | 2 | 0 | **9** |
| v3.8.16 | 4 | 9 | 1 | 0 | **14** |
| v3.8.15 | 1 | 0 | 0 | 0 | **1** |
| v3.8.14 | 0 | 1 | 0 | 0 | **1** |
| v3.8.13 | 0 | 3 | 0 | 0 | **3** |
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
| v3.7.38 | 1 | 27 | 0 | 0 | **28** |
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
| v3.2.0-beta.3 | 1 | 4 | 0 | 0 | **5** |
| v3.2.0-beta.2 | 0 | 4 | 0 | 0 | **4** |
| v3.2.0-beta.1 | 2 | 5 | 0 | 0 | **7** |
| v3.1.4 | 0 | 3 | 0 | 0 | **3** |
| v3.1.3 | 0 | 4 | 0 | 0 | **4** |
| v3.1.2 | 0 | 3 | 0 | 0 | **3** |
| v3.1.1 | 1 | 5 | 0 | 0 | **6** |
| v3.1.0 | 3 | 5 | 0 | 0 | **8** |
| v3.0.2 | 2 | 5 | 0 | 0 | **7** |
| v3.0.1 | 1 | 2 | 0 | 0 | **3** |
| v3.0.0 | 5 | 8 | 0 | 0 | **13** |
| v3.0.0-beta.10 | 3 | 17 | 0 | 0 | **20** |
| v3.0.0-beta.9 | 0 | 3 | 0 | 0 | **3** |
| v3.0.0-beta.8 | 2 | 3 | 0 | 0 | **5** |
| v3.0.0-beta.7 | 1 | 2 | 0 | 0 | **3** |
| v3.0.0-beta.6 | 1 | 2 | 0 | 0 | **3** |
| v3.0.0-beta.5 | 0 | 2 | 0 | 0 | **2** |
| v3.0.0-beta.4 | 1 | 3 | 0 | 0 | **4** |
| v3.0.0-beta.3 | 1 | 2 | 0 | 0 | **3** |
| v3.0.0-beta.2 | 5 | 2 | 0 | 0 | **7** |
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
| v1.0.2 | 0 | 3 | 0 | 0 | **3** |
| v1.0.1 | 0 | 4 | 0 | 0 | **4** |
| v1.0.0 | 0 | 1 | 0 | 0 | **1** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | arm64 | x86_64 | universal | Total |
|----------|-------|-------|-------|-------|
| 🪟 Windows | 109 | 851 | 0 | **960** |
| 🍎 macOS | 1332 | 378 | 351 | **2061** |
| 🐧 Linux | 74 | 106 | 0 | **180** |

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v4.3.2 | 109 | 2026-09-28 |
| v4.2.7 | 106 | 2026-09-12 |
| v4.1.4 | 66 | 2026-08-28 |
| v3.14.7 | 61 | 2026-07-22 |
| v3.6.4 | 54 | 2026-05-17 |
| v3.12.1 | 52 | 2026-06-25 |
| v3.6.7 | 48 | 2026-05-18 |
| v3.6.5 | 48 | 2026-05-18 |
| v4.1.1 | 42 | 2026-08-18 |
| v3.7.1 | 42 | 2026-05-18 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | Downloads |
|---------|-----------|-----|----|----|----|-----------|
| v4.3.3-beta.16 | 2026-10-09 | 1d | 0 | 13 | 0 | **13** |
| v4.3.3-beta.15 | 2026-10-08 | 2d | 1 | 3 | 0 | **4** |
| v4.3.3-beta.14 | 2026-10-08 | 2d | 1 | 3 | 0 | **4** |
| v4.3.3-beta.13 | 2026-10-08 | 2d | 0 | 0 | 0 | **0** |
| v4.3.3-beta.12 | 2026-10-08 | 2d | 1 | 2 | 0 | **3** |
| v4.3.3-beta.11 | 2026-10-05 | 5d | 3 | 4 | 0 | **7** |
| v4.3.3-beta.10 | 2026-10-04 | 6d | 3 | 2 | 0 | **5** |
| v4.3.3-beta.9 | 2026-10-04 | 6d | 1 | 2 | 0 | **3** |
| v4.3.3-beta.8 | 2026-10-04 | 6d | 1 | 2 | 0 | **3** |
| v4.3.3-beta.7 | 2026-10-03 | 7d | 1 | 3 | 0 | **4** |
| v4.3.3-beta.6 | 2026-10-03 | 7d | 1 | 1 | 0 | **2** |
| v4.3.3-beta.5 | 2026-10-02 | 8d | 0 | 3 | 0 | **3** |
| v4.3.3-beta.4 | 2026-10-02 | 8d | 0 | 1 | 0 | **1** |
| v4.3.3-beta.3 | 2026-10-02 | 8d | 1 | 3 | 0 | **4** |
| v4.3.3-beta.2 | 2026-10-02 | 8d | 0 | 3 | 0 | **3** |
| v4.3.3-beta.1 | 2026-10-02 | 8d | 0 | 9 | 2 | **11** |
| v4.3.2 | 2026-09-28 | 12d | 53 | 51 | 5 | **109** |
| v4.3.1 | 2026-09-28 | 12d | 1 | 3 | 0 | **4** |
| v4.3.0 | 2026-09-28 | 12d | 2 | 4 | 0 | **6** |
| v4.3.0-beta.49 | 2026-09-28 | 12d | 0 | 2 | 0 | **2** |
| v4.3.0-beta.48 | 2026-09-28 | 12d | 0 | 3 | 0 | **3** |
| v4.3.0-beta.47 | 2026-09-27 | 13d | 1 | 1 | 0 | **2** |
| v4.3.0-beta.46 | 2026-09-27 | 13d | 0 | 3 | 0 | **3** |
| v4.3.0-beta.45 | 2026-09-27 | 13d | 1 | 1 | 0 | **2** |
| v4.3.0-beta.44 | 2026-09-26 | 14d | 2 | 5 | 0 | **7** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq)**

---

# ChromIQ-Patches

![downloads](https://img.shields.io/badge/downloads-45-212121) ![clones](https://img.shields.io/badge/clones-358-2196F3) ![views](https://img.shields.io/badge/views-113-4CAF50) ![releases](https://img.shields.io/badge/releases-5-6f42c1)

*Tracking since **2026-07-02** (98 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~98 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 3 | 1 | ▲ +200.0% |
| Views | 0 | 4 | ▼ -100.0% |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 14 | 14 |
| Last 90 Days | 62 | 55 |
| Lifetime | 358 | 185 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 14 | 14 | 0 | 0.0% |
| Last 90 Days | 62 | 55 | 7 | 11.3% |
| Lifetime | 358 | 185 | 173 | 48.3% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 15 | 9 |
| Last 90 Days | 40 | 23 |
| Lifetime | 113 | 50 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 9 | — |
| 🗅️ Unique cloners | 14 | 155.6% |
| 📥 Downloads | 1 | 11.1% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 3

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| Bing | 1 | 1 |
| Yahoo | 1 | 1 |
| github.com | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 15 | 9 | 6 | 40.0% |
| Last 90 Days | 40 | 23 | 17 | 42.5% |
| Lifetime | 113 | 50 | 63 | 55.8% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 1 | 8 | 18 |
| 🍎 macOS | 0 | 7 | 24 |
| 🐧 Linux | 0 | 0 | 3 |
| **All** | **1** | **15** | **45** |

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|-----|---------|-------|-------|----------|
| 30 days | all | **1** | 1 | 0 | 0 | 0 |
| 30 days | stable | **1** | 1 | 0 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days | all | **15** | 8 | 7 | 0 | 0 |
| 90 days | stable | **15** | 8 | 7 | 0 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-07-03** on; the stable/beta split from **2026-07-03**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. Read the stable column for users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v1.2.1` - **22** downloads (published 2026-07-07)

<details>
<summary><strong>📦 Per-version downloads</strong> (5 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v1.2.1 | 9 | 12 | 1 | 0 | **22** |
| v1.2.0 | 5 | 7 | 2 | 0 | **14** |
| v1.1.0 | 0 | 1 | 0 | 0 | **1** |
| v1.0.1 | 1 | 3 | 0 | 0 | **4** |
| v1.0.0 | 3 | 1 | 0 | 0 | **4** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | arm64 | x86_64 | universal | Total |
|----------|-------|-------|-------|-------|
| 🪟 Windows | 0 | 18 | 0 | **18** |
| 🍎 macOS | 18 | 3 | 3 | **24** |
| 🐧 Linux | 0 | 3 | 0 | **3** |

**Top 5 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.2.1 | 22 | 2026-07-07 |
| v1.2.0 | 14 | 2026-07-03 |
| v1.0.1 | 4 | 2026-07-02 |
| v1.0.0 | 4 | 2026-07-02 |
| v1.1.0 | 1 | 2026-07-02 |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq-patches)**

---

# ChromIQ-Gamut-Viewer

![downloads](https://img.shields.io/badge/downloads-39-212121) ![clones](https://img.shields.io/badge/clones-2496-2196F3) ![views](https://img.shields.io/badge/views-64-4CAF50) ![releases](https://img.shields.io/badge/releases-96-6f42c1)

*Tracking since **2026-08-13** (57 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~57 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 4 | 6 | ▼ -33.3% |
| Views | 0 | 1 | ▼ -100.0% |
| Downloads | 1 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 66 | 62 |
| Last 90 Days | 2496 | 520 |
| Lifetime | 2496 | 520 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 66 | 62 | 4 | 6.1% |
| Last 90 Days | 2496 | 520 | 1976 | 79.2% |
| Lifetime | 2496 | 520 | 1976 | 79.2% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 8 | 3 |
| Last 90 Days | 64 | 17 |
| Lifetime | 64 | 17 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 3 | — |
| 🗅️ Unique cloners | 62 | 2066.7% |
| 📥 Downloads | 3 | 100.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 0

*No referrer data available.*

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 8 | 3 | 5 | 62.5% |
| Last 90 Days | 64 | 17 | 47 | 73.4% |
| Lifetime | 64 | 17 | 47 | 73.4% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 1 | 9 | 10 |
| 🍎 macOS | 2 | 19 | 23 |
| 🐧 Linux | 0 | 4 | 6 |
| **All** | **3** | **32** | **39** |

*ℹ️ Not counted above: 11 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|-----|---------|-------|-------|----------|
| 30 days | all | **3** | 1 | 2 | 0 | 0 |
| 30 days | stable | **3** | 1 | 2 | 0 | 0 |
| 30 days | beta | **0** | 0 | 0 | 0 | 0 |
| 90 days (56 days tracked) | all | **32** | 9 | 19 | 4 | 0 |
| 90 days | stable | **32** | 9 | 19 | 4 | 0 |
| 90 days | beta | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-08-15** on; the stable/beta split from **2026-08-15**. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. Read the stable column for users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS.*
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

![downloads](https://img.shields.io/badge/downloads-0-212121) ![clones](https://img.shields.io/badge/clones-7805-2196F3) ![views](https://img.shields.io/badge/views-31-4CAF50) ![releases](https://img.shields.io/badge/releases-0-6f42c1)

*Tracking since **2026-07-30** (71 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~71 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 213 | 217 | ▼ -1.8% |
| Views | 0 | 16 | ▼ -100.0% |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1039 | 457 |
| Last 90 Days | 7805 | 4635 |
| Lifetime | 7805 | 4635 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 1039 | 457 | 582 | 56.0% |
| Last 90 Days | 7805 | 4635 | 3170 | 40.6% |
| Lifetime | 7805 | 4635 | 3170 | 40.6% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 18 | 7 |
| Last 90 Days | 31 | 14 |
| Lifetime | 31 | 14 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 7 | — |
| 🗅️ Unique cloners | 457 | 6528.6% |
| 📥 Downloads | 0 | 0.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 3

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 13 | 2 |
| Bing | 1 | 1 |
| DuckDuckGo | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 18 | 7 | 11 | 61.1% |
| Last 90 Days | 31 | 14 | 17 | 54.8% |
| Lifetime | 31 | 14 | 17 | 54.8% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 0 | 0 | 0 |
| 🍎 macOS | 0 | 0 | 0 |
| 🐧 Linux | 0 | 0 | 0 |
| **All** | **0** | **0** | **0** |

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|-----|---------|-------|-------|----------|
| 30 days | all | **0** | 0 | 0 | 0 | 0 |
| 90 days (57 days tracked) | all | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **2026-08-14** on. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. Read the stable column for users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#github-traffic-downloads-dashboard)**

---

# homebrew-chromiq

> ℹ️ This is ChromIQ's Homebrew tap: it has no downloads of its own. Homebrew clones it when someone installs ChromIQ with brew and fetches it again on updates, so the number of different cloners in the last 14 days is a rough indicator of how many machines use the Homebrew install. It is not a download count, and machines that have not run brew lately do not show. The Homebrew downloads themselves are counted under ChromIQ (Homebrew).

**Different cloners in the last 14 days:** 0 (as of 2026-10-09; GitHub's own 14-day count, recorded daily from 2026-10-09 on)

![downloads](https://img.shields.io/badge/downloads-0-212121) ![clones](https://img.shields.io/badge/clones-0-2196F3) ![views](https://img.shields.io/badge/views-0-4CAF50) ![releases](https://img.shields.io/badge/releases-0-6f42c1)

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 0 | 0 | — |
| Views | 0 | 0 | — |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 0 | 0 |
| Last 90 Days | 0 | 0 |
| Lifetime | 0 | 0 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 0 | 0 | 0 | 0% |
| Last 90 Days | 0 | 0 | 0 | 0% |
| Lifetime | 0 | 0 | 0 | 0% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 0 | 0 |
| Last 90 Days | 0 | 0 |
| Lifetime | 0 | 0 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 0 | — |
| 🗅️ Unique cloners | 0 | — |
| 📥 Downloads | 0 | — |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 0

*No referrer data available.*

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 0 | 0 | 0 | 0% |
| Last 90 Days | 0 | 0 | 0 | 0% |
| Lifetime | 0 | 0 | 0 | 0% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 0 | 0 | 0 |
| 🍎 macOS | 0 | 0 | 0 |
| 🐧 Linux | 0 | 0 | 0 |
| **All** | **0** | **0** | **0** |

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|-----|---------|-------|-------|----------|
| 30 days (0 days tracked) | all | **0** | 0 | 0 | 0 | 0 |
| 90 days (0 days tracked) | all | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **the second tracked day** on. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. Read the stable column for users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#homebrew-chromiq)**

---

# MacReplica

![downloads](https://img.shields.io/badge/downloads-14-212121) ![clones](https://img.shields.io/badge/clones-591-2196F3) ![views](https://img.shields.io/badge/views-36-4CAF50) ![releases](https://img.shields.io/badge/releases-5-6f42c1)

*Tracking since **2026-10-02** (7 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~7 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 488 | 103 | ▲ +373.8% |
| Views | 18 | 18 | ▬ 0% |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 591 | 212 |
| Last 90 Days | 591 | 212 |
| Lifetime | 591 | 212 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 591 | 212 | 379 | 64.1% |
| Last 90 Days | 591 | 212 | 379 | 64.1% |
| Lifetime | 591 | 212 | 379 | 64.1% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 36 | 9 |
| Last 90 Days | 36 | 9 |
| Lifetime | 36 | 9 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 9 | — |
| 🗅️ Unique cloners | 212 | 2355.6% |
| 📥 Downloads | 0 | 0.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 1

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 5 | 3 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 36 | 9 | 27 | 75.0% |
| Last 90 Days | 36 | 9 | 27 | 75.0% |
| Lifetime | 36 | 9 | 27 | 75.0% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 0 | 0 | 0 |
| 🍎 macOS | 0 | 0 | 14 |
| 🐧 Linux | 0 | 0 | 0 |
| **All** | **0** | **0** | **14** |

*ℹ️ Not counted above: 3 lifetime downloads of other release files (demo projects, screenshots, checksums), which are not the app.*

**Downloads in the last 30 and 90 days, all releases (for a user estimate):**

| Window | Channel | All | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew |
|--------|---------|-----|---------|-------|-------|----------|
| 30 days (0 days tracked) | all | **0** | 0 | 0 | 0 | 0 |
| 90 days (0 days tracked) | all | **0** | 0 | 0 | 0 | 0 |

*Per-day downloads are the difference between two daily readings of GitHub's lifetime counters, available from **the second tracked day** on. What these numbers can and cannot tell:*

- *A download is a file someone fetched, not a person. One person on two computers, or one who downloads the same version twice, counts twice.*
- *People who installed once and never update do not show up at all after their first download, however much they use the app.*
- *An occasional tool is fetched long after a release, not only in its first days. The 30- and 90-day windows and the 90-day release curves catch those late downloads; a first-week count misses them.*
- *Betas are mostly testers, often the same few people on every beta. Read the stable column for users.*
- *Homebrew counts installs and upgrades made with brew (each fetches its own copy of the Mac file). They are not counted again under macOS.*
- *Clones of the source code are not downloads and are not counted here.*

🆕 **Latest Release:** `v1.0.4` - **4** downloads (published 2026-10-04)

<details>
<summary><strong>📦 Per-version downloads</strong> (5 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | 🍺 Homebrew | Total |
|---------|-----------|----------|----------|----------|-------|
| v1.0.4 | 0 | 4 | 0 | 0 | **4** |
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
| 🍎 macOS | 14 | **14** |
| 🐧 Linux | 0 | **0** |

**Top 5 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.0.4 | 4 | 2026-10-04 |
| v1.0.0 | 4 | 2026-10-02 |
| v1.0.1 | 3 | 2026-10-03 |
| v1.0.2 | 2 | 2026-10-04 |
| v1.0.3 | 1 | 2026-10-04 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | Downloads |
|---------|-----------|-----|----|----|----|-----------|
| v1.0.4 | 2026-10-04 | 6d | 0 | 4 | 0 | **4** |
| v1.0.3 | 2026-10-04 | 6d | 0 | 1 | 0 | **1** |
| v1.0.2 | 2026-10-04 | 6d | 0 | 2 | 0 | **2** |
| v1.0.1 | 2026-10-03 | 7d | 0 | 3 | 0 | **3** |
| v1.0.0 | 2026-10-02 | 8d | 0 | 4 | 0 | **4** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#macreplica)**

---

*This dashboard is automatically updated daily using GitHub Actions.*
