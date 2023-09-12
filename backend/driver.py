from google.cloud.sql.connector import Connector
import sqlalchemy
import google.auth

import os
from dotenv import load_dotenv

import db_modules

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

if __name__ == "__main__":
    
    # create connection pool with 'creator' argument to our connection object function
    engine = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )

    credentials, project_id = google.auth.default()
    
    # res = db_modules.highest_crime_occurences(engine)
    # for i in res:
        # print(i)

    # db_modules.create_user(engine, "Aydan Test", 12, "M", "X", "aydan@test.com", "hashedpassword")

    # res = db_modules.login_user(engine, "joseph07@example.com", "Pp!0X2ltxc")
    # res = db_modules.login_user(engine, "aydan@test.com", "hashedpassword")


    # res = db_modules.get_crimes_by_crimecode(engine, 624)
    # print(res)

    # res = db_modules.get_all_crimecodes(engine)
    
    # FIRST TEST CASE - ADD A USER, TEST THAT UPDATE PASSWORD WORKS, LOGIN WORKS, CHANGE PASSWORD WORKS, LOGIN IS UPDATED TO WORK WITH THIS
    db_modules.remove_user(engine, "aydan@test.com")
    db_modules.create_user(engine, "aydan@test.com", 18, 'M', 'X', "aydan@test.com", "hashedpassword")
    res = db_modules.login_user(engine, "aydan@test.com", "hashedpassword")
    print("initial login", res)
    db_modules.update_password(engine, "aydan@test.com", "newpassword")
    res = db_modules.login_user(engine, "aydan@test.com", "hashedpassword")
    print("login with wrong password",res)
    res = db_modules.login_user(engine, "aydan@test.com", "newpassword")
    print("login with new password", res)
    db_modules.remove_user(engine, "aydan@test.com")