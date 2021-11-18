import requests
import logging

def verify_status(url, min_hashrate, raw_hashrate, update):
    # criticality
    # warning = 1
    # critical = 2
    logging.basicCOnfig(level=logging.INFO,filename='telegram_bot.log', filemode='w',format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    print("Haciendo el request")
    status = requests.get(url).json()
    for device in status["miner"]["devices"]:
        hashrate = float(device["hashrate_raw"])/raw_hashrate
        temperature = float(device["temperature"])
        if hashrate < min_hashrate/2 or temperature > 70:
            criticality = 2
            notify_issue(update, device["info"], hashrate, temperature, criticality)
            logging.info("Status CRITICAL")
        elif hashrate < min_hashrate or temperature >= 65:
            criticality = 1
            logging.info("Status WARNING")
            notify_issue(update, device["info"], hashrate, temperature, criticality)
        else:
            notify_issue(update,device["info"],hashrate,temperature,0)
            logging.info("Status OK")

def notify_issue(update, device, hashrate, temperature, criticality):
    message = f"Device {device} Hashrate: {hashrate} Temperature: {temperature}"
    if criticality == 2:
        message = f"CRITICAL {message}"
    elif criticaly == 1:
        message = f"WARNING {message}"
    else:
        message = f"OK  {message}"
    update.message.reply_text(message)
