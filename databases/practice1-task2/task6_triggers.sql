-- Добавить 2 триггера (один из них ДО операции по изменению данных,
-- второй после) и функции или процедуры-обработчики к ним.

create or replace function delete_rental_references() returns trigger
    language plpgsql
as
$$
begin
    update rentals
    set car_plate = null
    where car_plate = old.car_plate;

    return null;
end;
$$;

drop trigger car_model_delete_trigger on cars;

create trigger car_model_delete_trigger
    before delete
    on cars
    for each row
execute function delete_rental_references();

create table cars_update
(
    update_id  serial,
    car_plate  varchar(7),
    updated_at timestamp,
    old_price  money,
    new_price  money
);


create or replace function insert_update_of_cars() returns trigger
    language plpgsql
as
$$
begin
    insert into cars_update(car_plate, updated_at, old_price, new_price)
    values (new.car_plate, now(), old.price, new.price);

    return null;
end;
$$;

create trigger cars_update_logger_trigger
    after update
    on cars
    for each row
execute function insert_update_of_cars();

update cars
set price = 525::money
where car_plate = '5a66b92';

select *
from cars
where car_plate = '5a66b92';

select *
from cars_update;

delete
from cars
where car_plate = '000109e';

delete from car_model
where model_id = 214;


SELECT column_name
    FROM information_schema.columns
    WHERE table_schema = 'public'
        AND table_name   = 'rentals';