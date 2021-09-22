from sqlite import SQLite

database = SQLite('./sqlite3.db')
database.create_table('users', [
                'id INTEGER PRIMARY KEY AUTOINCREMENT',
                'name TEXT NOT NULL',
                'age INTEGER',
                'gender TEXT',
                'nationality TEXT'
            ])
database.insert('users', ('name', 'age', 'gender', 'nationality'), [
    ('James', 25, 'male', 'USA'),
    ('Leila', 32, 'female', 'France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike', 40, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada')
])

data = database.get('SELECT * from users WHERE id = 2')
print(data)
updated_data = database.update('users', 'name = "Maxim"', 'id = 2')
print(updated_data)
deleted_data = database.delete('users', 'id = 5')
print(deleted_data)
