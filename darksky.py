import requests
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
    resp = requests.get("http://ipinfo.io/loc")
    return resp.text.strip()

def pretty_summary():
    forecast = get_forecast()

    summary = forecast["hourly"]["summary"]
    icon    = emojis.get(forecast["hourly"]["icon"], "🌈")

    weekly_sum = forecast["daily"]["summary"]
    return icon + " " + summary + "\n" + weekly_sum

print(pretty_summary())
