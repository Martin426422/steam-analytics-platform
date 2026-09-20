import pandas as pd
from sqlalchemy import create_engine, text
from datetime import date

# =====================
# READ SILVER
# =====================

df = pd.read_csv(
    "data/silver/steam_silver.csv",
    encoding="utf-8-sig"
)

# =====================
# CONNECTION
# =====================

engine = create_engine(
    "mssql+pyodbc://@Martin\\SQLEXPRESS/SteamAnalytics"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# =====================
# GAMES DIMENSION
# =====================

print("Loading games...")

games_df = df[
    ["appid", "name", "developer", "publisher"]
].drop_duplicates()

existing_games = pd.read_sql(
    "SELECT appid FROM games",
    engine
)

new_games = games_df[
    ~games_df["appid"].isin(existing_games["appid"])
]

if len(new_games) > 0:

    insert_games = text("""
        INSERT INTO games
        (
            appid,
            name,
            developer,
            publisher
        )
        VALUES
        (
            :appid,
            :name,
            :developer,
            :publisher
        )
    """)

    with engine.begin() as conn:
        conn.execute(
            insert_games,
            new_games.to_dict("records")
        )

print(f"Loaded {len(new_games)} new games.")

# =====================
# GAME STATS FACT
# =====================

print("Loading stats...")

stats_df = df.drop(
    columns=["name", "developer", "publisher"]
).copy()

stats_df["snapshot_date"] = date.today()

stats_df["estimated_owners"] = (
(stats_df["owners_min"] + stats_df["owners_max"]) / 2
).astype(int)

try:

    with engine.begin() as conn:

        conn.exec_driver_sql("""
            DELETE
            FROM game_stats
            WHERE snapshot_date = CAST(GETDATE() AS DATE)
        """)

        insert_stats = text("""
            INSERT INTO game_stats
            (
                appid,
                positive,
                negative,
                avg_playtime_forever,
                avg_playtime_2weeks,
                median_playtime_forever,
                median_playtime_2weeks,
                price_usd,
                initial_price_usd,
                discount,
                ccu,
                owners_min,
                owners_max,
                etl_load_date,
                positive_review_pct,
                snapshot_date,
                estimated_owners
            )
            VALUES
            (
                :appid,
                :positive,
                :negative,
                :avg_playtime_forever,
                :avg_playtime_2weeks,
                :median_playtime_forever,
                :median_playtime_2weeks,
                :price_usd,
                :initial_price_usd,
                :discount,
                :ccu,
                :owners_min,
                :owners_max,
                :etl_load_date,
                :positive_review_pct,
                :snapshot_date,
                :estimated_owners
            )
        """)

        conn.execute(
            insert_stats,
            stats_df.to_dict("records")
        )

    print(f"Loaded {len(stats_df)} game stats rows.")

except Exception as e:

    print("\n====================")
    print("GAME_STATS ERROR")
    print("====================")
    print(e)
    print("====================")

print("Load completed successfully.")

print(stats_df.columns.tolist())