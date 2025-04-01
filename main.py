import mysql.connector


class Sosiski:
    def __init__(self, name, price, date):
        self.name = name
        self.price = price
        self.date = date


cnx = mysql.connector.connect(
    host="localhost",
    user="pk21",
    password="1234",
    database="sosiski")
cursor = cnx.cursor()
cursor.execute("SELECT * FROM sosiski")
ans = cursor.fetchall()
print(ans)
sosiski = []
for item in ans:
    tmp_sosiska = Sosiski(item[1],item[2],item[3])
    sosiski.append(tmp_sosiska)

for item in sosiski:
    print(item.name, item.price, item.date)
