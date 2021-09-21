from tkinter import Tk, Label, Entry, Button, Listbox
import tkinter.messagebox as message_box


# import mysql

def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if id == '' or name == '' or phone == '':
        message_box.showerror('Insert Status', 'All fields are required')
    else:
        # mysql
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        message_box.showinfo('Insert Status', 'Inserted successfully')


def delete():
    if e_id.get() == '':
        message_box.showerror('Delete Status', 'ID is compulsory for delete')
    else:
        # mysql
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        message_box.showinfo('Delete Status', 'Deleted successfully')


def update():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if id == '' or name == '' or phone == '':
        message_box.showerror('Update Status', 'All fields are required')
    else:
        # mysql
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        message_box.showinfo('Update Status', 'Updated successfully')


def get():
    if e_id.get() == '':
        message_box.showerror('Fetch Status', 'ID is compulsory for fetch')
    else:
        # mysql
        message_box.showinfo('Fetch Status', e_id)


def show():
    list.delete(0, list.size())
    rows = [
        [1, 'dasdasdad'],
        [2, 'dadaddad']
    ]
    list.delete(0, list.size())
    for row in rows:
        insertData = str(row[0]) + ' ' * 10 + str(row[1])
        list.insert(list.size() + 1, insertData)


root = Tk()
root.geometry('600x300')
root.title('Autostation')
root.resizable(width=False, height=False)

id = Label(root, text='Enter id', font=('bold', 10))
id.place(x=20, y=30)

name = Label(root, text='Enter name', font=('bold', 10))
name.place(x=20, y=60)

phone = Label(root, text='Enter phone', font=('bold', 10))
phone.place(x=20, y=90)

e_id = Entry()
e_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

e_phone = Entry()
e_phone.place(x=150, y=90)

insert = Button(root, text='insert', font=('italic', 10), bg='white', command=insert)
insert.place(x=20, y=140)

delete = Button(root, text='delete', font=('italic', 10), bg='white', command=delete)
delete.place(x=70, y=140)

update = Button(root, text='update', font=('italic', 10), bg='white', command=update)
update.place(x=130, y=140)

get = Button(root, text='get', font=('italic', 10), bg='white', command=get)
get.place(x=190, y=140)

list = Listbox(root)
list.place(x=290, y=30)
show()

root.mainloop()
