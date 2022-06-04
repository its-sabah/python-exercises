-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- UNIONS

USE sql_store;

/*SELECT 'Apples' AS fruits
UNION
SELECT 'bana' AS cars */

-- exercise: write a query to produce a report 
-- 	with customer_id, first_name, points, type
-- 	where: points <2000 is bronze, 2000<points<3000 silver, 
-- 	points >3000 gold, sorted by first_name

SELECT customer_id, first_name, points, 'Bronze' AS type
FROM customers 
WHERE points < 2000
UNION
SELECT customer_id, first_name, points, 'Silver' AS type
FROM customers 
WHERE (points >= 2000 )
	AND (points < 3000)
UNION 
SELECT customer_id, first_name, points, 'Gold' AS type
FROM customers 
WHERE points > 3000
ORDER BY first_name