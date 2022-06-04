-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- REGEXP operator

-- Get the customers whose
	-- first names are elka or ambur
    -- last names  end with ey or on
    -- last names start with my or contains se
    -- last names contain b followed by r or u

USE sql_store;
SELECT first_name, last_name
FROM customers
WHERE
	 first_name REGEXP 'ELKA|AMBUR'
	-- last_name REGEXP 'ey$|on%'
    -- last_name REGEXP '^my|se'
    -- last_name REGEXP 'b[ru]'