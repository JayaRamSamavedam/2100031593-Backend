import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="safertek"
)
cursor = conn.cursor()
cursor.execute("""SELECT DATE_FORMAT(OrderDate, '%Y-%m') AS OrderMonth,
         DATE_FORMAT(OrderDate, '%M') AS MonthName,
         COUNT(*) AS TotalOrders,
         SUM(Products.Price * OrderItems.Quantity) AS TotalSales
 FROM Orders
 JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
 JOIN Products ON OrderItems.ProductID = Products.ProductID
 WHERE YEAR(OrderDate)=2023
 GROUP BY DATE_FORMAT(OrderDate, '%Y-%m'), DATE_FORMAT(OrderDate, '%M')
 ORDER BY OrderMonth;

""")
customers = cursor.fetchall()

for customer in customers:
    print(customer)

conn.close()
