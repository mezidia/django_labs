import sqlite3
from sqlite3 import Error

from typing import List


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

    def create_table(self, table_name: str, fields: List[str]):
        """
        Method for creating the table

        Example:
            SQLite().create_table('users', [
                'id INTEGER PRIMARY KEY AUTOINCREMENT',
                'name TEXT NOT NULL',
                'age INTEGER',
                'gender TEXT',
                'nationality TEXT'
            ])

        :param table_name: name of the table, that you want to create
        :param fields: list of the fields as strings
        :return:
        """
        cursor = self.connection.cursor()
        fields_string = ''
        for index in range(len(fields)):
            if index == len(fields) - 1:
                fields_string += fields[index]
            else:
                fields_string += fields[index] + ',\n'
        print(fields_string)
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({fields_string});'
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            raise f"The error '{e}' occurred"
