import psycopg2
import requests
import os
import urllib.parse as urlparse
import operator
import json


url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port


def check_exists(track_id, cursor):
    exists_query = '''
    select exists (
        select 1
        from pets
        where animal_id = %s
    )'''
    cursor.execute(exists_query, (track_id,))
    return cursor.fetchone()[0]


def update():
    res = requests.get(
        "https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL")
    result = res.json()
    total = {}
    try:
        connection = psycopg2.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      dbname=dbname)

        # local
        # connection = psycopg2.connect(user="postgres",
        #                               password="0725",
        #                               host="127.0.0.1",
        #                               port="5432",
        #                               dbname="pets")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")

        # Selecting rows from pets table using cursor.fetchall
        select_all = "select * from pets"
        cursor.execute(select_all)
        Pets = cursor.fetchall()

        # Check if pets adopted and delete
        delete_query = """Delete from pets where animal_id = %s"""
        deleted_count = 0
        for index in range(len(Pets)):
            exist = Pets[index][0] in map(operator.itemgetter("animal_id"), result)
            if exist:
                pass
            else:
                cursor.execute(delete_query, (Pets[index][0],))
                connection.commit()
                deleted_count += 1
        
        # Check if api data in db and save to db
        insert_query = """ INSERT INTO pets (animal_id, animal_subid, animal_area_pkid, animal_shelter_pkid, animal_place, animal_kind, animal_sex, animal_bodytype, animal_colour, animal_age, animal_sterilization, animal_bacterin, animal_foundplace, animal_title, animal_status, animal_remark, animal_caption, animal_opendate, animal_closeddate, animal_update, animal_createtime, shelter_name, album_file, album_update, "cDate", shelter_address, shelter_tel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        inserted_count = 0
        for index in range(len(result)):
            # if not exist in db => save to db
            key = result[index]["animal_id"]
            exists = check_exists(key, cursor)
            if(exists):
                pass
            else:
                record = result[index]
                record_to_insert = (record["animal_id"], record["animal_subid"], record["animal_area_pkid"], record["animal_shelter_pkid"], record["animal_place"], record["animal_kind"], record["animal_sex"], record["animal_bodytype"], record["animal_colour"], record["animal_age"], record["animal_sterilization"], record["animal_bacterin"], record["animal_foundplace"],
                                    record["animal_title"], record["animal_status"], record["animal_remark"], record["animal_caption"], record["animal_opendate"], record["animal_closeddate"], record["animal_update"], record["animal_createtime"], record["shelter_name"], record["album_file"], record["album_update"], record["cDate"], record["shelter_address"], record["shelter_tel"])
                cursor.execute(insert_query, record_to_insert)
                connection.commit()
                inserted_count += 1

        total["delete"] = deleted_count
        total["insert"] = inserted_count
        total["api"] = len(result)
        total["db"] = len(Pets)

    except(Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            return(json.dumps(total))
            print("PostgreSQL connection is closed")


if __name__ == "__main__":
    update()
