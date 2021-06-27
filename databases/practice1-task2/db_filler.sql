-- states

create or replace function fill_states(states_num integer) returns void
    language plpgsql
as
$$
begin
    for _ in 1..states_num
        loop
            insert into states (state)
            values ('state' || currval('states_state_id_seq'));
        end loop;
end;
$$;

begin;
select fill_states(50);
end;

select *
from states;

-- addresses

create or replace function fill_addresses() returns void
    language plpgsql
as
$$
declare
    states_length integer = (select count(*)
                             from states);
    apartment     integer;
begin
    for i in 0..10000
        loop
            if random() < 0.25 then
                apartment = random() * 1000;
            else
                apartment = null;
            end if;

            insert into addresses(state_id, street, building,
                                  apartments)
            values (floor(random() * (states_length) + 1),
                    'street' || currval('addresses_address_id_seq'),
                    (random() * 100 + 1)::int,
                    apartment);
        end loop;
end;
$$;

begin;
SELECT fill_addresses();
end;

select *
from addresses;

alter sequence addresses_address_id_seq restart with 1;

-- customers

create or replace function fill_customers() returns void
    language plpgsql
as
$$
declare
    temp_name       varchar(50);
    temp_surname    varchar(50);
    addresses_count integer = (select count(*)
                               from addresses);
begin
    call fill_names_surnames();

    for temp_name, temp_surname in select name, surname
                                   from names
                                            cross join surnames
                                   order by random()
        loop
            insert into customers(name, surname, phone, address_id)
            values (temp_name,
                    temp_surname,
                    (floor(random() * 999999999) + 1000000000)::numeric,
                    (floor(random() * addresses_count)) + 1)
            on conflict do nothing;
        end loop;

    drop table names;
    drop table surnames;
end;
$$;

begin;
select fill_customers();
end;

select *
from customers;

-- branches

create or replace function fill_branches() returns void
    language plpgsql
as
$$
begin
    create temporary sequence branch_num start 1 maxvalue 32766;

    for _ in 1..32000
        loop
            insert into branches(branch_num, phone, address_id)
            values (nextval('branch_num'),
                    (floor(random() * 999999999) + 1000000000)::numeric,
                    (floor(random() * 10000) + 1))
            on conflict (branch_num) do nothing;
        end loop;

    drop sequence branch_num;
end;
$$;

begin;
select fill_branches();
end;

select *
from branches;

-- Brands

begin;
create temp sequence brands_pk_seq start 1;
insert into brands
    (values (nextval('brands_pk_seq'), 'Audi'),
            (nextval('brands_pk_seq'), 'BMW'),
            (nextval('brands_pk_seq'), 'Buick'),
            (nextval('brands_pk_seq'), 'Cadillac'),
            (nextval('brands_pk_seq'), 'Chevrolet'),
            (nextval('brands_pk_seq'), 'Chrysler'),
            (nextval('brands_pk_seq'), 'Dodge'),
            (nextval('brands_pk_seq'), 'Ferrari'),
            (nextval('brands_pk_seq'), 'Ford'),
            (nextval('brands_pk_seq'), 'GM'),
            (nextval('brands_pk_seq'), 'GEM'),
            (nextval('brands_pk_seq'), 'GMC'),
            (nextval('brands_pk_seq'), 'Honda'),
            (nextval('brands_pk_seq'), 'Hummer'),
            (nextval('brands_pk_seq'), 'Hyundai'),
            (nextval('brands_pk_seq'), 'Infiniti'),
            (nextval('brands_pk_seq'), 'Isuzu'),
            (nextval('brands_pk_seq'), 'Jaguar'),
            (nextval('brands_pk_seq'), 'Jeep'),
            (nextval('brands_pk_seq'), 'Kia'),
            (nextval('brands_pk_seq'), 'Lamborghini'),
            (nextval('brands_pk_seq'), 'Land Rover'),
            (nextval('brands_pk_seq'), 'Lexus'),
            (nextval('brands_pk_seq'), 'Lincoln'),
            (nextval('brands_pk_seq'), 'Lotus'),
            (nextval('brands_pk_seq'), 'Mazda'),
            (nextval('brands_pk_seq'), 'Mercedes-Benz'),
            (nextval('brands_pk_seq'), 'Mercury'),
            (nextval('brands_pk_seq'), 'Mitsubishi'),
            (nextval('brands_pk_seq'), 'Nissan'),
            (nextval('brands_pk_seq'), 'Oldsmobile'),
            (nextval('brands_pk_seq'), 'Peugeot'),
            (nextval('brands_pk_seq'), 'Pontiac'),
            (nextval('brands_pk_seq'), 'Porsche'),
            (nextval('brands_pk_seq'), 'Regal'),
            (nextval('brands_pk_seq'), 'Saab'),
            (nextval('brands_pk_seq'), 'Saturn'),
            (nextval('brands_pk_seq'), 'Subaru'),
            (nextval('brands_pk_seq'), 'Suzuki'),
            (nextval('brands_pk_seq'), 'Toyota'),
            (nextval('brands_pk_seq'), 'Volkswagen'),
            (nextval('brands_pk_seq'), 'Volvo'));
drop sequence brands_pk_seq;
end;

select *
from brands;

-- Car_model

begin;
select fill_car_model();
end;

select *
from car_model;

-- Cars

create or replace function fill_cars() returns void
    language plpgsql
as
$$
declare
    model_count integer = (select count(*)
                           from car_model);
begin
    create temporary sequence car_plate_seq start 1 increment 55;

    for _ in 1..50000
        loop
            insert into cars
            values (substr(md5(nextval('car_plate_seq')::text), 0, 8),
                    (100 + floor(random() * 1000))::numeric::money,
                    (floor(random() * model_count) + 1))
            on conflict (car_plate) do nothing;
        end loop;
    drop sequence car_plate_seq;
end;
$$;

begin;
select fill_cars();
end;

select *
from cars;


-- Rentals

create or replace function fill_rentals() returns void
    language plpgsql
as
$$
declare
    customer_count   integer = (select count(*)
                                from customers);
    branch_count     integer = (select count(*)
                                from brands);
    temp_customer_id integer;
    temp_car_plate   varchar(7);
    temp_branch_id   integer;
    temp_timestamp   timestamp;
begin
    create temporary sequence car_plate_seq start 1 increment 55 maxvalue 2200000 cycle;

    for _ in 0..1000000
        loop
            temp_customer_id = floor(random() * customer_count);
            temp_car_plate = substr(md5(nextval('car_plate_seq')::text), 0, 8);
            temp_branch_id = (floor(random() * branch_count) + 1);
            temp_timestamp = (select timestamp '2010-01-01 00:00:00' +
                                     random() *
                                     (now() -
                                      timestamp '2010-01-01 00:00:00'));

            while random() < 0.20
                loop
                    perform nextval('car_plate_seq');
                end loop;

            if (select exists(select car_plate
                              from cars
                              where car_plate = temp_car_plate)) then

                insert into rentals(customer_id, car_plate, branch_id,
                                    rent_date_start, duration)
                values (temp_customer_id,
                        temp_car_plate,
                        temp_branch_id,
                        temp_timestamp,
                        (floor(random() * 7 + 1))::smallint);
            else
            end if;
        end loop;

    delete
    from rentals
    where customer_id in (select c.customer_id
                          from rentals
                                   inner join customers c
                                              on rentals.customer_id = c.customer_id
                          group by c.customer_id
                          having count(c.customer_id) = 1);

    drop sequence car_plate_seq;
end;
$$;

begin;
select fill_rentals();
end;

select *
from rentals;