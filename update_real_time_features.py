"""
update_real_time_features.py

Real-time/daily feature update simulation for UCI Online Retail II dataset.
Handles:
- Column name inconsistencies
- Customer-level aggregations
- Rolling 7-day and 30-day sales
- Daily sales aggregation
- Output CSVs for ML pipelines
"""

import pandas as pd
from datetime import timedelta

# Load Excel dataset
file_path = "/content/online_retail_II.xlsx"  # Update path if needed
sheet_name = "Year 2010-2011"

df = pd.read_excel(file_path, sheet_name=sheet_name)

# Strip whitespace from columns
df.columns = df.columns.str.strip()

# Drop rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Compute total sales per row
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Simulate "today" as max invoice date
today = df['InvoiceDate'].max().normalize()
start_date = today - timedelta(days=90)  # Use last 90 days for rolling features
df_recent = df[df['InvoiceDate'] >= start_date]

# -----------------------------
# Customer-level aggregates
# -----------------------------
customer_agg = df_recent.groupby('CustomerID').agg(
    total_orders=pd.NamedAgg(column='InvoiceNo', aggfunc=pd.Series.nunique),
    total_spent=pd.NamedAgg(column='TotalSales', aggfunc='sum'),
    avg_order_value=pd.NamedAgg(column='TotalSales', aggfunc='mean')
).reset_index()

# -----------------------------
# Daily sales per customer
# -----------------------------
daily_sales = df_recent.groupby(['CustomerID', df_recent['InvoiceDate'].dt.date])[['TotalSales']].sum()
daily_sales = daily_sales.rename(columns={'TotalSales':'daily_sales'}).reset_index()

# -----------------------------
# Rolling features
# -----------------------------
df_recent = df_recent.sort_values(['CustomerID', 'InvoiceDate'])
df_recent['rolling_7d_sales'] = df_recent.groupby('CustomerID')['TotalSales'].apply(
    lambda x: x.rolling('7d', on=df_recent['InvoiceDate']).sum()
)
df_recent['rolling_30d_sales'] = df_recent.groupby('CustomerID')['TotalSales'].apply(
    lambda x: x.rolling('30d', on=df_recent['InvoiceDate']).sum()
)

# -----------------------------
# Save updated features
# -----------------------------
customer_agg.to_csv("customer_agg_latest.csv", index=False)
daily_sales.to_csv("daily_sales_latest.csv", index=False)
df_recent[['CustomerID','InvoiceDate','rolling_7d_sales','rolling_30d_sales']].to_csv(
    "customer_rolling_latest.csv", index=False
)

print("Real-time features updated successfully!")
print("Saved files:")
print(" - customer_agg_latest.csv")
print(" - daily_sales_latest.csv")
print(" - customer_rolling_latest.csv")
