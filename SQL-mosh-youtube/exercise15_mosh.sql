-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- JOINING MULTIPLE TABLES  Clause

-- join payments to client id and payment method from the sql_invoicing data base
-- client name, invoice id, date, amount, payment method

USE sql_invoicing;

SELECT  p.date,
		c.name, 		
        p.amount,
        pm.name AS payment_method
FROM payments p
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id
JOIN clients c
	ON c.client_id = p.client_id