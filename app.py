from flask import Flask
from flask_cors import CORS, cross_origin
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
@cross_origin()
def home():
    animal_id = request.args.get("animal_id")
    animal_kind = request.args.get("animal_kind")
    top = request.args.get("top")
    skip = request.args.get("skip")
    result = Query().query_all(animal_id, animal_kind, top, skip)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
    return(response)
    # return(json.dumps(result, cls=DateEncoder, ensure_ascii=False))


@app.route("/update", methods=["GET"])
@cross_origin()
def new():
    return update()

        
if __name__ == "__main__":
    app.run()
