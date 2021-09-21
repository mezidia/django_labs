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

root.mainloop()
