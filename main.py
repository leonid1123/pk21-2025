import mysql.connector
from tkinter import *


class App:
    def __init__(self):
        self.my_list = []
        self.my_inv = ["что-то"]
        self.font_style = {'font': ('Helvetica', 16)}
        self.db_connect()
        self.get_all_items()
        self.get_all_inv()

        self.win = Tk()
        self.setUI()

        self.win.mainloop()

    def setUI(self):
        self.win.title("Инвентарь и вещи")
        self.win.geometry("1300x600")
        my_list_var = Variable(value=self.my_list)
        items_view = Listbox(listvariable=my_list_var, width=80, **self.font_style)
        items_view.grid(row=1, column=0, rowspan=4)
        lbl_items = Label(text="Вещи", **self.font_style)
        lbl_items.grid(row=0, column=0)
        lbl_inv = Label(text="Инвентарь", **self.font_style)
        lbl_inv.grid(row=5, column=0)
        my_inv_var = Variable(value=self.my_inv)
        inv_view = Listbox(listvariable=my_inv_var, width=80, **self.font_style)
        inv_view.grid(row=6, column=0)
        name_lbl = Label(text="Название")
        type_lbl = Label(text="Тип")
        price_lbl = Label(text="Цена")
        name_lbl.grid(row=1, column=1)
        type_lbl.grid(row=2, column=1)
        price_lbl.grid(row=3, column=1)
        name_entry = Entry()
        type_entry = Entry()
        price_entry = Entry()
        name_entry.grid(row=1, column=2)
        type_entry.grid(row=2, column=2)
        price_entry.grid(row=3, column=2)
        add_item_btn = Button(text="Добавить")
        add_item_btn.grid(row=4, column=1, columnspan=2)

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
            tmp = f"Название:{item[1]}, тип:{item[2]}, цена:{item[3]} золотых"
            self.my_list.append(tmp)

    def get_all_inv(self):
        """метод получения всех записей из таблицы inventory"""
        sql = """SELECT items.name, inventory.quantity
        FROM inventory
        INNER JOIN items
        ON inventory.id_item = items.id"""
        self.cur.execute(sql)
        ans = self.cur.fetchall()
        for item in ans:
            tmp = f"Название: {item[0]}, количество:{item[1]}"
            self.my_inv.append(tmp)


app = App()
