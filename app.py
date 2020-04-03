from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from service.open_gov import update
from service.query import Query
from flask import jsonify


app = Flask(__name__)
# json config
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/", methods=["GET"])
def home():
    result = Query().query_all()
    return(jsonify(result))


@app.route("/update", methods=["GET"])
def new():
    return update()


if __name__ == "__main__":
    app.run()
