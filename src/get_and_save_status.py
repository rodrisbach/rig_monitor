import requests
import json

with open("config.json") as jsonfile:
    config = json.load(jsonfile)

status = requests.get(config["rig_url"])
print(status.json())

status = requests.get(config["rig_url"]).json()

for device in status["miner"]["devices"]:
    if device["hashrate_raw"] < 30000000:
        print("Hay problemas con el hashrate")
    else:
        print(f'El hashrate es {device["hashrate"]}')


print(status["miner"]["total_hashrate_raw"])
