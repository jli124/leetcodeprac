# 183. Customers Who Never Order
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

/* Sub query and left Join */

#-------------------------------------------------------------------------------
#    Soluton1
#-------------------------------------------------------------------------------
SELECT Name Customer
FROM Customers
WHERE Id NOT IN (
	SELECT Id 
	FROM orders)
;


#-------------------------------------------------------------------------------
#    Soluton2
#-------------------------------------------------------------------------------

/* Write your MySQL query statement below */
select name as Customers
from Customers c
left join Orders o
on c.Id = o.CustomerID
where o.CustomerId is NULL;