SELECT *
FROM "Order"
         INNER JOIN order_status os
                    ON "Order".order_status_order_status_id = os.order_status_id
WHERE order_status_order_status_id = 4;