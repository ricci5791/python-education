-- Придувать 3 различных запроса SELECT с осмысленным использованием разных видов
-- JOIN.
-- Используя explain добавить только необходимые индексы для уменьшения стоимости
-- (cost) запросов.

create index my_rental_idx on rentals (rental_id, duration);
drop index my_rental_idx;

explain
select c.customer_id, a.street, a.building, coalesce(a.apartments, 0)
from customers c
         left join rentals r using (customer_id)
         inner join addresses a using (address_id)
where r.rental_id is null;

explain
select c.customer_id,
       r.rental_id,
       r.rent_date_start,
       (cars.price * r.duration) as total
from customers c
         left join rentals r using (customer_id)
         inner join cars using (car_plate)
where (cars.price * r.duration)::numeric < 2000;

explain
select c.customer_id,
       r.rental_id,
       r.rent_date_start,
       (cars.price * r.duration) as total
from customers c
         left join rentals r using (customer_id)
         inner join cars using (car_plate)
         inner join car_model using (model_id)
         inner join brands using (brand_id)
where (cars.price * r.duration)::numeric < 2000
  and brand_id = 20;

create index my_rental_timestamp on rentals (rent_date_start);

explain
select c.customer_id, c.name, c.surname, r.rental_id, r.rent_date_start
from customers c
         inner join rentals r using (customer_id)
where r.rent_date_start < '2011-01-01'::timestamp;

explain
select c.car_plate, b.brand_name, cm.model_name
from rentals r
         right join cars c using (car_plate)
         join car_model cm using (model_id)
         join brands b using (brand_id)
where r.rental_id is null;