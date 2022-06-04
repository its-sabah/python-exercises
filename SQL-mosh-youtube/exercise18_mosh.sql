-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- Outer Joins between multiple tables

-- write a query that shows order date, order_id, first_name, shipper, status
-- it needs to show all orders that have been processed/shipped
USE sql_store;

SELECT o.order_date, 
o.order_id, 
c.first_name,  
sh.name AS shipper, 
os.name AS status
FROM customers c
JOIN orders o
	ON c.customer_id = o.customer_id
LEFT JOIN shippers sh
	ON o.shipper_id = sh.shipper_id
JOIN order_statuses os
	ON os.order_status_id = o.status
ORDER BY o.status 