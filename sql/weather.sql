-- ---------------------------------------------------------------------------
-- SENSORS AND LOCATIONS
-- ---------------------------------------------------------------------------


-- create the sensor locations table
--
-- This describes the locations (current or historical) of data.

CREATE TABLE location (
  id integer PRIMARY KEY CHECK (id >= 0),
  description varchar UNIQUE NOT NULL
);


-- create the sensor mapping table
--
-- This maps current sensor numbers to locations.

CREATE TABLE sensor_location (
  sensor integer PRIMARY KEY CHECK (sensor >= 0),
  location integer UNIQUE NOT NULL REFERENCES location (id)
);


-- ---------------------------------------------------------------------------
-- WEATHER LATEST
-- ---------------------------------------------------------------------------


-- create the 'latest' (current) weather table

CREATE TABLE weather_latest (
  location integer REFERENCES location (id) PRIMARY KEY,

  datetime timestamp with time zone,
  temp numeric(4, 1),
  humidity integer
);


-- weather_latest_update()
--
-- This function updates the weather_latest table with new information.  If no
-- data is stored for the specified sensor, it will be stored as the first
-- set; if there is data, it will be replaced, if the data is older than the
-- new data.

CREATE FUNCTION weather_latest_update(
  new_sensor integer,
  new_datetime timestamp,
  new_temp numeric(4, 1),
  new_humidity integer
) RETURNS void AS $$
DECLARE
  new_location integer;
BEGIN
  new_location = (SELECT location FROM sensor_location
                    WHERE sensor = new_sensor);

  -- find out of there's a row already for this location
  IF (SELECT COUNT(*) FROM weather_latest
	WHERE location = new_location) = 0 THEN
    -- no row already - just store this one as the first

    INSERT INTO weather_latest (datetime, location, temp, humidity)
      SELECT new_datetime, new_location, new_temp, new_humidity;

  -- see if this row is newer than the one already stored
  ELSIF new_datetime > (SELECT datetime FROM weather_latest
                          WHERE location = new_location) THEN

    -- it's newer - replace the existing row
    UPDATE weather_latest
      SET datetime = new_datetime, temp = new_temp, humidity = new_humidity
      WHERE location = new_location;

  END IF;
END
$$ LANGUAGE plpgsql;


-- ---------------------------------------------------------------------------
-- WEATHER HISTORY
-- ---------------------------------------------------------------------------


-- create the historical data table

CREATE TABLE weather_history (
  datetime timestamp with time zone,
  location integer REFERENCES location (id),

  temp numeric(4, 1),
  humidity integer,

  PRIMARY KEY (datetime, location)
);


-- weather_history_insert()
--
-- This function adds data to the weather_history table with new information.

CREATE FUNCTION weather_history_insert(
  new_sensor integer,
  new_datetime timestamp,
  new_temp numeric(4, 1),
  new_humidity integer
) RETURNS void AS $$
DECLARE
  new_location integer;
BEGIN
  new_location = (SELECT location FROM sensor_location
                    WHERE sensor = new_sensor);

  INSERT INTO weather_history (location, datetime, temp, humidity)
    VALUES (new_location, new_datetime, new_temp, new_humidity);
END
$$ LANGUAGE plpgsql;
