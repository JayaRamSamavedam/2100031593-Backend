select o.OrderID,c.CustomerID,o.OrderDate,c.FirstName,c.LastName,c.Email
from orders o
join customers c on o.CustomerID = c.CustomerID;