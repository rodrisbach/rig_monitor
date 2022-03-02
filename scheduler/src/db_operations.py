class Operations:
    
    @staticmethod
    def get_database_creation(database :str):
        query = f"""CREATE DATABASE [IF NOT EXISTS] {database};"""
        return query

    @staticmethod
    def get_table_creation(table :str)
        query = f"""
                   CREATE TABLE [IF NOT EXISTS] {table} (
                   timestamp DATETIME PRIMARY KEY,
                   device VARCHAR(50) NOT NULL,
                   hashrate FLOAT NOT NULL,
                   temperature FLOAT NOT NULL
                   );"""
        return query