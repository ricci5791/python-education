ALTER TABLE users
ADD phone_number integer;

ALTER TABLE users
ALTER COLUMN phone_number TYPE varchar(10);