from .. config import env
from .. database import pages
from .. database import neo4jconn

import json

class PagesResource:
    def __init__(self):
        self.db = neo4jconn.Neo4JConn(**env.db_settings)
        self.pages = pages.Pages(self.db)

    def on_get(self, req, resp):
        res = self.pages.select()
        output = []
        for r in res:
            output.append(r['title'])
        resp.body = json.dumps(output)

class PagesSearchTitleResource:
    def __init__(self):
        self.db = neo4jconn.Neo4JConn(**env.db_settings)
        self.pages = pages.Pages(self.db)

    def on_get(self, req, resp, title):
        res = self.pages.search_title(title)
        output = []
        for r in res:
            output.append(r['title'])
        resp.body = json.dumps(output)

class PagesShortestPathResource:
    def __init__(self):
        self.db = neo4jconn.Neo4JConn(**env.db_settings)
        self.pages = pages.Pages(self.db)

    def on_get(self, req, resp, a_id, b_id):
        res = self.pages.shortest_path(a_id, b_id)
        output = []
        for r in res:
            output.append(r['title'])
        resp.body = json.dumps(output)
