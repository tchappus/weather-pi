import time
import accuweather
import image

STATE_CURRENT = 1
STATE_TODAY = 2
STATE_TOMORROW = 3
STATE_FIVE_DAY = 4
STATE_MOONS = 5

timer = 0
state = STATE_CURRENT
data_timer = 0

def fetch_weather():
    try:
        global weather_1h
        weather_1h = accuweather.get_weather_1h()
    except:
        weather_1h = None
    
    try:
        global weather_5d
        weather_5d = accuweather.get_weather_5d()
    except:
        weather_5d = None

fetch_weather()

while True:
    image.new_image()

    if data_timer > 3600:
        data_timer = 0
        fetch_weather()
    else:
        data_timer = data_timer + 1

    if timer > 5:
        state = state + 1
        if state > STATE_MOONS:
            state = STATE_CURRENT

        timer = 0
    
    if weather_1h == None or weather_5d == None:
        image.draw_error()

    elif state == STATE_CURRENT:
        image.draw_current(weather_1h)
        
    elif state == STATE_TODAY:
        image.draw_today(weather_5d)

    elif state == STATE_TOMORROW:
        image.draw_tomorrow(weather_5d)

    elif state == STATE_FIVE_DAY:
        image.draw_five_day(weather_5d)
    
    elif state == STATE_MOONS:
        image.draw_moons(weather_5d)


    timer = timer + 1

    image.show()
    time.sleep(1)
