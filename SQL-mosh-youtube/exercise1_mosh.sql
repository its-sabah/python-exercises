-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- SELECT clause 

-- Return all the products
 -- name
 -- unit price
 -- new price (unit price * 1.1)
 
 USE sql_store;
 
 SELECT name, unit_price, unit_price*1.1 AS new_price
 FROM products