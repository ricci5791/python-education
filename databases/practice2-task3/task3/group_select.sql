SELECT c.category_title, count(p.category_id) AS products_count
FROM categories c
         INNER JOIN products p on p.category_id = c.category_id
GROUP BY c.category_title
ORDER BY products_count DESC;