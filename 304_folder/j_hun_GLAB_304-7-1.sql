-- connected succesfully
SELECT  * FROM  departments WHERE  location_id = 1700;

-- 
SELECT  employee_id, first_name, last_name, department_id
FROM   employees
WHERE  department_id IN (1, 3, 9, 10, 11)
ORDER BY first_name, last_name;

-- 
SELECT   employee_id, first_name, last_name, department_id
FROM employees
WHERE department_id IN (SELECT department_id
        FROM      departments
        WHERE location_id = 1700)
ORDER BY first_name, last_name;

-- 
SELECT employee_id, first_name, last_name
FROM  employees
WHERE  department_id NOT IN (SELECT department_id
        FROM   departments
        WHERE location_id = 1700)
ORDER BY first_name , last_name;

--
SELECT employee_id, first_name, last_name, salary
FROM   employees
WHERE salary = (SELECT MAX(salary) FROM  employees)
ORDER BY first_name, last_name;

--
SELECT employee_id, first_name, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary)FROM employees);

-- 
SELECT department_name
FROM departments d
WHERE EXISTS ( SELECT * FROM employees e 
	WHERE salary > 10000 AND e.department_id = d.department_id)
ORDER BY department_name; 

-- 
SELECT department_name
FROM departments d
WHERE NOT EXISTS ( SELECT * FROM employees e
        WHERE salary > 10000 AND e.department_id = d.department_id) ORDER BY department_name; 

-- This is where the queries for the classic models begin. These have been consolidated for assignment turn in. 
SELECT productCode, ROUND(SUM(quantityOrdered * priceEach)) AS sales
FROM orderdetails
	INNER JOIN orders USING (orderNumber)
WHERE YEAR(shippedDate) = 2003
GROUP BY productCode
ORDER BY sales DESC
LIMIT 5;

-- 
SELECT productName, sales
FROM  (SELECT productCode, ROUND(SUM(quantityOrdered * priceEach)) AS sales
    FROM orderdetails  INNER JOIN orders USING (orderNumber)
    WHERE YEAR(shippedDate) = 2003
    GROUP BY productCode
    ORDER BY sales DESC
    LIMIT 5) as top5products2003
INNER JOIN products USING (productCode);