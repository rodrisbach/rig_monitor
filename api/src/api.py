import json, sys
from scheduler.src.rig import Rig
from bot.src.response import Response
from flask import Flask, request

INVALID_USER = "Invalid user. You are not allowed to use this bot"
app = Flask(__name__)

def main():
    try:
        jsonfile = open("../config/test.json")
    except OSError:
        print("OS error occurred trying to open config file")
        sys.exit(1)
    except FileNotFoundError:
        print("Config file not found. Aborting")
        sys.exit(1)
    else:
        with jsonfile:
            config = json.load(jsonfile)
    token = config["telegram_token"]
    bot_url = f'https://api.telegram.org/bot{token}/'
    global rig = Rig(config["rig_url"],config["rig_password"],config["min_hashrate"],config["wallet_address"],config["coin"],config["flexpool_api"])
    app.run(debug=True, host='0.0.0.0', port=8080)


@app.route('/', methods=['POST'])
def response_message():

    data = request.get_json()
    response = Response()
    print(data)
    if response.validate_user(data,config["telegram_username"]):
        response.prepare_message(data, rig)
    else:
        response.set_message(INVALID_USER)
    response.send_message(response, bot_url)
    
if __name__ == '__main__':
    main()