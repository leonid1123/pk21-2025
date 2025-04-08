import mysql.connector

con = mysql.connector.connect(host="localhost",
                        user='pk21',
                        password="1234",
                        database='items')
cur = con.cursor()
cur.execute("SELECT * FROM items")
ans = cur.fetchall()
for item in ans:
    print(item)
