import pandas as pd
from sqlalchemy import create_engine
from datetime import date

# Read silver layer
df = pd.read_csv("data/silver/steam_silver.csv")

# Connection
engine = create_engine(
    "mssql+pyodbc://Martin\\SQLEXPRESS/SteamAnalytics"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# =====================
# GAMES
# =====================

print("Loading games...")

games_df = df[
    ["appid", "name", "developer", "publisher"]
].drop_duplicates()

games_df.to_sql(
    "games",
    engine,
    if_exists="append",
    index=False
)

print("Games loaded.")

# =====================
# GAME_STATS
# =====================

print("Loading stats...")

stats_df = df.drop(
    columns=["name", "developer", "publisher"]
).copy()

stats_df["snapshot_date"] = date.today()

stats_df.to_sql(
    "game_stats",
    engine,
    if_exists="append",
    index=False
)

print("Stats loaded.")

print(f"Loaded {len(games_df)} games")
print(f"Loaded {len(stats_df)} game stats rows")