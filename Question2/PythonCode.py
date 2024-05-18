import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="safertek"
)
cursor = conn.cursor()
cursor.execute("""SELECT * FROM Orders
WHERE OrderDate BETWEEN '2023-01-01' AND '2023-01-31';""")
customers = cursor.fetchall()

for customer in customers:
    print(customer)

conn.close()
