import requests
import datetime
import os

NUT_AP_ID = "c2932629"
NUT_AP_KEY = "79c8002b2fde664316c161a6a461bdd3"
NUT_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
TOKEN = "Bearer 123"
SHEET_ENDPOINT = "https://api.sheety.co/2a9a8ad76e089ab38475204925988018/myWorkouts/workouts"
headers_nut = {
    "x-app-id": NUT_AP_ID,
    "x-app-key": NUT_AP_KEY,
}

title = input("What you did today to burn calories: ")

params_nut = {
    "query": title,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 175,
    "age": 22

}

response_nut = requests.post(url=NUT_ENDPOINT, headers=headers_nut,
                             json=params_nut)

result = response_nut.json()

headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json",
}

date = f"{datetime.datetime.now():%d/%m/%Y}"
time = f"{datetime.datetime.now().strftime("%X")}"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    print(f"{sheet_inputs["workout"]["calories"]} burned calories")

    response_sheets_post = requests.post(
        url=SHEET_ENDPOINT,
        json=sheet_inputs,
        headers=headers
    )
