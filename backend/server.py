# RUN WITH flask --app server.py run

# Networking/connectivity imports
from flask import Flask, request, Response
from flask_cors import CORS
from google.cloud.sql.connector import Connector
import sqlalchemy
import google.auth


# Internal files that we setup
import utils, db_modules

# Util imports
import os
import json
from dotenv import load_dotenv


load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
INSTANCE_NAME = os.getenv("INSTANCE_NAME")

# initialize Connector object
connector = Connector()

def getconn():
    return connector.connect(
        INSTANCE_NAME,
        "pymysql",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )


# create connection pool with 'creator' argument to our connection object function
engine = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

credentials, project_id = google.auth.default()
app = Flask(__name__)
CORS(app)

@app.before_request
def before():
    if request.method == "OPTIONS":
        return None

@app.route("/")
@app.route("/status")
def hello_world():
    return "Backend server running!"

@app.route("/create-user", methods=["POST"])
def create_user():
    name = request.args.get("name")
    age = request.args.get("age")
    sex = request.args.get("sex")
    descent = request.args.get("descent")
    email = request.args.get("email")
    password = request.args.get("password")

    if not (name and age and sex and descent and email and password):
        return Response("", status=400)
    
    res = db_modules.create_user(engine, name, age, sex, descent, email, password)
    if len(res) == 0:
        return Response("", 400)

    response_data = json.dumps(utils.generate_user_response(res[0]))
    return Response(response_data, 200)
    
@app.route("/update-password", methods=["POST", "PUT"])
def update_user():
    email = request.args.get("email")
    old_password = request.args.get("oldPassword")
    new_password = request.args.get("newPassword")

    if not (email and old_password and new_password):
        return Response("", 400)
    res = db_modules.update_password(engine, email, old_password, new_password)
    if len(res) == 0:
        return Response("", 400)

    response_data = json.dumps(utils.generate_user_response(res[0]))
    return Response(response_data, 200)
 
@app.route("/login", methods=["POST"])
def login():
    email = request.args.get("email")
    password = request.args.get("password")

    if not email and not password:
        return Response("", 400)
    
    res = db_modules.login_user(engine, email, password)
    if len(res) == 0:
        return Response("", 400)

    response_data = json.dumps(utils.generate_user_response(res[0]))
    return Response(response_data, 200)

@app.route("/delete-user", methods=["DELETE", "POST"])
def remove_user():
    print("RECV")
    email = request.values.get("email")
    print(email)
    if email and db_modules.remove_user(engine, email):
        return Response("", 200)

    return Response("", 400)

@app.route("/create-history", methods=["POST"])
def create_history():
    userID = request.args.get("userID")
    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")

    if userID and latitude and longitude and db_modules.create_user_history(engine, userID, latitude, longitude):
        return Response("", 200)
    else:
        return Response("", 400)

@app.route("/read-history", methods=["GET"])
def read_history():
    userID = request.args.get("userID")
    
    if not userID:
        return Response("", 400)
    
    res = db_modules.read_user_history(engine, userID)

    def convert_data(data):
        userID = data[0]
        locationID = data[1]
        timestamp = data[2].isoformat()
        return {"userID": userID, "locationID": locationID, "timestamp":timestamp}


    response_data = json.dumps([convert_data(data) for data in res])
    return Response(response_data, 200)

@app.route("/clear-history", methods=["GET"])
def clear_history():
    userID = request.args.get("userID")

    if userID and db_modules.clear_user_history(engine, userID):
        return Response("", 200)
    return Response("", 400)

@app.route("/crimes", methods=["GET"])
def all_crimes():
    res = db_modules.get_bounded_crimes(engine)
    response_data = json.dumps([utils.generate_crime_data(data) for data in res])
    return Response(response_data, 200)

@app.route("/all-crime-codes", methods=["GET"])
def list_crimecodes():
    res = db_modules.get_all_crimecodes(engine)
    response_data = json.dumps([{"code": data[0], "description": data[1]} for data in res])
    return Response(response_data, 200)

@app.route("/crimes-by-code", methods=["GET"])
def get_crimes_by_code():
    crimeCode = request.args.get("crimeCode")
    
    if not crimeCode:
        return Response("", 400)
    
    res = db_modules.get_crimes_by_crimecode(engine, crimeCode)
    response_data = json.dumps([utils.generate_crime_data(data) for data in res])
    return Response(response_data, 200)

@app.route("/most-probable-crimes", methods=["GET"])
def get_most_probable_crimes():
    res = db_modules.most_probable_crimes(engine)
    response_data = json.dumps([utils.generate_most_probable_crimes_data(data) for data in res])
    return Response(response_data, 200)

@app.route("/highest-crime-counts", methods=["GET"])
def get_highest_crime_counts():
    res = db_modules.highest_crime_counts(engine)
    response_data = json.dumps([utils.generate_highest_crime_counts_data(data) for data in res])
    return Response(response_data, 200)
    
@app.route("/get-nearest-crimes", methods=["GET"])
def get_nearest_crimes():
    userID = request.args.get("userID")
    if not userID:
        return Response("", 400)
    res = db_modules.get_nearest_crimes(engine, userID)
    print(res)
    response_data = json.dumps(utils.generate_nearest_crime_data(res))
    return Response(response_data, 200)