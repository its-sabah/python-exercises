-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- IN operator

-- RETURN products with
-- 	quantitiy in stock equal to 49, 38, 72

USE sql_store;
SELECT *
FROM products
WHERE quantity_in_stock IN (49, 38, 72)