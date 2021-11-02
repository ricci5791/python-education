drop schema if exists car_rental_package cascade;
create schema car_rental_package;

create or replace procedure car_rental_package.add_new_model(new_brand_name varchar(20),
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

create or replace function car_rental_package.get_start_end_rental_data(given_start_date timestamp default '2010-01-01'::timestamp,
                                                                        given_end_date timestamp default now())
    returns table
            (
                rental_id  integer,
                start_date timestamp,
                end_date   timestamp
            )
    language plpgsql
as
$$
begin
    return query select rentals.rental_id,
                        rentals.rent_date_start,
                        rentals.rent_date_start +
                        make_interval(days := rentals.duration) as rent_end_date
                 from rentals
                 where rentals.rent_date_start > given_start_date
                   and rentals.rent_date_start +
                       make_interval(days := rentals.duration) <
                       given_end_date;
end;
$$;

call car_rental_package.add_new_model('lexus33', 'rx400');

select * from car_rental_package.get_start_end_rental_data();