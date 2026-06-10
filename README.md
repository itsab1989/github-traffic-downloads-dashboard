See full Reference and Usage Guide at:
https://itsab1989.github.io/github-traffic-downloads-dashboard/

> This is a modified version of the original [github-traffic-dashboard](https://github.com/soul-traveller/github-traffic-dashboard), extended with platform-specific download statistics (Windows / macOS / Linux).

# 📊 GitHub Traffic & Downloads Dashboard

This dashboard tracks historical traffic data (clones, views, and release downloads) for GitHub repositories.

**Last Updated:** 2026-06-10T13:59:52.507878Z

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

![downloads](https://img.shields.io/badge/downloads-1230-212121) ![clones](https://img.shields.io/badge/clones-7614-2196F3) ![views](https://img.shields.io/badge/views-1287-4CAF50) ![releases](https://img.shields.io/badge/releases-210-6f42c1)

*Tracking since **2026-05-02** (38 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~38 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 249 | 868 | ▼ -71.3% |
| Views | 73 | 310 | ▼ -76.5% |
| Downloads | 443 | 113 | ▲ +292.0% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 5609 | 1326 |
| Last 90 Days | 7614 | 1750 |
| Lifetime | 7614 | 1750 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 5609 | 1326 | 4283 | 76.4% |
| Last 90 Days | 7614 | 1750 | 5864 | 77.0% |
| Lifetime | 7614 | 1750 | 5864 | 77.0% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 985 | 368 |
| Last 90 Days | 1287 | 456 |
| Lifetime | 1287 | 456 |

### 🎯 Engagement Ratios

*How interest deepens over the last 30 days. Views, clones and downloads are independent GitHub metrics, so this is not a strict per-user funnel - clones can exceed views (CI, mirrors, `git clone` without a page view), which shows up as a ratio above 100%.*

| Stage | Count | Ratio to previous stage |
|-------|-------|-------------------------|
| 👀 Views | 985 | — |
| 🗅️ Clones | 5609 | 569.4% |
| 📥 Downloads | 630 | 11.2% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 10

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| ifun.de | 66 | 45 |
| Google | 25 | 10 |
| printerknowledge.com | 19 | 6 |
| reddit.com | 19 | 6 |
| github.com | 17 | 7 |
| dpreview.com | 5 | 4 |
| hub.displaycal.net | 4 | 3 |
| Bing | 3 | 2 |
| forum.luminous-landscape.com | 2 | 2 |
| DuckDuckGo | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 985 | 368 | 617 | 62.6% |
| Last 90 Days | 1287 | 456 | 831 | 64.6% |
| Lifetime | 1287 | 456 | 831 | 64.6% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 118 | 118 | 208 |
| 🍎 macOS | 494 | 494 | 973 |
| 🐧 Linux | 18 | 18 | 49 |
| **All** | **630** | **630** | **1230** |

🆕 **Latest Release:** `v3.8.17` - **9** downloads (published 2026-06-10)

<details>
<summary><strong>📦 Per-version downloads</strong> (210 releases - click to expand)</summary>

| Release | 🪟 Windows | 🍎 macOS | 🐧 Linux | Total |
|---------|-----------|----------|----------|-------|
| v3.8.17 | 2 | 5 | 2 | **9** |
| v3.8.16 | 4 | 9 | 1 | **14** |
| v3.8.15 | 1 | 0 | 0 | **1** |
| v3.8.14 | 0 | 1 | 0 | **1** |
| v3.8.13 | 0 | 3 | 0 | **3** |
| v3.8.12 | 5 | 2 | 0 | **7** |
| v3.8.11 | 4 | 1 | 0 | **5** |
| v3.8.10 | 0 | 3 | 0 | **3** |
| v3.8.9 | 2 | 1 | 0 | **3** |
| v3.8.8 | 4 | 7 | 0 | **11** |
| v3.8.7 | 0 | 0 | 0 | **0** |
| v3.8.6 | 2 | 2 | 0 | **4** |
| v3.8.5 | 2 | 4 | 0 | **6** |
| v3.8.4 | 15 | 4 | 0 | **19** |
| v3.8.3 | 11 | 2 | 0 | **13** |
| v3.8.2 | 2 | 2 | 0 | **4** |
| v3.8.1 | 1 | 1 | 0 | **2** |
| v3.8.0 | 12 | 7 | 2 | **21** |
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
| v3.7.42 | 12 | 3 | 0 | **15** |
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
| v3.7.38 | 1 | 24 | 0 | **25** |
| v3.7.37 | 1 | 3 | 0 | **4** |
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
| 🪟 Windows | 30 | 178 | 0 | **208** |
| 🍎 macOS | 530 | 214 | 229 | **973** |
| 🐧 Linux | 16 | 33 | 0 | **49** |

*💡 Low-volume builds (<2% of lifetime downloads), candidates to stop shipping: 🐧 Linux arm64 (16, 1.3%).*

**Top 10 Releases by Downloads (lifetime):**

| Release | Downloads | Published |
|---------|-----------|-----------|
| v3.6.4 | 54 | 2026-05-17 |
| v3.6.7 | 48 | 2026-05-18 |
| v3.6.5 | 48 | 2026-05-18 |
| v3.7.1 | 42 | 2026-05-18 |
| v3.7.0 | 41 | 2026-05-18 |
| v3.6.6 | 38 | 2026-05-18 |
| v3.7.38 | 25 | 2026-05-24 |
| v3.8.0 | 21 | 2026-05-29 |
| v3.0.0-beta.10 | 20 | 2026-05-08 |
| v3.8.4 | 19 | 2026-06-02 |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | Downloads |
|---------|-----------|-----|----|----|----|-----------|
| v3.8.17 | 2026-06-10 | 1d | 2 | 5 | 2 | **9** |
| v3.8.16 | 2026-06-09 | 2d | 4 | 9 | 1 | **14** |
| v3.8.15 | 2026-06-09 | 2d | 1 | 0 | 0 | **1** |
| v3.8.14 | 2026-06-09 | 2d | 0 | 1 | 0 | **1** |
| v3.8.13 | 2026-06-09 | 2d | 0 | 3 | 0 | **3** |
| v3.8.12 | 2026-06-08 | 3d | 5 | 2 | 0 | **7** |
| v3.8.11 | 2026-06-08 | 3d | 4 | 1 | 0 | **5** |
| v3.8.10 | 2026-06-08 | 3d | 0 | 3 | 0 | **3** |
| v3.8.9 | 2026-06-07 | 4d | 2 | 1 | 0 | **3** |
| v3.8.8 | 2026-06-04 | 7d | 4 | 7 | 0 | **11** |
| v3.8.7 | 2026-06-04 | 7d | 0 | 0 | 0 | **0** |
| v3.8.6 | 2026-06-04 | 7d | 2 | 2 | 0 | **4** |
| v3.8.5 | 2026-06-03 | 8d | 2 | 4 | 0 | **6** |
| v3.8.4 | 2026-06-02 | 9d | 15 | 4 | 0 | **19** |
| v3.8.3 | 2026-05-31 | 11d | 11 | 2 | 0 | **13** |
| v3.8.2 | 2026-05-30 | 12d | 2 | 2 | 0 | **4** |
| v3.8.1 | 2026-05-30 | 12d | 1 | 1 | 0 | **2** |
| v3.8.0 | 2026-05-29 | 13d | 12 | 7 | 2 | **21** |
| v3.8.0-beta.31 | 2026-05-29 | 13d | 1 | 1 | 0 | **2** |
| v3.8.0-beta.30 | 2026-05-29 | 13d | 0 | 1 | 0 | **1** |
| v3.8.0-beta.29 | 2026-05-29 | 13d | 0 | 1 | 0 | **1** |
| v3.8.0-beta.28 | 2026-05-29 | 13d | 0 | 1 | 0 | **1** |
| v3.8.0-beta.27 | 2026-05-29 | 13d | 0 | 1 | 0 | **1** |
| v3.8.0-beta.26 | 2026-05-29 | 13d | 1 | 2 | 0 | **3** |
| v3.8.0-beta.25 | 2026-05-29 | 13d | 0 | 0 | 0 | **0** |
| v3.8.0-beta.24 | 2026-05-29 | 13d | 5 | 6 | 4 | **15** |
| v3.8.0-beta.23 | 2026-05-28 | 14d | 4 | 6 | 4 | **14** |
| v3.8.0-beta.22 | 2026-05-28 | 14d | 1 | 1 | 0 | **2** |
| v3.8.0-beta.21 | 2026-05-28 | 14d | 1 | 0 | 0 | **1** |
| v3.8.0-beta.20 | 2026-05-28 | 14d | 4 | 3 | 2 | **9** |
| v3.8.0-beta.19 | 2026-05-28 | 14d | 0 | 0 | 0 | **0** |
| v3.8.0-beta.18 | 2026-05-28 | 14d | 0 | 0 | 0 | **0** |
| v3.8.0-beta.17 | 2026-05-28 | 14d | 0 | 1 | 1 | **2** |
| v3.8.0-beta.16 | 2026-05-27 | 15d | 2 | 1 | 0 | **3** |
| v3.8.0-beta.15 | 2026-05-27 | 15d | 2 | 1 | 0 | **3** |
| v3.8.0-beta.14 | 2026-05-27 | 15d | 6 | 1 | 0 | **7** |
| v3.8.0-beta.13 | 2026-05-27 | 15d | 0 | 0 | 0 | **0** |
| v3.8.0-beta.12 | 2026-05-27 | 15d | 0 | 0 | 0 | **0** |
| v3.8.0-beta.11 | 2026-05-27 | 15d | 1 | 0 | 0 | **1** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq)**

---

*This dashboard is automatically updated daily using GitHub Actions.*
