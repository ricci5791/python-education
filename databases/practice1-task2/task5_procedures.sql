-- Написать 2 любые хранимые процедуры. В них использовать транзакции для
-- insert, update, delete.

create or replace procedure add_new_model(new_brand_name varchar(20),
                                          new_model_name varchar(20))
    language plpgsql
as
$$
begin
    insert into brands(brand_name)
    values (new_brand_name);

    insert into car_model(brand_id, model_name)
    values (currval('brands_brand_id_seq'), new_model_name);

    commit;
end;
$$;

call add_new_model('lexus2', 'rx400');

create or replace procedure delete_or_update_model_price(price_threshold money,
                                                         additional_price money)
    language plpgsql
as
$$
declare
    deletion_cars_counter integer = (select count(*)
                                     from cars
                                     where price < price_threshold);
    car                   cars%rowtype;
begin
    raise notice '%', deletion_cars_counter;

    if deletion_cars_counter > 2000 then
        raise exception 'Too many cars will be deleted: %', deletion_cars_counter using
            hint = 'Try to raise price threshold';
    end if;

    for car in select * from cars
        loop
            if car.price < price_threshold then
                update rentals
                set car_plate = null
                where car_plate = car.car_plate;

                delete
                from cars
                where car_plate = car.car_plate;
            else
                update cars
                set price = price + additional_price
                where car_plate = car.car_plate;
            end if;
        end loop;
exception
    when sqlstate 'P0001' then
        raise notice 'WARNING -- Too many records to delete: %', deletion_cars_counter;
        commit;
end;
$$;

select *
from cars;

call delete_or_update_model_price(9500::money, 2233::money);
call delete_or_update_model_price(9035::money, 2233::money);

select *
from cars;