from tkinter import Tk, Label, Entry, Button, Listbox
import tkinter.messagebox as message_box

from mysql.connector import MySQL


def insert_route():
    route_name = entries['route_name'].get()
    place_from = entries['place_form'].get()
    place_to = entries['place_to'].get()
    price = entries['price'].get()
    time = entries['time'].get()
    car = entries['car'].get()

    if all(entries.values()):
        database = MySQL('host', 'user', 'password', 'db_name')
        result = database.insert('routes', '(route_name, place_from, place_to, price, time, car)',
                                 [(route_name, place_from, place_to, price, time, car)])
        assert result is True  # TODO: make an Exception raise
        route_name.delete(0, 'end')
        place_from.delete(0, 'end')
        place_to.delete(0, 'end')
        price.delete(0, 'end')
        time.delete(0, 'end')
        car.delete(0, 'end')
        show()
        message_box.showinfo('Insert Status', 'Inserted successfully')
    else:
        message_box.showerror('Insert Status', 'All fields are required')


def delete_route():
    route_name = entries['route_name'].get()
    if route_name:
        database = MySQL('host', 'user', 'password', 'db_name')
        result = database.delete('routes', f'route_name = {route_name}')
        assert result is True  # TODO: make an Exception raise
        route_name.delete(0, 'end')
        show()
        message_box.showinfo('Delete Status', 'Deleted successfully')
    else:
        message_box.showerror('Delete Status', 'Name of the route is compulsory for delete')


def update_route():
    route_name = entries['route_name'].get()
    place_from = entries['place_form'].get()
    place_to = entries['place_to'].get()
    price = entries['price'].get()
    time = entries['time'].get()
    car = entries['car'].get()

    if all(entries.values()):
        database = MySQL('host', 'user', 'password', 'db_name')
        result = database.update('routes', f'route_name = {route_name}, place_from = {place_from}, '
                                           f'place_to = {place_to}, price = {price}, time = {time}, car = {car}',
                                 f'route_name = {route_name}')
        assert result is True  # TODO: make an Exception raise
        route_name.delete(0, 'end')
        place_from.delete(0, 'end')
        place_to.delete(0, 'end')
        price.delete(0, 'end')
        time.delete(0, 'end')
        car.delete(0, 'end')
        show()
        message_box.showinfo('Update Status', 'Updated successfully')
    else:
        message_box.showerror('Update Status', 'All fields are required')


def get_route():
    route_name = entries['route_name'].get()
    if route_name:
        database = MySQL('host', 'user', 'password', 'db_name')
        route = database.get(f'SELECT * from routes WHERE route_name = {route_name}')
        message_box.showinfo('Fetch Status', route[0][0])
    else:
        message_box.showerror('Fetch Status', 'ID is compulsory for fetch')


def show():
    database = MySQL('host', 'user', 'password', 'db_name')
    routes = database.get(f'SELECT * from routes')
    routes_list.delete(0, routes_list.size())
    cars_list.delete(0, cars_list.size())
    for route in routes:
        insert_data = str(route[0]) + ' ' * 10 + str(route[1])
        routes_list.insert(routes_list.size() + 1, insert_data)
        cars_list.insert(cars_list.size() + 1, insert_data)

# TODO: make buttons for exporting
root = Tk()
root.geometry('600x400')
root.title('Autostation')
root.resizable(width=False, height=False)

labels_texts = [
    'Name of the route',
    'Enter place from',
    'Enter place to',
    'Enter price',
    'Enter time',
    'Enter car id'
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
    'time',
    'car'
]

for index in range(len(entries_texts)):
    entry = Entry()
    entry.place(x=150, y=30 * (index + 1))
    entries[entries_texts[index]] = entry


def insert_car():
    route_name = entries['route_name'].get()
    print(route_name)


buttons_texts = [
    ['insert', {'route': insert_route, 'car': insert_car}],
    ['delete', {'route': insert_route, 'car': insert_car}],
    ['update', {'route': insert_route, 'car': insert_car}],
    ['get', {'route': insert_route, 'car': insert_car}],
]

for index in range(len(buttons_texts)):
    button = Button(root, text=buttons_texts[index][0], font=('italic', 10), bg='white',
                    command=buttons_texts[index][1]['route'])
    button.place(x=20 + 60 * index, y=260)
    button = Button(root, text=buttons_texts[index][0], font=('italic', 10), bg='white',
                    command=buttons_texts[index][1]['car'])
    button.place(x=20 + 60 * index, y=300)

routes_list = Listbox(root)
routes_list.place(x=290, y=50)

cars_list = Listbox(root)
cars_list.place(x=430, y=50)
show()

root.mainloop()
