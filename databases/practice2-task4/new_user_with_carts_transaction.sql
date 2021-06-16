CREATE OR REPLACE VIEW chosen_products_price AS
(
SELECT sum(price)
FROM products
WHERE product_id IN (11, 45, 489,
                     52, 100));

CREATE OR REPLACE VIEW another_products_price AS
(
SELECT sum(price)
FROM products
WHERE product_id IN (5, 99, 547,
                     1025, 80));

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
CREATE TEMPORARY SEQUENCE cart_seq START 2001;

INSERT INTO users
VALUES (3001, 'test@email.com', 'some_password', 'Emil', 'Gadjiev', 'Ralf', 0,
        'France', 'Mano', 'Some address');

SAVEPOINT user_created;

INSERT INTO carts
VALUES (nextval('cart_seq'), 3001, (SELECT * FROM chosen_products_price),
        (SELECT * FROM chosen_products_price), current_timestamp),
       (nextval('cart_seq'), 3001, (SELECT * FROM another_products_price),
        (SELECT * FROM another_products_price) + 20, current_timestamp);

SAVEPOINT carts_created;

ROLLBACK TO user_created;

RELEASE user_created;

DROP SEQUENCE cart_seq;

COMMIT;