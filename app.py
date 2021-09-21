from tkinter import Tk, Label, Entry, Button
import tkinter.messagebox as MessageBox

# import mysql

def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if id == '' or name == '' or phone == '':
        MessageBox.showerror('Insert Status', 'All fields are required')
    else:
        print('mysql')
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        MessageBox.showinfo('Insert Status', 'Inserted successfully')
        # mysql

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

delete = Button(root, text='delete', font=('italic', 10), bg='white', command=insert)
delete.place(x=70, y=140)

update = Button(root, text='update', font=('italic', 10), bg='white', command=insert)
update.place(x=130, y=140)

get = Button(root, text='get', font=('italic', 10), bg='white', command=insert)
get.place(x=190, y=140)

root.mainloop()
