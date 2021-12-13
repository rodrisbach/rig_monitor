import json, logging
from scheduler.src.rig import Rig
from apscheduler.schedulers.background import BackgroundScheduler
from bootle import run,post

def main():

    try:
        jsonfile = open("../config/config.json")
    except OSError:
        print("OS error occurred trying to open config file")
        sys.exit(1)
    except FileNotFoundError:
        print("Config file not found. Aborting")
        sys.exit(1)
    else:
        with jsonfile:
            config = json.load(jsonfile)

#    logging.basicConfig(level=logging.INFO,filename=config["log_path"], filemode='w',format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
#    logging.getLogger('apscheduler').setLevel(logging.INFO)
    token = config["telegram_token"]
    updater = Updater(token=token, use_context=True)
    scheduler = BackgroundScheduler()
    scheduler.start()
    rig = Rig(config["rig_url"],config["rig_password"],config["min_hashrate"],config["wallet_address"],config["coin"],config["flexpool_api"])
#    scheduler.add_job(rig.verify_status,'interval', seconds=10, args=(updater))


if __name__ == "__main__":
    main()
