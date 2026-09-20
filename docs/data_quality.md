# Data Quality Validation

## Overview

Data quality checks are performed throughout the ETL pipeline to ensure the reliability of dashboard metrics and warehouse reporting.

---

## Duplicate Detection

### Validation Rule

Each Steam game should be uniquely identified by:

```text
appid
```

### Check

```python
df.drop_duplicates(
    subset=["appid"],
    keep="first"
)
```

### Results

```text
Rows before deduplication: 5000
Rows after deduplication: 4996
```

Duplicate records were successfully removed during the Silver layer transformation process.

---

## Unicode Validation

### Validation Rule

Game titles containing international characters must be preserved throughout the pipeline.

### Test Record

```text
1468810
鬼谷八荒 Tale of Immortal
```

### Result

Unicode values are stored correctly in:

- Silver Layer
- SQL Server
- Power BI Dashboard

---

## Rating Validation

### Validation Rule

```text
0 <= positive_review_pct <= 100
```

### Validation Query

```sql
SELECT *
FROM game_stats
WHERE positive_review_pct > 100
```

### Result

```text
0 rows returned
```

All rating values fall within the expected range.

---

## Referential Integrity

### Validation Rule

Every record in:

```text
game_stats
```

must have a matching record in:

```text
games
```

### Relationship

```text
games.appid
    ↓
game_stats.appid
```

### Result

Foreign key relationships are enforced in SQL Server.

---

## Review Count Validation

### Validation Rule

```text
review_count =
positive + negative
```

### Purpose

Review volume is used alongside rating percentages to avoid misleading metrics.

Example:

```text
100% rating based on 10 reviews
```

is treated differently from:

```text
95% rating based on 1,000,000 reviews
```

---

## Estimated Owners Validation

### Validation Rule

```text
estimated_owners =
(owners_min + owners_max) / 2
```

### Purpose

Converts SteamSpy ownership ranges into a single analytical metric suitable for aggregation and reporting.

---

## Snapshot Validation

### Validation Rule

All rows loaded during a pipeline execution must share the same:

```text
snapshot_date
```

### Purpose

Ensures consistency across reporting views and dashboard metrics.

---

## Data Quality Summary

Current validation controls include:

✅ Duplicate removal

✅ Unicode preservation

✅ Rating range validation

✅ Referential integrity verification

✅ Review count validation

✅ Estimated owners verification

✅ Snapshot consistency checks