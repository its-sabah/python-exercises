-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- IS NULL operator

 -- get the orders that are not shipped
 
 USE sql_store;
 SELECT order_id, order_date, status, shipped_date, shipper_id
 FROM orders
 WHERE shipped_date IS NULL