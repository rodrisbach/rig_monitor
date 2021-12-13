import requests

class Response:
    def __init__(self):
        self.message = ""

    def get_chat_id(data):
        chat_id = data['message']['chat']['id']
        return chat_id

    def send_message(prepared_data, bot_url):    
        message_url = bot_url + 'sendMessage'
        requests.post(message_url, json=prepared_data)  # don't forget to make import requests lib

    def validate_user(data, expected_username):
        if data["message"]["from"]["username"] == expected_username:
            return True
        return False

    def prepare_message(self, data, rig):
        command = data["message"]["text"]
        if command == "/start":
            answer = "Hi, see below the available commands: \n/status -> Get Rig and Cards status"
        if command == "/status":
            answer = rig.get_status()
        json_data = {
            "chat_id": self.get_chat_id(data),
            "text": answer,
        }
        return json_data

    def set_message(self, message):
        self.message = message