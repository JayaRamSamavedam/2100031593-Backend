import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="safertek"
)
cursor = conn.cursor()
cursor.execute("""select o.OrderID,c.CustomerID,o.OrderDate,c.FirstName,c.LastName,c.Email 
from orders o 
join customers c on o.CustomerID = c.CustomerID;""")
customers = cursor.fetchall()

for customer in customers:
    print(customer)

conn.close()
