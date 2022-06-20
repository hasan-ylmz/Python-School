import mysql.connector

veritab = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd ="",
    database ="first_demo"
)

#  "INSERT INTO" komutu ile kayıt ekleriz .

mycursor = veritab.cursor()

sorgu = "INSERT INTO Urun (Urun_kodu,Urun_ısım,Urun_kategorı,Urun_tedarıkcısı,Urun_mıktar,Urun_Bırım,Urun_kayıt_tarıhs,Urun_Cıkıs_tarıh) VALUES (%s, %s, %s, %s ,%s,%s, %s, %s))"
deger = (Entry1,Entry2,TCombobox1,Entry3,Entry4,Entry5,Entry6,Entry7)
mycursor.execute(sorgu,deger)

# veritabanına veritab commit ile ekliyoruz .
veritab.commit()

print(mycursor.rowcount ,"kayıt eklendi .")
