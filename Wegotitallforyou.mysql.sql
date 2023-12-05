CREATE TABLE `salesrep` (
  `id` integer PRIMARY KEY,
  `last_name` varchar(255),
  `first_name` varchar(255),
  `middle_name` varchar(255)
);

CREATE TABLE `customer` (
  `id` integer PRIMARY KEY,
  `last_name` varchar(255),
  `first_name` varchar(255),
  `middle_name` varchar(255)
);

CREATE TABLE `product` (
  `id` integer PRIMARY KEY,
  `product_name` varchar(255),
  `cost` float,
  `selling` float,
  `vendor_id` integer
);

CREATE TABLE `vendor` (
  `id` integer PRIMARY KEY,
  `vendor_name` varchar(255)
);

CREATE TABLE `invoice` (
  `id` integer PRIMARY KEY,
  `date_created` date,
  `product_list` integer[],
  `customer_id` integer,
  `salesrep_id` integer
);

ALTER TABLE `invoice` ADD FOREIGN KEY (`product_list`) REFERENCES `product` (`id`);

ALTER TABLE `invoice` ADD FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`);

ALTER TABLE `invoice` ADD FOREIGN KEY (`salesrep_id`) REFERENCES `salesrep` (`id`);

ALTER TABLE `product` ADD FOREIGN KEY (`vendor_id`) REFERENCES `vendor` (`id`);
