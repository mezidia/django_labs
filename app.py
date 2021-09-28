from tkinter import Tk, Label, Entry, Button, Listbox
import tkinter.messagebox as message_box
from config import *

from mysql_api.connector import MySQL
# from sqlite_api.connector import SQLite
# from postgresql_api.connector import PostgreSQL


def insert_route():
    route_name = entries['route_name'].get()
    place_from = entries['place_from'].get()
    place_to = entries['place_to'].get()
    price = entries['price'].get()
    car = entries['car_id'].get()

    if all(entries.values()):
        database = MySQL(host, user, password, db_name)
        result = database.insert('routes', '(name, place_from, place_to, price, car)',
                                 [(route_name, place_from, place_to, price, car)])
        if result:
            entries['route_name'].delete(0, 'end')
            entries['place_from'].delete(0, 'end')
            entries['place_to'].delete(0, 'end')
            entries['price'].delete(0, 'end')
            entries['car_id'].delete(0, 'end')
            show()
            message_box.showinfo('Insert Status', 'Inserted successfully')
        else:
            message_box.showerror('Insert Status', 'An error occurred while inserting')
    else:
        message_box.showerror('Insert Status', 'All fields are required')


def insert_car():
    car_name = entries['car_name'].get()

    if car_name:
        database = MySQL(host, user, password, db_name)
        result = database.insert('cars', '(name)', [(f"('{car_name}')")])
        if result:
            entries['car_name'].delete(0, 'end')
            show()
            message_box.showinfo('Insert Status', 'Inserted successfully')
        else:
            message_box.showerror('Insert Status', 'An error occurred while inserting')
    else:
        message_box.showerror('Insert Status', 'All fields are required')


def delete_route():
    route_name = entries['route_name'].get()
    if route_name:
        database = MySQL(host, user, password, db_name)
        result = database.delete('routes', f'name = {route_name}')
        if result:
            entries['route_name'].delete(0, 'end')
            show()
            message_box.showinfo('Delete Status', 'Deleted successfully')
        else:
            message_box.showerror('Delete Status', 'An error occurred while deleting')
    else:
        message_box.showerror('Delete Status', 'Name of the route is compulsory for delete')


def delete_car():
    car_id = entries['car_id'].get()
    if car_id:
        database = MySQL(host, user, password, db_name)
        result = database.delete('routes', f'name = {car_id}')
        if result:
            entries['car_id'].delete(0, 'end')
            show()
            message_box.showinfo('Delete Status', 'Deleted successfully')
        else:
            message_box.showerror('Delete Status', 'An error occurred while deleting')
    else:
        message_box.showerror('Delete Status', 'Name of the route is compulsory for delete')


def update_route():
    route_name = entries['route_name'].get()
    place_from = entries['place_from'].get()
    place_to = entries['place_to'].get()
    price = entries['price'].get()
    car = entries['car_id'].get()

    if all(entries.values()):
        database = MySQL(host, user, password, db_name)
        result = database.update('routes', f"name = '{route_name}', place_from = '{place_from}',"
                                           f"place_to = '{place_to}', price = '{price}', car = '{car}'",
                                 f"name = '{route_name}'")
        if result:
            entries['route_name'].delete(0, 'end')
            entries['place_from'].delete(0, 'end')
            entries['place_to'].delete(0, 'end')
            entries['price'].delete(0, 'end')
            entries['car_id'].delete(0, 'end')
            show()
            message_box.showinfo('Update Status', 'Updated successfully')
        else:
            message_box.showerror('Update Status', 'An error occurred while updating')
    else:
        message_box.showerror('Update Status', 'All fields are required')


def update_car():
    car_id = entries['car_id'].get()
    car_name = entries['car_name'].get()

    if car_id != '' and car_name != '':
        database = MySQL(host, user, password, db_name)
        result = database.update('cars', f"name = '{car_name}'",
                                 f"id = '{car_id}'")
        if result:
            entries['car_id'].delete(0, 'end')
            entries['car_name'].delete(0, 'end')
            show()
            message_box.showinfo('Update Status', 'Updated successfully')
        else:
            message_box.showerror('Update Status', 'An error occurred while updating')
    else:
        message_box.showerror('Update Status', 'All fields are required')


def get_route():
    route_name = entries['route_name'].get()
    if route_name:
        database = MySQL(host, user, password, db_name)
        route = database.get(f"SELECT * from routes WHERE name = '{route_name}'")
        message_box.showinfo('Fetch Status', route[0][0])
    else:
        message_box.showerror('Fetch Status', 'ID is compulsory for fetch')


def get_car():
    car_id = entries['car_id'].get()
    if car_id:
        database = MySQL(host, user, password, db_name)
        car = database.get(f'SELECT * from cars WHERE id = {car_id}')
        message_box.showinfo('Fetch Status', car[0][0])
    else:
        message_box.showerror('Fetch Status', 'ID is compulsory for fetch')


def show():
    database = MySQL(host, user, password, db_name)
    routes = database.get(f'SELECT * from routes')
    cars = database.get(f'SELECT * from cars')
    routes_list.delete(0, routes_list.size())
    cars_list.delete(0, cars_list.size())
    for route in routes:
        insert_data = str(route[0]) + ' ' * 10 + str(route[1])
        routes_list.insert(routes_list.size() + 1, insert_data)
    for car in cars:
        insert_data = str(car[0]) + ' ' * 10 + str(car[1])
        cars_list.insert(cars_list.size() + 1, insert_data)


root = Tk()
root.geometry('600x400')
root.title('Autostation')
root.resizable(width=False, height=False)

labels_texts = [
    'Name of the route',
    'Enter place from',
    'Enter place to',
    'Enter price',
    'Enter car id',
    'Enter car name',
]

for index in range(len(labels_texts)):
    label = Label(root, text=labels_texts[index], font=('bold', 10))
    label.place(x=20, y=30 * (index + 1))

routes_label = Label(root, text='Available routes', font=('bold', 10))
routes_label.place(x=290, y=30)

cars_label = Label(root, text='Available cars', font=('bold', 10))
cars_label.place(x=430, y=30)

entries = {}
entries_texts = [
    'route_name',
    'place_from',
    'place_to',
    'price',
    'car_id',
    'car_name',
]

for index in range(len(entries_texts)):
    entry = Entry()
    entry.place(x=150, y=30 * (index + 1))
    entries[entries_texts[index]] = entry

buttons_texts = [
    ['insert', {'route': insert_route, 'car': insert_car}],
    ['delete', {'route': delete_route, 'car': delete_car}],
    ['update', {'route': update_route, 'car': update_car}],
    ['get', {'route': get_route, 'car': get_car}],
]

routes_buttons_label = Label(root, text='Work with routes:', font=('bold', 10))
routes_buttons_label.place(x=20, y=240)

cars_buttons_label = Label(root, text='Work with cars:', font=('bold', 10))
cars_buttons_label.place(x=20, y=300)

for index in range(len(buttons_texts)):
    button = Button(root, text=buttons_texts[index][0], font=('italic', 10), bg='white',
                    command=buttons_texts[index][1]['route'])
    button.place(x=20 + 60 * index, y=260)
    button = Button(root, text=buttons_texts[index][0], font=('italic', 10), bg='white',
                    command=buttons_texts[index][1]['car'])
    button.place(x=20 + 60 * index, y=320)

routes_list = Listbox(root)
routes_list.place(x=290, y=50)

cars_list = Listbox(root)
cars_list.place(x=430, y=50)


def export_to_sqlite():
    pass
    # mysql_database = MySQL(host, user, password, db_name)
    # sqlite_database = SQLite('path')
    # data = mysql_database.get('SELECT * from routes')
    # data = [row[1:] for row in data]
    # sqlite_database.insert('routes', ('route_name', 'place_from', 'place_to', 'price', 'car'), data)


def export_to_postgresql():
    pass
    # postgresql_database = PostgreSQL(host, user, password, db_name)
    # sqlite_database = SQLite('path')
    # data = sqlite_database.get('SELECT * from routes')
    # data = [row[1:] for row in data]
    # postgresql_database.insert('routes', '(route_name, place_from, place_to, price, car)', data)


def create_tables():
    mysql_database = MySQL(host, user, password, db_name)
    # postgresql_database = PostgreSQL()
    # sqlite_database = SQLite()
    cars_fields = [
        'id INT AUTO_INCREMENT PRIMARY KEY',
        'name VARCHAR(45) NOT NULL'
    ]
    routes_fields = [
        'id INT AUTO_INCREMENT PRIMARY KEY',
        'name VARCHAR(45) NOT NULL',
        'place_from VARCHAR(45) NOT NULL',
        'place_to VARCHAR(45) NOT NULL',
        'price FLOAT NOT NULL',
        'car INT NOT NULL',
        'FOREIGN KEY(car) REFERENCES cars(id)'
    ]
    mysql_database.create_table('cars', cars_fields)
    mysql_database.create_table('routes', routes_fields)
    # postgresql_database.create_table('cars', cars_fields)
    # postgresql_database.create_table('routes', routes_fields)
    # sqlite_database.create_table('cars', cars_fields)
    # sqlite_database.create_table('routes', routes_fields)


export_to_sqlite_button = Button(root, text='Export from MySQL to SQLite', font=('italic', 10), bg='white',
                                 command=export_to_sqlite)
export_to_sqlite_button.place(x=290, y=260)
export_to_postgre_button = Button(root, text='Export from SQLite to PostgreSQL', font=('italic', 10), bg='white',
                                  command=export_to_postgresql)
export_to_postgre_button.place(x=290, y=320)

create_tables()
show()
root.mainloop()
