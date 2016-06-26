from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687",
        auth=basic_auth("neo4j", "moatkongargos"))
session = driver.session()

# import files must be located in neo4j-*/import
res = session.run("""
        USING PERIODIC COMMIT 1000
        LOAD CSV FROM "file:///pages.csv" AS line
        FIELDTERMINATOR '|'
        CREATE (:Page {id:toInt(line[0]), title: line[1]})
        """)

for r in res:
    print(r)

session.close()
