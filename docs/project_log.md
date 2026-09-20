# Project Log

## Project Goal

Build an end-to-end Steam analytics platform that:

- Collects data from SteamSpy API
- Processes data through an ETL pipeline
- Stores data in SQL Server
- Delivers business insights through Power BI
- Supports automated refreshes

---

## Milestone 1 - Data Extraction

### Status

✅ Completed

### Result

Successfully connected to SteamSpy API and extracted game data.

Output:

```text
data/raw/steam_raw.csv
```

---

## Milestone 2 - Silver Layer

### Status

✅ Completed

### Implemented

- Data cleaning
- Type standardisation
- Duplicate removal
- Business metric calculations

Output:

```text
data/silver/steam_silver.csv
```

---

## Milestone 3 - Warehouse Design

### Status

✅ Completed

### Implemented

SQL Server warehouse consisting of:

```text
games
game_stats
```

Additional Gold reporting views:

```text
vw_gold_game_performance

vw_gold_latest_game_performance

vw_gold_publisher_stats
```

---

## Milestone 4 - Unicode Issue Resolution

### Status

✅ Completed

### Problem

Asian game titles were displayed as:

```text
????
```

Example:

```text
???? Tale of Immortal
```

### Root Cause

Unicode corruption during SQL loading using:

```python
pandas.to_sql()
```

### Solution

Replaced loading process with parameterized SQL inserts.

### Validation

Successfully loaded:

```text
鬼谷八荒 Tale of Immortal
```

---

## Milestone 5 - Schema Alignment

### Status

✅ Completed

### Problem

The game_stats table remained empty after loading.

### Root Cause

Schema mismatch between ETL output and SQL schema.

Examples:

```text
etl_load_date
estimated_owners
```

### Solution

Synchronized the ETL pipeline and SQL warehouse schema.

---

## Milestone 6 - Dashboard Development

### Status

✅ Completed

### Pages

#### Executive Overview

- Market KPIs
- Top Games by CCU
- Publisher Overview
- Pricing Overview

#### Ratings Analysis

- Review Volume Analysis
- Sentiment Analysis
- Most Reviewed Games

#### Publishers Analysis

- Publisher Portfolio Analysis
- Ratings Comparison
- Activity Comparison
- Pricing Comparison

#### Market & Pricing Analysis

- Price Segmentation
- Activity Analysis
- Rating Analysis
- Market Structure

---

## Milestone 7 - KPI Redesign

### Status

✅ Completed

### Problem

Games with only a few reviews frequently appeared as:

```text
100%
```

causing misleading rankings.

### Solution

Introduced:

```text
review_count
```

and redesigned review-related KPIs and dashboard visuals.

---

## Milestone 8 - Pipeline Automation

### Status

✅ Completed

### Components

```text
Automation/run_pipeline.bat
```

Pipeline execution:

```text
Extract
↓
Transform
↓
Load
```

### Validation

Pipeline successfully processes:

```text
4996 game records
```

from extraction to SQL Server loading.

---

## Current Project Status

### Data Engineering

✅ Completed

### SQL Warehouse

✅ Completed

### Dashboard

✅ Completed

### Automation

✅ Completed

### Documentation

✅ In Progress

---

## Next Planned Improvements

### Historical Snapshot Storage

Store multiple snapshots over time instead of replacing the latest dataset.

Benefits:

- CCU trends
- Rating trends
- Publisher growth analysis
- Historical market comparisons

### Monitoring

- ETL logging
- Alerting
- Pipeline health monitoring