import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="safertek"
)

# Create a cursor object
cursor = conn.cursor()

# Creating tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
  CustomerID INT NOT NULL,
  FirstName VARCHAR(45) NULL,
  LastName VARCHAR(45) NULL,
  Email VARCHAR(45) NULL,
  DateOfBirth DATE NULL,
  PRIMARY KEY (CustomerID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
  ProductID INT NOT NULL,
  ProductName VARCHAR(45) NULL,
  Price INT NULL,
  PRIMARY KEY (ProductID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
  OrderID INT NOT NULL,
  CustomerID INT NULL,
  OrderDate DATE NULL,
  PRIMARY KEY (OrderID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orderitems (
  OrderItemID INT NOT NULL,
  OrderID INT NULL,
  ProductID INT NULL,
  Quantity INT NULL,
  PRIMARY KEY (OrderItemID)
);
""")

# Inserting data into tables
customer_data = [
    (1, 'John', 'Doe', 'john.doe@example.com', '1985-01-15'),
    (2, 'Jane', 'Smith', 'jane.smith@example.com', '1990-06-20')
]

cursor.executemany("""
INSERT INTO customers (CustomerID, FirstName, LastName, Email, DateOfBirth) 
VALUES (%s, %s, %s, %s, %s)
""", customer_data)

product_data = [
    (1, 'Laptop', 1000),
    (2, 'Smartphone', 600),
    (3, 'Headphones', 100)
]

cursor.executemany("""
INSERT INTO products (ProductID, ProductName, Price) 
VALUES (%s, %s, %s)
""", product_data)

order_data = [
    (1, 1, '2023-01-10'),
    (2, 2, '2023-01-12')
]

cursor.executemany("""
INSERT INTO orders (OrderID, CustomerID, OrderDate) 
VALUES (%s, %s, %s)
""", order_data)

order_item_data = [
    (1, 1, 1, 1),
    (2, 1, 3, 2),
    (3, 2, 2, 1),
    (4, 2, 3, 1)
]

cursor.executemany("""
INSERT INTO orderitems (OrderItemID, OrderID, ProductID, Quantity) 
VALUES (%s, %s, %s, %s)
""", order_item_data)

# Commit and close connection
conn.commit()
conn.close()
