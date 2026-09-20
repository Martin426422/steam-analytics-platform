# ETL Design Decisions

## Business Key Selection

### Decision

Steam AppID was selected as the business key across the entire solution.

### Reason

Game titles are not unique.

Examples found during validation:

- Fallout: New Vegas
- F.E.A.R.
- DOOM 3

appeared multiple times under different AppIDs.

Using game names as primary identifiers could lead to incorrect aggregation and duplicate counting.

### Result

All warehouse relationships are based on:

```text
appid
```

instead of:

```text
name
```

---

## Duplicate Removal Strategy

### Decision

Records are deduplicated in the Silver layer.

### Logic

```python
df.drop_duplicates(
    subset=["appid"],
    keep="first"
)
```

### Result

```text
Rows before deduplication: 5000
Rows after deduplication: 4996
```

---

## Unicode Preservation

### Problem

Games containing Asian characters were loaded into SQL Server as:

```text
???? Tale of Immortal
```

instead of:

```text
鬼谷八荒 Tale of Immortal
```

### Root Cause

Unicode characters were corrupted during loading through:

```python
pandas.to_sql()
```

### Solution

The loading logic was replaced with explicit parameterized SQL inserts.

### Validation

Unicode validation game:

```text
1468810
鬼谷八荒 Tale of Immortal
```

is successfully stored and displayed.

---

## Estimated Owners Calculation

### Source Data

SteamSpy provides ownership ranges:

```text
200000 .. 500000
```

### Transformation

```python
estimated_owners =
(owners_min + owners_max) / 2
```

### Purpose

Provides a single value useful for aggregation and dashboard metrics.

---

## Review Volume Integration

### Problem

Games with very few reviews often appeared as:

```text
100%
```

which produced misleading rankings.

Example:

```text
10 reviews
10 positive
0 negative
```

### Solution

Review count was introduced as an analytical metric:

```python
review_count =
positive + negative
```

### Result

Ratings are analysed together with review volume.

---

## Snapshot Strategy

### Current Approach

The warehouse stores only the latest snapshot.

Each pipeline execution refreshes the latest available data.

### Benefits

- Simpler ETL process
- Smaller storage footprint
- Faster refreshes

### Limitation

Historical trend analysis is currently unavailable.

Examples:

- CCU trends
- Rating trends
- Publisher growth trends

cannot be analysed yet.

---

## Future Improvement

Future versions will store historical snapshots in:

```text
game_stats
```

using:

```text
appid
snapshot_date
```

as the natural grain of the fact table.

This will enable:

- Time series analysis
- Trend reporting
- Historical comparisons
- Growth analytics