-- Создать 3 представления (1 из них должно быть материализированным и
-- хранить данные от "тяжелого" запроса).

create view car_full_info_view as
select car_plate,
       brand_name,
       model_name,
       price
from brands
         inner join car_model using (brand_id)
         inner join cars using (model_id);

select *
from car_full_info_view;

create view customers_full_info_view as
select name, surname, phone, state, street, building, apartments
from customers
         inner join addresses using (address_id)
         inner join states using (state_id);

select *
from customers_full_info_view;

create materialized view show_customers_rents_detail_info_view as
select c.customer_id,
       c.name,
       c.surname,
       c.phone,
       s.state,
       ad.street,
       ad.building,
       count(r.rental_id) as total_rentals
from customers c
         inner join addresses ad using (address_id)
         inner join rentals r using (customer_id)
         inner join states s using (state_id)
group by c.customer_id, s.state, ad.street, ad.building;

refresh materialized view show_customers_rents_detail_info_view;

select *
from show_customers_rents_detail_info_view;

create materialized view rents_with_lt_2000_total_view as
select c.customer_id,
       r.rental_id,
       r.rent_date_start,
       (cars.price * r.duration) as total
from customers c
         left join rentals r using (customer_id)
         inner join cars using (car_plate)
where (cars.price * r.duration)::numeric < 2000;

refresh materialized view rents_with_lt_2000_total_view;