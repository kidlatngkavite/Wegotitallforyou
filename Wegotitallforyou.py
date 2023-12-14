import sqlite3
from datetime import datetime

conn = sqlite3.connect("Wegotitallforyou.db")
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = 1")
sql = ""
values = []
value = ()

#Strings to create each table
createSalesRepTableQuery = """CREATE TABLE IF NOT EXISTS [salesrep] (
  [id] integer PRIMARY KEY AUTOINCREMENT,
  [last_name] nvarchar(255),
  [first_name] nvarchar(255),
  [middle_name] nvarchar(255)
  )"""

createCustomerTableQuery = """CREATE TABLE IF NOT EXISTS [customer] (
  [id] integer PRIMARY KEY AUTOINCREMENT,
  [last_name] nvarchar(255),
  [first_name] nvarchar(255),
  [middle_name] nvarchar(255)
  )"""

createProductTableQuery = """CREATE TABLE IF NOT EXISTS [product] (
  [id] integer PRIMARY KEY AUTOINCREMENT,
  [product_name] nvarchar(255),
  [cost] float,
  [selling] float,
  [vendor_id] integer,
  FOREIGN KEY(vendor_id) REFERENCES vendor(id)
  )"""

createVendorTableQuery = """CREATE TABLE IF NOT EXISTS [vendor] (
  [id] integer PRIMARY KEY AUTOINCREMENT,
  [vendor_name] nvarchar(255)
  )"""

createInvoiceTableQuery = """CREATE TABLE IF NOT EXISTS [invoice] (
  [id] integer PRIMARY KEY AUTOINCREMENT,
  [datetime_created] datetime,
  [customer_id] integer,
  [salesrep_id] integer,
  FOREIGN KEY(customer_id) REFERENCES customer(id),
  FOREIGN KEY(salesrep_id) REFERENCES salesrep(id)
  )"""

createOrderListTableQuery = """CREATE TABLE IF NOT EXISTS [orderlist] (
  [invoice_id] integer,
  [quantity] integer,
  [product_id] integer,
  FOREIGN KEY(invoice_id) REFERENCES invoice(id),
  FOREIGN KEY(product_id) REFERENCES product(id)
  )"""

#Create Tables
cursor.execute(createSalesRepTableQuery)
cursor.execute(createCustomerTableQuery)
cursor.execute(createProductTableQuery)
cursor.execute(createVendorTableQuery)
cursor.execute(createInvoiceTableQuery)
cursor.execute(createOrderListTableQuery)

#Insert Sample Data to Employee Table
sql = "INSERT INTO salesrep (last_name, first_name, middle_name) \
  values (:values(0), :values(1), :values(2))"
values = [
  ("salesrepEscolar", "Ferdinand", "Camba"),
  ("salesrepDanganan", "Duvall", "Q"),
  ("salesrepBonggal", "Arvin", "W"),
  ("salesrepLoma", "Mark", "Y"),
  ("salesrepLeonardo", "Rico", "M"),
  ("salesrepBernardo", "Kathryn", "A"),
  ("salesrepPadilla", "Daniel", "J"),
  ("salesrepDiaz", "Ogie", "M")
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Salesrep Table: {cursor.rowcount} records inserted")
conn.commit()

#Insert Sample Data to customer Table
sql = "INSERT INTO customer (last_name, first_name, middle_name) \
  values (:values(0), :values(1), :values(2))"
values = [
  ("customerEscolar", "Ferdinand", "Camba"),
  ("customerDanganan", "Duvall", "Q"),
  ("customerBonggal", "Arvin", "W"),
  ("customerLoma", "Mark", "Y"),
  ("customerLeonardo", "Rico", "M"),
  ("customerBernardo", "Kathryn", "A"),
  ("customerPadilla", "Daniel", "J"),
  ("customerDiaz", "Ogie", "M")
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Customer Table: {cursor.rowcount} records inserted")
conn.commit()

#Insert Sample Data to Vendor Table
sql = "INSERT INTO vendor (vendor_name) values (:values(0))"
values = [
  ("Ace Hardware",),
  ("Handyman",),
  ("Tolsen",),
  ("Makita",),
  ("Royu",),
  ("Omni",),
  ("Firefly",)
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Vendor Table: {cursor.rowcount} records inserted")

#Insert Sample Data to Product Table
sql = "INSERT INTO product (product_name, cost, selling, vendor_id) \
  values (:values(0), :values(1), :values(2), :values(3))"
values = [
  ("Drill", 5000, 7500, 1),
  ("Drillbit", 100, 150,1),
  ("Drill", 5500, 8000, 4),
  ("Drillbit", 120, 180,4),
  ("Bulb 9w", 50, 90, 6),
  ("12 Awg per meter", 40, 60,5),
  ("Bulb 12w", 90, 130, 7)
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Product Table: {cursor.rowcount} records inserted")
conn.commit()

#Insert Sample Data to  Invoice Table
sql = "INSERT INTO invoice (datetime_created, customer_id, salesrep_id) \
  values (:values(0), :values(1), :values(2))"
value = (datetime.now(),1,1)
cursor.execute(sql,value)
conn.commit()
print(f"Invoice Table: {cursor.rowcount} records inserted")

#Insert Sample Data to  Orderlist Table
sql = "INSERT INTO orderlist (invoice_id, quantity, product_id) \
  values (:values(0), :values(1), :values(2))"
values = [(1, 4, 1),
          (1, 5, 2),
          (1, 10, 5),
          (1, 100, 6)
        ]
cursor.executemany(sql,values)
conn.commit()
print(f"Orderlist Table: {cursor.rowcount} records inserted")