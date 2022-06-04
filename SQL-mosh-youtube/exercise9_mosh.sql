-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- ORDER BY clause
USE sql_store; 

SELECT *, (quantity*unit_price) AS total_price
FROM order_items
WHERE order_id = 2
ORDER BY total_price DESC

