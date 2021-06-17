-- first index on users
CREATE INDEX users_index ON users (user_id);
DROP INDEX users_index;

EXPLAIN
SELECT *
FROM users
         INNER JOIN carts c ON users.user_id = c.users_user_id
WHERE user_id = 5;

-- second index on products
CREATE INDEX products_price_index ON products (price);
DROP INDEX products_price_index;

EXPLAIN
SELECT product_id, price
FROM products
WHERE price < 50;

-- third index on cart_products
CREATE INDEX products_carts_index ON cart_product (carts_cart_id, products_product_id);
DROP INDEX products_carts_index;

EXPLAIN
SELECT *
FROM cart_product
WHERE carts_cart_id = 5;

EXPLAIN
SELECT *
FROM cart_product
WHERE products_product_id = 510;

-- fourth index on carts
CREATE INDEX cart_total_index ON carts (total, users_user_id);
DROP INDEX cart_total_index;

EXPLAIN
SELECT user_id, sum(o.total) AS total_spent
FROM users
         INNER JOIN carts c ON users.user_id = c.users_user_id
         INNER JOIN "Order" O ON c.cart_id = O.carts_cart_id
WHERE c.total < 100
GROUP BY user_id
ORDER BY total_spent DESC;

EXPLAIN
SELECT c.users_user_id, c.cart_id, sum(o.total) AS total_spent
FROM carts c
         INNER JOIN "Order" O ON c.cart_id = O.carts_cart_id
WHERE c.total < 100
GROUP BY c.users_user_id, c.cart_id
ORDER BY total_spent DESC;