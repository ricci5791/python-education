-- Вывести продукты, которые ни разу не попадали в корзину.

SELECT *
FROM products
         LEFT JOIN cart_product cp
                   ON products.product_id = cp.products_product_id
WHERE CP.carts_cart_id IS NULL;

-- 2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли).

SELECT *
FROM products
         FULL JOIN cart_product cp
                   ON products.product_id = cp.products_product_id
         FULL JOIN carts c ON cp.carts_cart_id = c.cart_id
         FULL JOIN "Order" o ON c.cart_id = o.carts_cart_id
WHERE o."order_id" IS NULL;

-- 3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.

SELECT product_id, count(carts_cart_id) AS product_count
FROM products p
         INNER JOIN cart_product cp ON p.product_id = cp.products_product_id
GROUP BY p.product_id
ORDER BY product_count DESC
LIMIT 10;

-- 4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.

SELECT product_id,
       count(o.order_id)       AS order_count,
       count(cp.carts_cart_id) AS product_count
FROM products p
         INNER JOIN cart_product cp ON p.product_id = cp.products_product_id
         INNER JOIN carts c ON cp.carts_cart_id = c.cart_id
         INNER JOIN "Order" o ON c.cart_id = o.carts_cart_id
GROUP BY p.product_id
ORDER BY order_count DESC
LIMIT 10;

-- 5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).

SELECT user_id, first_name, last_name, sum(o.total) AS total_spent
FROM users
         INNER JOIN carts c ON users.user_id = c.users_user_id
         INNER JOIN "Order" O ON c.cart_id = O.carts_cart_id
GROUP BY user_id
ORDER BY total_spent DESC
LIMIT 5;

-- 6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).

SELECT users.*, count(c.cart_id) order_count
FROM users
         JOIN carts c ON users.user_id = c.users_user_id
         JOIN "Order" o ON c.cart_id = o.carts_cart_id
GROUP BY user_id
ORDER BY order_count DESC
LIMIT 5;

-- 7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.

SELECT users.*, count(c.cart_id) AS cart_count
FROM users
         INNER JOIN carts c ON users.user_id = c.users_user_id
         FULL JOIN "Order" o ON c.cart_id = o.carts_cart_id
WHERE o.order_id IS NULL
GROUP BY users.user_id
ORDER BY cart_count DESC
LIMIT 5;