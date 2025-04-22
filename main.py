import mysql.connector
from tkinter import *

class App:
    def __init__(self):
        self.my_list = []
        self.my_inv = ["что-то"]
        font_style = {'font': ('Helvetica', 16)}
        self.db_connect()
        self.get_all_items()
        self.get_all_inv()

        win = Tk()
        win.title("Инвентарь и вещи")
        win.geometry("1000x600")
        my_list_var = Variable(value=self.my_list)
        items_view = Listbox(listvariable=my_list_var, width=80, **font_style)
        items_view.grid(row=1, column=0)
        lbl_items = Label(text="Вещи", **font_style)
        lbl_items.grid(row=0, column=0)
        lbl_inv = Label(text="Инвентарь", **font_style)
        lbl_inv.grid(row=2, column=0)
        my_inv_var = Variable(value=self.my_inv)
        inv_view = Listbox(listvariable=my_inv_var, width=80, **font_style)
        inv_view.grid(row=3, column=0)
        win.mainloop()

    def db_connect(self):
        """метод для подключения к базе данных.
        БД - локальная, пользователь - pk21,
        пароль - 1234"""
        self.con = mysql.connector.connect(host="localhost",
                                      user='pk21',
                                      password="1234",
                                      database='items')
        self.cur = self.con.cursor()

    def get_all_items(self):
        """Метод получения всех записей из таблицы items"""
        self.cur.execute("SELECT * FROM items")
        ans = self.cur.fetchall()
        for item in ans:
            tmp = f"Название:{item[3]}, тип:{item[1]}, цена:{item[2]} золотых"
            self.my_list.append(tmp)

    def get_all_inv(self):
        """метод получения всех записей из таблицы inventory"""
        sql = """SELECT items.name, inventory.quantity
        FROM inventory
        INNER JOIN items
        ON inventory.item_id = items.id_items"""
        self.cur.execute(sql)
        ans = self.cur.fetchall()
        for item in ans:
            tmp = f"Название: {item[0]}, количество:{item[1]}"
            self.my_inv.append(tmp)


app = App()
