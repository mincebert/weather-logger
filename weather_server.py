#!/usr/bin/env python3

# weather-server



from datetime import datetime

from fastapi import FastAPI
import uvicorn

import psycopg


# details of the database to query
DBNAME = "weather"
DBHOST = "localhost"
DBUSER = "weather_read"
DBPASSWORD = "read"



# --- FastAPI app ---



app = FastAPI()


@app.get("/version")
def read_version():
    return { "version": "0.1.4" }


@app.get("/get_latest")
def read_latest():
    # get the current date and time without timezone offset
    now = datetime.now().astimezone()

    # connect to the database and get a cursor
    try:
        with psycopg.connect(f"""
                         dbname={DBNAME} host={DBHOST} user={DBUSER}
                         password={DBPASSWORD}""") as conn:

            with conn.cursor() as cur:
                # get the latest weather data indexed by descriptive location
                cur.execute("""
                        SELECT description, temp, humidity, datetime,
                               CURRENT_TIMESTAMP - datetime AS age
                        FROM weather_latest JOIN location ON location = id
                        ORDER BY location
                        """)

                # assemble a list of results as a dictionary indexed by the
                # location description
                r = {}
                for sensor in cur:
                    r[sensor[0]] = {
                        "temp": sensor[1],
                        "humidity": sensor[2],
                        "datetime": sensor[3],
                        "age": sensor[4]
                    }

    except (psycopg.InterfaceError, psycopg.OperationalError):
        return { "status": 200, "datetime": now }


    # return the results
    return { "sensors": r, "status": 100, "datetime": now }



# --- main ---



def main():
    config = uvicorn.Config("weather_server:app", host=None, log_level="info")
    server = uvicorn.Server(config)
    server.run()

if __name__ == "__main__":
    main()
