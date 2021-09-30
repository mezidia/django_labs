from mysql.connector import connect, Error

from typing import List


class MySQL:
    def __init__(self, host: str, user: str, password: str, db_name: str):
        """
        Constructor of the class and also the connection to database

        Example:
            database = MySQL(host, user, password, db_name)

        :param host: database host
        :param user: database user
        :param password: database password
        :param db_name: database name
        :return: nothing to return
        """
        connection = None
        try:
            connection = connect(host=host, user=user, password=password, database=db_name)
        except Error as e:
            raise Exception(f"The error '{e}' occurred")
        self.connection = connection

    def create_table(self, table_name: str, fields: List[str]) -> bool:
        """
        Method for creating the table

        Example:
            result = MySQL().create_table('users', [
                'id INT AUTO_INCREMENT PRIMARY KEY',
                'name VARCHAR(45)',
                'age INT',
                'gender VARCHAR(45)',
                'nationality VARCHAR(45)'
            ])
            assert result == True

        :param table_name: name of the table, that you want to create
        :param fields: list of the fields as strings
        :return: result of the execution
        """
        cursor = self.connection.cursor()
        fields_string = ''
        for index in range(len(fields)):
            if index == len(fields) - 1:
                fields_string += fields[index]
            else:
                fields_string += fields[index] + ',\n'
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({fields_string});'
        try:
            cursor.execute(query)
            self.connection.commit()
            return True
        except Error as e:
            raise Exception(f"The error '{e}' occurred")

    def insert(self, table_name: str, fields_names: str, fields_values: List[tuple]) -> bool:
        """
        Method for inserting data into the table

        Example:
            result = MySQL().insert('users', ('name', 'age', 'gender', 'nationality'), [
                ('James', 25, 'male', 'USA'),
                ('Leila', 32, 'female', 'France'),
                ('Brigitte', 35, 'female', 'England'),
                ('Mike', 40, 'male', 'Denmark'),
                ('Elizabeth', 21, 'female', 'Canada')
            ])
            assert result == True

        :param table_name: name of the table, in that you to want to insert
        :param fields_names: names of the fields you want to insert
        :param fields_values: list of tuples with the values of the fields
        :return: result of the execution
        """
        cursor = self.connection.cursor()
        fields_string = ''
        for index in range(len(fields_values)):
            if index == len(fields_values) - 1:
                fields_string += str(fields_values[index])
            else:
                fields_string += str(fields_values[index]) + ',\n'
        query = f'INSERT INTO {table_name} {fields_names} VALUES {fields_string};'
        try:
            cursor.execute(query)
            self.connection.commit()
            return True
        except Error as e:
            raise Exception(f"The error '{e}' occurred")

    def get(self, query: str) -> list:
        """
        Function to fetch data

        Example:
            data = MySQL().get('SELECT * from users')
            print(data)

        :param query: SQL-query to get data
        :return: list of the fetched data
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            raise Exception(f"The error '{e}' occurred")

    def update(self, table_name: str, updated_value: str, condition: str) -> bool:
        """
        Function to update field in the table

        Example:
            result = MySQL().update('users', 'name = "Valentyn"', 'id = 4')
            assert result == True

        :param table_name: name of the table
        :param updated_value: field name and the value
        :param condition: condition to find necessary field
        :return: result of the execution
        """
        cursor = self.connection.cursor()
        try:
            query = f'UPDATE {table_name} SET {updated_value} WHERE {condition}'
            cursor.execute(query)
            self.connection.commit()
            return True
        except Error as e:
            raise Exception(f"The error '{e}' occurred")

    def delete(self, table_name: str, condition: str) -> bool:
        """
        Function to delete field in the table

        Example:
            result = MySQL().delete('users', 'id = 5')
            assert result == True

        :param table_name: name of the table
        :param condition: condition to find necessary field
        :return: result of the execution
        """
        cursor = self.connection.cursor()
        try:
            query = f'DELETE FROM {table_name} WHERE {condition}'
            cursor.execute(query)
            self.connection.commit()
            return True
        except Error as e:
            raise Exception(f"The error '{e}' occurred")

    def clear_table(self, table_name: str) -> None:
        """
        Method for clearing the table
        """
        cursor = self.connection.cursor()
        cursor.execute(f'DELETE FROM {table_name};')
        self.connection.commit()

    def close(self):
        """
        Method for closing the connection
        """
        self.connection.close()
