-- Написать 2 любые хранимые процедуры с использованием условий, циклов и транзакций.

CREATE OR REPLACE PROCEDURE lower_staff_shipping_price(discount integer)
    LANGUAGE plpgsql
AS
$$
DECLARE
    order_row  record;
    difference integer;
BEGIN
    FOR order_row IN SELECT o.order_id, o.shipping_total
                     FROM "Order" o
                              JOIN carts c ON o.carts_cart_id = c.cart_id
                              JOIN users u ON c.users_user_id = u.user_id
                     WHERE is_staff = 1
        LOOP
            difference = order_row.shipping_total - discount;

            if difference < 0 then
                difference = 0;
            END IF;

            UPDATE "Order"
            SET shipping_total = difference
            WHERE order_id = order_row.order_id;

        END loop;
    COMMIT;
END;
$$;

CREATE OR REPLACE PROCEDURE get_top_thousand_spender(creation_date timestamp default '2018-01-01'::timestamp)
    LANGUAGE plpgsql
AS
$$
DECLARE
    user_id    users.user_id%type;
    first_name users.first_name%type;
    last_name  users.last_name%type;
    total      integer;
BEGIN
    <<select_block>>
    BEGIN
        SELECT u.user_id, u.first_name, u.last_name, sum(o.total) AS total_spent
        FROM users u
                 INNER JOIN carts c ON u.user_id = c.users_user_id
                 INNER JOIN "Order" O ON c.cart_id = O.carts_cart_id
        WHERE order_status_order_status_id IN (3, 4)
          AND created_at < creation_date
        GROUP BY u.user_id
        ORDER BY total_spent DESC
        LIMIT 5
        INTO user_id, first_name, last_name, total;

        IF total < 1000 THEN
            RAISE NOTICE 'No user has found, max total sum is %', total;
            EXIT select_block;
        END IF;

        RAISE NOTICE 'User % % (user id = %) spent % from % to nowadays',
            first_name, last_name, user_id, total, creation_date;
    END;
END;
$$;

CALL get_top_thousand_spender();

START TRANSACTION;
CALL lower_staff_shipping_price(5);

SELECT *
FROM "Order"
ORDER BY order_id;

COMMIT;