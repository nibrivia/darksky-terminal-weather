# Uses the DarkSky API to print the weather
# https://darksky.net/dev

import requests
import os
from api_key import API_KEY

def get_forecast(params = dict(units = "si")):
    params_str = "&".join([str(key) + "=" + str(val) for key, val in params.items()])

    resp = requests.get("https://api.darksky.net/forecast/" + API_KEY + "/" + get_latlong() + "?" + params_str)
    return resp.json()

emojis = {
        "clear-day"   : "☀️",
        "clear-night" : "🌘",
        "rain"        : "🌧️",
        "snow"        : "❄️",
        "sleet"       : "sleet 🌨️",
        "wind"        : "🍃",
        "fog"         : "🌁",
        "cloudy"      : "☁️",
        "partly-cloudy-day"   : "⛅",
        "partly-cloudy-night" : "⛅"
        }

def get_latlong():
    if 'SSH_CLIENT' in os.environ:
        ip = os.environ['SSH_CLIENT'].split()[0]
        resp = requests.get("http://ipinfo.io/" + ip + "/loc")
        return resp.text.strip()

    resp = requests.get("http://ipinfo.io/loc")
    return resp.text.strip()

import json
from datetime import datetime
def pretty_summary():
    forecast = get_forecast()

    summary = forecast["hourly"]["summary"]
    icon    = emojis.get(forecast["hourly"]["icon"], "🌈")

    daily_sum  = forecast["daily"]["summary"]
    daily_icon = emojis.get(forecast["daily"]["icon"], "🌈")

    attribution = "Powered by DarkSky: https://darksky.net/poweredby/"
    
    return icon + "  " + summary + "\n" + daily_icon + "  " + daily_sum + "\n" + attribution

def one_line():
    forecast = get_forecast()
    #print(json.dumps(forecast, indent = 2))

    cur_temp = forecast["currently"]["temperature"]
    min_desc = forecast["minutely"]["summary"]
    min_icon = emojis.get(forecast["minutely"]["icon"], "")
    sunset_time = datetime.fromtimestamp(forecast["daily"]["data"][0]["sunsetTime"])
    return "%s  %.1fC, %s. %s set" % (min_icon, cur_temp, min_desc, sunset_time.strftime("%H:%M"))

if __name__ == "__main__":
    print(one_line())
