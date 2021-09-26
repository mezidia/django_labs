from connector import MySQL
from config import *

database = MySQL(host, user, password, db_name)

result = database.create_table('users', [
    'id INT AUTO_INCREMENT PRIMARY KEY',
    'name VARCHAR(45) NOT NULL',
    'age INT',
    'gender VARCHAR(45)',
    'nationality VARCHAR(45)'
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

result = database.update('users', "name = 'Valentyn'", 'id = 2')
assert result is True

result = database.delete('users', 'id = 5')
assert result is True

database.close()