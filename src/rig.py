import requests, json

class Rig:
    RAW_HASHRATE = 100000
    def __init__(self, url, min_hashrate):
        self.url = url
        self.min_hashrate = min_hashrate

    def get_status(self):
        try:
            status = requests.get(self.url, timeout=10).json()
        except requests.exceptions.RequestException as error:
            message = f"Error: {error}"
        for gpu in status["gpus"]:
            hashrate = int(gpu["hashrate"])/self.RAW_HASHRATE
            temperature = gpu["temperature"]
            device = gpu["name"]
            message = f"{message}\n {device}\nHashrate: {hashrate}\nTemperature: {temperature}\n"
        return message