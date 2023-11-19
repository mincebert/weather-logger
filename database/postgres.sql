-- weather-logger/sql/postgres.sql

-- Create the weather database and roles at the DBA level.
-- The tables are created in the 'weather.sql' script.


-- create a group for all users with basic access to connect to the database

CREATE ROLE weather_users;


-- weather_admin owns the database and has full control

CREATE ROLE weather_admin
  WITH LOGIN PASSWORD 'admin' IN ROLE weather_users;


-- weather_update only has the ability to log new data

CREATE ROLE weather_update
  WITH LOGIN PASSWORD 'update' IN ROLE weather_users;


-- weather_read only has the ability to read data

CREATE ROLE weather_read
  WITH LOGIN PASSWORD 'read' IN ROLE weather_users;


-- create the database and set the owner to weather_admin

CREATE DATABASE weather OWNER weather_admin;

\c weather
ALTER SCHEMA public OWNER TO weather_admin;
\c postgres
