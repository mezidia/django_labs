# MySQL

## Overview

MySQL Database Service is a fully managed database service to deploy cloud-native applications. HeatWave, an integrated, high-performance query accelerator boosts MySQL performance by 5400x. [Learn More »](https://www.oracle.com/mysql/heatwave/)

## Connector

We developed our [class](https://github.com/mezidia/medivac/blob/main/mysql_api/connector.py) to make a work with 
database easier. Constructor of the class has a path to database as a variable. 

There are several main methods: 

- [create_table](https://github.com/mezidia/medivac/blob/main/mysql_api/connector.py#L27-L58)
- [insert](https://github.com/mezidia/medivac/blob/main/mysql_api/connector.py#L60-L92)
- [get](https://github.com/mezidia/medivac/blob/main/mysql_api/connector.py#L94-L111)
- [update](https://github.com/mezidia/medivac/blob/main/mysql_api/connector.py#L113-L133)
- [delete](https://github.com/mezidia/medivac/blob/main/mysql_api/connector.py#L135-L154)
- [clear_table](https://github.com/mezidia/medivac/blob/main/mysql_api/connector.py#L156-L162)
- [close](https://github.com/mezidia/medivac/blob/main/mysql_api/connector.py#L164-L168)

All these methods has docstrings, so you can read what they do and which parameters takes.

## Example

There is [example file](https://github.com/mezidia/medivac/blob/main/mysql_api/example.py), 
but you can also view the code below:

```python
from mysql_api.connector import MySQL
from config import host, user, password, db_name

database = MySQL(host, user, password, db_name)

result = database.create_table('users', [
    'id INT AUTO_INCREMENT PRIMARY KEY',
    'name VARCHAR(45) NOT NULL',
    'age INT',
    'gender VARCHAR(45)',
    'nationality VARCHAR(45)'
])

result = database.insert('users', '(name, age, gender, nationality)', [
    ('James', 25, 'male', 'USA'),
    ('Leila', 32, 'female', 'France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike', 40, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada')
])

data = database.get('SELECT * from users')
print(data)
"""
Expected output:

[('Leila', 32, 'female', 'France')]
"""

result = database.update('users', "name = 'Valentyn'", 'id = 2')

result = database.delete('users', 'id = 5')

database.close()
```
