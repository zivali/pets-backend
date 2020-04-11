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
    def query_all(self, animal_id, animal_kind, top, skip):
        if ((animal_id is None) and (animal_kind is None) and (top is None) and (skip is None)):
            # Selecting rows from pets table using cursor.fetchall
            select_all_query = "SELECT * FROM pets"
            self.cursor.execute(select_all_query)
            print(animal_id)
            Pets = self.cursor.fetchall()
            # result = json.dumps(Pets, ensure_ascii=False, indent=2)
            return(Pets)
        else:
            # optional parameters
            query = "SELECT * FROM (SELECT * FROM pets ORDER BY pets.c_date DESC) p WHERE (p.animal_id=%(id)s OR %(id)s IS NULL) AND (animal_kind=%(kind)s OR %(kind)s IS NULL) LIMIT %(top)s OFFSET %(skip)s"
            param = dict(id=animal_id, kind=animal_kind, top=top, skip=skip)
            self.cursor.execute(query, param)
            result = self.cursor.fetchall()
            return(result)

    def __del__(self):
        self.cursor.close()
        self.connection.close()


if __name__ == "__main__":
    # instantiate a class
    q = Query().query()
