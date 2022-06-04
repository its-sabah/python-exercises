-- SQL W MOSH https://youtu.be/7S_tz1z_5bA?t=2215
-- Self Outer Join

-- write a query that shows *all* the employees and who they report too
USE sql_hr;

SELECT e.employee_id,
		e.first_name,
        m.first_name AS manager
FROM employees e
LEFT JOIN employees m
	ON e.reports_to = m.employee_id