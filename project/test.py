import falcon
import json
from . resources.pages import *
from . resources.static import *
from . config import env

class TestResource:
    def on_get(self, req, resp):
        resp.body = "server is running"

class StaticSink:
    def __call__(self, req, resp, filename):
        file_ending = filename[filename.rfind('.'):]
        try:
            resp.content_type = env.mime_types[file_ending]
            with open('project/static/' + filename) as f:
                resp.body = f.read()
        except Exception:
            raise falcon.HTTPNotFound(description="404 Not Found")

api = falcon.API()
api.add_route('/', StaticResource())
api.add_route('/test', TestResource())
api.add_route('/pages', PagesResource())
api.add_route('/pages/shortestPath', PagesShortestPathResource())
api.add_sink(StaticSink(), r'/static/(?P<filename>.*)')
