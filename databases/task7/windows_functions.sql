-- Сравнить цену каждого продукта n с средней ценой продуктов в категории
-- продукта n. Использовать window function. Таблица результата должна содержать
-- такие колонки: category_title, product_title, price, avg.

SELECT category_title,
       product_title,
       price,
       avg(price) over (partition by c.category_id) as avg_cat_price
FROM categories c
         JOIN products p on c.category_id = p.category_id;