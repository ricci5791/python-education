create or replace function get_car_with_low_price()
    returns table
            (
                concat_str text
            )
    language plpgsql
as
$$
declare
    max_car_price money = (select max(cars.price)
                           from cars);
begin
    return query (select cars.car_plate::varchar || ' ' ||
                         cars.price::varchar || ' ' ||
                         b.brand_name::varchar || ' ' ||
                         cm.model_name::varchar as concat_str
                  from cars
                           join car_model cm on cars.model_id = cm.model_id
                           join brands b on b.brand_id = cm.brand_id
                  where cars.price = max_car_price
                  group by b.brand_name, cm.model_name, cars.car_plate);
end;
$$;

drop function get_car_with_low_price();

select *
from get_car_with_low_price();