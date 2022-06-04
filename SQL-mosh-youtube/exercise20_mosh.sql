-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- Using clause


USE sql_store;
-- USING clause to simplify JOIN statements by replacing the ON condition
/*SELECT * o.order_id,
			c.first_name, 
			sh.name AS shipper
	FROM orders o
	JOIN customers c
	--	ON o.customer_id  = c.customer_id
		USING (customer_id)
	LEFT JOIN shippers sh
		USING (shipper_id) */
    
-- WE can also use the USING clause for compound JOIN statements
/* SELECT *
FROM order_items oi
JOIN order_item_notes oin
	-- ON oi.order_id = oin_order_id
    -- AND oi.product_id = oin.product_id
    USING (order_id, product_id) */
 
 -- Exercise: sql invoicing database, use the payments table 
 -- 	to create a table w date, client, amount n paymnet method
 USE sql_invoicing;
 SELECT p.date, c.name AS client, p.amount, pm.name AS payment_method
 FROM clients c
 JOIN payments p
	USING (client_id)
 JOIN payment_methods pm
	ON pm.payment_method_id = p.payment_method
