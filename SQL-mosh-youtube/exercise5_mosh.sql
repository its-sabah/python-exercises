-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- BETWEEN operator

-- Return customers born between
--	 1/1/1990 and 1/1/2000
USE sql_store; 
SELECT customer_id, first_name, last_name, birth_date
FROM customers
WHERE birth_date BETWEEN '1990-01-01' AND '2000-01-01'