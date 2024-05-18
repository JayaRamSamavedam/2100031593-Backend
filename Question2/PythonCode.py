import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="safertek"
)
cursor = conn.cursor()
cursor.execute("""SELECT * FROM Orders
WHERE MONTH(OrderDate)=1 AND YEAR(OrderDate)=2023;""")
customers = cursor.fetchall()

for customer in customers:
    print(customer)

conn.close()
