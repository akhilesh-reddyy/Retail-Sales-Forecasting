import pandas as pd

# Load latest sales
latest = pd.read_csv("data/latest_sales.csv")
# Update rolling averages
rolling_avg = latest.groupby("store_id")["weekly_sales"].rolling(4).mean().reset_index()
rolling_avg.rename(columns={"weekly_sales": "rolling_4_week_avg"}, inplace=True)

# Merge back and save
latest = latest.merge(rolling_avg, on=["store_id", "level_1"])
latest.to_csv("data/updated_features.csv", index=False)
print("Updated features saved.")
