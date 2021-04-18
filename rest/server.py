import falcon, json


class CompaniesResource(object):
  companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
  people = {"Mike": {"likes": "Heavy Metal"}, "Bob": {"likes": "Mince"}}

  def on_get_companies(self, req, resp):
    resp.body = json.dumps(self.companies)

  def on_get_people(self, req, resp):
    resp.body = json.dumps(self.people)

  def on_post_people(self, req, resp):
    resp.status = falcon.HTTP_201
    resp.body = json.dumps({'success': True})
    j = json.loads(req.stream.read(req.content_length or 0))
    self.people[j['name']] = {"likes": j['likes']}

api = falcon.API()
companies_endpoint = CompaniesResource()
api.add_route('/companies', companies_endpoint, suffix='companies')
api.add_route('/people', companies_endpoint, suffix='people')
