import falcon
import json
from . resources.pages import *

class TestResource:
    def on_get(self, req, resp):
        quote = {
            'quote': 'whatever',
            'author': 'nirvana'
        }
        resp.body = json.dumps(quote)

api = falcon.API()
api.add_route('/test', TestResource())
api.add_route('/pages', PageResource())
api.add_route('/pages/search/{title}', PageSearchTitleResource())
