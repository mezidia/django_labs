from tkinter import Tk, Label, Entry, Button, Listbox
import tkinter.messagebox as message_box
from sqlalchemy import create_engine, select, insert, update, delete
from sqlalchemy.orm import Session
import pandas as pd

from models import Base, Place, Car, Route

engine_sqlite = create_engine('sqlite:///app.sqlite')
engine_mysql = create_engine('mysql+pymysql://root:Password@localhost/medivac')
engine_postgresql = create_engine('postgresql+psycopg2://postgres:Password@localhost/medivac')
Base.metadata.create_all(engine_sqlite)
Base.metadata.create_all(engine_mysql)
Base.metadata.create_all(engine_postgresql)
session_sqlite = Session(bind=engine_sqlite)
session_mysql = Session(bind=engine_mysql)
session_postgresql = Session(bind=engine_postgresql)


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
        try:
            connection = engine_mysql.connect()
            ins = insert(Route)
            _ = connection.execute(ins,
                                   name=route_name,
                                   place_from=place_from,
                                   place_to=place_to,
                                   price=price,
                                   car=car
                                   )

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
        try:
            connection = engine_mysql.connect()
            ins = insert(Car)
            _ = connection.execute(ins, name=car_name)
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
        try:
            connection = engine_mysql.connect()
            ins = insert(Place)
            _ = connection.execute(ins, name=place_name)

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
        try:
            connection = engine_mysql.connect()
            s = delete(Route).where(Route.name == route_name)
            _ = connection.execute(s)
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
        try:
            connection = engine_mysql.connect()
            s = delete(Car).where(Car.name == car_name)
            _ = connection.execute(s)

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
        try:
            connection = engine_mysql.connect()
            s = delete(Place).where(Place.name == place_name)
            _ = connection.execute(s)

            entries['place_name'].delete(0, 'end')
            show()
            message_box.showinfo('Delete Status', 'Deleted successfully')
        except Exception as e:
            print(e)
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
        try:
            connection = engine_mysql.connect()
            s = update(Route).where(
                Route.name == route_name
            ).values(
                place_from=place_from,
                place_to=place_to,
                price=price,
                car=car
            )
            _ = connection.execute(s)

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
    message_box.showinfo('Update Status', 'Car can not be updated')


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
        connection = engine_mysql.connect()
        s = select([Route]).where(
            Route.name == route_name
        )
        route = connection.execute(s).first()
        if route:
            message = f"""
                Name: {route.name}
                From: {route.place_from}
                To: {route.place_to}
                Price: {route.price}
                Car name: {route.car}
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
        connection = engine_mysql.connect()
        s = select([Car]).where(
            Car.name == car_name
        )
        car = connection.execute(s).first()
        if car:
            message = f"""
                Name: {car.name}
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
        connection = engine_mysql.connect()
        s = select([Place]).where(
            Place.name == place_name
        )
        place = connection.execute(s).first()
        if place:
            message = f"""
                Name: {place.name}
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
    routes = engine_mysql.connect().execute(select(Route)).fetchall()
    cars = engine_mysql.connect().execute(select(Car)).fetchall()
    places = engine_mysql.connect().execute(select(Place)).fetchall()
    routes_list.delete(0, routes_list.size())
    cars_list.delete(0, cars_list.size())
    places_list.delete(0, places_list.size())
    for route in routes:
        insert_data = route[1]
        routes_list.insert(routes_list.size() + 1, insert_data)
    for car in cars:
        insert_data = car[1]
        cars_list.insert(cars_list.size() + 1, insert_data)
    for place in places:
        insert_data = place[1]
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

def show_csv(data: list) -> None:
    """
    Function for showing data in csv format
    :return: nothing to return
    """
    df = pd.DataFrame(data)
    print(df.to_csv(index=False))


def export_data(from_session: Session, to_session: Session) -> None:
    """
    Function for exporting data from one database to another one
    :return: nothing to return
    """
    connection = from_session.connection()
    s_cars = select([Car])
    s_places = select([Place])
    s_routes = select([Route])
    cars = connection.execute(s_cars).fetchall()
    places = connection.execute(s_places).fetchall()
    routes = connection.execute(s_routes).fetchall()
    show_csv(cars)
    show_csv(places)
    show_csv(routes)

    to_session.query(Route).delete()
    to_session.query(Place).delete()
    to_session.query(Car).delete()
    to_session.commit()
    for car in cars:
        car_object = Car(id=car[0], name=car[1])
        to_session.add(car_object)
        to_session.commit()
    for place in places:
        place_object = Place(id=place[0], name=place[1])
        to_session.add(place_object)
        to_session.commit()
    for route in routes:
        route_object = Route(id=route[0], name=route[1], place_from=route[2], place_to=route[3], price=route[4],
                             car=route[5])
        to_session.add(route_object)
        to_session.commit()


def export_to_sqlite():
    """
    Function for exporting data from MySQL to SQLite databases
    :return: MessageBox call
    """
    try:
        export_data(session_mysql, session_sqlite)
    except Exception as e:
        print(e)
        return message_box.showerror('Exporting Status', 'Error was occurred while exporting')
    return message_box.showinfo('Exporting Status', 'Export from MySQL to SQLite was successful')


def export_to_postgresql():
    """
    Function for exporting data from SQLite to PostgreSQL databases
    :return: MessageBox call
    """
    try:
        export_data(session_sqlite, session_postgresql)
    except Exception as e:
        print(e)
        return message_box.showerror('Exporting Status', 'Error was occurred while exporting')
    return message_box.showinfo('Exporting Status', 'Export from SQLite to PostgreSQL was successful')


def create_some_data():
    """
    Function for create start data
    """
    if session_mysql.query(Car).count() == 0 and session_mysql.query(Place).count() == 0 and \
            session_mysql.query(Route).count() == 0:
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
             'price': 100.0, 'car': cars_values[1]['name']}
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
            route = Route(name=route_object['name'],
                          place_from=route_object['place_from'],
                          place_to=route_object['place_to'],
                          price=route_object['price'],
                          car=route_object['car'])
            session_mysql.add(route)
            session_mysql.commit()


export_to_sqlite_button = Button(root, text='Export from MySQL to SQLite', font=('italic', 10), bg='white',
                                 command=export_to_sqlite)
export_to_sqlite_button.place(x=290, y=260)
export_to_postgre_button = Button(root, text='Export from SQLite to PostgreSQL', font=('italic', 10), bg='white',
                                  command=export_to_postgresql)
export_to_postgre_button.place(x=290, y=320)

create_some_data()
show()
root.mainloop()
