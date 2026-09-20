# Architecture

## Solution Overview

Steam Analytics Platform follows a layered data architecture designed to separate data ingestion, transformation, storage and reporting responsibilities.

```text
SteamSpy API
    ↓
Raw Layer
    ↓
Silver Layer
    ↓
SQL Server Data Warehouse
    ↓
Gold Views
    ↓
Power BI Dashboard
```

---

## Data Flow

### Extract Layer

The extraction process retrieves data from the SteamSpy API and stores it in the Raw layer.

Output:

```text
data/raw/steam_raw.csv
```

Script:

```text
ETL/extract_steam.py
```

---

### Transform Layer

Data is cleaned, standardized and validated before loading.

Key transformations:

- Duplicate removal
- Data type standardization
- Rating calculations
- Estimated owners calculation
- Unicode validation

Output:

```text
data/silver/steam_silver.csv
```

Script:

```text
ETL/transform_steam.py
```

---

### Load Layer

Transformed data is loaded into SQL Server.

Target tables:

```text
games
game_stats
```

Script:

```text
ETL/load_mssql.py
```

---

## Data Warehouse

### Dimension Table

#### games

Stores descriptive game information.

```text
appid
name
developer
publisher
```

---

### Fact Table

#### game_stats

Stores performance-related metrics.

```text
appid
snapshot_date

positive
negative
positive_review_pct

price_usd
discount

ccu

owners_min
owners_max
estimated_owners
```

---

## Gold Layer

The Gold Layer provides reporting-ready views.

### vw_gold_game_performance

General analytical view.

### vw_gold_latest_game_performance

Latest available snapshot.

### vw_gold_publisher_stats

Publisher-level aggregations.

---

## Dashboard Layer

Power BI consumes reporting-ready Gold views.

Pages:

```text
Executive Overview

Ratings Analysis

Publishers Analysis

Market & Pricing Analysis
```

---

## Automation

Pipeline execution flow:

```text
run_pipeline.bat

Extract
↓
Transform
↓
Load
```

Execution can be scheduled through:

```text
Windows Task Scheduler
```

using a weekly refresh schedule.

---

## Future Architecture Enhancements

Planned improvements:

- Historical snapshot storage
- Trend analysis
- ETL logging
- Pipeline monitoring
- Alerting and failure notifications