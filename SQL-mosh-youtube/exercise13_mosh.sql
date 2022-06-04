-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- JOIN ACCROSS DATABASE Clause
USE sql_inventory;

SELECT *
FROM sql_store.order_items oi
JOIN products p
	ON oi.product_id = p.product_id
