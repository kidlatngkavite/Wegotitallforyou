CREATE TABLE [salesrep] (
  [id] integer PRIMARY KEY,
  [last_name] nvarchar(255),
  [first_name] nvarchar(255),
  [middle_name] nvarchar(255)
)
GO

CREATE TABLE [customer] (
  [id] integer PRIMARY KEY,
  [last_name] nvarchar(255),
  [first_name] nvarchar(255),
  [middle_name] nvarchar(255)
)
GO

CREATE TABLE [product] (
  [id] integer PRIMARY KEY,
  [product_name] nvarchar(255),
  [cost] float,
  [selling] float,
  [vendor_id] integer
)
GO

CREATE TABLE [vendor] (
  [id] integer PRIMARY KEY,
  [vendor_name] nvarchar(255)
)
GO

CREATE TABLE [invoice] (
  [id] integer PRIMARY KEY,
  [date_created] date,
  [customer_id] integer,
  [salesrep_id] integer
)
GO

CREATE TABLE [orderlist] (
  [invoice_id] integer,
  [quantity] integer,
  [product_id] integer
)
GO

ALTER TABLE [invoice] ADD FOREIGN KEY ([customer_id]) REFERENCES [customer] ([id])
GO

ALTER TABLE [invoice] ADD FOREIGN KEY ([salesrep_id]) REFERENCES [salesrep] ([id])
GO

ALTER TABLE [product] ADD FOREIGN KEY ([vendor_id]) REFERENCES [vendor] ([id])
GO

ALTER TABLE [orderlist] ADD FOREIGN KEY ([invoice_id]) REFERENCES [invoice] ([id])
GO

ALTER TABLE [orderlist] ADD FOREIGN KEY ([product_id]) REFERENCES [product] ([id])
GO
