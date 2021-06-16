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
        (SELECT * FROM chosen_products_price), current_timestamp);

INSERT INTO cart_product
VALUES (currval('cart_seq'), 11),
       (currval('cart_seq'), 45),
       (currval('cart_seq'), 489),
       (currval('cart_seq'), 52),
       (currval('cart_seq'), 100);

SAVEPOINT first_cart_filled;

INSERT INTO carts
VALUES (nextval('cart_seq'), 3001, (SELECT * FROM another_products_price),
        (SELECT * FROM another_products_price) + 20, current_timestamp);

INSERT INTO cart_product
VALUES (currval('cart_seq'), 5),
       (currval('cart_seq'), 99),
       (currval('cart_seq'), 547),
       (currval('cart_seq'), 1025),
       (currval('cart_seq'), 80);

SAVEPOINT carts_created;

ROLLBACK TO first_cart_filled;

RELEASE user_created;
RELEASE carts_created;

DROP SEQUENCE cart_seq;

COMMIT;