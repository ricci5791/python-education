CREATE OR REPLACE FUNCTION update_carts_price() RETURNS TRIGGER
    LANGUAGE plpgsql AS
$$
BEGIN
    UPDATE "Order"
    SET total = "Order".total - old.price + new.price
    FROM carts c
             INNER JOIN cart_product cp ON c.cart_id = cp.carts_cart_id
             INNER JOIN products p ON cp.products_product_id = new.product_id
    where "Order".carts_cart_id = c.cart_id;

    return null;
END;
$$;

SELECT o.order_id, o.total, product_id
FROM products
         INNER JOIN cart_product cp
                    ON products.product_id = cp.products_product_id
         INNER JOIN carts c ON cp.carts_cart_id = c.cart_id
         INNER JOIN "Order" O ON c.cart_id = O.carts_cart_id
WHERE product_id = 1;

CREATE TRIGGER change_product_price
    AFTER UPDATE
        OF price
    ON products
    FOR EACH ROW
EXECUTE FUNCTION update_carts_price();

UPDATE products
SET price = 700
WHERE product_id = 1;

--second trigger

CREATE TABLE logging
(
    log_id              serial PRIMARY KEY,
    created_at          timestamp    NOT NULL,
    affected_rows_count integer      NOT NULL,
    table_name          varchar(255) NOT NULL
);

CREATE OR REPLACE FUNCTION log_insert() RETURNS TRIGGER
    language plpgsql AS
$$
DECLARE
    row_index bigint := nextval('logging_log_id_seq');
BEGIN
    INSERT INTO logging
    VALUES (row_index,
            now(),
            (SELECT count(*) FROM new_table),
            TG_TABLE_NAME);
    RETURN NULL;
END;
$$;

CREATE TRIGGER new_insertion_data
    AFTER INSERT
    ON users
    REFERENCING NEW TABLE AS new_table
    FOR EACH STATEMENT
EXECUTE FUNCTION log_insert();

SELECT *
FROM logging;

SELECT *
FROM users
ORDER BY user_id DESC;

INSERT INTO users
VALUES (3015, 'email', 'password', 'first', 'last', 'middle', 0, 'country 3005',
        'city 3005', 'address 3005'),
       (3016, 'email', 'password', 'first', 'last', 'middle', 0, 'country 3005',
        'city 3005', 'address 3005');