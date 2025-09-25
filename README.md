# Retail Sales Forecasting Project

## Project Overview
This project predicts future retail store sales using SQL for feature engineering and Python-based ML models for time-series forecasting. It integrates database-level aggregations with machine learning pipelines to generate actionable business insights.

### Skills Demonstrated
- Advanced SQL for rolling, lag, and aggregate features.
- Time-series forecasting with Python (Prophet, ARIMA, or RandomForestRegressor).
- Visualization of predictions and errors.
- Optional: End-to-end deployment with real-time updates.

## Problem Statement
Retail chains need accurate sales forecasts to optimize inventory, staffing, and promotions. This project addresses:
- Sales prediction per store/product.
- Capturing seasonality, promotions, and holidays.
- Providing interpretable insights for business decision-making.

## Dataset
Source: [Kaggle - Walmart Sales Forecasting](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting/data)  
Features:
- Store ID, Product ID
- Date of sale
- Weekly sales
- Promotions and holiday indicators

## SQL Feature Engineering
- Total weekly/monthly sales per store/product.
- Rolling average of last 4 and 12 weeks.
- Lag features for previous week/month sales.
- Flags for holidays, promotions, and seasonality.

## Machine Learning Pipeline
Models: ARIMA, Prophet, or RandomForestRegressor (for feature-based regression).  

Workflow:
1. Load feature data from SQL into Python.
2. Merge and clean feature tables.
3. Split data into train/test sets.
4. Train time-series/ML model.
5. Evaluate using RMSE, MAE, MAPE.
6. Visualize forecasts vs actual sales.
7. Optional: Interpret features with SHAP for tree-based models.

## Visualizations
- Forecast vs actual line plots
- Heatmap of prediction errors by store/product
- Feature importance for ML models
