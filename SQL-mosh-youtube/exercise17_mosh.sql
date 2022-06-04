-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- OUTER Join Syntax

-- write a query that brings product_id and quanitity and name, 
-- joining the products table and order items table -  
-- including products that have neevr been ordered 

USE sql_store;

SELECT p.product_id, p.name, o.order_id
FROM products p 
LEFT JOIN order_items o
	 ON o.product_id = p.product_id




