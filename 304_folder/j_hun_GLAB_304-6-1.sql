--
select c.customerName as 'Customer Name', concat(e.lastName, ', ', e.firstName) as 'Sales Rep'
from customers c JOIN employees e 
on c.salesRepEmployeeNumber = e.employeeNumber
order by c.customerName asc;

--
select p.productName as 'Product Name', sum(od.quantityOrdered) as 'Total # Ordered', sum(od.quantityOrdered * od.priceEach) as 'Total Sale'
from products p LEFT JOIN orderdetails od 
on p.productCode=od.productCode
group by p.productName, p.buyPrice
order by 3 desc;

--
SELECT 
    status AS 'Order Status', COUNT(status) AS 'Total Orders'
FROM
    orders
GROUP BY status
ORDER BY status;

--
select 
     pl.productLine as 'Product Line', 
     count(od.productCode) as 'total Sold'
from productLines pl join products p 
on pl.productLine=p.productLine
 JOIN orderdetails od on p.productCode=od.productCode
group by pl.productLine -- group by is dictating how the data is being grouped before it is counted. 
order by 2 desc;

--
select 
   monthname(paymentDate) AS Month, 
   year(paymentDate) AS Year,
   format(sum(amount), 2) AS 'Payments Received'
from payments
group by year(paymentDate), monthname(paymentDate) 
order by paymentDate;

--
SELECT p.productName Name, p.productLine AS `Product Line`, p.productScale AS `Scale`, p.productVendor AS `Vendor` FROM productlines l NATURAL JOIN products p 
WHERE l.productLine = "Classic Cars" OR l.productLine = "Vintage Cars"
ORDER BY p.productLine DESC, p.productName ASC;

