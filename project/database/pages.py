#from database.neo4jconn import Neo4JConn

class Pages:
    def __init__(self, db):
        self.__db = db

    def select(self):
        query = """
            MATCH (p: Page)
            RETURN p.title as title, p.id as id
            LIMIT {limit}
        """
        results = self.__db.fetch(query, {'limit': 10})
        return results

    def search_title(self, title, limit=8):
        query = """
            MATCH (a:Page)
            WHERE a.title STARTS WITH {title}
            RETURN a.title as title, a.id as id
            LIMIT {limit}
        """
        results = self.__db.fetch(query,
                {'title': title, 'limit': limit})
        return results

    def shortest_path(self, a_id, b_id):
        query = """
            MATCH (a:Page {id:{a_id}}), (b:Page {id:{b_id}}),
            p = shortestPath((a)-[*]->(b))
            RETURN p
        """
        results = self.__db.fetch(query,
                {'a_id': a_id, 'b_id': b_id})
        try:
            return results.next()['path'].nodes
        except StopIteration:
            return []
