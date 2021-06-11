CREATE DATABASE Shop;

CREATE TABLE IF NOT EXISTS Users
(
    user_id     integer PRIMARY KEY,
    email       varchar(255),
    password    varchar(255),
    first_name  varchar(255),
    last_name   varchar(255),
    middle_name varchar(255),
    is_staff    int2,
    country     varchar(255),
    city        varchar(255),
    address     text
);

CREATE TABLE IF NOT EXISTS Categories
(
    category_id          integer PRIMARY KEY,
    category_title       varchar(255),
    category_description text
);

CREATE TABLE IF NOT EXISTS Products
(
    product_id          serial PRIMARY KEY,
    product_title       varchar(255),
    product_description text,
    in_stock            integer,
    price               float,
    slug                varchar(45),
    category_id         integer,
    CONSTRAINT fk_category
        FOREIGN KEY (category_id)
            REFERENCES Categories (category_id)
);

CREATE TABLE IF NOT EXISTS Carts
(
    cart_id       integer PRIMARY KEY,
    Users_user_id integer,
    subtotal      decimal,
    total         decimal,
    timestamp     timestamp(2),
    CONSTRAINT fk_category
        FOREIGN KEY (Users_user_id)
            REFERENCES Users (user_id)
);

CREATE TABLE IF NOT EXISTS Cart_product
(
    carts_cart_id       integer,
    products_product_id integer,
    CONSTRAINT fk_cart_id
        FOREIGN KEY (carts_cart_id)
            REFERENCES Carts (cart_id),
    CONSTRAINT fk_product_id
        FOREIGN KEY (products_product_id)
            REFERENCES Products (product_id)
);

CREATE TABLE IF NOT EXISTS Order_status
(
    order_status_id integer PRIMARY KEY,
    status_name     varchar(255)
);

CREATE TABLE IF NOT EXISTS "Order"
(
    order_id                     integer PRIMARY KEY,
    Carts_cart_id                integer,
    Order_status_order_status_id integer,
    shipping_total               decimal,
    total                        decimal,
    created_at                   timestamp(2),
    updated_at                   timestamp(2),
    CONSTRAINT fk_cart_id
        FOREIGN KEY (Carts_cart_id)
            REFERENCES Carts (cart_id),
    CONSTRAINT fk_order_status
        FOREIGN KEY (Order_status_order_status_id)
            REFERENCES Order_status (order_status_id)
);