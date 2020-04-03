import psycopg2
import urllib.parse as urlparse
import os
from psycopg2.extras import RealDictCursor
import json

url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port


class Query:
    def __init__(self):
        self.connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  dbname=dbname)

        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        # Print PostgreSQL Connection properties
        print(self.connection.get_dsn_parameters(), "\n")

    # TODO imporve performance
    def query_all(self):
        # Selecting rows from pets table using cursor.fetchall
        select_all = "select * from pets"
        self.cursor.execute(select_all)
        Pets = self.cursor.fetchall()
        # result = json.dumps(Pets, ensure_ascii=False, indent=2)
        return(Pets)

    # def query_by_condition(self):

    def __del__(self):
        self.cursor.close()
        self.connection.close()


if __name__ == "__main__":
    # instantiate a class
    q = Query().query()
