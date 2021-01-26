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
    def query_all(self, animal_id, animal_kind, top, skip, animal_bodytype, animal_sex, animal_age, animal_area_pkid, animal_sterilization, animal_bacterin):
        if ((animal_id is None) and (animal_kind is None) and (top is None) and (skip is None) and (animal_bodytype is None) and (animal_sex is None) and (animal_age is None) and (animal_area_pkid is None)  and (animal_sterilization is None) and (animal_bacterin is None)):
            # Selecting rows from pets table using cursor.fetchall
            select_all_query = "SELECT * FROM pets ORDER BY pets.c_date DESC"
            self.cursor.execute(select_all_query)
            Pets = self.cursor.fetchall()
            # result = json.dumps(Pets, ensure_ascii=False, indent=2)
            return(Pets)
        else:
            # optional parameters
            query = "SELECT * FROM (SELECT * FROM pets ORDER BY pets.c_date DESC) p WHERE (p.animal_id=%(id)s OR %(id)s IS NULL) AND (animal_kind=%(kind)s OR %(kind)s IS NULL) AND (animal_bodytype=%(bodytype)s OR %(bodytype)s IS NULL) AND (animal_sex=%(sex)s OR %(sex)s IS NULL) AND (animal_age=%(age)s OR %(age)s IS NULL) AND (animal_area_pkid=%(area)s OR %(area)s IS NULL) AND (animal_area_pkid=%(area)s OR %(area)s IS NULL) AND (animal_sterilization=%(sterilization)s OR %(sterilization)s IS NULL) AND (animal_bacterin=%(bacterin)s OR %(bacterin)s IS NULL) LIMIT %(top)s OFFSET %(skip)s"
            param = dict(id=animal_id, kind=animal_kind, bodytype=animal_bodytype, sex=animal_sex, age=animal_age, area=animal_area_pkid, sterilization=animal_sterilization, bacterin=animal_bacterin, top=top, skip=skip)
            print(param)
            self.cursor.execute(query, param)
            result = self.cursor.fetchall()
            return(result)

    def __del__(self):
        self.cursor.close()
        self.connection.close()


if __name__ == "__main__":
    # instantiate a class
    q = Query().query()
