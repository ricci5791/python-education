-- Создать функцию, которая сетит shipping_total = 0 в таблице order, если город
-- юзера равен x. Использовать IF clause

CREATE OR REPLACE FUNCTION set_shipping_fee_by_city(city text) RETURNS void

    LANGUAGE plpgsql
AS
$$

BEGIN
    UPDATE "Order" o
    SET shipping_total = CASE
                             WHEN u.city = $1 then 0
                             ELSE shipping_total END
    FROM carts c,
         users u
    WHERE o.carts_cart_id = c.cart_id
      AND u.user_id = c.users_user_id;
END ;

$$;

SELECT *
FROM "Order"
ORDER BY order_id;

SELECT set_shipping_fee_by_city('city 1');

SELECT *
FROM "Order"
ORDER BY order_id;

DROP FUNCTION set_shipping_fee_by_city(feeless_city text);