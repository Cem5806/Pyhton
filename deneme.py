import sqlite3 

db = sqlite3.connect("deneme.db")
db.row_factory = sqlite3.Row
imlec = db.cursor()


class kişi():

    def kişi_oluştur(self, isim, yaş):
        self.isim = isim
        self.yaş = yaş

        imlec.execute("insert into sahis(name,yas) values (?, ?)", (self.isim, self.yaş))
        db.commit()

    def kişi_telefon_ekle(self, telefon):
        self.telefon = telefon
        self.id = imlec.execute("select id from sahis where name = ?", (self.isim,)).fetchone()[0]

        imlec.execute("insert into phonebook(number,owner_id) values (?, ?)", (self.telefon,self.id))
        db.commit()

k1 = kişi()
while True:
    print("1- Kişi oluştur")
    print("2- Kişileri listele")
    print("3- Çıkış")
    secim = int(input("Seçiminiz: "))
    if secim == 1:
        k1.kişi_oluştur(input("kişi ismi:  "),input("kişi yaş: "))
        k1.kişi_telefon_ekle(input("Telefon: "))
    elif secim == 2:
        isimler = imlec.execute("select * from sahis").fetchall()
        print("\tAD\t|\tTelefon\t")
        print("---------------------------------------")
        for i in isimler:
            print(i["name"],"\t|\t",imlec.execute("select number from phonebook where owner_id = ?",(i["id"],)).fetchone()["number"])
    elif secim == 3:
        break