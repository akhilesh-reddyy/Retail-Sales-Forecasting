"""
update_real_time_features.py

This script simulates updating real-time/rolling features for
customers in the Online Retail II dataset. Intended for daily
or streaming feature updates for forecasting models.
"""

import pandas as pd
from datetime import datetime, timedelta

# Load dataset
df = pd.read_csv("data/online_retail_II.csv")
df = df.dropna(subset=['CustomerID'])
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Simulate "today" as max invoice date in dataset
today = df['InvoiceDate'].max().normalize()

# Filter last 90 days of transactions for performance
start_date = today - timedelta(days=90)
df_recent = df[df['InvoiceDate'] >= start_date]

# Feature engineering: customer-level aggregates
customer_agg = df_recent.groupby('CustomerID').agg(
    total_orders=pd.NamedAgg(column='InvoiceNo', aggfunc=pd.Series.nunique),
    total_spent=pd.NamedAgg(column='UnitPrice', aggfunc=lambda x: (x*df_recent.loc[x.index,'Quantity']).sum()),
    avg_order_value=pd.NamedAgg(column='UnitPrice', aggfunc=lambda x: (x*df_recent.loc[x.index,'Quantity']).mean())
).reset_index()

# Rolling features: last 7, 30 days per customer
df_recent = df_recent.sort_values(['CustomerID', 'InvoiceDate'])

df_recent['rolling_7d_sales'] = df_recent.groupby('CustomerID')['Quantity','UnitPrice'].apply(
    lambda x: (x['Quantity'] * x['UnitPrice']).rolling(7, min_periods=1).sum()
).reset_index(level=0, drop=True)

df_recent['rolling_30d_sales'] = df_recent.groupby('CustomerID')['Quantity','UnitPrice'].apply(
    lambda x: (x['Quantity'] * x['UnitPrice']).rolling(30, min_periods=1).sum()
).reset_index(level=0, drop=True)

# Save updated features
customer_agg.to_csv("data/customer_agg_latest.csv", index=False)
df_recent[['CustomerID','InvoiceDate','rolling_7d_sales','rolling_30d_sales']].to_csv(
    "data/customer_rolling_latest.csv", index=False
)

print("Real-time features updated successfully!")
print("Saved files:")
print(" - data/customer_agg_latest.csv")
print(" - data/customer_rolling_latest.csv")
