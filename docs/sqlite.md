# SQLite

## Overview

SQLite is a C-language library that implements a **small**, **fast**, **self-contained**, **high-reliability**, **full-featured**, SQL database engine. SQLite is the most used database engine in the world. SQLite is built into all mobile phones and most computers and comes bundled inside countless other applications that people use every day. [More Information...](https://www.sqlite.org/about.html)

## Connector

We developed our [class](https://github.com/mezidia/medivac/blob/main/sqlite_api/connector.py) to make a work with 
database easier. Constructor of the class has a path to database as a variable. 

There are several main methods: 

- [create_table](https://github.com/mezidia/medivac/blob/main/sqlite_api/connector.py#L25-L56)
- [insert](https://github.com/mezidia/medivac/blob/main/sqlite_api/connector.py#L58-L90)
- [get](https://github.com/mezidia/medivac/blob/main/sqlite_api/connector.py#L92-L109)
- [update](https://github.com/mezidia/medivac/blob/main/sqlite_api/connector.py#L111-L131)
- [delete](https://github.com/mezidia/medivac/blob/main/sqlite_api/connector.py#L133-L152)
- [clear_table](https://github.com/mezidia/medivac/blob/main/sqlite_api/connector.py#L154-L160)
- [close](https://github.com/mezidia/medivac/blob/main/sqlite_api/connector.py#L162-L166)

All these methods has docstrings, so you can read what they do and which parameters takes.

## Example

There is [example file](https://github.com/mezidia/medivac/blob/main/sqlite_api/example.py), but you can also view the code below:

```python
from sqlite_api.connector import SQLite

path_to_database = './sqlite3.db'
database = SQLite(path_to_database)

result = database.create_table('users', [
    'id INTEGER PRIMARY KEY AUTOINCREMENT',
    'name TEXT NOT NULL',
    'age INTEGER',
    'gender TEXT',
    'nationality TEXT'
])
assert result is True

result = database.insert('users', ('name', 'age', 'gender', 'nationality'), [
    ('James', 25, 'male', 'USA'),
    ('Leila', 32, 'female', 'France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike', 40, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada')
])
assert result is True

data = database.get('SELECT * from users WHERE id = 2')
print(data)
"""
Expected output:

[('Leila', 32, 'female', 'France')]
"""

result = database.update('users', 'name = "Maxim"', 'id = 2')
assert result is True

result = database.delete('users', 'id = 5')
assert result is True

database.close()
```