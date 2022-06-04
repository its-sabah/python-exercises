-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- CROSS JOINs

USE sql_store;

-- explicit syntax
/*SELECT c.first_name AS name, p.name AS product
FROM customers c
CROSS JOIN products p
ORDER BY c.first_name */

-- implicit syntac
/* SELECT c.first_name AS name, p.name AS product
FROM customers c, products p
ORDER BY c.first_name */

-- exercise: do a cross join between shippers and products
	-- explicitly
    /* SELECT s.name AS shipper, p.name AS product
    FROM shippers s
    CROSS JOIN products p
    ORDER BY s.name */
    
    -- implicitly
    /* SELECT s.name AS shipper, p.name AS product
    FROM shippers s, products p
    ORDER BY s.name */