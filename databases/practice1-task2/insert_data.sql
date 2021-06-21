CREATE PROCEDURE fill_names_surnames()
    LANGUAGE plpgsql
AS
$$
BEGIN
    CREATE TEMPORARY TABLE names
    (
        name_id serial PRIMARY KEY,
        name    varchar(30)
    );

    CREATE TEMPORARY TABLE surnames
    (
        surname_id serial PRIMARY KEY,
        surname    varchar(30)
    );

    COPY names
        FROM '/docker-entrypoint-initdb.d/csv/names.csv'
        DELIMITER ',';
    COPY surnames
        FROM '/docker-entrypoint-initdb.d/csv/surnames.csv'
        DELIMITER ',';
END;
$$;