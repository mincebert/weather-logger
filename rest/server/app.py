# weather-server.py

# run with 'gunicorn3 server.app:api'


import datetime

import falcon
import json
import psycopg2


class WeatherEndpoint:
    def on_get(self, req, resp, name):
        if name == "latest":
            self.on_get_latest(req, resp, name)
    
    def on_get_latest(self, req, resp, name):
        # get the latest data from the database
        cur.execute(
            "SELECT sensor, datetime, temp, humidity FROM weather_latest")

        # go through the results, row by row, building the return value
        r = []
        for sensor, datetime_, temp, humidity in cur:
            # convert some of types of some parts of the data to be those that
            # can be represented in JSON
            r.append( (sensor, datetime_.isoformat(), float(temp),
                       float(humidity)) )

        # return the results
        resp.body = json.dumps(r)


# connect to the weather database and get a cursor
conn = psycopg2.connect("dbname=weather")
cur = conn.cursor()

# get an API endpoing
weather_endpoint = WeatherEndpoint()

# start the server, using the endpoint
api = falcon.API()
api.add_route("/weather/{name}", weather_endpoint)
