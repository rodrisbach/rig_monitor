import requests, json, sys
from rig import Rig
from bottle import (  
    run, post, response, request as bottle_request
)

def get_chat_id(data):

    chat_id = data['message']['chat']['id']
    return chat_id

def get_message(data):

    message_text = data['message']['text']
    return message_text

def send_message(prepared_data, bot_url):
 
    message_url = bot_url + 'sendMessage'
    requests.post(message_url, json=prepared_data)  # don't forget to make import requests lib


def prepare_response(data, rig):

    command = data["message"]["text"]
    if command == "/start":
        answer = "Hi, see below the available commands: \n/status -> Get Rig and Cards status"
    if command == "/status":
        answer = rig.get_status()
    json_data = {
        "chat_id": get_chat_id(data),
        "text": answer,
    }
    return json_data

@post('/')
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
    rig = Rig(config["rig_url"],config["rig_password"],config["min_hashrate"],config["wallet_address"],config["coin"],config["flexpool_api"])
    data = bottle_request.json
    print(data)
    response = prepare_response(data, rig)
    send_message(response, bot_url)  

    return response  

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
