# temperature-server.py


import falcon
import json
import psycopg2


conn = psycopg2.connect("dbname=weather")
cur = conn.cursor()

class WeatherResource(object):
  def on_get_weather_latest(self, req, resp):
    cur.execute("SELECT sensor, datetime, temp, humidity")
    results = cur.fetchall()
    resp.body = json.dumps(results)

  def on_get_people(self, req, resp):
    resp.body = json.dumps(self.people)

  def on_post_people(self, req, resp):
    resp.status = falcon.HTTP_201
    resp.body = json.dumps({'success': True})
    j = json.loads(req.stream.read(req.content_length or 0))
    self.people[j['name']] = {"likes": j['likes']}

api = falcon.API()
weather_endpoint = WeatherResource()
api.add_route('/weather/latest', weather_endpoint, suffix='weather_latest')
