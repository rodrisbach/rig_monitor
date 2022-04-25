from rig import Rig
from db_operations import Operations
from utilities import read_config
from apscheduler.schedulers.background import BlockingScheduler
import logging, mysql.connector
from mysql.connector import Error


def main():

    config = read_config("config.json")
    query_database_creation = Operations.get_database_creation(config["db_name"])
    query_device_table_creation = Operations.get_table_creation(config["device_metrics_table"])

    try:
        connection = mysql.connector.connect(host=config["database"]["name"],
                                             username=config["database"]["user"],
                                             password=config["database"]["password"])
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query_database_creation)
            cursor.execute(query_device_table_creation)

    except Error as error:
        logging.critical("Error while connecting to MySQL", error)
        sys.exit(1)

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
