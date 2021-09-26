from connector import PostgreSQL
from config import *

database = PostgreSQL(host, user, password, db_name)

result = database.create_table('users', [
    'id SERIAL PRIMARY KEY',
    'name TEXT NOT NULL',
    'age INTEGER',
    'gender TEXT',
    'nationality TEXT'
])
assert result is True

result = database.insert('users', '(name, age, gender, nationality)', [
    ('James', 25, 'male', 'USA'),
    ('Leila', 32, 'female', 'France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike', 40, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada')
])
assert result is True

data = database.get('SELECT * from users')
print(data)

result = database.update('users', "name = 'Maxim'", 'id = 2')
assert result is True

result = database.delete('users', 'id = 5')
assert result is True

database.close()