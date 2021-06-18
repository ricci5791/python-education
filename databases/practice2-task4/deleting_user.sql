SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;

UPDATE "Order"
SET order_status_order_status_id = CASE
                                       WHEN order_status_order_status_id IN (1, 2)
                                           THEN 5
                                       ELSE order_status_order_status_id END,
updated_at = CURRENT_TIMESTAMP
WHERE carts_cart_id in (SELECT cart_id FROM carts WHERE users_user_id = 3001);

UPDATE carts
SET users_user_id = NULL
WHERE users_user_id = 3001;

DELETE
FROM users
WHERE user_id = 3001;

COMMIT;

SELECT *
FROM carts
WHERE cart_id = 2003;

SELECT *
FROM "Order"
WHERE carts_cart_id = 2003;