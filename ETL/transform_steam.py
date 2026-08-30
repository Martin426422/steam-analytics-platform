import pandas as pd

df = pd.read_csv("data/raw/steam_raw.csv")

# owners split
owners_split = df["owners"].str.replace(",", "").str.split(" .. ")

df["owners_min"] = owners_split.str[0].astype(int)
df["owners_max"] = owners_split.str[1].astype(int)

# drop source column
df.drop(columns=["owners"], inplace=True)

# price
df["price"] = pd.to_numeric(df["price"]) / 100
df["initialprice"] = pd.to_numeric(df["initialprice"]) / 100

# discount
df["discount"] = pd.to_numeric(df["discount"])

# rating_pct
df["rating_pct"]=(
    df["positive"] / (df["positive"] + df["negative"])* 100
    ).round(2)

df["rating_pct"] = (df["rating_pct"].fillna(0))

# score_rank_drop
df.drop(columns=["score_rank"], inplace=True)

# userscore_drop
df.drop(columns=["userscore"], inplace=True)

print(f"Rows before deduplication: {len(df)}")

df.drop_duplicates(
    subset=["appid"],
    keep="first",
    inplace=True
)

df["developer"] = df["developer"].fillna("Unknown")
df["publisher"] = df["publisher"].fillna("Unknown")

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

# save silver data
df.to_csv("data/silver/steam_silver.csv",index=False)

print(df.head())
print(df.dtypes)
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
print(f"Duplicate AppIDs: {df.duplicated(subset=['appid']).sum()}")
print(f"Rows after deduplication: {len(df)}")
print(df.describe())
print(df.columns.tolist())