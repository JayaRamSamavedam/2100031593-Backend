import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="safertek"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM customers")
customers = cursor.fetchall()

for customer in customers:
    print(customer)

conn.close()
