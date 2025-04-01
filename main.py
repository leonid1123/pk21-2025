import mysql.connector


class Keyboards:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cnx = mysql.connector.connect(
    host="localhost",
    user="pk21",
    password="1234",
    database="keyboard")
cursor = cnx.cursor()
cursor.execute("SELECT * FROM keyboard")
ans = cursor.fetchall()
print(ans)

k1 = Keyboards("белая", 1200)
k2 = Keyboards("Китай дешевый",5400)
x=[k1,k2]
for item in x:
    print(item.name, item.price)



print("name: ", k1.name)
print("price: ", k1.price)
print("name: ", k2.name)
print("price: ", k2.price)

