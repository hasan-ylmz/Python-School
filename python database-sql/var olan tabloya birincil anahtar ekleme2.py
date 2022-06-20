import mysql.connector

veritab = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd ="",
    database ="first_demo"
)

#  "INSERT INTO" komutu ile kayıt ekleriz .

mycursor = veritab.cursor()

sorgu = "INSERT INTO employees_3 (name,address) VALUES (%s ,%s)"
deger = ("Hasan", "Ktu uzem NO:34")
mycursor.execute(sorgu,deger)

# veritabanına veritab commit ile ekliyoruz .
veritab.commit()

print(mycursor.rowcount ,"kayıt eklendi .")
