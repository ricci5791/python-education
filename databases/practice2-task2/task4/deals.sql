-- 1. среднюю сумму всех завершенных сделок

SELECT AVG(total)
FROM "Order"
WHERE order_status_order_status_id = 4;

SELECT AVG(total)
FROM "Order"
         INNER JOIN order_status os on "Order".order_status_order_status_id =
                                       os.order_status_id
WHERE os.status_name = 'Finished';

-- 2. вывести максимальную сумму сделки за 3 квартал 2020

SELECT MAX(total)
FROM "Order"
WHERE created_at BETWEEN '2020-07-01' AND '2020-09-30';