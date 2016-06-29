import falcon
import os

class StaticResource:
    def on_get(self, req, resp):
        resp.content_type = "text/html"
        with open('project/static/index.html') as f:
            resp.body = f.read()
