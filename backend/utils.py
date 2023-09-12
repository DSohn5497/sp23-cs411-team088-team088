def generate_most_probable_crimes_data(data):
    crime_code = data[0]
    description = data[1]
    probability = float(data[2])
    return {
        "crimeCode": crime_code,
        "description": description,
        "probability": probability,
    }

def generate_highest_crime_counts_data(data):
    area = data[0]
    count = data[1]
    return {
        "area": area,
        "count": count,
    }

def generate_nearest_crime_data(data):
    crime = generate_crime_data(data[:-1])
    probability = float(data[14])
    return {
        'crime': crime,
        'probability': probability
    }


def generate_crime_data(data):
    crime_id = data[0]
    crime_code = data[1]
    crime_code_description = data[2]
    time_occured = data[3]
    victim_id = data[4]
    age = data[5]
    sex = data[6]
    descent = data[7]
    location_id = data[8]
    latitude = data[9]
    longitude = data[10]
    area = data[11]
    street = data[12]
    weapon_id = data[13]
    return {
        "id": crime_id,
        "crimeCode": {
            "code": crime_code,
            "description": crime_code_description,
        },
        "timeOccuredAt": time_occured.isoformat(),
        "victim": {
            "id": victim_id,
            "age": age,
            "sex": sex,
            "descent": descent,
        },
        "location": {
            "id": location_id,
            "latitude": latitude,
            "longitude": longitude,
            "area": area,
            "street": street,
        },
        "weapon": {
            "code": weapon_id,
            "description": "",
        }
    }

def generate_user_response(user_data):
    res_userID = user_data[0]
    res_name = user_data[1]
    res_age = user_data[2]
    res_sex = user_data[3]
    res_descent = user_data[4]
    res_email = user_data[5]
    res_password = user_data[6]

    response_data = {
        "userID": res_userID,
        "name": res_name,
        "age": res_age,
        "sex": res_sex,
        "descent": res_descent,
        "email": res_email,
        "password": res_password
    }
    return response_data