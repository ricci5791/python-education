CREATE DATABASE CarRental;

CREATE TABLE IF NOT EXISTS States
(
    state_id serial PRIMARY KEY,
    state    varchar(15)
);

CREATE TABLE IF NOT EXISTS Addresses
(
    address_id serial PRIMARY KEY,
    state_id   serial      NOT NULL,
    street     varchar(50) NOT NULL,
    building   smallint    NOT NULL,
    apartments smallint,
    CONSTRAINT addresses_state_id_fk
        FOREIGN KEY (state_id)
            REFERENCES States
);

CREATE TABLE IF NOT EXISTS Customers
(
    customer_id serial PRIMARY KEY,
    name        varchar(30) UNIQUE    NOT NULL,
    surname     varchar(30) UNIQUE    NOT NULL,
    phone       numeric(10, 0) UNIQUE NOT NULL,
    address_id  serial,
    CONSTRAINT customers_address_id_fk
        FOREIGN KEY (address_id) REFERENCES Addresses
);

CREATE TABLE IF NOT EXISTS Branches
(
    branch_id  serial PRIMARY KEY,
    branch_num smallint UNIQUE NOT NULL,
    phone      numeric(10, 0),
    address_id serial,
    CONSTRAINT branches_address_id_fk
        FOREIGN KEY (address_id) REFERENCES Addresses
);

CREATE TABLE IF NOT EXISTS Brands
(
    brand_id   serial PRIMARY KEY,
    brand_name varchar(20) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Car_model
(
    model_id   serial PRIMARY KEY,
    brand_id   serial,
    model_name varchar(20) UNIQUE NOT NULL,
    CONSTRAINT car_model_model_id_fk
        FOREIGN KEY (brand_id)
            REFERENCES Brands
);

CREATE TABLE IF NOT EXISTS Cars
(
    car_plate varchar(7) PRIMARY KEY,
    price     money NOT NULL,
    model_id  serial,
    CONSTRAINT cars_model_id_fk
        FOREIGN KEY (model_id)
            REFERENCES Car_model
);

CREATE TABLE IF NOT EXISTS Rentals
(
    rental_id       serial PRIMARY KEY,
    customer_id     serial,
    car_plate       varchar(7),
    branch_id       serial,
    rent_date_start timestamp,
    duration        smallint NOT NULL,
    CONSTRAINT rentals_customer_id_fk
        FOREIGN KEY (customer_id)
            REFERENCES Customers,
    CONSTRAINT rentals_car_plate_fk
        FOREIGN KEY (car_plate)
            REFERENCES Cars,
    CONSTRAINT rentals_branch_id_fk
        FOREIGN KEY (branch_id)
            REFERENCES Branches
);