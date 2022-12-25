from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps
import json
import datetime
import screen

font_awesome = ImageFont.truetype('./fonts/Font Awesome 6 Free-Solid-900.otf', 16)
font_awesome_sm = ImageFont.truetype('./fonts/Font Awesome 6 Free-Solid-900.otf', 10)
monaco = ImageFont.truetype('./fonts/Monaco.ttf', 10)
monaco_lg = ImageFont.truetype('./fonts/Monaco.ttf', 14)

moon_phase_icons = {
    'FirstQuarter': {
        'icon': './icons/first-quarter.jpg',
        'desc': '1stQ'
    },
    'FullMoon': {
        'icon': './icons/full-moon.jpg',
        'desc': 'FullM'
    },
    'LastQuarter': {
        'icon': './icons/last-quarter.jpg',
        'desc': 'LastQ'
    },
    'NewMoon': {
        'icon': './icons/new-moon.jpg',
        'desc': 'NewM'
    },
    'WaningCrescent': {
        'icon': './icons/waning-cres.jpg',
        'desc': 'WanC'
    },
    'WaningGibbous': {
        'icon': './icons/waning-gib.jpg',
        'desc': 'WanG'
    },
    'WaxingCrescent': {
        'icon': './icons/waxing-cres.jpg',
        'desc': 'WaxC'
    },
    'WaxingGibbous': {
        'icon': './icons/waxing-gib.jpg',
        'desc': 'WaxG'
    }
}

with open("ref-data.json") as ref_data_file:
    ref_data = json.load(ref_data_file)

def new_image():
    global image
    image = Image.new('1', (128, 64))
    global draw
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,128, 64), outline=0, fill=0)

def draw_error():
    new_image()
    draw.text((5, 5), "Network Error", font=monaco_lg, fill=255)

def draw_layout():
     # time
    date_time = datetime.datetime.now()
    date = date_time.strftime("%a%b%d")
    time = date_time.strftime("%I:%M %p")
    draw.text((78, 50), date.rjust(8), font=monaco, fill=255)
    draw.text((78, 40), time.rjust(8), font=monaco, fill=255)

    # other weather icons
    draw.text((78, 3), "\uf0e9", font=font_awesome_sm, fill=255)
    draw.text((78, 15), "\uf043", font=font_awesome_sm, fill=255)
    draw.text((78, 27), "\uf72e", font=font_awesome_sm, fill=255)

def draw_current(weather):
    draw_layout()
    draw.text((5, 3), "Right Now", font=monaco, fill=255)

    try:
        # temp
        temp = round(weather[0]['Temperature']['Value'])
        wind_speed = str(round(weather[0]['Wind']['Speed']['Value']))
        code = weather[0]['WeatherIcon']
        humidity = str(round(weather[0]['RelativeHumidity']))
        precip_prob = str(round(weather[0]['PrecipitationProbability']))

        if temp >= 1:
            temp = str(round((temp * 1.8) + 32)) + "°F"
        else:
            temp = str(temp) + "°C"

        draw.text((5, 19), ref_data['weatherCodes'][code]['icon'], font=font_awesome, fill=255)
        draw.text((32, 19), temp, font=monaco_lg, fill=255)
        desc = ref_data['weatherCodes'][code]['desc'].split("\n")
        draw.text((5, 40), desc[0], font=monaco, fill=255)
        if len(desc) > 1:
            draw.text((5, 50), desc[1], font=monaco, fill=255)

        # other weather
        ## percentage percipitation
        draw.text((90, 3), (str(precip_prob) + "%").rjust(6), font=monaco, fill=255)

        ## humidity
        draw.text((90, 15), (str(humidity) + "%").rjust(6), font=monaco, fill=255)

        ## wind speed
        draw.text((90, 27), (str(wind_speed) + " kph").rjust(6), font=monaco, fill=255)
    except:
        draw_error()

def draw_today(weather):
    draw_layout()

    draw.text((5, 3), "Today", font=monaco, fill=255)

    try:
        # temp
        temp = round(weather['DailyForecasts'][0]['Temperature']['Maximum']['Value'])
        wind_speed = str(round(weather['DailyForecasts'][0]['Day']['Wind']['Speed']['Value']))
        code = weather['DailyForecasts'][0]['Day']['Icon']
        precip_prob = str(round(weather['DailyForecasts'][0]['Day']['PrecipitationProbability']))

        if temp >= 1:
            temp = str(round((temp * 1.8) + 32)) + "°F"
        else:
            temp = str(temp) + "°C"

        draw.text((5, 19), ref_data['weatherCodes'][code]['icon'], font=font_awesome, fill=255)
        draw.text((32, 19), temp, font=monaco_lg, fill=255)
        desc = ref_data['weatherCodes'][code]['desc'].split("\n")
        draw.text((5, 40), desc[0], font=monaco, fill=255)
        if len(desc) > 1:
            draw.text((5, 50), desc[1], font=monaco, fill=255)

        # other weather
        ## percentage percipitation
        draw.text((90, 3), (str(precip_prob) + "%").rjust(6), font=monaco, fill=255)

        ## wind speed
        draw.text((90, 27), (str(wind_speed) + " kph").rjust(6), font=monaco, fill=255)
    except:
        draw_error()

def draw_tomorrow(weather):
    draw_layout()

    draw.text((5, 3), "Tomorrow", font=monaco, fill=255)

    try:
        # temp
        temp = round(weather['DailyForecasts'][1]['Temperature']['Maximum']['Value'])
        wind_speed = str(round(weather['DailyForecasts'][1]['Day']['Wind']['Speed']['Value']))
        code = weather['DailyForecasts'][1]['Day']['Icon']
        precip_prob = str(round(weather['DailyForecasts'][1]['Day']['PrecipitationProbability']))

        if temp >= 1:
            temp = str(round((temp * 1.8) + 32)) + "°F"
        else:
            temp = str(temp) + "°C"

        draw.text((5, 19), ref_data['weatherCodes'][code]['icon'], font=font_awesome, fill=255)
        draw.text((32, 19), temp, font=monaco_lg, fill=255)
        desc = ref_data['weatherCodes'][code]['desc'].split("\n")
        draw.text((5, 40), desc[0], font=monaco, fill=255)
        if len(desc) > 1:
            draw.text((5, 50), desc[1], font=monaco, fill=255)

        # other weather
        ## percentage percipitation
        draw.text((90, 3), (str(precip_prob) + "%").rjust(6), font=monaco, fill=255)

        ## wind speed
        draw.text((90, 27), (str(wind_speed) + " kph").rjust(6), font=monaco, fill=255)
    except:
        draw_error()


def draw_five_day(weather):
    draw.text((5, 3), "Next 4 Days", font=monaco, fill=255)

    try:
        for i in range(4):
            day = weather['DailyForecasts'][i]
            temp = round(day['Temperature']['Maximum']['Value'])
            code = day['Day']['Icon']

            if temp >= 1:
                temp = str(round((temp * 1.8) + 32)) + "°F"
            else:
                temp = str(temp) + "°C"

            
            draw.text((2 + (i * 32), 32), ref_data['weatherCodes'][code]['icon'], font=font_awesome, fill=255)
            draw.text((2 + (i * 32), 50), temp, font=monaco, fill=255)
            draw.text((2 + (i * 32), 19), (datetime.datetime.now() + datetime.timedelta(days=i)).strftime("%b%d"), font=monaco, fill=255)
    except:
        draw_error()
    
def draw_moons(weather):
    draw.text((5, 3), "Next 4 Days", font=monaco, fill=255)

    try:
        for i in range(4):
            day = weather['DailyForecasts'][i]
            phase = day['Moon']['Phase']
            
            moon_img = Image.open(moon_phase_icons[phase]['icon'])
            moon_img = ImageOps.invert(moon_img)
            moon_img = moon_img.resize((16, 16))
            image.paste(moon_img, (5 + (i * 32), 32))
            draw.text((2 + (i * 32), 50), moon_phase_icons[phase]['desc'], font=monaco, fill=255)
            draw.text((2 + (i * 32), 19), (datetime.datetime.now() + datetime.timedelta(days=i)).strftime("%b%d"), font=monaco, fill=255)
    except:
        draw_error()


def show():
    #image.show()
    screen.display(image)