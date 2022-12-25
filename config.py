import json

with open("config.json") as config_json:
    conf = json.load(config_json)

def get_accuweather_api_key():
    return conf['accuweather-api-key']

def get_location():
    return conf['location']