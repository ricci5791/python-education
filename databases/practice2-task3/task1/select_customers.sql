SELECT name, surname, second_name, email
FROM potential_customers
UNION
SELECT first_name, last_name, middle_name, email
FROM users
WHERE city = 'city 17';