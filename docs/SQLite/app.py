from sqlite import SQLite

database = SQLite('./app.sqlite')
database.create_table('users', [
                'id INTEGER PRIMARY KEY AUTOINCREMENT',
                'name TEXT NOT NULL',
                'age INTEGER',
                'gender TEXT',
                'nationality TEXT'
            ])
