import sqlalchemy
from uuid import uuid4

# TODO:
# Create user account
# Login with a user (verify if username and hashed password match, check if they're the same) -> Nullable User Object
# Read user histories -> POST
# Update user histories
# Clear user histories
# Get all crimes within a certain region (small)
# Get list of crime code strings, keep the mapping, 
# Get all crimes that have a certain crime code
# Update user's last search

def create_user(engine, name, age, sex, descent, email, password):
    userID = str(uuid4())
    # userID = 1002
    with engine.connect() as db_conn:
        # VALUES(\"{userID}\", \"{name}\", {age}, \"{sex}\", \"{descent}\", \"{email}\", \"{password}\");
        query = \
        f'''
            INSERT INTO Users (userID, name, age, sex, descent, email, password) 
            VALUES(\"{userID}\", \"{name}\", {age}, \"{sex}\", \"{descent}\", \"{email}\", \"{password}\");
        '''
        db_conn.execute(sqlalchemy.text(query))
        db_conn.commit()
    return login_user(engine, email, password)

def login_user(engine, email, password):
    with engine.connect() as db_conn:
        query = \
        f'''
            SELECT
                *
            FROM Users
            WHERE
                email = \"{email}\"
                AND password = \"{password}\"
            ;
        '''
        results = db_conn.execute(sqlalchemy.text(query)).fetchall()
    return results

def update_password(engine, email, old_password, new_password):
    with engine.connect() as db_conn:
        query = \
        f'''
            UPDATE Users
            SET password=\"{new_password}\"
            WHERE email = \"{email}\"; 
            '''
        db_conn.execute(sqlalchemy.text(query))
        db_conn.commit()
    return login_user(engine, email, new_password)

def remove_user(engine, email):
    with engine.connect() as db_conn:
        query = \
        f'''
            DELETE FROM Users
            WHERE email = \"{email}\"; 
            '''
        db_conn.execute(sqlalchemy.text(query))
        db_conn.commit()
    return True

def create_user_history(engine, userID, latitude, longitude):
    with engine.connect() as db_conn:
        query = \
        f'''INSERT INTO UserHistories (UserID, latitude, longitude, timestamp) VALUES (\"{userID}\", {latitude}, {longitude}, NOW());
        '''
        db_conn.execute(sqlalchemy.text(query))
        db_conn.commit()
    return True

def read_user_history(engine, userID):
    with engine.connect() as db_conn:
        query = \
        f'''
            SELECT *
            FROM UserHistories
            WHERE UserID = \"{userID}\"
        ;
        '''
        results = db_conn.execute(sqlalchemy.text(query)).fetchall()
    return results

def clear_user_history(engine, userID):
    with engine.connect() as db_conn:
        query = \
        f'''DELETE FROM UserHistories WHERE userID = \"{userID}\";
        '''
        db_conn.execute(sqlalchemy.text(query))
        db_conn.commit()
    return True

# TODO: Blocked until we can actually match the locations to the crimes
def get_bounded_crimes(engine, min_longitude=0, max_longitude=0, min_latitude=0, max_latitude=0, start_date=0, end_date=0):
    with engine.connect() as db_conn:
        query = \
        f'''
            SELECT crimeID, crimeCode, description, timeOccurred, victimID, age, sex, descent, locationID, latitude, longitude, area, street, weaponID FROM Crimes NATURAL JOIN CrimeCodes NATURAL JOIN AffectedBy NATURAL JOIN Victims NATURAL JOIN VictimizedAt NATURAL JOIN Locations;
        '''
        result = db_conn.execute(sqlalchemy.text(query)).fetchall()
    return result

def get_crimes_by_crimecode(engine, crimeCode):
    with engine.connect() as db_conn:
        query = \
        f'''
            SELECT crimeID, crimeCode, description, timeOccurred, victimID, age, sex, descent, locationID, latitude, longitude, area, street, weaponID FROM Crimes NATURAL JOIN CrimeCodes NATURAL JOIN AffectedBy NATURAL JOIN Victims NATURAL JOIN VictimizedAt NATURAL JOIN Locations
            WHERE crimeCode = {crimeCode};
        '''
        result = db_conn.execute(sqlalchemy.text(query)).fetchall()
    
    return result

def get_all_crimecodes(engine):
    with engine.connect() as db_conn:
        query = \
        f'''
            SELECT DISTINCT crimeCode, description
            FROM CrimeCodes;
        '''
        result = db_conn.execute(sqlalchemy.text(query)).fetchall()
    
    return result

# Most commmon crimes
def most_probable_crimes(engine):
    # connect to connection pool
    with engine.connect() as db_conn:
        query = \
        '''
            SELECT
            Crimes.CrimeCode,
            CrimeCodes.description,
            COUNT(*)/(SELECT COUNT(*) FROM Crimes) AS probability
            FROM Crimes
            JOIN CrimeCodes
            ON Crimes.crimeCode = CrimeCodes.crimeCode
            GROUP BY CrimeCode
            ORDER BY probability DESC
            LIMIT 15;
        '''

        results = db_conn.execute(sqlalchemy.text(query)).fetchall()
    return results

def highest_crime_counts(engine):
    with engine.connect() as db_conn:
        query = \
        '''
            SELECT Area, COUNT(*) AS TotalCount
            FROM Locations
            JOIN VictimizedAt
                ON (Locations.locationID = VictimizedAt.locationID)
            JOIN Victims
                ON (VictimizedAt.victimID = Victims.victimID)
            GROUP BY Area
            ORDER BY COUNT(*) DESC
            LIMIT 15;
        '''

        results = db_conn.execute(sqlalchemy.text(query)).fetchall()
    return results

def get_nearest_crimes(engine, user_id):
    with engine.connect() as db_conn:
        query = \
        f'''
        SELECT crimeID, crimeCode, description, timeOccurred, victimID, age, sex, descent, locationID, latitude, longitude, area, street, weaponID, probability
        FROM Crimes
        NATURAL JOIN CrimeCodes
        NATURAL JOIN AffectedBy
        NATURAL JOIN Victims
        NATURAL JOIN VictimizedAt
        NATURAL JOIN Locations
        NATURAL JOIN NearestCrimes
        WHERE userID = "{user_id}";
        '''

        results = db_conn.execute(sqlalchemy.text(query)).fetchall()[0]
    return results
