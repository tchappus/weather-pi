import requests
import config
import json

api_key = config.get_accuweather_api_key()
location = config.get_location()

def get_weather_1h():
    response = requests.get("https://dataservice.accuweather.com/forecasts/v1/hourly/1hour/" + location, params={
        'apikey': api_key,
        'details': 'true',
        'metric': 'true'
    })
    return response.json()
    # with open("./sample-hourly.json") as output:
    #     weather = json.load(output)
    # return weather

def get_weather_5d():
    # with open("./output.json") as output:
    #     weather = json.load(output)
    # return weather
    response = requests.get("https://dataservice.accuweather.com/forecasts/v1/daily/5day/" + location, params={
        'apikey': api_key,
        'details': 'true',
        'metric': 'true'
    })
    return response.json()

