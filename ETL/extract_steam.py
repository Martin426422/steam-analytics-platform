import requests
import pandas as pd

all_games = []

for page in range(5):
    url = f"https://steamspy.com/api.php?request=all&page={page}"

    data = requests.get(url).json()

    df = pd.DataFrame.from_dict(data, orient="index")

    all_games.append(df)

final_df = pd.concat(all_games, ignore_index=True)

print(final_df.shape)

final_df.to_csv("data/raw/steam_raw.csv", index=False)

print(final_df.columns)
print(final_df.head())
print(final_df.dtypes)