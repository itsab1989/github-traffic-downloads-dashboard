See full Reference and Usage Guide at:
https://itsab1989.github.io/github-traffic-downloads-dashboard/

> This is a modified version of the original [github-traffic-dashboard](https://github.com/soul-traveller/github-traffic-dashboard), extended with platform-specific download statistics (Windows / macOS / Linux).

# 📊 GitHub Traffic & Downloads Dashboard

This dashboard tracks historical traffic data (clones, views, and release downloads) for GitHub repositories.

**Last Updated:** 2026-06-22T23:09:22.801095Z

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

# ChromIQ

![downloads](https://img.shields.io/badge/downloads-1473-212121) ![clones](https://img.shields.io/badge/clones-11675-2196F3) ![views](https://img.shields.io/badge/views-1834-4CAF50) ![releases](https://img.shields.io/badge/releases-299-6f42c1)

*Tracking since **2026-05-02** (51 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~51 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 1780 | 2281 | ▼ -22.0% |
| Views | 205 | 342 | ▼ -40.1% |
| Downloads | 157 | 128 | ▲ +22.7% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 6042 | 1413 |
| Last 90 Days | 11675 | 2608 |
| Lifetime | 11675 | 2608 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 6042 | 1413 | 4629 | 76.6% |
| Last 90 Days | 11675 | 2608 | 9067 | 77.7% |
| Lifetime | 11675 | 2608 | 9067 | 77.7% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1138 | 368 |
| Last 90 Days | 1834 | 587 |
| Lifetime | 1834 | 587 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 368 | — |
| 🗅️ Unique cloners | 1413 | 384.0% |
| 📥 Downloads | 873 | 237.2% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 10

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 210 | 7 |
| Google | 26 | 13 |
| printerknowledge.com | 25 | 10 |
| dpreview.com | 8 | 5 |
| reddit.com | 5 | 5 |
| ifun.de | 4 | 4 |
| hub.displaycal.net | 4 | 2 |
| forum.luminous-landscape.com | 3 | 1 |
| Bing | 2 | 2 |
| kagi.com | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 1138 | 368 | 770 | 67.7% |
| Last 90 Days | 1834 | 587 | 1247 | 68.0% |
| Lifetime | 1834 | 587 | 1247 | 68.0% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 210 | 210 | 300 |
| 🍎 macOS | 641 | 641 | 1120 |
| 🐧 Linux | 22 | 22 | 53 |
| **All** | **873** | **873** | **1473** |

🆕 **Latest Release:** `v3.11.25` - **6** downloads (published 2026-06-22)

<details>
<summary><strong>📦 Per-version downloads</strong> (299 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | Total |
|---------|-----------|----------|----------|-------|
| v3.11.25 | 4 | 2 | 0 | **6** |
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
| v3.10.5 | 2 | 3 | 2 | **7** |
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
| v3.8.0-beta.24 | 5 | 6 | 4 | **15** |
| v3.8.0-beta.23 | 4 | 6 | 4 | **14** |
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
| v3.8.0-beta.5 | 2 | 4 | 2 | **8** |
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
| v3.7.27 | 1 | 4 | 0 | **5** |
| v3.7.26 | 0 | 3 | 0 | **3** |
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
| v3.7.11 | 1 | 4 | 0 | **5** |
| v3.7.10 | 2 | 7 | 0 | **9** |
| v3.7.9 | 0 | 10 | 0 | **10** |
| v3.7.8 | 0 | 10 | 0 | **10** |
| v3.7.7 | 0 | 4 | 0 | **4** |
| v3.7.6 | 0 | 6 | 0 | **6** |
| v3.7.5 | 5 | 7 | 1 | **13** |
| v3.7.4 | 1 | 8 | 0 | **9** |
| v3.7.3 | 0 | 8 | 0 | **8** |
| v3.7.2 | 1 | 4 | 0 | **5** |
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
| v3.5.1 | 0 | 4 | 0 | **4** |
| v3.5.0 | 1 | 6 | 1 | **8** |
| v3.5.0-beta.6 | 0 | 4 | 1 | **5** |
| v3.5.0-beta.5 | 0 | 3 | 2 | **5** |
| v3.2.9 | 3 | 4 | 0 | **7** |
| v3.5.0-beta.4 | 0 | 5 | 1 | **6** |
| v3.5.0-beta.3 | 0 | 3 | 0 | **3** |
| v3.5.0-beta.2 | 0 | 5 | 0 | **5** |
| v3.5.0-beta.1 | 0 | 3 | 0 | **3** |
| v3.2.8 | 1 | 5 | 0 | **6** |
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
| v3.2.0-beta.1 | 0 | 3 | 0 | **3** |
| v3.1.4 | 0 | 3 | 0 | **3** |
| v3.1.3 | 0 | 4 | 0 | **4** |
| v3.1.2 | 0 | 3 | 0 | **3** |
| v3.1.1 | 1 | 5 | 0 | **6** |
| v3.1.0 | 1 | 3 | 0 | **4** |
| v3.0.2 | 0 | 3 | 0 | **3** |
| v3.0.1 | 0 | 2 | 0 | **2** |
| v3.0.0 | 2 | 6 | 0 | **8** |
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
| v2.9.0 | 0 | 4 | 0 | **4** |
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
| v2.2.2 | 0 | 7 | 0 | **7** |
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
| v2.0.4 | 0 | 3 | 0 | **3** |
| v2.0.3 | 0 | 4 | 0 | **4** |
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
| v1.1.3 | 0 | 7 | 0 | **7** |
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
| 🪟 Windows | 39 | 261 | 0 | **300** |
| 🍎 macOS | 645 | 232 | 243 | **1120** |
| 🐧 Linux | 18 | 35 | 0 | **53** |

*💡 Low-volume builds (<2% of lifetime downloads), candidates to stop shipping: 🐧 Linux arm64 (18, 1.2%).*

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v3.6.4 | 54 | 2026-05-17 |
| v3.6.7 | 48 | 2026-05-18 |
| v3.6.5 | 48 | 2026-05-18 |
| v3.7.1 | 42 | 2026-05-18 |
| v3.7.0 | 41 | 2026-05-18 |
| v3.6.6 | 38 | 2026-05-18 |
| v3.7.38 | 28 | 2026-05-24 |
| v3.8.0 | 22 | 2026-05-29 |
| v3.8.4 | 20 | 2026-06-02 |
| v3.0.0-beta.10 | 20 | 2026-05-08 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | Downloads |
|---------|-----------|-----|----|----|----|-----------|
| v3.11.25 | 2026-06-22 | 1d | 4 | 2 | 0 | **6** |
| v3.11.24 | 2026-06-22 | 1d | 1 | 5 | 0 | **6** |
| v3.11.23 | 2026-06-21 | 2d | 5 | 2 | 0 | **7** |
| v3.11.22 | 2026-06-21 | 2d | 0 | 0 | 0 | **0** |
| v3.11.21 | 2026-06-21 | 2d | 1 | 1 | 0 | **2** |
| v3.11.20 | 2026-06-21 | 2d | 2 | 2 | 0 | **4** |
| v3.11.19 | 2026-06-21 | 2d | 1 | 2 | 0 | **3** |
| v3.11.18 | 2026-06-20 | 3d | 8 | 5 | 0 | **13** |
| v3.11.17 | 2026-06-20 | 3d | 0 | 0 | 0 | **0** |
| v3.11.16 | 2026-06-19 | 4d | 1 | 0 | 0 | **1** |
| v3.11.15 | 2026-06-19 | 4d | 0 | 0 | 0 | **0** |
| v3.11.14 | 2026-06-19 | 4d | 0 | 0 | 0 | **0** |
| v3.11.13 | 2026-06-19 | 4d | 1 | 0 | 0 | **1** |
| v3.11.12 | 2026-06-19 | 4d | 0 | 0 | 0 | **0** |
| v3.11.11 | 2026-06-19 | 4d | 6 | 5 | 0 | **11** |
| v3.11.10 | 2026-06-19 | 4d | 0 | 2 | 0 | **2** |
| v3.11.9 | 2026-06-19 | 4d | 1 | 2 | 0 | **3** |
| v3.11.8 | 2026-06-19 | 4d | 1 | 5 | 0 | **6** |
| v3.11.7 | 2026-06-18 | 5d | 2 | 1 | 0 | **3** |
| v3.11.6 | 2026-06-18 | 5d | 2 | 2 | 0 | **4** |
| v3.11.5 | 2026-06-18 | 5d | 0 | 1 | 0 | **1** |
| v3.11.4 | 2026-06-18 | 5d | 2 | 1 | 0 | **3** |
| v3.11.3 | 2026-06-18 | 5d | 1 | 3 | 0 | **4** |
| v3.11.2 | 2026-06-18 | 5d | 0 | 2 | 0 | **2** |
| v3.11.1 | 2026-06-18 | 5d | 0 | 2 | 0 | **2** |
| v3.11.0 | 2026-06-17 | 6d | 3 | 2 | 0 | **5** |
| v3.10.28 | 2026-06-17 | 6d | 1 | 0 | 0 | **1** |
| v3.10.27 | 2026-06-17 | 6d | 0 | 0 | 0 | **0** |
| v3.10.26 | 2026-06-17 | 6d | 2 | 2 | 0 | **4** |
| v3.10.25 | 2026-06-17 | 6d | 0 | 0 | 0 | **0** |
| v3.10.24 | 2026-06-17 | 6d | 1 | 3 | 0 | **4** |
| v3.10.23 | 2026-06-17 | 6d | 0 | 2 | 0 | **2** |
| v3.10.22 | 2026-06-17 | 6d | 0 | 0 | 0 | **0** |
| v3.10.21 | 2026-06-17 | 6d | 1 | 2 | 0 | **3** |
| v3.10.20 | 2026-06-17 | 6d | 0 | 2 | 0 | **2** |
| v3.10.19 | 2026-06-17 | 6d | 1 | 2 | 0 | **3** |
| v3.10.18 | 2026-06-17 | 6d | 1 | 3 | 0 | **4** |
| v3.10.17 | 2026-06-17 | 6d | 0 | 0 | 0 | **0** |
| v3.10.16 | 2026-06-16 | 7d | 0 | 4 | 0 | **4** |
| v3.10.15 | 2026-06-16 | 7d | 3 | 2 | 0 | **5** |
| v3.10.14 | 2026-06-16 | 7d | 1 | 1 | 0 | **2** |
| v3.10.13 | 2026-06-16 | 7d | 0 | 2 | 0 | **2** |
| v3.10.12 | 2026-06-16 | 7d | 0 | 0 | 0 | **0** |
| v3.10.11 | 2026-06-16 | 7d | 0 | 0 | 0 | **0** |
| v3.10.10 | 2026-06-16 | 7d | 0 | 4 | 0 | **4** |
| v3.10.9 | 2026-06-16 | 7d | 1 | 2 | 0 | **3** |
| v3.10.8 | 2026-06-16 | 7d | 0 | 4 | 0 | **4** |
| v3.10.7 | 2026-06-16 | 7d | 0 | 1 | 0 | **1** |
| v3.10.6 | 2026-06-15 | 8d | 0 | 0 | 0 | **0** |
| v3.10.5 | 2026-06-15 | 8d | 2 | 3 | 2 | **7** |
| v3.10.4 | 2026-06-15 | 8d | 0 | 2 | 0 | **2** |
| v3.10.3 | 2026-06-15 | 8d | 0 | 1 | 0 | **1** |
| v3.10.2 | 2026-06-15 | 8d | 7 | 7 | 2 | **16** |
| v3.10.1 | 2026-06-15 | 8d | 0 | 0 | 0 | **0** |
| v3.10.0 | 2026-06-15 | 8d | 1 | 1 | 0 | **2** |
| v3.9.31 | 2026-06-15 | 8d | 0 | 0 | 0 | **0** |
| v3.9.30 | 2026-06-15 | 8d | 0 | 1 | 0 | **1** |
| v3.9.29 | 2026-06-15 | 8d | 2 | 3 | 0 | **5** |
| v3.9.28 | 2026-06-14 | 9d | 1 | 2 | 0 | **3** |
| v3.9.27 | 2026-06-14 | 9d | 0 | 1 | 0 | **1** |
| v3.9.26 | 2026-06-14 | 9d | 0 | 2 | 0 | **2** |
| v3.9.25 | 2026-06-14 | 9d | 0 | 1 | 0 | **1** |
| v3.9.24 | 2026-06-14 | 9d | 0 | 2 | 0 | **2** |
| v3.9.23 | 2026-06-14 | 9d | 1 | 2 | 0 | **3** |
| v3.9.22 | 2026-06-14 | 9d | 0 | 0 | 0 | **0** |
| v3.9.21 | 2026-06-14 | 9d | 3 | 3 | 0 | **6** |
| v3.9.20 | 2026-06-13 | 10d | 0 | 2 | 0 | **2** |
| v3.9.19 | 2026-06-13 | 10d | 2 | 0 | 0 | **2** |
| v3.9.18 | 2026-06-13 | 10d | 0 | 2 | 0 | **2** |
| v3.9.17 | 2026-06-13 | 10d | 1 | 1 | 0 | **2** |
| v3.9.16 | 2026-06-13 | 10d | 2 | 3 | 0 | **5** |
| v3.9.15 | 2026-06-13 | 10d | 1 | 1 | 0 | **2** |
| v3.9.14 | 2026-06-13 | 10d | 0 | 0 | 0 | **0** |
| v3.9.13 | 2026-06-13 | 10d | 2 | 2 | 0 | **4** |
| v3.9.12 | 2026-06-12 | 11d | 0 | 2 | 0 | **2** |
| v3.9.11 | 2026-06-12 | 11d | 0 | 0 | 0 | **0** |
| v3.9.10 | 2026-06-12 | 11d | 0 | 1 | 0 | **1** |
| v3.9.9 | 2026-06-12 | 11d | 0 | 0 | 0 | **0** |
| v3.9.8 | 2026-06-12 | 11d | 0 | 0 | 0 | **0** |
| v3.9.7 | 2026-06-12 | 11d | 0 | 0 | 0 | **0** |
| v3.9.6 | 2026-06-12 | 11d | 1 | 2 | 0 | **3** |
| v3.9.5 | 2026-06-12 | 11d | 0 | 0 | 0 | **0** |
| v3.9.4 | 2026-06-12 | 11d | 0 | 0 | 0 | **0** |
| v3.9.3 | 2026-06-11 | 12d | 1 | 0 | 0 | **1** |
| v3.9.2 | 2026-06-11 | 12d | 0 | 0 | 0 | **0** |
| v3.9.1 | 2026-06-11 | 12d | 1 | 1 | 0 | **2** |
| v3.9.0 | 2026-06-11 | 12d | 0 | 0 | 0 | **0** |
| v3.8.19 | 2026-06-10 | 13d | 4 | 4 | 0 | **8** |
| v3.8.18 | 2026-06-10 | 13d | 1 | 2 | 0 | **3** |
| v3.8.17 | 2026-06-10 | 13d | 2 | 5 | 2 | **9** |
| v3.8.16 | 2026-06-09 | 14d | 4 | 9 | 1 | **14** |
| v3.8.15 | 2026-06-09 | 14d | 1 | 0 | 0 | **1** |
| v3.8.14 | 2026-06-09 | 14d | 0 | 1 | 0 | **1** |
| v3.8.13 | 2026-06-09 | 14d | 0 | 3 | 0 | **3** |
| v3.8.12 | 2026-06-08 | 15d | 6 | 2 | 0 | **8** |
| v3.8.11 | 2026-06-08 | 15d | 4 | 1 | 0 | **5** |
| v3.8.10 | 2026-06-08 | 15d | 0 | 3 | 0 | **3** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq)**

---

*This dashboard is automatically updated daily using GitHub Actions.*
