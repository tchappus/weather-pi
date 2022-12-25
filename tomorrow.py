import requests
import json
import datetime

with open("./config.json") as config_file:
    api_key = json.load(config_file)['tomorrow-api-key']

with open("./ref-data.json") as ref_data:
    weather_codes = json.load(ref_data)['weatherCode']


def get_weather_1h(coords):
    response = requests.get("https://api.tomorrow.io/v4/timelines", params={ 'location': coords,
    'fields': 'temperature,weatherCode,humidity,windSpeed,windDirection,precipitationProbability,precipitationType,precipitationIntensity',
    'timesteps': '1h',
    'units': 'imperial',
    'timezone': 'America/New_York',
    'apikey': api_key })
    print(json.dumps(response.json(), indent=4))
    return response.json()

def get_weather_1d(coords):
    response = requests.get("https://api.tomorrow.io/v4/timelines", params={ 'location': coords,
    'fields': 'temperature,weatherCode,humidity,windSpeed,windDirection,precipitationProbability,precipitationType,precipitationIntensity',
    'timesteps': '1d',
    'units': 'imperial',
    'timezone': 'America/New_York',
    'apikey': api_key })
    print(json.dumps(response.json(), indent=4))
    return response.json()


weather = get_weather_1h('42.3978629,-82.1692391')
current_fields = weather['data']['timelines'][0]['intervals'][0]['values']
current_temp = round(current_fields['temperature'])
current_conds = weather_codes[str(current_fields['weatherCode'])]
current_humidity = current_fields['humidity']
current_wind_speed = current_fields['windSpeed']
current_wind_dir = current_fields['windDirection']
current_precip_prob = current_fields['precipitationProbability']
current_precip_type = current_fields['precipitationType']
current_precip_inten = current_fields['precipitationIntensity']
print(current_temp)
print(current_conds)
print(current_humidity)
print(current_wind_speed)
print(current_wind_dir)
print(current_precip_prob)
print(current_precip_inten)
print(current_precip_type)

weather_1d = get_weather_1d('42.3978629,-82.1692391')
today_fields = weather_1d['data']['timelines'][0]['intervals'][0]['values']
today_temp = round(today_fields['temperature'])
today_conds = weather_codes[str(today_fields['weatherCode'])]
today_humidity = today_fields['humidity']
today_wind_speed = today_fields['windSpeed']
today_wind_dir = today_fields['windDirection']
today_precip_prob = today_fields['precipitationProbability']
today_precip_type = today_fields['precipitationType']
today_precip_inten = today_fields['precipitationIntensity']
print(today_temp)
print(today_conds)
print(today_humidity)
print(today_wind_speed)
print(today_wind_dir)
print(today_precip_prob)
print(today_precip_inten)
print(today_precip_type)


tmrw_fields = weather_1d['data']['timelines'][0]['intervals'][1]['values']
tmrw_temp = round(tmrw_fields['temperature'])
tmrw_conds = weather_codes[str(tmrw_fields['weatherCode'])]
tmrw_humidity = tmrw_fields['humidity']
tmrw_wind_speed = tmrw_fields['windSpeed']
tmrw_wind_dir = tmrw_fields['windDirection']
tmrw_precip_prob = tmrw_fields['precipitationProbability']
tmrw_precip_type = tmrw_fields['precipitationType']
tmrw_precip_inten = tmrw_fields['precipitationIntensity']
print(tmrw_temp)
print(tmrw_conds)
print(tmrw_humidity)
print(tmrw_wind_speed)
print(tmrw_wind_dir)
print(tmrw_precip_prob)
print(tmrw_precip_inten)
print(tmrw_precip_type)
