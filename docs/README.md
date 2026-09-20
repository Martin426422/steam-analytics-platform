# Steam Analytics Platform

## Overview

Steam Analytics Platform is an end-to-end data engineering and business intelligence project built using Python, SQL Server and Power BI.

The solution automatically collects game data from the SteamSpy API, processes it through a multi-layer ETL pipeline, stores it in a SQL Server data warehouse and presents insights through interactive Power BI dashboards.

The project follows a layered architecture:

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

## Business Goal

The project aims to answer key business questions about the Steam ecosystem:

- Which games attract the highest player activity?
- How does review volume affect ratings?
- Which publishers dominate