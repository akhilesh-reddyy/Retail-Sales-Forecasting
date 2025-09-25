DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    store_id INT,
    product_id INT,
    date DATE,
    weekly_sales FLOAT,
    is_holiday BOOLEAN,
    promotion BOOLEAN
);
