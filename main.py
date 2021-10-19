import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")

nut_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("What exercise did you do today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

nut_params = {
    "query": exercise_text,
    "gender": "female",
    "weight_kg": 60,
    "height_cm": 155,
    "age": 24,
}

response = requests.post(url=nut_endpoint, json=nut_params, headers=headers)
response.raise_for_status()
workout_json = response.json()

sheety_endpoint = "https://api.sheety.co/f152023cd2003d67eac458538ae45d0b/myWorkouts/sheet1"

sheety_auth = {
    "Authorization": "Bearer 99898ye9sifj9d948y9sdfiu89u98uds9f8u89dun"
}

today = datetime.now()
today_formatted = today.strftime("%x")
time_formatted = today.strftime("%X")

for x in workout_json["exercises"]:

    exercise = x["name"].title()

    duration = round(x["duration_min"])

    calories = round(x["nf_calories"])

    sheety_params = {
        "sheet1": {
            "date": today_formatted,
            "time": time_formatted,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    sheety_response = requests.post(sheety_endpoint, json=sheety_params, headers=sheety_auth)
    # sheety_response.raise_for_status()
    print(sheety_response.text)
