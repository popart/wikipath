from config import env
from database.pages import Pages
from database.neo4jconn import Neo4JConn

db_api = {
    "db_addr": "localhost",
    "db_port": 7687,
    "username": "neo4j",
    "password": "moatkongargos"
}
#db = Neo4JConn(**db_api)
db = Neo4JConn(**env.db_settings)

pages = Pages(db)
res = pages.select()

for r in res:
    print(r['title'])
"""
db = Neo4JConn(**db_api)
"""


