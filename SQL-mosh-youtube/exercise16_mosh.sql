-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- Implict Join Syntax

USE SQL_store;

SELECT *
FROM orders o
JOIN customers c
	ON  o.customer_id = c.customer_id;
    
    
 -- Implicit Join Syntax (equivalent to the statement above)
SELECT *
FROM orders o, customers c
WHERE o.customer_id = c.customer_id

