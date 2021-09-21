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
            raise Exception(f"The error '{e}' occurred")
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
            print(f'Table {table_name} was successfully created')
        except Error as e:
            raise Exception(f"The error '{e}' occurred")

    def insert(self, table_name: str, fields_names: tuple, fields_values: List[tuple]):
        """
        Method for inserting data into the table

        Example:
            SQLite().insert('users', ('name', 'age', 'gender', 'nationality'), [
                ('James', 25, 'male', 'USA'),
                ('Leila', 32, 'female', 'France'),
                ('Brigitte', 35, 'female', 'England'),
                ('Mike', 40, 'male', 'Denmark'),
                ('Elizabeth', 21, 'female', 'Canada')
            ])

        :param table_name: name of the table, in that you to want to insert
        :param fields_names: names of the fields you want to insert
        :param fields_values: list of tuples with the values of the fields
        :return:
        """
        cursor = self.connection.cursor()
        fields_string = ''
        for index in range(len(fields_values)):
            if index == len(fields_values) - 1:
                fields_string += str(fields_values[index])
            else:
                fields_string += str(fields_values[index]) + ',\n'
        print(fields_string)
        query = f'INSERT INTO {table_name} {str(fields_names)} VALUES {fields_string};'
        try:
            cursor.execute(query)
            self.connection.commit()
            print('Data was successfully inserted')
        except Error as e:
            raise Exception(f"The error '{e}' occurred")

    def get(self, query: str) -> list:
        """
        Function to fetch 
        :param query:
        :return:
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            raise Exception(f"The error '{e}' occurred")
