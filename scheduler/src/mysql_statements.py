sql_create_database = """CREATE DATABASE [IF NOT EXISTS] rig;"""

sql_create_device_table = """ CREATE TABLE [IF NOT EXISTS] device_metrics (
                   timestamp datetime PRIMARY KEY,
                   device text NOT NULL,
                   hashrate float NOT NULL,
                   temperature float NOT NULL
                   );"""

sql_create_pool_table = """ CREATE TABLE [IF NOT EXISTS] pool_metrics (
                   timestamp datetime PRIMARY KEY,
                   uptime datetime NOT NULL,
                   hashrate float NOT NULL,
                   restarts integer NOT NULL
                   );"""