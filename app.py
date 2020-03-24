from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import requests
import os
from open_gov import update
import json

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import Pets


@app.route("/", methods=["GET"])
def home():
    # return json.dumps(update(), ensure_ascii=False)
    res = requests.get(
        "https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL")
    result = res.json()
    
    for index in range(len(result)):
        # if not exist in db => save to db
        exists = db.session.query(Pets.animal_id).filter_by(
            animal_id=result[index]["animal_id"]).scalar() is not None
        if(exists):
            pass
        else:
            try:
                pet = Pets(
                    animal_id=result[index]["animal_id"],
                    animal_subid=result[index]["animal_subid"],
                    animal_area_pkid=result[index]["animal_area_pkid"],
                    animal_shelter_pkid=result[index]["animal_shelter_pkid"],
                    animal_place=result[index]["animal_place"],
                    animal_kind=result[index]["animal_kind"],
                    animal_sex=result[index]["animal_sex"],
                    animal_bodytype=result[index]["animal_bodytype"],
                    animal_colour=result[index]["animal_colour"],
                    animal_age=result[index]["animal_age"],
                    animal_sterilization=result[index]["animal_sterilization"],
                    animal_bacterin=result[index]["animal_bacterin"],
                    animal_foundplace=result[index]["animal_foundplace"],
                    animal_title=result[index]["animal_title"],
                    animal_status=result[index]["animal_status"],
                    animal_remark=result[index]["animal_remark"],
                    animal_caption=result[index]["animal_caption"],
                    animal_opendate=result[index]["animal_opendate"],
                    animal_closeddate=result[index]["animal_closeddate"],
                    animal_update=result[index]["animal_update"],
                    animal_createtime=result[index]["animal_createtime"],
                    shelter_name=result[index]["shelter_name"],
                    album_file=result[index]["album_file"],
                    album_update=result[index]["album_update"],
                    cDate=result[index]["cDate"],
                    shelter_address=result[index]["shelter_address"],
                    shelter_tel=result[index]["shelter_tel"]
                )
                db.session.add(pet)
                db.session.commit()
                print("added"+str(result[index]["animal_id"]))
            except Exception as e:
                print(str(e))

    return(str(len(result)))
    # return json.dumps(result[0], ensure_ascii=False)


if __name__ == "__main__":
    app.run()
