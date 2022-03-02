from rig import Rig
from db_operations import Operations
from apscheduler.schedulers.background import BlockingScheduler
import json, logging, sys, mysql.connector
from mysql.connector import Error


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

    query_database_creation = Operations.get_database_creation(config["db_name"])
    query_device_table_creation = Operations.get_table_creation(config["device_metrics_table"])
    query_pool_table_creation = Operations.get_table_creation(config["pool_metrics_table"])

    try:
        connection = mysql.connector.connect(host=config["db_host"],
                                             username=config["db_user"],
                                             password=config["db_password"])
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query_database_creation)
            cursor.execute(query_device_table_creation)
            cursor.execute(query_pool_table_creation)

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
