from neo4j.v1.exceptions import ResultError

class Pages:
    def __init__(self, db):
        self.__db = db

    def select(self, params):
        search_params = {
            'limit': 10
        }
        where_clause = ""

        #todo: should move this kind of check to middleware
        if 'limit' in params and params['limit'].isdigit():
            search_params['limit'] = int(params['limit'])
        if 'startsWith' in params:
            where_clause = where_clause + \
                "AND p.title STARTS WITH {startsWith}\n"
            search_params['startsWith'] = params['startsWith']

        query = """
            MATCH (p: Page)
            WHERE 1=1
            %s
            RETURN p.title as title, p.id as id
            LIMIT {limit}
        """ % where_clause

        results = self.__db.fetch(query, search_params)
        return results

    def shortest_path(self, start, end):
        query = """
            MATCH (a:Page {id:{start}}), (b:Page {id:{end}}),
            p = shortestPath((a)-[*]->(b))
            RETURN p AS path
        """
        results = self.__db.fetch(query,
                {'start': start, 'end': end})
        try:
            return results.single()['path'].nodes
        except ResultError:
            return []
