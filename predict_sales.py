import pandas as pd
import joblib

model = joblib.load('scripts/sales_model.pkl')

# Predict on new data
new_data = pd.read_csv("data/online_retail_II.csv")
# (apply same preprocessing as train)
# ...
predictions = model.predict(new_data[['Quantity','UnitPrice','rolling_7d']])
