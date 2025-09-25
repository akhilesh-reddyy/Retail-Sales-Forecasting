import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load features
X_new = pd.read_csv("data/new_sales_features.csv")

# Load trained model
model = joblib.load("models/rf_sales_model.pkl")

# Make predictions
predictions = model.predict(X_new)
X_new["predicted_sales"] = predictions
X_new.to_csv("data/sales_predictions.csv", index=False)
print("Predictions saved to data/sales_predictions.csv")
