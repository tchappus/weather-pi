# weather-pi

This is a Python program that runs on a Raspberry Pi in my parent's kitchen that provides weather updates on a Adafruit 128x64 OLED display. It shows the current weather and other forecasts. 

## Requirements

* a Raspberry Pi
* initialize a venv and install the required packages using the provided requirements.txt file
* install Adafruit Blinka and CircuitPython - https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
* An API key for AccuWeather and the location key for the location you'd like to fetch the weather stats for. API Reference - https://developer.accuweather.com
* Font files, including for Font Awesome - https://fontawesome.com/

## Configuration

Create a config.json file with two key/values:

```json
{
    "accuweather-api-key": "<api key>",
    "location": "<accuweather location key>"
}
```
