import requests, json

class Rig:
    RAW_HASHRATE = 1000000
    def __init__(self, url, password, min_hashrate, address, coin, flexpool_api):
        self.url = url
        self.password = password
        self.min_hashrate = int(min_hashrate)
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
            login = requests.get(f"{self.url}/login?password={self.password}").json()
            sid = login["sid"]
            status = requests.get(f"{self.url}/summary?sid={sid}", timeout=10).json()
        except requests.exceptions.RequestException as error:
            message = f"Error: {error}"
            return message
        uptime = self.get_uptime(status["uptime"])
        rig_hashrate = round(float(status["hashrate"]/self.RAW_HASHRATE), 2)
        message = f'Pool Hashrate {rig_hashrate}MH/s \nUptime: {uptime} \nRestarts: {status["watchdog_stat"]["total_restarts"]}\n'
        for gpu in status["gpus"]:
            hashrate = round(float(gpu["hashrate"])/self.RAW_HASHRATE, 2)
            temperature = gpu["temperature"]
            device = gpu["name"]
            message = f"{message}\n{device}\nHashrate: {hashrate}MH/s\nTemperature: {temperature}°C\n"
        return message

    def verify_status(self):
        try:
            login = requests.get(f"{self.url}/login?password={self.password}").json()
            sid = login["sid"]
            status = requests.get(f"{self.url}/summary?sid={sid}", timeout=10).json()
        except requests.exceptions.RequestException as error:
            message = f"Error: {error}"
        for gpu in status["gpus"]:
            hashrate = round(float(gpu["hashrate"])/self.RAW_HASHRATE, 2)
            temperature = int(gpu["temperature"])
            device = gpu["name"]
            #message = f"\n{device['info']}\nHashrate: {device['hashrate']}MH/s\nTemperature: {temperature}°C\n"
            if hashrate < (self.min_hashrate/2) or int(temperature) > 70:
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
