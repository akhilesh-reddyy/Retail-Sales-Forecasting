import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("data/online_retail_II.csv")
df = df.dropna(subset=['CustomerID'])
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Feature Engineering
daily_sales = df.groupby(['CustomerID', df['InvoiceDate'].dt.date])['Quantity', 'UnitPrice'].sum()
daily_sales['total_sales'] = daily_sales['Quantity'] * daily_sales['UnitPrice']
daily_sales = daily_sales.reset_index()
daily_sales['rolling_7d'] = daily_sales.groupby('CustomerID')['total_sales'].transform(lambda x: x.rolling(7,1).sum())

X = daily_sales[['Quantity','UnitPrice','rolling_7d']]
y = daily_sales['total_sales']

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X, y)

# Save model
joblib.dump(rf, 'scripts/sales_model.pkl')
