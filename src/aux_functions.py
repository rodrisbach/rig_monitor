import requests

def verify_status(url, min_hashrate, raw_hashrate, update):
    try:
        status = requests.get(url).json()
    except requests.exceptions.RequestException as e:
        update.message.reply("NBminer no responde")
        raise
    for device in status["miner"]["devices"]:
        hashrate = float(device["hashrate_raw"])/raw_hashrate
        temperature = float(device["temperature"])
        message = f"\n{device['info']}\nHashrate: {device['hashrate']}\nTemperature: {temperature}"
        if hashrate < min_hashrate/2 or temperature > 70:
            message = f"CRITICAL!\n{message}"
            update.message.reply_text(message)
        elif hashrate < min_hashrate or temperature >= 65:
            message = f"WARNING!\n{message}"
            update.message.reply_text(message)
        else:
            update.message.reply_text("Todo OK")

def get_status(url, update):
    status = requests.get(url).json()
    for device in status["miner"]["devices"]:
        hashrate = device["hashrate"]
        temperature = device["temperature"]
        message = f"\n{device['info']}\nHashrate: {device['hashrate']}\nTemperature: {temperature}"
        update.message.reply_text(message)
 
