import sqlite3
from sqlite3 import Error


class SQLite:
    def __init__(self, path: str):
        """
        Constructor of the class and also the connection to database

        Example:
            database = SQLite("E:\\sm_app.sqlite")

        :param path: path to database as string
        :return: nothing to return
        """
        connection = None
        try:
            connection = sqlite3.connect(path)
            print('Connection to SQLite DB is successful')
        except Error as e:
            raise f"The error '{e}' occurred"
        self.connection = connection

