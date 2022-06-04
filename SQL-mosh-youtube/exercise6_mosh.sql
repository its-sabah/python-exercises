-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- LIKE operator

-- Get the customers whose
-- 	addresses contain TRAIL or AVENUE
--   phone numbers end with 9
USE sql_store;
SELECT last_name, address, phone
FROM customers
WHERE address LIKE '%Trail%' OR address LIKE '%avenue%'
-- WHERE phone LIKE '%9'

