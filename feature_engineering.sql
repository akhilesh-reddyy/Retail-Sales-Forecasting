-- Total sales per invoice
CREATE VIEW invoice_sales AS
SELECT 
    InvoiceNo,
    SUM(Quantity * UnitPrice) AS total_sales
FROM online_retail
GROUP BY InvoiceNo;

-- Customer-level aggregation
CREATE VIEW customer_agg AS
SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS total_orders,
    SUM(Quantity * UnitPrice) AS total_spent,
    AVG(Quantity * UnitPrice) AS avg_order_value
FROM online_retail
GROUP BY CustomerID;

-- Rolling features: last 30 days spending per customer
CREATE VIEW customer_rolling AS
SELECT
    CustomerID,
    InvoiceDate,
    SUM(Quantity * UnitPrice) OVER (
        PARTITION BY CustomerID
        ORDER BY InvoiceDate
        ROWS BETWEEN 29 PRECEDING AND CURRENT ROW
    ) AS rolling_30day_sales
FROM online_retail;
