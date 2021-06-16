CREATE TABLE potential_customers
(
    potential_customer_id serial PRIMARY KEY,
    email                 varchar(255),
    name                  varchar(255),
    surname               varchar(255),
    second_name           varchar(255),
    city                  varchar(255)
)