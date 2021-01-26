from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from service.open_gov import update
from service.query import Query
from flask import jsonify, request
import json
from datetime import date


# encode column c_date 
class DateEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, date):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


app = Flask(__name__)
# CORS config
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# json config
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False
app.json_encoder = DateEncoder

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/", methods=["GET"])
def home():
    animal_id = request.args.get("animal_id")
    animal_kind = request.args.get("animal_kind")
    top = request.args.get("top")
    skip = request.args.get("skip")
    animal_bodytype  = request.args.get("animal_bodytype")
    animal_sex  = request.args.get("animal_sex")
    animal_age = request.args.get("animal_age")
    animal_area_pkid = request.args.get("animal_area_pkid")
    animal_sterilization = request.args.get("animal_sterilization")
    animal_bacterin = request.args.get("animal_bacterin")
    result = Query().query_all(animal_id, animal_kind, top, skip, animal_bodytype, animal_sex, animal_age, animal_area_pkid, animal_sterilization, animal_bacterin)
    response = jsonify(result)
    # response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
    return(response)
    # return(json.dumps(result, cls=DateEncoder, ensure_ascii=False))


@app.route("/update", methods=["GET"])
def new():
    return update()

        
if __name__ == "__main__":
    app.run()
