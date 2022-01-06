import json, logging, sys
from rig import Rig
from apscheduler.schedulers.background import BlockingScheduler
import mysql.connector
from mysql.connector import Error
from mysql_statements import *

def main():

    try:
        jsonfile = open("config.json")
    except OSError:
        print("OS error occurred trying to open config file")
        sys.exit(1)
    except FileNotFoundError:
        print("Config file not found. Aborting")
        sys.exit(1)
    else:
        with jsonfile:
            config = json.load(jsonfile)

    try:
        connection = mysql.connector.connect(host=config["db_host"],
                                             username=config["db_user"],
                                             password=config["db_password"])
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(sql_create_database)
            cursor.execute(sql_create_pool_table)
            cursor.execute(sql_create_device_table)
    except Error as error:
        print("Error while connecting to MySQL", error)

    rig = Rig(config["rig_url"],
              config["rig_password"],
              config["min_hashrate"],
              config["wallet_address"],
              config["coin"],
              config["flexpool_api"])

    scheduler = BlockingScheduler()

    scheduler.add_job(rig.verify_status,'interval', seconds=10)
    scheduler.start()

def write_data(cursor, message)

if __name__ == "__main__":
    main()
