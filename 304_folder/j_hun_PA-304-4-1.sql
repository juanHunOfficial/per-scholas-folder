-- number 1
-- Display the name, product line, and buy price of all products. The output columns 
-- should display as: “Name,” “Product Line,” and “Buy Price.” The output should display
-- the most expensive items first. 
select productName as Name, productLine as "Product Line", buyPrice as "Buy Price"
from products
order by buyPrice desc;

-- number 2
-- Display the first name, last name, and city name of all customers from Germany. 
-- The output columns should display as: “First Name,” “Last Name,” and “City.” The output 
-- should be sorted by “Last Name” (ascending).
select contactFirstName as "First Name", contactLastName as "Last Name", city as "City"
from customers
where country = "Germany"
order by contactLastName;

-- number 3
-- Display each of the unique values of the status field in the orders table. The output 
-- should be sorted alphabetically, ascending.
-- Hint: The output should show exactly six rows.
select distinct(status)
from orders
order by status;

-- number 4
-- Display all fields from the payments table for payments made on or after January 1, 2005. 
-- The output should be sorted by the payment date from highest to lowest.
select *
from payments
where paymentDate >= '2005-01-01'
order by paymentDate desc;

-- number 5
-- Display the last Name, first Name, email address, and job title of all employees working 
-- out of the San Francisco office. The output should be sorted by “Last Name.”
select lastName as "Last Name", firstName as "First Name", email as "Email Address", jobTitle as "Job Title"
from employees
where officeCode = 1
order by lastName;
-- to figure out which was the right office code.
select distinct(city),officeCode
from offices;

-- number 6
-- Display the name, product line, scale, and vendor of all of the car products – both 
-- classic and vintage. The output should display all vintage cars first (sorted 
-- alphabetically by name), and all classic cars last (also sorted alphabetically by name). 
select productName as "Name", productLine as "Product Line", productScale as "Product Scale", productVendor as "Vendor"
from products
where productLine = "Classic Cars" or productLine = "Vintage Cars"
order by productLine desc, productName;

 


