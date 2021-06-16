SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;

INSERT INTO carts
VALUES (2003, 3001, (SELECT * FROM another_products_price),
        (SELECT * FROM another_products_price) + 20, current_timestamp);

INSERT INTO cart_product
VALUES (2003, 5),
       (2003, 99),
       (2003, 547),
       (2003, 1025),
       (2003, 80);

INSERT INTO "Order"
VALUES ((SELECT order_id FROM "Order" ORDER BY order_id DESC LIMIT 1) + 1,
        2003,
        1,
        100,
        (SELECT total FROM carts WHERE cart_id = 2003),
        CURRENT_TIMESTAMP);

SAVEPOINT order_created;

UPDATE "Order"
SET order_status_order_status_id = 2
WHERE order_id = 1501;

RELEASE SAVEPOINT order_created;
COMMIT;

SELECT *
FROM "Order"
WHERE carts_cart_id = 2003;