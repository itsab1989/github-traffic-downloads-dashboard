See full Reference and Usage Guide at:
https://itsab1989.github.io/github-traffic-downloads-dashboard/

> This is a modified version of the original [github-traffic-dashboard](https://github.com/soul-traveller/github-traffic-dashboard), extended with platform-specific download statistics (Windows / macOS / Linux).

# 📊 GitHub Traffic & Downloads Dashboard

This dashboard tracks historical traffic data (clones, views, and release downloads) for GitHub repositories.

**Last Updated:** 2026-08-17T15:45:46.157581Z

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

# ChromIQ

![downloads](https://img.shields.io/badge/downloads-0-212121) ![clones](https://img.shields.io/badge/clones-23309-2196F3) ![views](https://img.shields.io/badge/views-5040-4CAF50) ![releases](https://img.shields.io/badge/releases-0-6f42c1)

*Tracking since **2026-05-02** (106 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~106 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 3548 | 1207 | ▲ +194.0% |
| Views | 390 | 321 | ▲ +21.5% |
| Downloads | 81 | 140 | ▼ -42.1% |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 7034 | 2909 |
| Last 90 Days | 18276 | 5515 |
| Lifetime | 23309 | 6537 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 7034 | 2909 | 4125 | 58.6% |
| Last 90 Days | 18276 | 5515 | 12761 | 69.8% |
| Lifetime | 23309 | 6537 | 16772 | 72.0% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 1707 | 310 |
| Last 90 Days | 4518 | 1005 |
| Lifetime | 5040 | 1172 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 310 | — |
| 🗅️ Unique cloners | 2909 | 938.4% |
| 📥 Downloads | 514 | 165.8% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 10

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| Google | 71 | 26 |
| itsab1989.github.io | 60 | 15 |
| github.com | 29 | 9 |
| hub.displaycal.net | 21 | 4 |
| dpreview.com | 15 | 7 |
| Bing | 15 | 5 |
| chatgpt.com | 8 | 2 |
| printerknowledge.com | 5 | 3 |
| DuckDuckGo | 2 | 1 |
| forum.luminous-landscape.com | 2 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 1707 | 310 | 1397 | 81.8% |
| Last 90 Days | 4518 | 1005 | 3513 | 77.8% |
| Lifetime | 5040 | 1172 | 3868 | 76.7% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 176 | 544 | 0 |
| 🍎 macOS | 261 | 1201 | 0 |
| 🐧 Linux | 43 | 109 | 0 |
| **All** | **514** | **1888** | **0** |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | Downloads |
|---------|-----------|-----|----|----|----|-----------|
| v4.1.0 | 2026-08-16 | 2d | 6 | 3 | 0 | **9** |
| v4.0.2-beta.12 | 2026-08-15 | 3d | 0 | 1 | 0 | **1** |
| v4.0.2-beta.11 | 2026-08-14 | 4d | 0 | 2 | 0 | **2** |
| v4.0.2-beta.10 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v4.0.2-beta.9 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v4.0.2-beta.8 | 2026-08-14 | 4d | 0 | 1 | 0 | **1** |
| v4.0.2-beta.7 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v4.0.2-beta.6 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v4.0.2-beta.5 | 2026-08-14 | 4d | 0 | 1 | 0 | **1** |
| v4.0.2-beta.4 | 2026-08-14 | 4d | 0 | 1 | 0 | **1** |
| v4.0.2-beta.3 | 2026-08-14 | 4d | 1 | 1 | 0 | **2** |
| v4.0.2-beta.2 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v4.0.2-beta.1 | 2026-08-14 | 4d | 0 | 1 | 0 | **1** |
| v4.0.1 | 2026-08-13 | 5d | 2 | 5 | 0 | **8** |
| v4.0.0 | 2026-08-13 | 5d | 3 | 6 | 0 | **18** |
| v4.0.0-beta.5 | 2026-08-11 | 7d | 0 | 2 | 0 | **4** |
| v4.0.0-beta.4 | 2026-08-11 | 7d | 0 | 1 | 0 | **1** |
| v4.0.0-beta.3 | 2026-08-11 | 7d | 1 | 0 | 0 | **1** |
| v4.0.0-beta.2 | 2026-08-11 | 7d | 0 | 1 | 0 | **1** |
| v4.0.0-beta.1 | 2026-08-11 | 7d | 2 | 2 | 0 | **8** |
| v3.14.8-beta.222 | 2026-08-10 | 8d | 1 | 0 | 0 | **1** |
| v3.14.8-beta.221 | 2026-08-10 | 8d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.220 | 2026-08-10 | 8d | 1 | 0 | 0 | **1** |
| v3.14.8-beta.219 | 2026-08-10 | 8d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.218 | 2026-08-10 | 8d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.217 | 2026-08-10 | 8d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.216 | 2026-08-10 | 8d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.215 | 2026-08-10 | 8d | 1 | 0 | 0 | **1** |
| v3.14.8-beta.214 | 2026-08-10 | 8d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.213 | 2026-08-10 | 8d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.212 | 2026-08-10 | 8d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.211 | 2026-08-10 | 8d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.210 | 2026-08-10 | 8d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.207 | 2026-08-08 | 10d | 3 | 0 | 0 | **3** |
| v3.14.8-beta.206 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.205 | 2026-08-08 | 10d | 1 | 0 | 0 | **1** |
| v3.14.8-beta.204 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.203 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.202 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.201 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.200 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.199 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.198 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.197 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.196 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.195 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.194 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.193 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.192 | 2026-08-08 | 10d | 1 | 3 | 2 | **6** |
| v3.14.8-beta.191 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.190 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.189 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.188 | 2026-08-08 | 10d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.187 | 2026-08-08 | 10d | 1 | 0 | 0 | **1** |
| v3.14.8-beta.186 | 2026-08-07 | 11d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.185 | 2026-08-07 | 11d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.184 | 2026-08-07 | 11d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.183 | 2026-08-07 | 11d | 2 | 3 | 2 | **7** |
| v3.14.8-beta.182 | 2026-08-07 | 11d | 2 | 3 | 2 | **7** |
| v3.14.8-beta.181 | 2026-08-07 | 11d | 0 | 1 | 0 | **1** |
| v3.14.8-beta.180 | 2026-08-07 | 11d | 1 | 0 | 0 | **1** |
| v3.14.8-beta.179 | 2026-08-07 | 11d | 0 | 1 | 0 | **1** |
| v3.14.8-beta.178 | 2026-08-07 | 11d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.177 | 2026-08-07 | 11d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.176 | 2026-08-07 | 11d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.175 | 2026-08-07 | 11d | 2 | 3 | 2 | **7** |
| v3.14.8-beta.174 | 2026-08-07 | 11d | 2 | 3 | 2 | **7** |
| v3.14.8-beta.173 | 2026-08-07 | 11d | 2 | 3 | 2 | **7** |
| v3.14.8-beta.172 | 2026-08-07 | 11d | 2 | 3 | 2 | **7** |
| v3.14.8-beta.171 | 2026-08-06 | 12d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.170 | 2026-08-06 | 12d | 0 | 1 | 0 | **2** |
| v3.14.8-beta.165 | 2026-08-06 | 12d | 0 | 1 | 0 | **1** |
| v3.14.8-beta.162 | 2026-08-06 | 12d | 1 | 0 | 0 | **1** |
| v3.14.8-beta.160 | 2026-08-06 | 12d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.159 | 2026-08-06 | 12d | 0 | 1 | 0 | **1** |
| v3.14.8-beta.158 | 2026-08-06 | 12d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.157 | 2026-08-06 | 12d | 0 | 1 | 0 | **1** |
| v3.14.8-beta.156 | 2026-08-06 | 12d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.155 | 2026-08-06 | 12d | 2 | 4 | 2 | **10** |
| v3.14.8-beta.154 | 2026-08-06 | 12d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.153 | 2026-08-06 | 12d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.152 | 2026-08-06 | 12d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.151 | 2026-08-06 | 12d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.150 | 2026-08-06 | 12d | 0 | 1 | 0 | **1** |
| v3.14.8-beta.149 | 2026-08-06 | 12d | 2 | 3 | 2 | **9** |
| v3.14.8-beta.148 | 2026-08-06 | 12d | 1 | 1 | 0 | **2** |
| v3.14.8-beta.147 | 2026-08-05 | 13d | 0 | 1 | 0 | **1** |
| v3.14.8-beta.146 | 2026-08-05 | 13d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.145 | 2026-08-05 | 13d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.144 | 2026-08-05 | 13d | 2 | 1 | 0 | **4** |
| v3.14.8-beta.143 | 2026-08-05 | 13d | 1 | 0 | 0 | **1** |
| v3.14.8-beta.142 | 2026-08-05 | 13d | 1 | 1 | 0 | **2** |
| v3.14.8-beta.141 | 2026-08-05 | 13d | 1 | 1 | 0 | **2** |
| v3.14.8-beta.140 | 2026-08-05 | 13d | 0 | 1 | 0 | **1** |
| v3.14.8-beta.139 | 2026-08-05 | 13d | 2 | 1 | 0 | **4** |
| v3.14.8-beta.138 | 2026-08-05 | 13d | 1 | 1 | 0 | **3** |
| v3.14.8-beta.137 | 2026-08-04 | 14d | 1 | 1 | 0 | **3** |
| v3.14.8-beta.136 | 2026-08-04 | 14d | 1 | 1 | 0 | **3** |
| v3.14.8-beta.135 | 2026-08-04 | 14d | 0 | 1 | 0 | **2** |
| v3.14.8-beta.134 | 2026-08-04 | 14d | 1 | 0 | 0 | **2** |
| v3.14.8-beta.133 | 2026-08-04 | 14d | 1 | 1 | 0 | **3** |
| v3.14.8-beta.132 | 2026-08-04 | 14d | 0 | 1 | 0 | **3** |
| v3.14.8-beta.131 | 2026-08-04 | 14d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.130 | 2026-08-04 | 14d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.129 | 2026-08-04 | 14d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.128 | 2026-08-04 | 14d | 0 | 1 | 0 | **2** |
| v3.14.8-beta.127 | 2026-08-03 | 15d | 0 | 1 | 0 | **1** |
| v3.14.8-beta.126 | 2026-08-03 | 15d | 0 | 0 | 0 | **0** |
| v3.14.8-beta.125 | 2026-08-03 | 15d | 0 | 2 | 0 | **3** |
| v3.14.8-beta.124 | 2026-08-03 | 15d | 0 | 0 | 0 | **0** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq)**

---

# ChromIQ-Patches

![downloads](https://img.shields.io/badge/downloads-0-212121) ![clones](https://img.shields.io/badge/clones-329-2196F3) ![views](https://img.shields.io/badge/views-82-4CAF50) ![releases](https://img.shields.io/badge/releases-0-6f42c1)

*Tracking since **2026-07-02** (43 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~43 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 4 | 5 | ▼ -20.0% |
| Views | 3 | 1 | ▲ +200.0% |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 15 | 13 |
| Last 90 Days | 329 | 156 |
| Lifetime | 329 | 156 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 15 | 13 | 2 | 13.3% |
| Last 90 Days | 329 | 156 | 173 | 52.6% |
| Lifetime | 329 | 156 | 173 | 52.6% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 9 | 7 |
| Last 90 Days | 82 | 34 |
| Lifetime | 82 | 34 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 7 | — |
| 🗅️ Unique cloners | 13 | 185.7% |
| 📥 Downloads | 7 | 100.0% |

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
| Last 30 Days | 9 | 7 | 2 | 22.2% |
| Last 90 Days | 82 | 34 | 48 | 58.5% |
| Lifetime | 82 | 34 | 48 | 58.5% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 3 | 9 | 0 |
| 🍎 macOS | 4 | 16 | 0 |
| 🐧 Linux | 0 | 3 | 0 |
| **All** | **7** | **28** | **0** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq-patches)**

---

# ChromIQ-Gamut-Viewer

![downloads](https://img.shields.io/badge/downloads-0-212121) ![clones](https://img.shields.io/badge/clones-720-2196F3) ![views](https://img.shields.io/badge/views-2-4CAF50) ![releases](https://img.shields.io/badge/releases-0-6f42c1)

*Tracking since **2026-08-13** (3 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~3 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 720 | 0 | — |
| Views | 2 | 0 | — |
| Downloads | 1 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 720 | 170 |
| Last 90 Days | 720 | 170 |
| Lifetime | 720 | 170 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 720 | 170 | 550 | 76.4% |
| Last 90 Days | 720 | 170 | 550 | 76.4% |
| Lifetime | 720 | 170 | 550 | 76.4% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 2 | 1 |
| Last 90 Days | 2 | 1 |
| Lifetime | 2 | 1 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 1 | — |
| 🗅️ Unique cloners | 170 | 17000.0% |
| 📥 Downloads | 1 | 100.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 0

*No referrer data available.*

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 2 | 1 | 1 | 50.0% |
| Last 90 Days | 2 | 1 | 1 | 50.0% |
| Lifetime | 2 | 1 | 1 | 50.0% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 1 | 1 | 0 |
| 🍎 macOS | 0 | 0 | 0 |
| 🐧 Linux | 0 | 0 | 0 |
| **All** | **1** | **1** | **0** |

**Recent Release Reception (first ~14 days):**

*Downloads each release accrued in its early life. Measured over each release's own early-life window, so a brand-new release isn't unfairly compared against a mature one. Only releases published within ~14 days appear.*

| Release | Published | Age | 🪟 | 🍎 | 🐧 | Downloads |
|---------|-----------|-----|----|----|----|-----------|
| v2.20.0 | 2026-08-17 | 1d | 0 | 0 | 0 | **0** |
| v2.19.0 | 2026-08-17 | 1d | 0 | 0 | 0 | **0** |
| v2.18.0 | 2026-08-17 | 1d | 0 | 0 | 0 | **0** |
| v2.17.0 | 2026-08-17 | 1d | 0 | 0 | 0 | **0** |
| v2.16.0 | 2026-08-17 | 1d | 0 | 0 | 0 | **0** |
| v2.15.1 | 2026-08-16 | 2d | 0 | 0 | 0 | **0** |
| v2.15.0 | 2026-08-16 | 2d | 0 | 0 | 0 | **0** |
| v2.14.0 | 2026-08-16 | 2d | 0 | 0 | 0 | **0** |
| v2.13.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.12.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.11.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.10.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.9.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.8.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.7.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.6.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.5.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.4.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.3.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.2.1 | 2026-08-15 | 3d | 1 | 0 | 0 | **1** |
| v2.2.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.1.0 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.0.1 | 2026-08-15 | 3d | 0 | 0 | 0 | **0** |
| v2.0.0 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.9.6 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.9.2 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.9.1 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.9.0 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.8.0 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.7.1 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.7.0 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.6.1 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.6.0 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.5.2 | 2026-08-14 | 4d | 0 | 2 | 0 | **2** |
| v1.5.1 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.5.0 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.4.0 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.3.1 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.3.0 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.2.0 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.1.0 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.0.1 | 2026-08-14 | 4d | 0 | 0 | 0 | **0** |
| v1.0.0 | 2026-08-14 | 4d | 1 | 2 | 2 | **5** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#chromiq-gamut-viewer)**

---

# github-traffic-downloads-dashboard

![downloads](https://img.shields.io/badge/downloads-0-212121) ![clones](https://img.shields.io/badge/clones-3876-2196F3) ![views](https://img.shields.io/badge/views-8-4CAF50) ![releases](https://img.shields.io/badge/releases-0-6f42c1)

*Tracking since **2026-07-30** (17 active days). Where the 90-day and Lifetime columns match the 30-day column, it is because only ~17 days have been tracked so far.*

**This week vs last week:**

| Metric | This week | Last week | Change |
|--------|-----------|-----------|--------|
| Clones | 3103 | 556 | ▲ +458.1% |
| Views | 7 | 0 | — |
| Downloads | 0 | 0 | — |

### 🗅️ Clones

*Repository clone statistics showing total and unique clones over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 3876 | 2655 |
| Last 90 Days | 3876 | 2655 |
| Lifetime | 3876 | 2655 |

### 📄 Repeat vs New Clones

*Analysis of repository adoption showing repeat clones vs new unique clones.*

*Note: GitHub API does not provide geographical location data for cloners.*

| Period | Total Clones | Unique Clones | Repeat Clones | Repeat % |
|--------|--------------|----------------|----------------|----------|
| Last 30 Days | 3876 | 2655 | 1221 | 31.5% |
| Last 90 Days | 3876 | 2655 | 1221 | 31.5% |
| Lifetime | 3876 | 2655 | 1221 | 31.5% |

### 👀 Views

*Repository view statistics showing total and unique views over different time periods.*

| Period | Total | Unique |
|--------|-------|--------|
| Last 30 Days | 8 | 3 |
| Last 90 Days | 8 | 3 |
| Lifetime | 8 | 3 |

### 🎯 Engagement Ratios

*Of the people who looked at the repo in the last 30 days, how many took a deeper action? Cloning (developer interest) and downloading (end-user adoption) are independent actions, each shown relative to unique visitors. Uniques are per-day and cloning/downloading can happen without a page view (CI, mirrors, direct links), so ratios above 100% are possible. Downloads have no unique-people equivalent, so the total is shown.*

| Action | Count | Ratio to unique visitors |
|--------|-------|--------------------------|
| 👀 Unique visitors | 3 | — |
| 🗅️ Unique cloners | 2655 | 88500.0% |
| 📥 Downloads | 0 | 0.0% |

### 📞 Referrers

*Top referrer sources driving traffic to this repository.*

**Total Unique Referrers:** 2

| Referrer | Total Views | Unique Visitors |
|----------|-------------|----------------|
| github.com | 6 | 1 |
| DuckDuckGo | 1 | 1 |

### 👥 Repeat vs New Visitors

*Analysis of visitor engagement showing repeat visitors vs new unique visitors.*

*Note: GitHub API does not provide geographical location data for visitors.*

| Period | Total Views | Unique Visitors | Repeat Visitors | Repeat % |
|--------|-------------|-----------------|-----------------|----------|
| Last 30 Days | 8 | 3 | 5 | 62.5% |
| Last 90 Days | 8 | 3 | 5 | 62.5% |
| Lifetime | 8 | 3 | 5 | 62.5% |

### 📥 Release Downloads

*Pre-compiled release-asset downloads, split by platform. This is separate from clones.*

*Lifetime totals reflect all-time downloads (GitHub's cumulative counter). Per-day figures (Last 30/90 Days) are derived from daily snapshots and only accrue from the first tracked day onward.*

| Platform | Last 30 Days | Last 90 Days | Lifetime |
|----------|-----------|-----------|----------|
| 🪟 Windows | 0 | 0 | 0 |
| 🍎 macOS | 0 | 0 | 0 |
| 🐧 Linux | 0 | 0 | 0 |
| **All** | **0** | **0** | **0** |

### 📈 Interactive Charts

*Clones/views and per-platform download charts - with hover tooltips, dark mode, and release-date markers - are rendered live on the dashboard page (GitHub can't run the charts inside this README):*

📊 **[Open the interactive dashboard →](https://itsab1989.github.io/github-traffic-downloads-dashboard/dashboard.html#github-traffic-downloads-dashboard)**

---

*This dashboard is automatically updated daily using GitHub Actions.*
