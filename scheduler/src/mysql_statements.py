sql_create_database = """CREATE DATABASE [IF NOT EXISTS] rig;"""

sql_create_device_table = """ CREATE TABLE [IF NOT EXISTS] device_metrics (
                   timestamp DATETIME PRIMARY KEY,
                   device VARCHAR(50) NOT NULL,
                   hashrate FLOAT NOT NULL,
                   temperature FLOAT NOT NULL
                   );"""

sql_create_pool_table = """ CREATE TABLE [IF NOT EXISTS] pool_metrics (
                   timestamp DATETIME PRIMARY KEY,
                   uptime DATETIME NOT NULL,
                   hashrate FLOAT NOT NULL,
                   restarts INT NOT NULL
                   );"""