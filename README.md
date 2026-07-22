See full Reference and Usage Guide at:
https://itsab1989.github.io/github-traffic-downloads-dashboard/

> This is a modified version of the original [github-traffic-dashboard](https://github.com/soul-traveller/github-traffic-dashboard), extended with platform-specific download statistics (Windows / macOS / Linux).

# 📊 GitHub Traffic & Downloads Dashboard

This dashboard tracks historical traffic data (clones, views, and release downloads) for GitHub repositories.

**Last Updated:** 2026-07-22T00:12:39.332438Z

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

![downloads](https://img.shields.io/badge/downloads-440-212121) ![clones](https://img.shields.io/badge/clones-16899-2196F3) ![views](https://img.shields.io/badge/views-3605-4CAF50) ![releases](https://img.shields.io/badge/releases-200-6f42c1)

*Tracking since **2026-05-02** (80 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~80 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 794 | 743 | ▲ +6.9% |
| Views | 343 | 306 | ▲ +12.1% |
| Downloads | 146 | 109 | ▲ +33.9% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 5224 | 1141 |
| Last 90 Days | 16899 | 3749 |
| Lifetime | 16899 | 3749 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 5224 | 1141 | 4083 | 78.2% |
| Last 90 Days | 16899 | 3749 | 13150 | 77.8% |
| Lifetime | 16899 | 3749 | 13150 | 77.8% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1771 | 307 |
| Last 90 Days | 3605 | 894 |
| Lifetime | 3605 | 894 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 307 | — |
| 🗅️ Unique cloners | 1141 | 371.7% |
| 📥 Downloads | 641 | 208.8% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 10

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| Google | 50 | 22 |
| printerknowledge.com | 26 | 11 |
| forum.luminous-landscape.com | 14 | 2 |
| github.com | 11 | 5 |
| Bing | 11 | 2 |
| dpreview.com | 6 | 6 |
| hub.displaycal.net | 5 | 3 |
| yandex.ru | 2 | 2 |
| qianwen.com | 2 | 1 |
| DuckDuckGo | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 1771 | 307 | 1464 | 82.7% |
| Last 90 Days | 3605 | 894 | 2711 | 75.2% |
| Lifetime | 3605 | 894 | 2711 | 75.2% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 210 | 411 | 137 |
| 🍎 macOS | 377 | 1009 | 265 |
| 🐧 Linux | 54 | 76 | 38 |
| **All** | **641** | **1496** | **440** |

🆕 **Latest Release:** `v3.14.3` - **16** downloads (published 2026-07-21)

<details>
<summary><strong>📦 Per-version downloads</strong> (200 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | Total |
|---------|-----------|----------|----------|-------|
| v3.14.3 | 4 | 9 | 3 | **16** |
| v3.14.2 | 3 | 2 | 0 | **5** |
| v3.14.1 | 1 | 2 | 0 | **3** |
| v3.14.0 | 2 | 3 | 0 | **5** |
| v3.13.12-beta.35 | 2 | 3 | 0 | **5** |
| v3.13.12-beta.34 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.33 | 0 | 2 | 0 | **2** |
| v3.13.12-beta.32 | 0 | 1 | 0 | **1** |
| v3.13.12-beta.31 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.30 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.29 | 0 | 1 | 0 | **1** |
| v3.13.12-beta.28 | 0 | 1 | 0 | **1** |
| v3.13.12-beta.27 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.26 | 2 | 2 | 0 | **4** |
| v3.13.12-beta.25 | 3 | 3 | 2 | **8** |
| v3.13.12-beta.24 | 1 | 1 | 0 | **2** |
| v3.13.12-beta.23 | 4 | 4 | 1 | **9** |
| v3.13.12-beta.22 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.21 | 1 | 2 | 0 | **3** |
| v3.13.12-beta.20 | 1 | 1 | 0 | **2** |
| v3.13.12-beta.19 | 2 | 2 | 0 | **4** |
| v3.13.12-beta.18 | 0 | 1 | 0 | **1** |
| v3.13.12-beta.17 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.16 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.15 | 0 | 2 | 0 | **2** |
| v3.13.12-beta.14 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.13 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.12 | 0 | 1 | 0 | **1** |
| v3.13.12-beta.11 | 0 | 1 | 0 | **1** |
| v3.13.12-beta.10 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.9 | 2 | 0 | 0 | **2** |
| v3.13.12-beta.8 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.7 | 1 | 0 | 0 | **1** |
| v3.13.12-beta.6 | 0 | 0 | 0 | **0** |
| v3.13.12-beta.5 | 2 | 1 | 0 | **3** |
| v3.13.12-beta.4 | 0 | 1 | 0 | **1** |
| v3.13.12-beta.3 | 0 | 1 | 0 | **1** |
| v3.13.12-beta.2 | 0 | 1 | 0 | **1** |
| v3.13.12-beta.1 | 1 | 1 | 0 | **2** |
| v3.13.11 | 4 | 11 | 0 | **15** |
| v3.13.10 | 1 | 2 | 0 | **3** |
| v3.13.9 | 6 | 4 | 2 | **12** |
| v3.13.8 | 1 | 5 | 0 | **6** |
| v3.13.7 | 1 | 1 | 0 | **2** |
| v3.13.7-beta.5 | 0 | 0 | 0 | **0** |
| v3.13.7-beta.4 | 1 | 1 | 0 | **2** |
| v3.13.7-beta.3 | 0 | 0 | 0 | **0** |
| v3.13.7-beta.2 | 0 | 1 | 0 | **1** |
| v3.13.7-beta.1 | 2 | 0 | 0 | **2** |
| v3.13.6 | 8 | 6 | 1 | **15** |
| v3.13.6-beta.4 | 0 | 1 | 0 | **1** |
| v3.13.6-beta.3 | 0 | 0 | 0 | **0** |
| v3.13.6-beta.2 | 0 | 1 | 0 | **1** |
| v3.13.6-beta.1 | 0 | 0 | 0 | **0** |
| v3.13.5 | 5 | 9 | 0 | **14** |
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
| v3.13.0-beta.39 | 5 | 10 | 5 | **20** |
| v3.13.0-beta.38 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.37 | 1 | 1 | 0 | **2** |
| v3.13.0-beta.36 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.35 | 0 | 1 | 0 | **1** |
| v3.13.0-beta.34 | 2 | 3 | 2 | **7** |
| v3.13.0-beta.33 | 2 | 4 | 2 | **8** |
| v3.13.0-beta.32 | 0 | 0 | 0 | **0** |
| v3.13.0-beta.31 | 4 | 6 | 4 | **14** |
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

</details>

**By Architecture (lifetime):**

*Lifetime downloads split by CPU architecture - useful for deciding which builds are still worth shipping.*

| Platform | arm64 | x86_64 | universal | Total |
|----------|-------|-------|-------|-------|
| 🪟 Windows | 17 | 120 | 0 | **137** |
| 🍎 macOS | 194 | 50 | 21 | **265** |
| 🐧 Linux | 18 | 20 | 0 | **38** |

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v3.13.0-beta.39 | 20 | 2026-06-30 |
| v3.13.0-beta.91 | 17 | 2026-07-04 |
| v3.14.3 | 16 | 2026-07-21 |
| v3.13.11 | 15 | 2026-07-18 |
| v3.13.6 | 15 | 2026-07-13 |
| v3.13.5 | 14 | 2026-07-12 |
| v3.13.0-beta.31 | 14 | 2026-06-29 |
| v3.13.9 | 12 | 2026-07-17 |
| v3.13.3 | 11 | 2026-07-09 |
| v3.13.12-beta.23 | 9 | 2026-07-20 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | Downloads |
|---------|-----------|-----|----|----|----|-----------|
| v3.14.3 | 2026-07-21 | 2d | 4 | 9 | 3 | **16** |
| v3.14.2 | 2026-07-21 | 2d | 3 | 2 | 0 | **5** |
| v3.14.1 | 2026-07-21 | 2d | 1 | 2 | 0 | **3** |
| v3.14.0 | 2026-07-21 | 2d | 2 | 3 | 0 | **5** |
| v3.13.12-beta.35 | 2026-07-21 | 2d | 2 | 3 | 0 | **5** |
| v3.13.12-beta.34 | 2026-07-21 | 2d | 0 | 0 | 0 | **0** |
| v3.13.12-beta.33 | 2026-07-21 | 2d | 0 | 2 | 0 | **2** |
| v3.13.12-beta.32 | 2026-07-21 | 2d | 0 | 1 | 0 | **1** |
| v3.13.12-beta.31 | 2026-07-21 | 2d | 0 | 0 | 0 | **0** |
| v3.13.12-beta.30 | 2026-07-21 | 2d | 0 | 0 | 0 | **0** |
| v3.13.12-beta.29 | 2026-07-21 | 2d | 0 | 1 | 0 | **1** |
| v3.13.12-beta.28 | 2026-07-20 | 3d | 0 | 1 | 0 | **1** |
| v3.13.12-beta.27 | 2026-07-20 | 3d | 0 | 0 | 0 | **0** |
| v3.13.12-beta.26 | 2026-07-20 | 3d | 2 | 2 | 0 | **4** |
| v3.13.12-beta.25 | 2026-07-20 | 3d | 3 | 3 | 2 | **8** |
| v3.13.12-beta.24 | 2026-07-20 | 3d | 1 | 1 | 0 | **2** |
| v3.13.12-beta.23 | 2026-07-20 | 3d | 4 | 4 | 1 | **9** |
| v3.13.12-beta.22 | 2026-07-20 | 3d | 0 | 0 | 0 | **0** |
| v3.13.12-beta.21 | 2026-07-19 | 4d | 1 | 2 | 0 | **3** |
| v3.13.12-beta.20 | 2026-07-19 | 4d | 1 | 1 | 0 | **2** |
| v3.13.12-beta.19 | 2026-07-19 | 4d | 2 | 2 | 0 | **4** |
| v3.13.12-beta.18 | 2026-07-19 | 4d | 0 | 1 | 0 | **1** |
| v3.13.12-beta.17 | 2026-07-19 | 4d | 0 | 0 | 0 | **0** |
| v3.13.12-beta.16 | 2026-07-19 | 4d | 0 | 0 | 0 | **0** |
| v3.13.12-beta.15 | 2026-07-19 | 4d | 0 | 2 | 0 | **2** |
| v3.13.12-beta.14 | 2026-07-19 | 4d | 0 | 0 | 0 | **0** |
| v3.13.12-beta.13 | 2026-07-19 | 4d | 0 | 0 | 0 | **0** |
| v3.13.12-beta.12 | 2026-07-19 | 4d | 0 | 1 | 0 | **1** |
| v3.13.12-beta.11 | 2026-07-19 | 4d | 0 | 1 | 0 | **1** |
| v3.13.12-beta.10 | 2026-07-19 | 4d | 0 | 0 | 0 | **0** |
| v3.13.12-beta.9 | 2026-07-19 | 4d | 2 | 0 | 0 | **2** |
| v3.13.12-beta.8 | 2026-07-19 | 4d | 0 | 0 | 0 | **0** |
| v3.13.12-beta.7 | 2026-07-19 | 4d | 1 | 0 | 0 | **1** |
| v3.13.12-beta.6 | 2026-07-19 | 4d | 0 | 0 | 0 | **0** |
| v3.13.12-beta.5 | 2026-07-18 | 5d | 2 | 1 | 0 | **3** |
| v3.13.12-beta.4 | 2026-07-18 | 5d | 0 | 1 | 0 | **1** |
| v3.13.12-beta.3 | 2026-07-18 | 5d | 0 | 1 | 0 | **1** |
| v3.13.12-beta.2 | 2026-07-18 | 5d | 0 | 1 | 0 | **1** |
| v3.13.12-beta.1 | 2026-07-18 | 5d | 1 | 1 | 0 | **2** |
| feature/126-chartread-engine | 2026-07-18 | 1d | 0 | 0 | 0 | **0** |
| v3.13.11 | 2026-07-18 | 5d | 4 | 11 | 0 | **15** |
| v3.13.10 | 2026-07-18 | 5d | 1 | 2 | 0 | **3** |
| v3.13.9 | 2026-07-17 | 6d | 6 | 4 | 2 | **12** |
| v3.13.8 | 2026-07-17 | 6d | 1 | 5 | 0 | **6** |
| v3.13.7 | 2026-07-16 | 7d | 1 | 1 | 0 | **2** |
| v3.13.7-beta.6 | 2026-07-16 | 1d | 0 | 0 | 0 | **0** |
| v3.13.7-beta.5 | 2026-07-15 | 8d | 0 | 0 | 0 | **0** |
| v3.13.7-beta.4 | 2026-07-15 | 8d | 1 | 1 | 0 | **2** |
| v3.13.7-beta.3 | 2026-07-15 | 8d | 0 | 0 | 0 | **0** |
| v3.13.7-beta.2 | 2026-07-14 | 9d | 0 | 1 | 0 | **1** |
| v3.13.7-beta.1 | 2026-07-14 | 9d | 2 | 0 | 0 | **2** |
| v3.13.6 | 2026-07-13 | 10d | 8 | 6 | 1 | **15** |
| v3.13.6-beta.4 | 2026-07-13 | 10d | 0 | 1 | 0 | **1** |
| v3.13.6-beta.3 | 2026-07-13 | 10d | 0 | 0 | 0 | **0** |
| v3.13.6-beta.2 | 2026-07-13 | 10d | 0 | 1 | 0 | **1** |
| v3.13.6-beta.1 | 2026-07-13 | 10d | 0 | 0 | 0 | **0** |
| v3.13.5 | 2026-07-12 | 11d | 5 | 9 | 0 | **14** |
| v3.13.4 | 2026-07-12 | 11d | 4 | 4 | 0 | **8** |
| v3.13.4-beta.11 | 2026-07-12 | 11d | 0 | 1 | 0 | **1** |
| v3.13.4-beta.10 | 2026-07-11 | 12d | 0 | 1 | 0 | **1** |
| v3.13.4-beta.9 | 2026-07-11 | 12d | 0 | 1 | 0 | **1** |
| v3.13.4-beta.8 | 2026-07-11 | 12d | 0 | 0 | 0 | **0** |
| v3.13.4-beta.7 | 2026-07-11 | 12d | 0 | 1 | 0 | **1** |
| v3.13.4-beta.6 | 2026-07-11 | 12d | 0 | 2 | 0 | **2** |
| v3.13.4-beta.5 | 2026-07-11 | 12d | 0 | 1 | 0 | **1** |
| v3.13.4-beta.4 | 2026-07-10 | 13d | 0 | 1 | 0 | **1** |
| v3.13.4-beta.3 | 2026-07-10 | 13d | 0 | 2 | 0 | **2** |
| v3.13.4-beta.2 | 2026-07-10 | 13d | 0 | 2 | 0 | **2** |
| v3.13.4-beta.1 | 2026-07-10 | 13d | 0 | 0 | 0 | **0** |
| v3.13.3 | 2026-07-09 | 14d | 5 | 4 | 2 | **11** |
| v3.13.2 | 2026-07-09 | 14d | 2 | 3 | 1 | **6** |
| v3.13.1 | 2026-07-08 | 15d | 5 | 3 | 1 | **9** |
| v3.13.0 | 2026-07-08 | 15d | 1 | 7 | 0 | **8** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq)**

---

# ChromIQ-Patches

![downloads](https://img.shields.io/badge/downloads-31-212121) ![clones](https://img.shields.io/badge/clones-315-2196F3) ![views](https://img.shields.io/badge/views-74-4CAF50) ![releases](https://img.shields.io/badge/releases-5-6f42c1)

*Tracking since **2026-07-02** (19 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~19 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 3 | 17 | ▼ -82.4% |
| Views | 1 | 4 | ▼ -75.0% |
| Downloads | 1 | 5 | ▼ -80.0% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 315 | 144 |
| Last 90 Days | 315 | 144 |
| Lifetime | 315 | 144 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 315 | 144 | 171 | 54.3% |
| Last 90 Days | 315 | 144 | 171 | 54.3% |
| Lifetime | 315 | 144 | 171 | 54.3% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 74 | 28 |
| Last 90 Days | 74 | 28 |
| Lifetime | 74 | 28 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 28 | — |
| 🗅️ Unique cloners | 144 | 514.3% |
| 📥 Downloads | 22 | 78.6% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 2

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 6 | 2 |
| printerknowledge.com | 2 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 74 | 28 | 46 | 62.2% |
| Last 90 Days | 74 | 28 | 46 | 62.2% |
| Lifetime | 74 | 28 | 46 | 62.2% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 6 | 6 | 10 |
| 🍎 macOS | 13 | 13 | 18 |
| 🐧 Linux | 3 | 3 | 3 |
| **All** | **22** | **22** | **31** |

🆕 **Latest Release:** `v1.2.1` - **8** downloads (published 2026-07-07)

<details>
<summary><strong>📦 Per-version downloads</strong> (5 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | Total |
|---------|-----------|----------|----------|-------|
| v1.2.1 | 1 | 6 | 1 | **8** |
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
| 🍎 macOS | 15 | 1 | 2 | **18** |
| 🐧 Linux | 0 | 3 | 0 | **3** |

**Top 5 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v1.2.0 | 14 | 2026-07-03 |
| v1.2.1 | 8 | 2026-07-07 |
| v1.0.1 | 4 | 2026-07-02 |
| v1.0.0 | 4 | 2026-07-02 |
| v1.1.0 | 1 | 2026-07-02 |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq-patches)**

---

*This dashboard is automatically updated daily using GitHub Actions.*
