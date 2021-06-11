-- 1. Продукты, цена которых больше 80.00 и меньше или равно 150.00

SELECT *
from products
WHERE price > 80
  AND price <= 150;

-- 2. заказы совершенные после 01.10.2020 (поле created_at)

SELECT *
from "Order"
WHERE created_at >= '2020-10-01';

-- 3. заказы полученные за первое полугодие 2020 года

SELECT *
from "Order"
WHERE created_at >= '2020-01-01'
  AND created_at <= '2020-07-01';

SELECT *
from "Order"
WHERE created_at BETWEEN '2020-01-01'
          AND '2020-07-01';

-- 4. подукты следующих категорий Category 7, Category 11, Category 18

SELECT *
from products
WHERE category_id IN (7, 11, 18);

SELECT *
from products
WHERE category_id = 7
   OR category_id = 11
   OR category_id = 18;

-- 5. незавершенные заказы по состоянию на 31.12.2020

SELECT *
FROM "Order"
WHERE order_status_order_status_id < 4;

-- 6.Вывести все корзины, которые были созданы, но заказ так и не был оформлен.

select c.*
from "Order" inner join carts c on "Order".carts_cart_id = c.cart_id
where "Order".order_status_order_status_id = 5;
