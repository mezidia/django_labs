from tkinter import *
import tkinter.messagebox as MessageBox

# import mysql

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

root.mainloop()
