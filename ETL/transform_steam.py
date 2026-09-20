import pandas as pd
from datetime import date

# =====================
# READ RAW
# =====================

df = pd.read_csv(
    "data/raw/steam_raw.csv",
    encoding="utf-8-sig"
)

df["etl_load_date"] = date.today()

# =====================
# OWNERS
# =====================

owners_split = (
    df["owners"]
    .str.replace(",", "", regex=False)
    .str.split(" .. ")
)

df["owners_min"] = owners_split.str[0].astype(int)
df["owners_max"] = owners_split.str[1].astype(int)

# TO POTRZEBNE DLA game_stats
df["estimated_owners"] = (
    (df["owners_min"] + df["owners_max"]) / 2
).astype(int)

df.drop(columns=["owners"], inplace=True)

# =====================
# PRICE
# =====================

df["price"] = pd.to_numeric(df["price"]) / 100
df["initialprice"] = pd.to_numeric(df["initialprice"]) / 100

# =====================
# DISCOUNT
# =====================

df["discount"] = pd.to_numeric(df["discount"])

# =====================
# REVIEW %
# =====================

df["rating_pct"] = (
    df["positive"] /
    (df["positive"] + df["negative"])
    * 100
).round(2)

df["rating_pct"] = df["rating_pct"].fillna(0)

# =====================
# DROP UNUSED
# =====================

df.drop(columns=["score_rank"], inplace=True)
df.drop(columns=["userscore"], inplace=True)

# =====================
# DEDUPLICATION
# =====================

print(f"Rows before deduplication: {len(df)}")

df.drop_duplicates(
    subset=["appid"],
    keep="first",
    inplace=True
)

# =====================
# FILL NULLS
# =====================

df["developer"] = df["developer"].fillna("Unknown")
df["publisher"] = df["publisher"].fillna("Unknown")

# =====================
# RENAME
# =====================

df.rename(
    columns={
        "price": "price_usd",
        "initialprice": "initial_price_usd",
        "average_forever": "avg_playtime_forever",
        "average_2weeks": "avg_playtime_2weeks",
        "median_forever": "median_playtime_forever",
        "median_2weeks": "median_playtime_2weeks",
        "rating_pct": "positive_review_pct"
    },
    inplace=True
)

# =====================
# TEST UNICODE
# =====================

test = df[df["appid"] == 1468810]

print("\n========== TEST ==========")
print(test[["appid", "name"]])
print("==========================")

# =====================
# SAVE SILVER
# =====================

df.to_csv(
    "data/silver/steam_silver.csv",
    index=False,
    encoding="utf-8-sig"
)

print(f"Rows after deduplication: {len(df)}")
print(df.columns.tolist())