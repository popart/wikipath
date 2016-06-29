from .. config import env
from .. database import pages
from .. database import neo4jconn

import json
import falcon

class PagesResource:
    def __init__(self):
        self.db = neo4jconn.Neo4JConn(**env.db_settings)
        self.pages = pages.Pages(self.db)

    def on_get(self, req, resp):
        res = self.pages.select(req.params)
        out = list(map(lambda record: {
                'id': record['id'],
                'title': record['title']
            }, res))
        resp.body = json.dumps(out)

class PagesCountResource:
    def __init__(self):
        self.db = neo4jconn.Neo4JConn(**env.db_settings)
        self.pages = pages.Pages(self.db)

    def on_get(self, req, resp):
        res = self.pages.count(req.params)
        resp.body = json.dumps(res)

class PagesShortestPathResource:
    def __init__(self):
        self.db = neo4jconn.Neo4JConn(**env.db_settings)
        self.pages = pages.Pages(self.db)

    def on_get(self, req, resp):
        try:
            start = req.params['start']
            end = req.params['end']
        except KeyError as e:
            raise falcon.HTTPMissingParam(e.args[0])

        path = self.pages.shortest_path(start, end)
        out = list(map(lambda node: node.properties, path))
        resp.body = json.dumps(out)
