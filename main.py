import mysql.connector
from tkinter import *

class App:
    def __init__(self):
        my_list = []
        font_style = {'font': ('Helvetica', 16)}
        con = mysql.connector.connect(host="localhost",
                        user='pk21',
                        password="1234",
                        database='items')
        cur = con.cursor()
        cur.execute("SELECT * FROM items")
        ans = cur.fetchall()
        for item in ans:
            tmp = f"Название:{item[3]}, тип:{item[1]}, цена:{item[2]} золотых"
            my_list.append(tmp)
        win = Tk()
        win.title("Инвентарь и вещи")
        win.geometry("800x300")
        my_list_var = Variable(value=my_list)
        items_view = Listbox(listvariable=my_list_var, width=80, **font_style)
        items_view.grid(row=0, column=0)
        win.mainloop()


app = App()
