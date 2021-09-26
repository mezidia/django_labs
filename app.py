from tkinter import Tk, Label, Entry, Button, Listbox
import tkinter.messagebox as message_box


# import mysql

def insert():
    id = e_route_name.get()
    name = e_place_from.get()
    phone = e_place_to.get()

    if id == '' or name == '' or phone == '':
        message_box.showerror('Insert Status', 'All fields are required')
    else:
        # mysql
        e_route_name.delete(0, 'end')
        e_place_from.delete(0, 'end')
        e_place_to.delete(0, 'end')
        show()
        message_box.showinfo('Insert Status', 'Inserted successfully')


def delete():
    if e_route_name.get() == '':
        message_box.showerror('Delete Status', 'ID is compulsory for delete')
    else:
        # mysql
        e_route_name.delete(0, 'end')
        e_place_from.delete(0, 'end')
        e_place_to.delete(0, 'end')
        show()
        message_box.showinfo('Delete Status', 'Deleted successfully')


def update():
    id = e_route_name.get()
    name = e_place_from.get()
    phone = e_place_to.get()

    if id == '' or name == '' or phone == '':
        message_box.showerror('Update Status', 'All fields are required')
    else:
        # mysql
        e_route_name.delete(0, 'end')
        e_place_from.delete(0, 'end')
        e_place_to.delete(0, 'end')
        show()
        message_box.showinfo('Update Status', 'Updated successfully')


def get():
    if e_route_name.get() == '':
        message_box.showerror('Fetch Status', 'ID is compulsory for fetch')
    else:
        # mysql
        message_box.showinfo('Fetch Status', e_route_name)


def show():
    rows = [
        [1, 'dasdasdad'],
        [2, 'dadaddad']
    ]
    routes_list.delete(0, routes_list.size())
    cars_list.delete(0, cars_list.size())
    for row in rows:
        insert_data = str(row[0]) + ' ' * 10 + str(row[1])
        routes_list.insert(routes_list.size() + 1, insert_data)
        cars_list.insert(cars_list.size() + 1, insert_data)


root = Tk()
root.geometry('600x300')
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
    label.place(x=20, y=30*(index+1))

routes_label = Label(root, text='Available routes', font=('bold', 10))
routes_label.place(x=290, y=30)

cars_label = Label(root, text='Available cars', font=('bold', 10))
cars_label.place(x=430, y=30)

e_route_name = Entry()
e_route_name.place(x=150, y=30)

e_place_from = Entry()
e_place_from.place(x=150, y=60)

e_place_to = Entry()
e_place_to.place(x=150, y=90)

e_price = Entry()
e_price.place(x=150, y=120)

e_time = Entry()
e_time.place(x=150, y=150)

e_car = Entry()
e_car.place(x=150, y=180)

insert = Button(root, text='insert', font=('italic', 10), bg='white', command=insert)
insert.place(x=20, y=260)

delete = Button(root, text='delete', font=('italic', 10), bg='white', command=delete)
delete.place(x=70, y=260)

update = Button(root, text='update', font=('italic', 10), bg='white', command=update)
update.place(x=130, y=260)

get = Button(root, text='get', font=('italic', 10), bg='white', command=get)
get.place(x=190, y=260)

routes_list = Listbox(root)
routes_list.place(x=290, y=50)

cars_list = Listbox(root)
cars_list.place(x=430, y=50)
show()

root.mainloop()
