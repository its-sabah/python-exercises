-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- INNER JOIN Clause

USE sql_store;
SELECT oi.order_id, p.product_id, oi.quantity, oi.unit_price
FROM order_items oi
JOIN products p
	ON oi.product_id = p.product_id
ORDER BY oi.order_id