import falcon
import json
from . resources.pages import *

class TestResource:
    def on_get(self, req, resp):
        resp.body = "server is running"

api = falcon.API()
api.add_route('/test', TestResource())
api.add_route('/pages', PagesResource())
api.add_route('/pages/shortestPath', PagesShortestPathResource())
