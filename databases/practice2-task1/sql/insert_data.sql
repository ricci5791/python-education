COPY users
FROM '/docker-entrypoint-initdb.d/csv/users.csv'
DELIMITER ',';

COPY order_status
FROM '/docker-entrypoint-initdb.d/csv/order_statuses.csv'
DELIMITER ',';

COPY categories
FROM '/docker-entrypoint-initdb.d/csv/categories.csv'
DELIMITER ',';

COPY products
FROM '/docker-entrypoint-initdb.d/csv/products.csv'
DELIMITER ',';

COPY carts
FROM '/docker-entrypoint-initdb.d/csv/carts.csv'
DELIMITER ',';

COPY "Order"
FROM '/docker-entrypoint-initdb.d/csv/orders.csv'
DELIMITER ',';

COPY cart_product
FROM '/docker-entrypoint-initdb.d/csv/cart_products.csv'
DELIMITER ',';