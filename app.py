from tkinter import Tk, Label, Entry, Button, Listbox
import tkinter.messagebox as message_box
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import true
from models import Base, Place, Car, Route
# import psycopg2
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# # Устанавливаем соединение с postgres
# connection = psycopg2.connect(user="root", password="Hogger")
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# import pymysql
# pymysql.install_as_MySQLdb()

# import pandas as pd

# engine_sqlite = create_engine('sqlite:///app.sqlite')
engine_mysql = create_engine(f'mysql+mysqldb://{user}:{pass}@localhost/{dbname}')
# engine_postgresql = create_engine(f'postgresql+psycopg2://{user}:{pass}@localhost/{dbname}')
# Base.metadata.create_all(engine_sqlite)
Base.metadata.create_all(engine_mysql)
# Base.metadata.create_all(engine_postgresql)
# session_sqlite = Session(bind=engine_sqlite)
session_mysql = Session(bind=engine_mysql)
# session_postgresql = Session(bind=engine_postgresql)

def insert_route():
    """
    Function for inserting data into 'routes' table
    :return: MessageBox call
    """
    route_name = entries['route_name'].get()
    place_from = entries['place_from'].get()
    place_to = entries['place_to'].get()
    price = entries['price'].get()
    car = entries['car_name'].get()

    if all(entries.values()):
        route = Route(
            name=route_name,
            place_from=place_from,
            place_to=place_to,
            price=price,
            car=car
        )
        try:
            session_mysql.add(route)
            session_mysql.commit()

            entries['route_name'].delete(0, 'end')
            entries['place_from'].delete(0, 'end')
            entries['place_to'].delete(0, 'end')
            entries['price'].delete(0, 'end')
            entries['car_name'].delete(0, 'end')
            show()
            message_box.showinfo('Insert Status', 'Inserted successfully')
        except:
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
        car = Car(name=car_name)
        try:
            session_mysql.add(car)
            session_mysql.commit()
            entries['car_name'].delete(0, 'end')
            show()
            message_box.showinfo('Insert Status', 'Inserted successfully')
        except:
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
        place = Place(name=place_name)
        try:
            session_mysql.add(place)
            session_mysql.commit()

            entries['place_name'].delete(0, 'end')
            show()
            message_box.showinfo('Insert Status', 'Inserted successfully')
        except:
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
        route = session_mysql.query(Route).filter(Route.name == route_name).one()
        try:
            session_mysql.delete(route)
            session_mysql.commit()

            entries['route_name'].delete(0, 'end')
            show()
            message_box.showinfo('Delete Status', 'Deleted successfully')
        except:
            message_box.showerror('Delete Status', 'An error occurred while deleting')
    else:
        message_box.showerror('Delete Status', 'Name of the route is compulsory for delete')


def delete_car():
    """
    Function for deleting a row in 'cars' table
    :return: MessageBox call
    """
    car_name = entries['car_name'].get()
    if car_name:
        car = session_mysql.query(Car).filter(Car.name == car_name).one()
        try:
            session_mysql.delete(car)
            session_mysql.commit()

            entries['car_name'].delete(0, 'end')
            show()
            message_box.showinfo('Delete Status', 'Deleted successfully')
        except:
            message_box.showerror('Delete Status', 'An error occurred while deleting')
    else:
        message_box.showerror('Delete Status', 'Id of the car is compulsory for delete')


def delete_place():
    """
    Function for deleting a row in 'places' table
    :return: MessageBox call
    """
    place_name = entries['place_name'].get()
    if place_name:
        place = session_mysql.query(Place).filter(Place.name == place_name).one()
        try:
            session_mysql.delete(place)
            session_mysql.commit()

            entries['place_name'].delete(0, 'end')
            show()
            message_box.showinfo('Delete Status', 'Deleted successfully')
        except:
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
    car = entries['car_name'].get()
    if all(entries.values()):
        route = session_mysql.query(Route).filter(Route.name == route_name).one()
        route.place_from = place_from
        route.place_to = place_to
        route.price = price
        route.car = car
        try:
            session_mysql.add(route)
            session_mysql.commit()

            entries['route_name'].delete(0, 'end')
            entries['place_from'].delete(0, 'end')
            entries['place_to'].delete(0, 'end')
            entries['price'].delete(0, 'end')
            entries['car_name'].delete(0, 'end')
            show()
            message_box.showinfo('Update Status', 'Updated successfully')
        except:
            message_box.showerror('Update Status', 'An error occurred while updating')
    else:
        message_box.showerror('Update Status', 'All fields are required')


def update_car():
    """
    Function for updating a row in 'cars' table
    :return: MessageBox call
    """
    message_box.showinfo('Update Status', 'Place can not be updated')


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
        route = session_mysql.query(Route).filter(Route.name == route_name).one()

        if route:
            message = f"""
                Name: {route.get('name')}
                From: {route.get('place_from')}
                To: {route.get('place_to')}
                Price: {route.get('price')}
                Car ID: {route.get('car')}
                """
            entries['route_name'].delete(0, 'end')
            message_box.showinfo('Fetch Status', message)
        else:
            message_box.showerror('Fetch Status', 'Route with this name is not in the table')
    else:
        message_box.showerror('Fetch Status', 'ID is compulsory for fetch')


def get_car():
    """
    Function for getting a row from 'cars' table
    :return: MessageBox call
    """
    car_name = entries['car_name'].get()
    if car_name:
        car = session_mysql.query(Car).filter(Car.name == car_name).one()

        if car:
            message = f"""
                Name: {car.get('name')}
                """
            entries['car_name'].delete(0, 'end')
            message_box.showinfo('Fetch Status', message)
        else:
            message_box.showerror('Fetch Status', 'Car with this name is not in the table')
    else:
        message_box.showerror('Fetch Status', 'ID is compulsory for fetch')


def get_place():
    """
    Function for getting a row from 'places' table
    :return: MessageBox call
    """
    place_name = entries['place_name'].get()
    if place_name:
        place = session_mysql.query(Place).filter(Place.name == place_name).one()

        if place:
            message = f"""
                Name: {place.get('name')}
                """
            entries['place_name'].delete(0, 'end')
            message_box.showinfo('Fetch Status', message)
        else:
            message_box.showerror('Fetch Status', 'Place with this name is not in the table')
    else:
        message_box.showerror('Fetch Status', 'Name is compulsory for fetch')


def show():
    """
    Function for filling the listboxes with the data from database
    :return: nothing to return
    """
    routes = select(Route)
    cars = select(Car)
    places = select(Place)
    routes_list.delete(0, routes_list.size())
    cars_list.delete(0, cars_list.size())
    places_list.delete(0, places_list.size())
    for route in routes:
        insert_data = route.get('name')
        routes_list.insert(routes_list.size() + 1, insert_data)
    for car in cars:
        insert_data = car.get('name')
        cars_list.insert(cars_list.size() + 1, insert_data)
    for place in places:
        insert_data = place.get('name')
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

def create_some_data():
    """
    Function for create start data
    """
    if True:
        cars_values = [
            {'name': 'Glovo'},
            {'name': 'Raketa'},
            {'name': 'Medivac'}
        ]
        places_values = [
            {'name': 'Kyiv'},
            {'name': 'Odesa'},
            {'name': 'Alushta'},
            {'name': 'Vinnytsia'}
        ]
        routes_values = [
            {'name': 'Kyiv-Odesa', 'place_from': places_values[0]['name'], 'place_to': places_values[1]['name'],
             'price': 23.32, 'car': cars_values[0]['name']},
            {'name': 'Odesa-Alushta', 'place_from': places_values[1]['name'], 'place_to': places_values[2]['name'],
             'price': 137.0, 'car': cars_values[2]['name']},
            {'name': 'Alushta-Kyiv', 'place_from': places_values[2]['name'], 'place_to': places_values[0]['name'],
             'price': 100.0, 'car': cars_values[1]['name']},
            {'name': 'Vinnytsia-Alushta', 'place_from': places_values[3]['name'], 'place_to': places_values[2]['name'],
             'price': 87.0, 'car': cars_values[1]['name']}
        ]
        for car_object in cars_values:
            car = Car(name=car_object['name'])
            session_mysql.add(car)
            session_mysql.commit()
        for place_object in places_values:
            place = Place(name=place_object['name'])
            session_mysql.add(place)
            session_mysql.commit()
        for route_object in routes_values:
            place = Route(name=route_object['name'],
                          place_from=route_object['place_from'],
                          place_to=route_object['place_to'],
                          price=route_object['price'],
                          car=route_object['car'])
            session_mysql.add(place)
            session_mysql.commit()


create_some_data()
show()
root.mainloop()
