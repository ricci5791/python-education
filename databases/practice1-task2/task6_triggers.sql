-- Добавить 2 триггера (один из них ДО операции по изменению данных,
-- второй после) и функции или процедуры-обработчики к ним.

create trigger car_model_delete_trigger
    before delete
    on cars
    for each row
execute function delete_rental_references();

create or replace function delete_rental_references() returns trigger
    language plpgsql
as
$$
begin
    update rentals
    set car_plate = null
    where car_plate = old.given_car_plate;

    return null;
end;
$$;

create table cars_update
(
    update_id  serial,
    car_plate  varchar(7),
    updated_at timestamp
);

alter table cars_update
    alter column car_plate type varchar(7);

create trigger cars_update_logger_trigger
    after update
    on cars
    for each row
execute function insert_update_of_cars();

create or replace function insert_update_of_cars() returns trigger
    language plpgsql
as
$$
begin
    insert into cars_update(car_plate, updated_at)
    values (new.car_plate, now());

    return null;
end;
$$;

update cars
set price = 525::money
where car_plate = '5a66b92';

select *
from cars
where car_plate = '5a66b92';

select *
from cars_update;
