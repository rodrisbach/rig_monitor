import json, sys

def read_config(path: str) -> dict:
        try:
            jsonfile = open(path)
        except OSError:
            print("OS error occurred trying to open config file")
            sys.exit(1)
        except FileNotFoundError:
            print("Config file not found. Aborting")
            sys.exit(1)
        else:
            with jsonfile:
                config = json.load(jsonfile)
        return config
