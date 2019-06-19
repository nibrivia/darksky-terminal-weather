# darksky-terminal-weather
For use in MOTD, prints current weather

## Auth
To use your API key, create `api_key.py` with a variable called `API_KEY`.

```bash
echo "API_KEY = '{INSERT_KEY}'" > api_key.py
```

## MOTD setup

Add the following to your `.bash_profile`, `.bashrc`, or wherever...
```bash
python3 {PATH_TO_DIR}/darsky.py
```

## Attributions
Powered by [DarkSky](https://darksky.net/poweredby/) and [IPinfo](https://ipinfo.io/)
