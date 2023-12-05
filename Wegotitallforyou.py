import sqlite3

conn = sqlite3.connect("Wegotitallforyou.db")
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = 1")

createSalesRepTableQuery = """CREATE TABLE IF NOT EXISTS [salesrep] (
  [id] integer PRIMARY KEY,
  [last_name] nvarchar(255),
  [first_name] nvarchar(255),
  [middle_name] nvarchar(255)
  )"""

createCustomerTableQuery = """CREATE TABLE IF NOT EXISTS [customer] (
  [id] integer PRIMARY KEY,
  [last_name] nvarchar(255),
  [first_name] nvarchar(255),
  [middle_name] nvarchar(255)
  )"""

createProductTableQuery = """CREATE TABLE IF NOT EXISTS [product] (
  [id] integer PRIMARY KEY,
  [product_name] nvarchar(255),
  [cost] float,
  [selling] float,
  [vendor_id] integer,
  FOREIGN KEY(vendor_id) REFERENCES vendor(id)
  )"""

createVendorTableQuery = """CREATE TABLE IF NOT EXISTS [vendor] (
  [id] integer PRIMARY KEY,
  [vendor_name] nvarchar(255)
  )"""

#column product list should be an array but is not supported in sql lite.
#It can be stored as string and handled in the program
createInvoiceTableQuery = """CREATE TABLE IF NOT EXISTS [invoice] (
  [id] integer PRIMARY KEY,
  [date_created] date,
  [product_list] nvarchar(255),
  [customer_id] integer,
  [salesrep_id] integer,
  FOREIGN KEY(product_list) REFERENCES product(id),
  FOREIGN KEY(customer_id) REFERENCES customer(id),
  FOREIGN KEY(salesrep_id) REFERENCES salesrep(id)
  )"""

print(f"{createSalesRepTableQuery}")
print(f"{createCustomerTableQuery}")
print(f"{createProductTableQuery}")
print(f"{createVendorTableQuery}")
print(f"{createInvoiceTableQuery}")


cursor.execute(createSalesRepTableQuery)
cursor.execute(createCustomerTableQuery)
cursor.execute(createProductTableQuery)
cursor.execute(createVendorTableQuery)
cursor.execute(createInvoiceTableQuery)
#conn.commit()