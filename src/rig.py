import requests, json

class Rig:
    RAW_HASHRATE = 100000
    def __init__(self, url, min_hashrate, address, coin, flexpool_api):
        self.url = url
        self.min_hashrate = min_hashrate
        self.adress = address
        self.coin = coin
        self.flexpool_api = flexpool_api

    def get_uptime(self, seconds):
        days = seconds // (24 * 3600)
        seconds = seconds % (24 * 3600)
        hours = seconds // 3600
        seconds = seconds % 3600
        minutes = seconds // 60
        if days == 0 and hours == 0:
            uptime = f"{minutes} minutes"
        elif days == 0:
            uptime =f"{hours} hours {minutes} minutes"
        else:
            uptime = f"{days} days {hours} hours {minutes} minutes"
        return uptime

    def get_status(self):
        try:
            status = requests.get(self.url, timeout=10).json()
        except requests.exceptions.RequestException as error:
            message = f"Error: {error}"
        uptime = self.get_uptime(status["uptime"])
        message = f'Pool Hashrate {status["hashrate"]} \nUptime: {uptime} \nRestarts: {status["watchdog_stat"]["total_restarts"]}'
        for gpu in status["gpus"]:
            hashrate = int(gpu["hashrate"])/self.RAW_HASHRATE
            temperature = gpu["temperature"]
            device = gpu["name"]
            message = f"{message}\n {device}\nHashrate: {hashrate}\nTemperature: {temperature}\n"
        return message

    def verify_status(self):
        try:
            status = requests.get(self.url, timeout=10).json()
        except requests.exceptions.RequestException as error:
            message = f"Error: {error}"
        for gpu in status["gpus"]:
            hashrate = int(gpu["hashrate"])/self.RAW_HASHRATE
            temperature = gpu["temperature"]
            device = gpu["name"]
            message = f"\n{device['info']}\nHashrate: {device['hashrate']}\nTemperature: {temperature}"
            if hashrate < self.min_hashrate/2 or temperature > 70:
                message = "CRITICAL: {message}"
            elif hashrate < self.min_hashrate or temperature >= 65:
                message = "WARNING: {message}"
            else:
                message = ""
        return message


    def get_flexpool_balance(self):
        header = {'accept: application/json'}
        url = f"{self.flexpool_api}/miner/balance?coin={self.coin}&address={self.adress}"
        balance = requests.get(url, headers=header)
        return balance["balanceCountervalue"]