import sqlite3

db = sqlite3.connect("deneme.db")
db.row_factory = sqlite3.Row

imlec = db.cursor()

liste = imlec.execute("select * from sahis").fetchall()
for i in liste:
    print(i["name"], i["yas"])

print("**********************")
imlec_2 = db.cursor()
liste = imlec_2.execute("select * from sahis").fetchall()
for i in liste:
    print(i["name"], i["yas"])

