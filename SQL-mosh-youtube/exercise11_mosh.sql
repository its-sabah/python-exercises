-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- LIMIT Clause
USE sql_store; 

SELECT *
FROM orders
INNER JOIN customers 
	ON orders.customer_id = customer.customer_id