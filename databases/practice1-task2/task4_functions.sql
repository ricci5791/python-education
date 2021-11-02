-- Создать 2 функции (одна из них должна возвращать таблицу, одна из них должна
-- использовать циклы, одна из них должна использовать курсор)

create or replace function get_start_end_rental_data(given_start_date timestamp default '2010-01-01'::timestamp,
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

select *
from get_start_end_rental_data();

create or replace function get_rentals_for_branch(branch_id integer) returns void
    language plpgsql as
$$
declare
    ref cursor for select *
                   from rentals;
begin
    for rental in ref
        loop
            if rental.branch_id <> $1 then
                continue;
            else
                raise notice 'Rental % has been found with branch %', rental.rental_id, $1;
            end if;
        end loop;
end;
$$;

begin;
select get_rentals_for_branch(1);
end;