SELECT OrderItems.OrderID,ProductName,OrderItems.Quantity,
(Price*OrderItems.Quantity) as OrderPrice
FROM OrderItems
JOIN Products ON OrderItems.ProductID = Products.ProductID
ORDER BY OrderItems.OrderID ASC;
