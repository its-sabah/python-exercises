-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- WHERE clause 

-- Get Orders placed this year (2019)
USE sql_store;
SELECT order_id, customer_id, order_date
FROM orders
WHERE order_date >= '2019-01-01'