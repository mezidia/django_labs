from tkinter import Tk, Label, Entry, Button, Listbox
import tkinter.messagebox as message_box
from config import *

from sqlite3 import Error as SQLite_Error
from mysql.connector import Error as MySQL_Error
from psycopg2 import Error as Postgre_Error

from mysql_api.connector import MySQL
from sqlite_api.connector import SQLite
# from postgresql_api.connector import PostgreSQL


def insert_route():
    """
    Function for inserting data into 'routes' table
    :return: MessageBox call
    """
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
    """
    Function for inserting data into 'cars' table
    :return: MessageBox call
    """
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


def insert_place():
    """
    Function for inserting data into 'places' table
    :return: MessageBox call
    """
    place_name = entries['place_name'].get()

    if place_name:
        database = MySQL(host, user, password, db_name)
        result = database.insert('places', '(name)', [(f"('{place_name}')")])
        if result:
            entries['place_name'].delete(0, 'end')
            show()
            message_box.showinfo('Insert Status', 'Inserted successfully')
        else:
            message_box.showerror('Insert Status', 'An error occurred while inserting')
    else:
        message_box.showerror('Insert Status', 'All fields are required')


def delete_route():
    """
    Function for deleting a row in 'routes' table
    :return: MessageBox call
    """
    route_name = entries['route_name'].get()
    if route_name:
        database = MySQL(host, user, password, db_name)
        result = database.delete('routes', f"name = '{route_name}'")
        if result:
            entries['route_name'].delete(0, 'end')
            show()
            message_box.showinfo('Delete Status', 'Deleted successfully')
        else:
            message_box.showerror('Delete Status', 'An error occurred while deleting')
    else:
        message_box.showerror('Delete Status', 'Name of the route is compulsory for delete')


def delete_car():
    """
    Function for deleting a row in 'cars' table
    :return: MessageBox call
    """
    car_id = entries['car_id'].get()
    if car_id:
        database = MySQL(host, user, password, db_name)
        result = database.delete('cars', f"id = '{car_id}'")
        if result:
            entries['car_id'].delete(0, 'end')
            show()
            message_box.showinfo('Delete Status', 'Deleted successfully')
        else:
            message_box.showerror('Delete Status', 'An error occurred while deleting')
    else:
        message_box.showerror('Delete Status', 'Name of the route is compulsory for delete')


def delete_place():
    """
    Function for deleting a row in 'places' table
    :return: MessageBox call
    """
    place_name = entries['place_name'].get()
    if place_name:
        database = MySQL(host, user, password, db_name)
        result = database.delete('places', f"name = '{place_name}'")
        if result:
            entries['place_name'].delete(0, 'end')
            show()
            message_box.showinfo('Delete Status', 'Deleted successfully')
        else:
            message_box.showerror('Delete Status', 'An error occurred while deleting')
    else:
        message_box.showerror('Delete Status', 'Name of the route is compulsory for delete')


def update_route():
    """
    Function for updating a row in 'routes' table
    :return: MessageBox call
    """
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
    """
    Function for updating a row in 'cars' table
    :return: MessageBox call
    """
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


def update_place():
    """
    Function for updating a row in 'places' table
    :return: MessageBox call
    """
    message_box.showinfo('Update Status', 'Place can not be updated')


def get_route():
    """
    Function for getting a row from 'routes' table
    :return: MessageBox call
    """
    route_name = entries['route_name'].get()
    if route_name:
        database = MySQL(host, user, password, db_name)
        route = database.get(f"SELECT * from routes WHERE name = '{route_name}'")
        message=f"""
            Id: {route[0][0]}
            Name: {route[0][1]}
            From: {route[0][2]}
            To: {route[0][3]}
            Price: {route[0][4]}
            Car ID: {route[0][5]}
            """
        entries['route_name'].delete(0, 'end')
        message_box.showinfo('Fetch Status', message)
    else:
        message_box.showerror('Fetch Status', 'ID is compulsory for fetch')


def get_car():
    """
    Function for getting a row from 'cars' table
    :return: MessageBox call
    """
    car_id = entries['car_id'].get()
    if car_id:
        database = MySQL(host, user, password, db_name)
        car = database.get(f'SELECT * from cars WHERE id = {car_id}')
        message=f"""
            Car ID: {car[0][0]}
            Name: {car[0][1]}
            """
        entries['car_id'].delete(0, 'end')
        message_box.showinfo('Fetch Status', message)
    else:
        message_box.showerror('Fetch Status', 'ID is compulsory for fetch')


def get_place():
    """
    Function for getting a row from 'places' table
    :return: MessageBox call
    """
    place_name = entries['place_name'].get()
    if place_name:
        database = MySQL(host, user, password, db_name)
        place = database.get(f"SELECT * from places WHERE name = '{place_name}'")
        message=f"""
            Place ID: {place[0][0]}
            Name: {place[0][1]}
            """
        entries['place_name'].delete(0, 'end')
        message_box.showinfo('Fetch Status', message)
    else:
        message_box.showerror('Fetch Status', 'Name is compulsory for fetch')


def show():
    """
    Function for filling the listboxes with the data from database
    :return: nothing to return
    """
    database = MySQL(host, user, password, db_name)
    routes = database.get(f'SELECT * from routes')
    cars = database.get(f'SELECT * from cars')
    places = database.get(f'SELECT * from places')
    routes_list.delete(0, routes_list.size())
    cars_list.delete(0, cars_list.size())
    places_list.delete(0, places_list.size())
    for route in routes:
        insert_data = str(route[0]) + ' ' * 10 + str(route[1])
        routes_list.insert(routes_list.size() + 1, insert_data)
    for car in cars:
        insert_data = str(car[0]) + ' ' * 10 + str(car[1])
        cars_list.insert(cars_list.size() + 1, insert_data)
    for place in places:
        insert_data = str(place[0]) + ' ' * 10 + str(place[1])
        places_list.insert(places_list.size() + 1, insert_data)


root = Tk()
root.geometry('800x450')
root.title('Autostation')
root.resizable(width=False, height=False)

# Create labels section start
labels_texts = [
    'Name of the route',
    'Enter place from',
    'Enter place to',
    'Enter price',
    'Enter car id',
    'Enter car name',
    'Enter place name'
]

for index in range(len(labels_texts)):
    label = Label(root, text=labels_texts[index], font=('bold', 10))
    label.place(x=20, y=30 * (index + 1))

routes_label = Label(root, text='Available routes', font=('bold', 10))
routes_label.place(x=290, y=30)

cars_label = Label(root, text='Available cars', font=('bold', 10))
cars_label.place(x=430, y=30)

places_label = Label(root, text='Available places', font=('bold', 10))
places_label.place(x=570, y=30)

# Create labels section end
# Create entries section start

entries = {}
entries_texts = [
    'route_name',
    'place_from',
    'place_to',
    'price',
    'car_id',
    'car_name',
    'place_name'
]

for index in range(len(entries_texts)):
    entry = Entry()
    entry.place(x=150, y=30 * (index + 1))
    entries[entries_texts[index]] = entry

# Create entries section end
# Create buttons section start

buttons_texts = [
    ['insert', {'route': insert_route, 'car': insert_car, 'place': insert_place}],
    ['delete', {'route': delete_route, 'car': delete_car, 'place': delete_place}],
    ['update', {'route': update_route, 'car': update_car, 'place': update_place}],
    ['get', {'route': get_route, 'car': get_car, 'place': get_place}],
]

routes_buttons_label = Label(root, text='Work with routes:', font=('bold', 10))
routes_buttons_label.place(x=20, y=240)

cars_buttons_label = Label(root, text='Work with cars:', font=('bold', 10))
cars_buttons_label.place(x=20, y=300)

places_buttons_label = Label(root, text='Work with places:', font=('bold', 10))
places_buttons_label.place(x=20, y=360)

for index in range(len(buttons_texts)):
    button = Button(root, text=buttons_texts[index][0], font=('italic', 10), bg='white',
                    command=buttons_texts[index][1]['route'])
    button.place(x=20 + 60 * index, y=260)
    button = Button(root, text=buttons_texts[index][0], font=('italic', 10), bg='white',
                    command=buttons_texts[index][1]['car'])
    button.place(x=20 + 60 * index, y=320)
    button = Button(root, text=buttons_texts[index][0], font=('italic', 10), bg='white',
                    command=buttons_texts[index][1]['place'])
    button.place(x=20 + 60 * index, y=380)
# Create buttons section end

# Create listboxes section start
routes_list = Listbox(root)
routes_list.place(x=290, y=50)

cars_list = Listbox(root)
cars_list.place(x=430, y=50)

places_list = Listbox(root)
places_list.place(x=570, y=50)
# Create listboxes section end


def export_to_sqlite():
    """
    Function for exporting data from MySQL to SQLite databases
    :return: MessageBox call
    """
    mysql_database = MySQL(host, user, password, db_name)
    path_to_database = './sqlite3.db'
    sqlite_database = SQLite(path_to_database)
    try:
        sqlite_database.clear_table('routes')
        sqlite_database.clear_table('cars')
        sqlite_database.clear_table('places')
        data = mysql_database.get('SELECT * from routes')
        sqlite_database.insert('routes', ('id', 'name', 'place_from', 'place_to', 'price', 'car'), data)
        data = mysql_database.get('SELECT * from cars')
        sqlite_database.insert('cars', ('id', 'name'), data)
        data = mysql_database.get('SELECT * from places')
        sqlite_database.insert('places', ('id', 'name'), data)
    except (SQLite_Error, MySQL):
        message_box.showerror('Exporting Status', 'Error was occurred while exporting')
    message_box.showinfo('Exporting Status', 'Export from MySQL to SQLite was successful')


def export_to_postgresql():
    """
    Function for exporting data from SQLite to PostgreSQL databases
    :return: MessageBox call
    """
    mysql_database = MySQL(host, user, password, db_name)
    #postgresql_database = PostgreSQL(host, user, password, db_name)
    try:
        # postgresql_database.clear_table('routes')
        # postgresql_database.clear_table('cars')
        # postgresql_database.clear_table('places')
        data = mysql_database.get('SELECT * from routes')
        #postgresql_database.insert('routes', '(id, name, place_from, place_to, price, car)', data)
        data = mysql_database.get('SELECT * from cars')
        #postgresql_database.insert('cars', ('id', 'name'), data)
        data = mysql_database.get('SELECT * from places')
        #postgresql_database.insert('places', ('id', 'name'), data)
    except (SQLite_Error, Postgre_Error):
        message_box.showerror('Exporting Status', 'Error was occurred while exporting')
    message_box.showinfo('Exporting Status', 'Export from SQLite to PostgreSQL was successful')


def create_tables():
    """
    Function for creating tables in all three databases
    :return: nothing to return
    """
    mysql_database = MySQL(host, user, password, db_name)
    # postgresql_database = PostgreSQL()
    path_to_database = './sqlite3.db'
    sqlite_database = SQLite(path_to_database)
    cars_fields = [
        'id INT AUTO_INCREMENT PRIMARY KEY',
        'name VARCHAR(45) NOT NULL'
    ]
    place_fields = [
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
        'FOREIGN KEY(car) REFERENCES cars(id)',
        'FOREIGN KEY(place_from) REFERENCES places(name)',
        'FOREIGN KEY(place_to) REFERENCES places(name)'
    ]
    mysql_database.create_table('places', place_fields)
    mysql_database.create_table('cars', cars_fields)
    mysql_database.create_table('routes', routes_fields)
    # postgresql_database.create_table('cars', cars_fields)
    # postgresql_database.create_table('routes', routes_fields)
    # postgresql_database.create_table('places', place_fieldss)
    sqlite_database.create_table('places', place_fields)
    sqlite_database.create_table('cars', cars_fields)
    sqlite_database.create_table('routes', routes_fields)


export_to_sqlite_button = Button(root, text='Export from MySQL to SQLite', font=('italic', 10), bg='white',
                                 command=export_to_sqlite)
export_to_sqlite_button.place(x=290, y=260)
export_to_postgre_button = Button(root, text='Export from SQLite to PostgreSQL', font=('italic', 10), bg='white',
                                  command=export_to_postgresql)
export_to_postgre_button.place(x=290, y=320)

create_tables()
show()
root.mainloop()
