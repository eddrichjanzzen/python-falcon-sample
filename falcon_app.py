import falcon

class ThingsResource(object):
	def on_get(self, req, resp):
		"""Handles GET requests"""
		resp.status = falcon.HTTP_200
		resp.body = ('Hello world')


app = falcon.API()

things = ThingsResource()

app.add_route('/things', things)