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

    def search_title(self, title, limit=10):
        query = """
            MATCH (p: Page)
            WHERE p.title =~ {regex}
            RETURN p.title as title, p.id as id
            LIMIT {limit}
        """
        results = self.__db.fetch(query,
                {'regex': '(?i).*%s.*' % title, 'limit': limit})
        return results
