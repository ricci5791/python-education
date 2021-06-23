-- Написать представление для таблицы products

CREATE VIEW products_view AS
(
SELECT *
FROM products);

SELECT *
FROM products_view;

-- для таблиц order_status и order

CREATE VIEW order_status_order_view AS
(
SELECT ORDER_ID,
       CARTS_CART_ID,
       ORDER_STATUS_ID,
       STATUS_NAME,
       SHIPPING_TOTAL,
       TOTAL,
       CREATED_AT,
       UPDATED_AT
FROM "Order"
         INNER JOIN order_status os ON os.order_status_id =
                                       "Order".order_status_order_status_id);

SELECT *
FROM order_status_order_view;

-- для таблиц products и category.

CREATE VIEW products_categories_view AS
(
SELECT product_id,
       product_title,
       price,
       c.category_id,
       c.category_title,
       c.category_description
FROM products
         INNER JOIN categories c ON c.category_id = products.category_id
GROUP BY product_id, c.category_id);

-- Создать материализированное представление для "тяжелого" запроса на свое усмотрение.

CREATE MATERIALIZED VIEW spent_by_category_view AS
(
SELECT c.category_id, c.category_title, sum(products.price)
FROM products
         INNER JOIN categories c on c.category_id = products.category_id
         INNER JOIN cart_product cp
                    on products.product_id = cp.products_product_id
GROUP BY c.category_id, c.category_title);

SELECT * FROM spent_by_category_view ORDER BY category_id;

REFRESH MATERIALIZED VIEW spent_by_category_view;

-- Не забыть сделать запросы для удаления представлений.

DROP VIEW products_view;
DROP VIEW order_status_order_view;
DROP VIEW products_categories_view;
DROP MATERIALIZED VIEW spent_by_category_view;