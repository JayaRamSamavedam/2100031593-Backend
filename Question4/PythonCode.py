import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="safertek"
)
cursor = conn.cursor()
cursor.execute("""SELECT OrderItems.OrderID,ProductName,OrderItems.Quantity,
(Price*OrderItems.Quantity) as OrderPrice
FROM OrderItems
JOIN Products ON OrderItems.ProductID = Products.ProductID
ORDER BY OrderItems.OrderID ASC;""")
customers = cursor.fetchall()

for customer in customers:
    print(customer)

conn.close()
