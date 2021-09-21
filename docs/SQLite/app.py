from sqlite import SQLite

database = SQLite('./app.sqlite')
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

data = database.get('SELECT * from users')
print(data)
