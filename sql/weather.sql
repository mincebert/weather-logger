-- create the 'latest' (current) weather table

CREATE TABLE weather_latest (
  sensor integer PRIMARY KEY CHECK (sensor >= 0),

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
BEGIN
  -- find out of there's a row already for this sensor
  IF (SELECT COUNT(*) FROM weather_latest WHERE sensor = new_sensor) = 0 THEN
    -- no row already - just store this one as the first

    INSERT INTO weather_latest (datetime, sensor, temp, humidity)
      SELECT new_datetime, new_sensor, new_temp, new_humidity;

  -- see if this row is newer than the one already stored
  ELSIF new_datetime > (SELECT datetime FROM weather_latest
                          WHERE sensor = new_sensor) THEN

    -- it's newer - replace the existing row
    UPDATE weather_latest
      SET datetime = new_datetime, temp = new_temp, humidity = new_humidity
      WHERE sensor = new_sensor;

  END IF;
END
$$ LANGUAGE plpgsql;


-- create the historical data table

CREATE TABLE weather_history (
  sensor integer CHECK (sensor >= 0),
  datetime timestamp with time zone,

  temp numeric(4, 1),
  humidity integer,

  PRIMARY KEY (datetime, sensor)
);
