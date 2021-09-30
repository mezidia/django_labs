# PostgreSQL

## Overview

PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

## Connector

We developed our [class](https://github.com/mezidia/medivac/blob/main/postgresql_api/connector.py) to make a work with
database easier. Constructor of the class has a path to database as a variable.

There are several main methods:

- [create_table](https://github.com/mezidia/medivac/blob/main/postgresql_api/connector.py#L28-L59)
- [insert](https://github.com/mezidia/medivac/blob/main/postgresql_api/connector.py#L61-L93)
- [get](https://github.com/mezidia/medivac/blob/main/postgresql_api/connector.py#L95-L112)
- [update](https://github.com/mezidia/medivac/blob/main/postgresql_api/connector.py#L114-L134)
- [delete](https://github.com/mezidia/medivac/blob/main/postgresql_api/connector.py#L136-L155)
- [clear_table](https://github.com/mezidia/medivac/blob/main/postgresql_api/connector.py#L157-L163)
- [close](https://github.com/mezidia/medivac/blob/main/postgresql_api/connector.py#L165-L169)

All these methods has docstrings, so you can read what they do and which parameters takes.

## Example

There is [example file](https://github.com/mezidia/medivac/blob/main/postgresql_api/example.py),
but you can also view the code below:

```python
from postgresql_api.connector import PostgreSQL
from config import host, user, password, db_name

database = PostgreSQL(host, user, password, db_name)

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
