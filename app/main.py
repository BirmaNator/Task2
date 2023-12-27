import requests

from flask import Flask, jsonify

app = Flask(__name__)


REQUEST_TIMEOUT = 10
OFFICIAL_JOKE_API_URL = 'https://official-joke-api.appspot.com/random_joke'

PUNCHLINE_KEY_NAME = 'punchline'
ID_KEY_NAME = 'id'


@app.get("/")
def root():
    response = requests.get(OFFICIAL_JOKE_API_URL, verify=False, timeout=REQUEST_TIMEOUT)
    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        return 'joke url is not responding', 400
    
    data = response.json()

    if PUNCHLINE_KEY_NAME not in data:
        return f'{PUNCHLINE_KEY_NAME} is missing in API response', 424

    if ID_KEY_NAME not in data:
        return f'{ID_KEY_NAME} is missing in API response', 424
    
    result = {
        PUNCHLINE_KEY_NAME: data.get(PUNCHLINE_KEY_NAME),
        ID_KEY_NAME: data.get(ID_KEY_NAME)
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run()
