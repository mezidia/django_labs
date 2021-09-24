from connector import SQLite

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

result = database.update('users', 'name = "Maxim"', 'id = 2')
assert result is True

result = database.delete('users', 'id = 5')
assert result is True

database.close()
