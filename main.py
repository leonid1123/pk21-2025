import mysql.connector
from tkinter import *

class App:
    def __init__(self):
        con = mysql.connector.connect(host="localhost",
                        user='pk21',
                        password="1234",
                        database='items')
        cur = con.cursor()
        cur.execute("SELECT * FROM items")
        ans = cur.fetchall()
        for item in ans:
            print(item)
        win = Tk()
        win.title("Инвентарь и вещи")
        win.geometry("300x300")
        my_list = ["пупупу","чпунь","хочу 5"]
        my_list_var = Variable(value=my_list)
        items_view = Listbox(listvariable=my_list_var)
        items_view.grid(row=0, column=0)
        win.mainloop()


app = App()
