import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="safertek"
)
cursor = conn.cursor()
cursor.execute("""with data1 as (select p.ProductID,p.ProductName,sum(ot.Quantity) as numberoforders from 
 orderitems ot join
 products p  on p.ProductID = ot.ProductID
 group by p.ProductID,p.ProductName)
 select * from data1 where numberoforders = (select max(numberoforders) from data1);
""")
customers = cursor.fetchall()

for customer in customers:
    print(customer)

conn.close()
