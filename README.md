See full Reference and Usage Guide at:
https://itsab1989.github.io/github-traffic-downloads-dashboard/

> This is a modified version of the original [github-traffic-dashboard](https://github.com/soul-traveller/github-traffic-dashboard), extended with platform-specific download statistics (Windows / macOS / Linux).

# 📊 GitHub Traffic & Downloads Dashboard

This dashboard tracks historical traffic data (clones, views, and release downloads) for GitHub repositories.

**Last Updated:** 2026-07-13T16:01:29.852278Z

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

# ChromIQ

![downloads](https://img.shields.io/badge/downloads-1920-212121) ![clones](https://img.shields.io/badge/clones-15577-2196F3) ![views](https://img.shields.io/badge/views-3167-4CAF50) ![releases](https://img.shields.io/badge/releases-481-6f42c1)

*Tracking since **2026-05-02** (72 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~72 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 452 | 1664 | ▼ -72.8% |
| Views | 325 | 604 | ▼ -46.2% |
| Downloads | 132 | 244 | ▼ -45.9% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 6874 | 1506 |
| Last 90 Days | 15577 | 3458 |
| Lifetime | 15577 | 3458 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 6874 | 1506 | 5368 | 78.1% |
| Last 90 Days | 15577 | 3458 | 12119 | 77.8% |
| Lifetime | 15577 | 3458 | 12119 | 77.8% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1773 | 312 |
| Last 90 Days | 3167 | 816 |
| Lifetime | 3167 | 816 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 312 | — |
| 🗅️ Unique cloners | 1506 | 482.7% |
| 📥 Downloads | 667 | 213.8% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 10

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| Google | 59 | 19 |
| github.com | 36 | 7 |
| printerknowledge.com | 34 | 13 |
| dpreview.com | 12 | 6 |
| Bing | 10 | 3 |
| Yahoo | 8 | 1 |
| DuckDuckGo | 6 | 1 |
| reddit.com | 4 | 4 |
| forum.luminous-landscape.com | 3 | 1 |
| yandex.ru | 2 | 2 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 1773 | 312 | 1461 | 82.4% |
| Last 90 Days | 3167 | 816 | 2351 | 74.2% |
| Lifetime | 3167 | 816 | 2351 | 74.2% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 219 | 345 | 435 |
| 🍎 macOS | 405 | 914 | 1393 |
| 🐧 Linux | 43 | 61 | 92 |
| **All** | **667** | **1320** | **1920** |

🆕 **Latest Release:** `v3.13.6-beta.1` - **0** downloads (published 2026-07-13)

<details>
<summary><strong>📦 Per-version downloads</strong> (481 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | Total |
|---------|-----------|----------|----------|-------|
| v3.13.6-beta.1 | 0 | 0 | 0 | **0** |
| v3.13.5 | 3 | 8 | 0 | **11** |
| v3.13.4 | 4 | 4 | 0 | **8** |
| v3.13.4-beta.11 | 0 | 1 | 0 | **1** |
| v3.13.4-beta.10 | 0 | 1 | 0 | **1** |
| v3.13.4-beta.9 | 0 | 1 | 0 | **1** |
| v3.13.4-beta.8 | 0 | 0 | 0 | **0** |
| v3.13.4-beta.7 | 0 | 1 | 0 | **1** |
| v3.13.4-beta.6 | 0 | 2 | 0 | **2** |
| v3.13.4-beta.5 | 0 | 1 | 0 | **1** |
| v3.13.4-beta.4 | 0 | 1 | 0 | **1** |
| v3.13.4-beta.3 | 0 | 2 | 0 | **2** |
| v3.13.4-beta.2 | 0 | 2 | 0 | **2** |
| v3.13.4-beta.1 | 0 | 0 | 0 | **0** |
| v3.13.3 | 5 | 4 | 2 | **11** |
| v3.13.2 | 2 | 3 | 1 | **6** |
| v3.13.1 | 5 | 3 | 1 | **9** |
| v3.13.0 | 1 | 7 | 0 | **8** |
| v3.13.0-beta.143 | 0 | 2 | 0 | **2** |
| v3.13.0-beta.142 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.141 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.140 | 0 | 2 | 0 | **2** |
| v3.13.0-beta.139 | 0 | 2 | 0 | **2** |
| v3.13.0-beta.138 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.137 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.136 | 2 | 6 | 0 | **8** |
| v3.13.0-beta.135 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.134 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.133 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.132 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.131 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.130 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.129 | 0 | 2 | 0 | **2** |
| v3.13.0-beta.128 | 0 | 2 | 0 | **2** |
| v3.13.0-beta.127 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.126 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.125 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.124 | 0 | 3 | 0 | **3** |
| v3.13.0-beta.123 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.122 | 1 | 6 | 0 | **7** |
| v3.13.0-beta.122 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.121 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.120 | 0 | 2 | 0 | **2** |
| v3.13.0-beta.119 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.118 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.117 | 2 | 1 | 0 | **3** |
| v3.13.0-beta.116 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.115 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.114 | 1 | 2 | 0 | **3** |
| v3.13.0-beta.113 | 1 | 6 | 0 | **7** |
| v3.13.0-beta.112 | 1 | 1 | 0 | **2** |
| v3.13.0-beta.111 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.110 | 1 | 4 | 0 | **5** |
| v3.13.0-beta.109 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.108 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.107 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.106 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.105 | 2 | 3 | 2 | **7** |
| v3.13.0-beta.104 | 2 | 4 | 2 | **8** |
| v3.13.0-beta.103 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.102 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.101 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.100 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.99 | 2 | 0 | 0 | **2** |
| v3.13.0-beta.98 | 1 | 2 | 0 | **3** |
| v3.13.0-beta.97 | 1 | 1 | 0 | **2** |
| v3.13.0-beta.96 | 1 | 1 | 0 | **2** |
| v3.13.0-beta.95 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.94 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.93 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.92 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.91 | 5 | 8 | 4 | **17** |
| v3.13.0-beta.90 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.89 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.88 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.87 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.86 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.85 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.84 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.83 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.82 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.81 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.80 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.79 | 1 | 1 | 0 | **2** |
| v3.13.0-beta.78 | 0 | 2 | 0 | **2** |
| v3.13.0-beta.77 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.76 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.75 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.74 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.73 | 0 | 2 | 0 | **2** |
| v3.13.0-beta.72 | 2 | 3 | 2 | **7** |
| v3.13.0-beta.71 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.70 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.69 | 2 | 1 | 0 | **3** |
| v3.13.0-beta.68 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.67 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.66 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.65 | 2 | 3 | 2 | **7** |
| v3.13.0-beta.64 | 1 | 1 | 0 | **2** |
| v3.13.0-beta.63 | 0 | 2 | 0 | **2** |
| v3.13.0-beta.62 | 2 | 3 | 0 | **5** |
| v3.13.0-beta.60 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.59 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.58 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.57 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.56 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.55 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.54 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.53 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.52 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.51 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.50 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.49 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.48 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.47 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.46 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.45 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.44 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.43 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.42 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.41 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.40 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.39 | 4 | 8 | 5 | **17** |
| v3.13.0-beta.38 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.37 | 1 | 1 | 0 | **2** |
| v3.13.0-beta.36 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.35 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.34 | 2 | 3 | 2 | **7** |
| v3.13.0-beta.33 | 2 | 4 | 2 | **8** |
| v3.13.0-beta.32 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.31 | 4 | 5 | 3 | **12** |
| v3.13.0-beta.30 | 1 | 1 | 0 | **2** |
| v3.13.0-beta.29 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.28 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.27 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.26 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.25 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.24 | 2 | 1 | 0 | **3** |
| v3.13.0-beta.23 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.22 | 2 | 1 | 0 | **3** |
| v3.13.0-beta.21 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.20 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.19 | 1 | 0 | 0 | **1** |
| v3.13.0-beta.18 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.17 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.16 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.15 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.14 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.13 | 1 | 2 | 0 | **3** |
| v3.13.0-beta.12 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.11 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.10 | 0 | 2 | 0 | **2** |
| v3.13.0-beta.9 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.8 | 0 | 2 | 0 | **2** |
| v3.13.0-beta.7 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.6 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.5 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.4 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.3 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.2 | 0 | 0 | 0 | **0** |
| v3.12.1 | 29 | 22 | 1 | **52** |
| v3.13.0-beta.1 | 0 | 0 | 0 | **0** |
| v3.12.1-beta.1 | 2 | 0 | 0 | **2** |
| v3.12.0 | 5 | 5 | 0 | **10** |
| v3.12.0-beta.18 | 0 | 0 | 0 | **0** |
| v3.12.0-beta.17 | 0 | 0 | 0 | **0** |
| v3.12.0-beta.16 | 0 | 2 | 0 | **2** |
| v3.12.0-beta.15 | 0 | 1 | 0 | **1** |
| v3.12.0-beta.14 | 0 | 1 | 0 | **1** |
| v3.12.0-beta.13 | 0 | 1 | 0 | **1** |
| v3.12.0-beta.12 | 0 | 0 | 0 | **0** |
| v3.12.0-beta.11 | 0 | 1 | 0 | **1** |
| v3.12.0-beta.10 | 0 | 1 | 0 | **1** |
| v3.12.0-beta.9 | 1 | 1 | 0 | **2** |
| v3.12.0-beta.8 | 0 | 0 | 0 | **0** |
| v3.12.0-beta.7 | 0 | 0 | 0 | **0** |
| v3.12.0-beta.6 | 0 | 1 | 0 | **1** |
| v3.12.0-beta.5 | 1 | 1 | 0 | **2** |
| v3.12.0-beta.4 | 0 | 1 | 0 | **1** |
| v3.12.0-beta.3 | 0 | 0 | 0 | **0** |
| v3.12.0-beta.2 | 0 | 1 | 0 | **1** |
| v3.12.0-beta.1 | 0 | 1 | 0 | **1** |
| v3.11.25 | 7 | 6 | 0 | **13** |
| v3.11.24 | 1 | 5 | 0 | **6** |
| v3.11.23 | 5 | 2 | 0 | **7** |
| v3.11.22 | 0 | 0 | 0 | **0** |
| v3.11.21 | 1 | 1 | 0 | **2** |
| v3.11.20 | 2 | 2 | 0 | **4** |
| v3.11.19 | 1 | 2 | 0 | **3** |
| v3.11.18 | 8 | 5 | 0 | **13** |
| v3.11.17 | 0 | 0 | 0 | **0** |
| v3.11.16 | 1 | 0 | 0 | **1** |
| v3.11.15 | 0 | 0 | 0 | **0** |
| v3.11.14 | 0 | 0 | 0 | **0** |
| v3.11.13 | 1 | 0 | 0 | **1** |
| v3.11.12 | 0 | 0 | 0 | **0** |
| v3.11.11 | 6 | 5 | 0 | **11** |
| v3.11.10 | 0 | 2 | 0 | **2** |
| v3.11.9 | 1 | 2 | 0 | **3** |
| v3.11.8 | 1 | 5 | 0 | **6** |
| v3.11.7 | 2 | 1 | 0 | **3** |
| v3.11.6 | 2 | 2 | 0 | **4** |
| v3.11.5 | 0 | 1 | 0 | **1** |
| v3.11.4 | 2 | 1 | 0 | **3** |
| v3.11.3 | 1 | 3 | 0 | **4** |
| v3.11.2 | 0 | 2 | 0 | **2** |
| v3.11.1 | 0 | 2 | 0 | **2** |
| v3.11.0 | 3 | 2 | 0 | **5** |
| v3.10.28 | 1 | 0 | 0 | **1** |
| v3.10.27 | 0 | 0 | 0 | **0** |
| v3.10.26 | 2 | 2 | 0 | **4** |
| v3.10.25 | 0 | 0 | 0 | **0** |
| v3.10.24 | 1 | 3 | 0 | **4** |
| v3.10.23 | 0 | 2 | 0 | **2** |
| v3.10.22 | 0 | 0 | 0 | **0** |
| v3.10.21 | 1 | 2 | 0 | **3** |
| v3.10.20 | 0 | 2 | 0 | **2** |
| v3.10.19 | 1 | 2 | 0 | **3** |
| v3.10.18 | 1 | 3 | 0 | **4** |
| v3.10.17 | 0 | 0 | 0 | **0** |
| v3.10.16 | 0 | 4 | 0 | **4** |
| v3.10.15 | 3 | 2 | 0 | **5** |
| v3.10.14 | 1 | 1 | 0 | **2** |
| v3.10.13 | 0 | 2 | 0 | **2** |
| v3.10.12 | 0 | 0 | 0 | **0** |
| v3.10.11 | 0 | 0 | 0 | **0** |
| v3.10.10 | 0 | 4 | 0 | **4** |
| v3.10.9 | 1 | 2 | 0 | **3** |
| v3.10.8 | 0 | 4 | 0 | **4** |
| v3.10.7 | 0 | 1 | 0 | **1** |
| v3.10.6 | 0 | 0 | 0 | **0** |
| v3.10.5 | 2 | 6 | 4 | **12** |
| v3.10.4 | 0 | 2 | 0 | **2** |
| v3.10.3 | 0 | 1 | 0 | **1** |
| v3.10.2 | 7 | 7 | 2 | **16** |
| v3.10.1 | 0 | 0 | 0 | **0** |
| v3.10.0 | 1 | 1 | 0 | **2** |
| v3.9.31 | 0 | 0 | 0 | **0** |
| v3.9.30 | 0 | 1 | 0 | **1** |
| v3.9.29 | 2 | 3 | 0 | **5** |
| v3.9.28 | 1 | 2 | 0 | **3** |
| v3.9.27 | 0 | 1 | 0 | **1** |
| v3.9.26 | 0 | 2 | 0 | **2** |
| v3.9.25 | 0 | 1 | 0 | **1** |
| v3.9.24 | 0 | 2 | 0 | **2** |
| v3.9.23 | 1 | 2 | 0 | **3** |
| v3.9.22 | 0 | 0 | 0 | **0** |
| v3.9.21 | 3 | 3 | 0 | **6** |
| v3.9.20 | 0 | 2 | 0 | **2** |
| v3.9.19 | 2 | 0 | 0 | **2** |
| v3.9.18 | 0 | 2 | 0 | **2** |
| v3.9.17 | 1 | 1 | 0 | **2** |
| v3.9.16 | 2 | 3 | 0 | **5** |
| v3.9.15 | 1 | 1 | 0 | **2** |
| v3.9.14 | 0 | 0 | 0 | **0** |
| v3.9.13 | 2 | 2 | 0 | **4** |
| v3.9.12 | 0 | 2 | 0 | **2** |
| v3.9.11 | 0 | 0 | 0 | **0** |
| v3.9.10 | 0 | 1 | 0 | **1** |
| v3.9.9 | 0 | 0 | 0 | **0** |
| v3.9.8 | 0 | 0 | 0 | **0** |
| v3.9.7 | 0 | 0 | 0 | **0** |
| v3.9.6 | 1 | 2 | 0 | **3** |
| v3.9.5 | 0 | 0 | 0 | **0** |
| v3.9.4 | 0 | 0 | 0 | **0** |
| v3.9.3 | 1 | 0 | 0 | **1** |
| v3.9.2 | 0 | 0 | 0 | **0** |
| v3.9.1 | 1 | 1 | 0 | **2** |
| v3.9.0 | 0 | 0 | 0 | **0** |
| v3.8.19 | 4 | 4 | 0 | **8** |
| v3.8.18 | 1 | 2 | 0 | **3** |
| v3.8.17 | 2 | 5 | 2 | **9** |
| v3.8.16 | 4 | 9 | 1 | **14** |
| v3.8.15 | 1 | 0 | 0 | **1** |
| v3.8.14 | 0 | 1 | 0 | **1** |
| v3.8.13 | 0 | 3 | 0 | **3** |
| v3.8.12 | 6 | 2 | 0 | **8** |
| v3.8.11 | 4 | 1 | 0 | **5** |
| v3.8.10 | 0 | 3 | 0 | **3** |
| v3.8.9 | 2 | 1 | 0 | **3** |
| v3.8.8 | 4 | 7 | 0 | **11** |
| v3.8.7 | 0 | 0 | 0 | **0** |
| v3.8.6 | 2 | 2 | 0 | **4** |
| v3.8.5 | 2 | 4 | 0 | **6** |
| v3.8.4 | 16 | 4 | 0 | **20** |
| v3.8.3 | 12 | 2 | 0 | **14** |
| v3.8.2 | 2 | 2 | 0 | **4** |
| v3.8.1 | 1 | 1 | 0 | **2** |
| v3.8.0 | 13 | 7 | 2 | **22** |
| v3.8.0-beta.31 | 1 | 1 | 0 | **2** |
| v3.8.0-beta.30 | 0 | 1 | 0 | **1** |
| v3.8.0-beta.29 | 0 | 1 | 0 | **1** |
| v3.8.0-beta.28 | 0 | 1 | 0 | **1** |
| v3.8.0-beta.27 | 0 | 1 | 0 | **1** |
| v3.8.0-beta.26 | 1 | 2 | 0 | **3** |
| v3.8.0-beta.25 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.24 | 6 | 10 | 5 | **21** |
| v3.8.0-beta.23 | 6 | 9 | 5 | **20** |
| v3.8.0-beta.22 | 1 | 1 | 0 | **2** |
| v3.8.0-beta.21 | 1 | 0 | 0 | **1** |
| v3.8.0-beta.20 | 4 | 3 | 2 | **9** |
| v3.8.0-beta.19 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.18 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.17 | 0 | 1 | 1 | **2** |
| v3.8.0-beta.16 | 2 | 1 | 0 | **3** |
| v3.8.0-beta.15 | 2 | 1 | 0 | **3** |
| v3.8.0-beta.14 | 6 | 1 | 0 | **7** |
| v3.8.0-beta.13 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.12 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.11 | 1 | 0 | 0 | **1** |
| v3.8.0-beta.10 | 1 | 0 | 0 | **1** |
| v3.8.0-beta.9 | 1 | 1 | 0 | **2** |
| v3.7.42 | 13 | 3 | 0 | **16** |
| v3.8.0-beta.8 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.6 | 2 | 1 | 0 | **3** |
| v3.7.41 | 1 | 1 | 0 | **2** |
| v3.8.0-beta.5 | 4 | 6 | 4 | **14** |
| v3.8.0-beta.4 | 0 | 0 | 0 | **0** |
| v3.7.40 | 2 | 1 | 0 | **3** |
| v3.7.39 | 1 | 2 | 0 | **3** |
| v3.8.0-beta.3 | 0 | 0 | 0 | **0** |
| v3.8.0-beta.2 | 0 | 1 | 0 | **1** |
| v3.8.0-beta.1 | 0 | 1 | 0 | **1** |
| v3.7.38 | 1 | 27 | 0 | **28** |
| v3.7.37 | 1 | 10 | 0 | **11** |
| v3.7.36 | 1 | 3 | 0 | **4** |
| v3.7.35 | 0 | 3 | 0 | **3** |
| v3.7.34 | 0 | 3 | 0 | **3** |
| v3.7.33 | 1 | 4 | 0 | **5** |
| v3.7.32 | 1 | 4 | 0 | **5** |
| v3.7.31 | 1 | 3 | 0 | **4** |
| v3.7.30 | 0 | 3 | 0 | **3** |
| v3.7.29 | 0 | 3 | 0 | **3** |
| v3.7.28 | 0 | 4 | 0 | **4** |
| v3.7.27 | 2 | 6 | 2 | **10** |
| v3.7.26 | 0 | 4 | 0 | **4** |
| v3.7.25 | 2 | 3 | 0 | **5** |
| v3.7.24 | 2 | 3 | 0 | **5** |
| v3.7.23 | 0 | 4 | 0 | **4** |
| v3.7.22 | 2 | 7 | 2 | **11** |
| v3.7.21 | 1 | 5 | 0 | **6** |
| v3.7.20 | 0 | 4 | 0 | **4** |
| v3.7.19 | 4 | 5 | 0 | **9** |
| v3.7.18 | 0 | 4 | 0 | **4** |
| v3.7.17 | 1 | 4 | 0 | **5** |
| v3.7.16 | 0 | 3 | 0 | **3** |
| v3.7.15 | 1 | 6 | 0 | **7** |
| v3.7.14 | 3 | 5 | 0 | **8** |
| v3.7.13 | 0 | 5 | 0 | **5** |
| v3.7.12 | 0 | 4 | 0 | **4** |
| v3.7.11 | 2 | 6 | 0 | **8** |
| v3.7.10 | 2 | 7 | 0 | **9** |
| v3.7.9 | 0 | 10 | 0 | **10** |
| v3.7.8 | 0 | 10 | 0 | **10** |
| v3.7.7 | 0 | 4 | 0 | **4** |
| v3.7.6 | 0 | 6 | 0 | **6** |
| v3.7.5 | 5 | 7 | 1 | **13** |
| v3.7.4 | 1 | 8 | 0 | **9** |
| v3.7.3 | 0 | 8 | 0 | **8** |
| v3.7.2 | 2 | 6 | 2 | **10** |
| v3.7.1 | 0 | 40 | 2 | **42** |
| v3.7.0 | 3 | 35 | 3 | **41** |
| v3.6.7 | 3 | 42 | 3 | **48** |
| v3.6.6 | 4 | 32 | 2 | **38** |
| v3.6.5 | 3 | 42 | 3 | **48** |
| v3.6.4 | 3 | 48 | 3 | **54** |
| v3.6.3 | 0 | 4 | 0 | **4** |
| v3.6.2 | 0 | 3 | 0 | **3** |
| v3.6.1 | 0 | 6 | 0 | **6** |
| v3.6.0 | 3 | 9 | 4 | **16** |
| v3.5.13 | 1 | 4 | 3 | **8** |
| v3.5.12 | 0 | 4 | 0 | **4** |
| v3.5.11 | 0 | 3 | 0 | **3** |
| v3.5.10 | 1 | 3 | 0 | **4** |
| v3.5.9 | 2 | 3 | 0 | **5** |
| v3.5.8 | 1 | 5 | 0 | **6** |
| v3.5.7 | 1 | 3 | 0 | **4** |
| v3.5.6 | 0 | 3 | 0 | **3** |
| v3.5.5 | 0 | 6 | 0 | **6** |
| v3.5.4 | 0 | 3 | 0 | **3** |
| v3.5.3 | 0 | 4 | 0 | **4** |
| v3.5.2 | 1 | 4 | 0 | **5** |
| v3.5.1 | 0 | 5 | 0 | **5** |
| v3.5.0 | 1 | 7 | 1 | **9** |
| v3.5.0-beta.6 | 0 | 4 | 1 | **5** |
| v3.5.0-beta.5 | 0 | 3 | 2 | **5** |
| v3.2.9 | 3 | 4 | 0 | **7** |
| v3.5.0-beta.4 | 0 | 5 | 1 | **6** |
| v3.5.0-beta.3 | 0 | 3 | 0 | **3** |
| v3.5.0-beta.2 | 0 | 5 | 0 | **5** |
| v3.5.0-beta.1 | 0 | 3 | 0 | **3** |
| v3.2.8 | 2 | 7 | 0 | **9** |
| v3.2.7 | 0 | 6 | 0 | **6** |
| v3.2.6 | 0 | 3 | 0 | **3** |
| v3.2.5 | 0 | 3 | 0 | **3** |
| v3.2.4 | 0 | 3 | 0 | **3** |
| v3.2.3 | 0 | 2 | 0 | **2** |
| v3.2.2 | 0 | 3 | 0 | **3** |
| v3.2.1 | 0 | 2 | 0 | **2** |
| v3.2.0 | 0 | 3 | 0 | **3** |
| v3.2.0-beta.3 | 1 | 4 | 0 | **5** |
| v3.2.0-beta.2 | 0 | 4 | 0 | **4** |
| v3.2.0-beta.1 | 1 | 5 | 0 | **6** |
| v3.1.4 | 0 | 3 | 0 | **3** |
| v3.1.3 | 0 | 4 | 0 | **4** |
| v3.1.2 | 0 | 3 | 0 | **3** |
| v3.1.1 | 1 | 5 | 0 | **6** |
| v3.1.0 | 2 | 4 | 0 | **6** |
| v3.0.2 | 2 | 4 | 0 | **6** |
| v3.0.1 | 1 | 2 | 0 | **3** |
| v3.0.0 | 3 | 6 | 0 | **9** |
| v3.0.0-beta.10 | 3 | 17 | 0 | **20** |
| v3.0.0-beta.9 | 0 | 3 | 0 | **3** |
| v3.0.0-beta.8 | 2 | 3 | 0 | **5** |
| v3.0.0-beta.7 | 1 | 2 | 0 | **3** |
| v3.0.0-beta.6 | 1 | 2 | 0 | **3** |
| v3.0.0-beta.5 | 0 | 2 | 0 | **2** |
| v3.0.0-beta.4 | 1 | 3 | 0 | **4** |
| v3.0.0-beta.3 | 1 | 2 | 0 | **3** |
| v3.0.0-beta.2 | 5 | 2 | 0 | **7** |
| v3.0.0-beta.1 | 8 | 2 | 0 | **10** |
| v2.11.0 | 0 | 4 | 0 | **4** |
| v2.10.3 | 0 | 4 | 0 | **4** |
| v2.10.2 | 0 | 7 | 0 | **7** |
| v2.10.1 | 0 | 6 | 0 | **6** |
| v2.10.0 | 0 | 3 | 0 | **3** |
| v2.9.4 | 0 | 4 | 0 | **4** |
| v2.9.3 | 0 | 3 | 0 | **3** |
| v2.9.2 | 0 | 3 | 0 | **3** |
| v2.9.1 | 0 | 2 | 0 | **2** |
| v2.9.0 | 0 | 9 | 0 | **9** |
| v2.8.1 | 0 | 5 | 0 | **5** |
| v2.8.0 | 0 | 3 | 0 | **3** |
| v2.7.0 | 0 | 4 | 0 | **4** |
| v2.6.0 | 0 | 4 | 0 | **4** |
| v2.5.0 | 0 | 4 | 0 | **4** |
| v2.4.1 | 0 | 9 | 0 | **9** |
| v2.4.0 | 0 | 2 | 0 | **2** |
| v2.3.3 | 0 | 3 | 0 | **3** |
| v2.3.2 | 0 | 2 | 0 | **2** |
| v2.3.1 | 0 | 2 | 0 | **2** |
| v2.3.0 | 0 | 1 | 0 | **1** |
| v2.2.3 | 0 | 12 | 0 | **12** |
| v2.2.2 | 0 | 9 | 0 | **9** |
| v2.2.1 | 0 | 3 | 0 | **3** |
| v2.2.0 | 0 | 6 | 0 | **6** |
| v2.1.4 | 0 | 2 | 0 | **2** |
| v2.1.2 | 0 | 10 | 0 | **10** |
| v2.1.1 | 0 | 7 | 0 | **7** |
| v2.1.0 | 0 | 3 | 0 | **3** |
| v2.0.9 | 0 | 8 | 0 | **8** |
| v2.0.8 | 0 | 2 | 0 | **2** |
| v2.0.7 | 0 | 3 | 0 | **3** |
| v2.0.6 | 0 | 3 | 0 | **3** |
| v2.0.5 | 0 | 5 | 0 | **5** |
| v2.0.4 | 0 | 5 | 0 | **5** |
| v2.0.3 | 0 | 5 | 0 | **5** |
| v2.0.2 | 0 | 2 | 0 | **2** |
| v2.0.1 | 0 | 1 | 0 | **1** |
| v2.0.0 | 0 | 4 | 0 | **4** |
| v1.7.1 | 0 | 6 | 0 | **6** |
| v1.7.0 | 0 | 3 | 0 | **3** |
| v1.6.1 | 0 | 3 | 0 | **3** |
| v1.6.0 | 0 | 3 | 0 | **3** |
| v1.5.2 | 0 | 3 | 0 | **3** |
| v1.5.1 | 0 | 5 | 0 | **5** |
| v1.5.0 | 0 | 3 | 0 | **3** |
| v1.4.0 | 0 | 3 | 0 | **3** |
| v1.3.1 | 0 | 5 | 0 | **5** |
| v1.3.0 | 0 | 3 | 0 | **3** |
| v1.2.0 | 0 | 3 | 0 | **3** |
| v1.1.6 | 0 | 4 | 0 | **4** |
| v1.1.5 | 0 | 2 | 0 | **2** |
| v1.1.3 | 0 | 8 | 0 | **8** |
| v1.1.2 | 0 | 3 | 0 | **3** |
| v1.1.1 | 0 | 2 | 0 | **2** |
| v1.1.0 | 0 | 2 | 0 | **2** |
| v1.0.3 | 0 | 2 | 0 | **2** |
| v1.0.2 | 0 | 3 | 0 | **3** |
| v1.0.1 | 0 | 2 | 0 | **2** |
| v1.0.0 | 0 | 1 | 0 | **1** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | arm64 | x86_64 | universal | Total |
|----------|-------|-------|-------|-------|
| 🪟 Windows | 59 | 376 | 0 | **435** |
| 🍎 macOS | 836 | 282 | 275 | **1393** |
| 🐧 Linux | 37 | 55 | 0 | **92** |

*💡 Low-volume builds (<2% of lifetime downloads), candidates to stop shipping: 🐧 Linux arm64 (37, 1.9%).*

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v3.6.4 | 54 | 2026-05-17 |
| v3.12.1 | 52 | 2026-06-25 |
| v3.6.7 | 48 | 2026-05-18 |
| v3.6.5 | 48 | 2026-05-18 |
| v3.7.1 | 42 | 2026-05-18 |
| v3.7.0 | 41 | 2026-05-18 |
| v3.6.6 | 38 | 2026-05-18 |
| v3.7.38 | 28 | 2026-05-24 |
| v3.8.0 | 22 | 2026-05-29 |
| v3.8.0-beta.24 | 21 | 2026-05-29 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | Downloads |
|---------|-----------|-----|----|----|----|-----------|
| v3.13.6-beta.1 | 2026-07-13 | 1d | 0 | 0 | 0 | **0** |
| v3.13.5 | 2026-07-12 | 2d | 3 | 8 | 0 | **11** |
| v3.13.4 | 2026-07-12 | 2d | 4 | 4 | 0 | **8** |
| v3.13.4-beta.11 | 2026-07-12 | 2d | 0 | 1 | 0 | **1** |
| v3.13.4-beta.10 | 2026-07-11 | 3d | 0 | 1 | 0 | **1** |
| v3.13.4-beta.9 | 2026-07-11 | 3d | 0 | 1 | 0 | **1** |
| v3.13.4-beta.8 | 2026-07-11 | 3d | 0 | 0 | 0 | **0** |
| v3.13.4-beta.7 | 2026-07-11 | 3d | 0 | 1 | 0 | **1** |
| v3.13.4-beta.6 | 2026-07-11 | 3d | 0 | 2 | 0 | **2** |
| v3.13.4-beta.5 | 2026-07-11 | 3d | 0 | 1 | 0 | **1** |
| v3.13.4-beta.4 | 2026-07-10 | 4d | 0 | 1 | 0 | **1** |
| v3.13.4-beta.3 | 2026-07-10 | 4d | 0 | 2 | 0 | **2** |
| v3.13.4-beta.2 | 2026-07-10 | 4d | 0 | 2 | 0 | **2** |
| v3.13.4-beta.1 | 2026-07-10 | 4d | 0 | 0 | 0 | **0** |
| v3.13.3 | 2026-07-09 | 5d | 5 | 4 | 2 | **11** |
| v3.13.2 | 2026-07-09 | 5d | 2 | 3 | 1 | **6** |
| v3.13.1 | 2026-07-08 | 6d | 5 | 3 | 1 | **9** |
| v3.13.0 | 2026-07-08 | 6d | 1 | 7 | 0 | **8** |
| v3.13.0-beta.143 | 2026-07-07 | 7d | 0 | 2 | 0 | **2** |
| v3.13.0-beta.142 | 2026-07-07 | 7d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.141 | 2026-07-07 | 7d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.140 | 2026-07-07 | 7d | 0 | 2 | 0 | **2** |
| v3.13.0-beta.139 | 2026-07-07 | 7d | 0 | 2 | 0 | **2** |
| v3.13.0-beta.138 | 2026-07-07 | 7d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.137 | 2026-07-07 | 7d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.136 | 2026-07-07 | 7d | 2 | 6 | 0 | **8** |
| v3.13.0-beta.135 | 2026-07-06 | 8d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.134 | 2026-07-06 | 8d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.133 | 2026-07-06 | 8d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.132 | 2026-07-06 | 8d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.131 | 2026-07-06 | 8d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.130 | 2026-07-06 | 8d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.129 | 2026-07-06 | 8d | 0 | 2 | 0 | **2** |
| v3.13.0-beta.128 | 2026-07-06 | 8d | 0 | 2 | 0 | **2** |
| v3.13.0-beta.127 | 2026-07-06 | 8d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.126 | 2026-07-06 | 8d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.125 | 2026-07-06 | 8d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.124 | 2026-07-06 | 8d | 0 | 3 | 0 | **3** |
| v3.13.0-beta.123 | 2026-07-06 | 8d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.122 | 2026-07-06 | 8d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.121 | 2026-07-06 | 8d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.120 | 2026-07-05 | 9d | 0 | 2 | 0 | **2** |
| v3.13.0-beta.119 | 2026-07-05 | 9d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.118 | 2026-07-05 | 9d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.117 | 2026-07-05 | 9d | 2 | 1 | 0 | **3** |
| v3.13.0-beta.116 | 2026-07-05 | 9d | 1 | 0 | 0 | **1** |
| v3.13.0-beta.115 | 2026-07-05 | 9d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.114 | 2026-07-05 | 9d | 1 | 2 | 0 | **3** |
| v3.13.0-beta.113 | 2026-07-05 | 9d | 1 | 6 | 0 | **7** |
| v3.13.0-beta.112 | 2026-07-05 | 9d | 1 | 1 | 0 | **2** |
| v3.13.0-beta.111 | 2026-07-05 | 9d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.110 | 2026-07-05 | 9d | 1 | 4 | 0 | **5** |
| v3.13.0-beta.109 | 2026-07-05 | 9d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.108 | 2026-07-05 | 9d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.107 | 2026-07-05 | 9d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.106 | 2026-07-05 | 9d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.105 | 2026-07-05 | 9d | 2 | 3 | 2 | **7** |
| v3.13.0-beta.104 | 2026-07-05 | 9d | 2 | 4 | 2 | **8** |
| v3.13.0-beta.103 | 2026-07-05 | 9d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.102 | 2026-07-04 | 10d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.101 | 2026-07-04 | 10d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.100 | 2026-07-04 | 10d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.99 | 2026-07-04 | 10d | 2 | 0 | 0 | **2** |
| v3.13.0-beta.98 | 2026-07-04 | 10d | 1 | 2 | 0 | **3** |
| v3.13.0-beta.97 | 2026-07-04 | 10d | 1 | 1 | 0 | **2** |
| v3.13.0-beta.96 | 2026-07-04 | 10d | 1 | 1 | 0 | **2** |
| v3.13.0-beta.95 | 2026-07-04 | 10d | 1 | 0 | 0 | **1** |
| v3.13.0-beta.94 | 2026-07-04 | 10d | 1 | 0 | 0 | **1** |
| v3.13.0-beta.93 | 2026-07-04 | 10d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.92 | 2026-07-04 | 10d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.91 | 2026-07-04 | 10d | 5 | 8 | 4 | **17** |
| v3.13.0-beta.90 | 2026-07-04 | 10d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.89 | 2026-07-03 | 11d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.88 | 2026-07-03 | 11d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.87 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.86 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.85 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.84 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.83 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.82 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.81 | 2026-07-03 | 11d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.80 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.79 | 2026-07-03 | 11d | 1 | 1 | 0 | **2** |
| v3.13.0-beta.78 | 2026-07-03 | 11d | 0 | 2 | 0 | **2** |
| v3.13.0-beta.77 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.76 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.75 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.74 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.73 | 2026-07-03 | 11d | 0 | 2 | 0 | **2** |
| v3.13.0-beta.72 | 2026-07-03 | 11d | 2 | 3 | 2 | **7** |
| v3.13.0-beta.71 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.70 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.69 | 2026-07-03 | 11d | 2 | 1 | 0 | **3** |
| v3.13.0-beta.68 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.67 | 2026-07-03 | 11d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.66 | 2026-07-02 | 12d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.65 | 2026-07-02 | 12d | 2 | 3 | 2 | **7** |
| v3.13.0-beta.64 | 2026-07-02 | 12d | 1 | 1 | 0 | **2** |
| v3.13.0-beta.63 | 2026-07-02 | 12d | 0 | 2 | 0 | **2** |
| v3.13.0-beta.62 | 2026-07-02 | 12d | 2 | 3 | 0 | **5** |
| v3.13.0-beta.60 | 2026-07-01 | 13d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.59 | 2026-07-01 | 13d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.58 | 2026-07-01 | 13d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.57 | 2026-07-01 | 13d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.56 | 2026-07-01 | 13d | 1 | 0 | 0 | **1** |
| v3.13.0-beta.55 | 2026-07-01 | 13d | 1 | 0 | 0 | **1** |
| v3.13.0-beta.54 | 2026-07-01 | 13d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.53 | 2026-07-01 | 13d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.52 | 2026-07-01 | 13d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.51 | 2026-07-01 | 13d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.50 | 2026-07-01 | 13d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.49 | 2026-07-01 | 13d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.48 | 2026-06-30 | 14d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.47 | 2026-06-30 | 14d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.46 | 2026-06-30 | 14d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.45 | 2026-06-30 | 14d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.44 | 2026-06-30 | 14d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.43 | 2026-06-30 | 14d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.42 | 2026-06-30 | 14d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.41 | 2026-06-30 | 14d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.40 | 2026-06-30 | 14d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.39 | 2026-06-30 | 14d | 4 | 8 | 5 | **17** |
| v3.13.0-beta.38 | 2026-06-30 | 14d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.37 | 2026-06-30 | 14d | 1 | 1 | 0 | **2** |
| v3.13.0-beta.36 | 2026-06-30 | 14d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.35 | 2026-06-30 | 14d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.34 | 2026-06-30 | 14d | 2 | 3 | 2 | **7** |
| v3.13.0-beta.33 | 2026-06-30 | 14d | 2 | 4 | 2 | **8** |
| v3.13.0-beta.32 | 2026-06-30 | 14d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.31 | 2026-06-29 | 15d | 4 | 5 | 3 | **12** |
| v3.13.0-beta.30 | 2026-06-29 | 15d | 1 | 1 | 0 | **2** |
| v3.13.0-beta.29 | 2026-06-29 | 15d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.28 | 2026-06-29 | 15d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.27 | 2026-06-29 | 15d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.26 | 2026-06-29 | 15d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.25 | 2026-06-29 | 15d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.24 | 2026-06-29 | 15d | 2 | 1 | 0 | **3** |
| v3.13.0-beta.23 | 2026-06-29 | 15d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.22 | 2026-06-29 | 15d | 2 | 1 | 0 | **3** |
| v3.13.0-beta.21 | 2026-06-29 | 15d | 0 | 0 | 0 | **0** |
| v3.13.0-beta.20 | 2026-06-29 | 15d | 1 | 0 | 0 | **1** |
| v3.13.0-beta.19 | 2026-06-29 | 15d | 1 | 0 | 0 | **1** |
| v3.13.0-beta.18 | 2026-06-29 | 15d | 0 | 1 | 0 | **1** |
| v3.13.0-beta.17 | 2026-06-29 | 15d | 0 | 0 | 0 | **0** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq)**

---

# ChromIQ-Patches

![downloads](https://img.shields.io/badge/downloads-30-212121) ![clones](https://img.shields.io/badge/clones-299-2196F3) ![views](https://img.shields.io/badge/views-73-4CAF50) ![releases](https://img.shields.io/badge/releases-5-6f42c1)

*Tracking since **2026-07-02** (11 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~11 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 34 | 265 | ▼ -87.2% |
| Views | 9 | 64 | ▼ -85.9% |
| Downloads | 8 | 13 | ▼ -38.5% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 299 | 133 |
| Last 90 Days | 299 | 133 |
| Lifetime | 299 | 133 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 299 | 133 | 166 | 55.5% |
| Last 90 Days | 299 | 133 | 166 | 55.5% |
| Lifetime | 299 | 133 | 166 | 55.5% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 73 | 27 |
| Last 90 Days | 73 | 27 |
| Lifetime | 73 | 27 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 27 | — |
| 🗅️ Unique cloners | 133 | 492.6% |
| 📥 Downloads | 21 | 77.8% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 5

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 28 | 8 |
| dpreview.com | 11 | 5 |
| printerknowledge.com | 6 | 2 |
| Yahoo | 4 | 1 |
| Bing | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 73 | 27 | 46 | 63.0% |
| Last 90 Days | 73 | 27 | 46 | 63.0% |
| Lifetime | 73 | 27 | 46 | 63.0% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 6 | 6 | 10 |
| 🍎 macOS | 12 | 12 | 17 |
| 🐧 Linux | 3 | 3 | 3 |
| **All** | **21** | **21** | **30** |

🆕 **Latest Release:** `v1.2.1` - **7** downloads (published 2026-07-07)

<details>
<summary><strong>📦 Per-version downloads</strong> (5 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | Total |
|---------|-----------|----------|----------|-------|
| v1.2.1 | 1 | 5 | 1 | **7** |
| v1.2.0 | 5 | 7 | 2 | **14** |
| v1.1.0 | 0 | 1 | 0 | **1** |
| v1.0.1 | 1 | 3 | 0 | **4** |
| v1.0.0 | 3 | 1 | 0 | **4** |

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | arm64 | x86_64 | universal | Total |
|----------|-------|-------|-------|-------|
| 🪟 Windows | 0 | 10 | 0 | **10** |
| 🍎 macOS | 14 | 1 | 2 | **17** |
| 🐧 Linux | 0 | 3 | 0 | **3** |

**Top 5 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.2.0 | 14 | 2026-07-03 |
| v1.2.1 | 7 | 2026-07-07 |
| v1.0.1 | 4 | 2026-07-02 |
| v1.0.0 | 4 | 2026-07-02 |
| v1.1.0 | 1 | 2026-07-02 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | Downloads |
|---------|-----------|-----|----|----|----|-----------|
| v1.2.1 | 2026-07-07 | 7d | 1 | 5 | 1 | **7** |
| v1.2.0 | 2026-07-03 | 11d | 5 | 7 | 2 | **14** |
| v1.1.0 | 2026-07-02 | 12d | 0 | 1 | 0 | **1** |
| v1.0.1 | 2026-07-02 | 12d | 1 | 3 | 0 | **4** |
| v1.0.0 | 2026-07-02 | 12d | 3 | 1 | 0 | **4** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq-patches)**

---

*This dashboard is automatically updated daily using GitHub Actions.*
