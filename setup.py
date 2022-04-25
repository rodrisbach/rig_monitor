import json, sys, logging

path = str(__file__).rstrip("/setup.py")
try:
    jsonfile = open(sys.argv[1], "r")
except OSError:
    logging.critical("OS error occurred trying to open config file")
    sys.exit(1)
except FileNotFoundError:
    logging.critical("Config file not found. Aborting")
    sys.exit(1)
else:
    with jsonfile:
        config = json.load(jsonfile)

# API CONFIGURATION
with open(f"{path}/api/config.json", "w") as jsonfile:
    json.dump(config["telegram"], jsonfile)

# DATABASE CONFIGURATION
db_config = f'''MYSQL_DATABASE="{config["database"]["name"]}"
MYSQL_USER="{config["database"]["user"]}"
MYSQL_PASSWORD="{config["database"]["password"]}"
MYSQL_ROOT_PASSWORD="{config["database"]["root_password"]}"'''
db_config_file=open(f"{path}/db_config.env","w")
db_config_file.write(db_config)
db_config_file.close()

# MONITOR CONFIGURATION
monitor_config = {
    "rig": config["rig"],
    "wallet":config["wallet_addres"],
    "coin": config["coin"],
    "flexpool_api": config["flexpool_api"],
    "log_level": config["log_level"],
    "log_path": config["log_path"],
}

with open(f"{path}/monitor/config.json", "w") as jsonfile:
    json.dump(monitor_config, jsonfile)
