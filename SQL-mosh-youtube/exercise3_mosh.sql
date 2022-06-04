-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- AND OR NOT operators

-- From the order_items table, get the items
	-- for order #6
    -- where the total price is greater than 30
    
USE sql_store;
SELECT *, (unit_price*quantity) AS total_price
FROM order_items
WHERE order_id = 6 AND (unit_price*quantity)>30