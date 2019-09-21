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
    #return resp.text.strip()
    return "42.3649,-71.0987"

def pretty_summary():
    forecast = get_forecast()

    summary = forecast["hourly"]["summary"]
    icon    = emojis.get(forecast["hourly"]["icon"], "🌈")

    daily_sum  = forecast["daily"]["summary"]
    daily_icon = emojis.get(forecast["daily"]["icon"], "🌈")

    attribution = "Powered by DarkSky: https://darksky.net/poweredby/"
    
    return icon + "  " + summary + "\n" + daily_icon + "  " + daily_sum + "\n" + attribution

if __name__ == "__main__":
    print(pretty_summary())
