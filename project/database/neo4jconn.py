from neo4j.v1 import GraphDatabase, basic_auth

""" Neo4J database connector """
class Neo4JConn:

    def __init__(self, **kwargs):
        #super(Neo4JConn, self).__init__()
        config = {
            'host': kwargs['db_addr'],
            'port': kwargs['db_port'],
            'user': kwargs['username'],
            'password': kwargs['password']
        }
        driver = GraphDatabase.driver(
                "bolt://%s:%d" % (config['host'], config['port']),
                auth=basic_auth(config['user'], config['password']))
        self.__session = driver.session()

    def run(self, query, params):
        # should I create & close a new session for each query?
        self.__session.run(query, params)

    def fetch(self, query, params):
        return self.__session.run(query, params)

    def __del__(self):
        if self.__session:
            self.__session.close()
