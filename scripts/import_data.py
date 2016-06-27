from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687",
        auth=basic_auth("neo4j", "moatkongargos"))
session = driver.session()

session.run("""
        USING PERIODIC COMMIT 1000
        LOAD CSV FROM "file:///pages.csv" AS line
        FIELDTERMINATOR '|'
        CREATE (:Page {id:toInt(line[0]), title: line[1]})
        """)

session.run(""" CREATE INDEX ON :Page(id) """)
session.run(""" CREATE INDEX ON :Page(title) """)

session.run("""
        USING PERIODIC COMMIT 1000
        LOAD CSV FROM "file:///links.csv" AS line
        FIELDTERMINATOR '|'
        MATCH (a:Page),(b:Page)
        WHERE a.id = toInt(line[0]) AND b.id = toInt(line[1])
        CREATE (a)-[r:LINKS_TO]->(b)
        """)

session.close()
