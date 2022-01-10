import requests
from flask import *

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home_page():
    return '@Plugin'

@app.route('/tele-check/',methods=['GET'])
def telecheckres_page():
    user = str(request.args.get('user'))

    isChannel = requests.get(f'https://t.me/s/{user}/1', allow_redirects=False).status_code
    if isChannel == 200:
        data_set = {'type': 'Channel', 'stats': 'loaded'}
        return data_set

    elif isChannel == 302:
        isUser = requests.get(f'https://t.me/{user}').text
        if not 'members' in isUser:

            data_set = {'type': 'Pierson', 'stats': 'loaded'}
            return data_set

        elif 'members' in isUser:
            data_set = {'type': 'Group', 'stats': 'loaded'}
            return data_set


if __name__ == '__main__':
    app.run()