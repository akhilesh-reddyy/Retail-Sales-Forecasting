-- Aggregate total weekly sales per store
CREATE VIEW store_weekly_sales AS
SELECT 
    store_id,
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(WEEK FROM date) AS week,
    SUM(weekly_sales) AS total_weekly_sales
FROM sales
GROUP BY store_id, year, week;

-- Rolling 4-week average per store
CREATE VIEW store_rolling_avg AS
SELECT 
    store_id,
    week,
    year,
    AVG(total_weekly_sales) OVER (
        PARTITION BY store_id 
        ORDER BY year, week 
        ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
    ) AS rolling_4_week_avg
FROM store_weekly_sales;
