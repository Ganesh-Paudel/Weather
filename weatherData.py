from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv("API_KEY")
url = f"https://api.weatherstack.com/current?access_key={api_key}"


def getData(city):
    queryString = { 
        "query" : city,
        "units" : "m",
        }

    response = requests.get(url, params=queryString)

    if response.status_code != 200:
        print("Failed to fetch data")
        print("Error: ", response.status_code)
        return {"Code" : response.status_code }

    else:
        data = response.json()

        print("Weather Information: ")
        print(f"location: {data['location']['name']}")
        print(f"Current Status: {data['current']['weather_descriptions'][0]}")
        print(f"Wind speed: {data['current']['wind_speed']} and Wind direction: {data['current']['wind_dir']}")
        print(f"Uv index: {data['current']['uv_index']} ")
        print(f"Feels Like: {data['current']['feelslike']}")

        Datas = {
            "Code" : response.status_code,
            "location" : data['location']['name'],
            "Current Status" : data['current']['weather_descriptions'][0],
            "Wind speed" : data['current']['wind_speed'],
            "Wind direction": data['current']['wind_dir'],
            "Uv index": data['current']['uv_index'],
            "Feels Like": data['current']['feelslike']
        }
        return Datas