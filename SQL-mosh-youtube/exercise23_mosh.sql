-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- inserting a single & multiple rows

USE sql_store;
 -- writing out each value for each column
/*INSERT INTO customers
VALUES (DEFAULT, 
'John', 'Smith', 
'1990-01-01',  NULL, 'address', 'city', 'CA', DEFAULT);*/

-- specifying which columns to fill (multiple rows)
/*INSERT INTO customers (first_name, last_name,
			birth_date, address, city, state)
VALUES ('John', 'Smith', '1990-01-01', 
		'address', 'city', 'CA'),
        ('Mary', 'Jane', '1990-01-01', 
		'address', 'city', 'CA');*/
        
-- exercise: insert 3 rows in products table
INSERT INTO products (name, quantity_in_stock, unit_price)
VALUES ('apple', 10, 0.1),
		('banana', 5, 0.35),
        ('orange', 19, 0.45);