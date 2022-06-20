import mysql.connector

veritab = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd ="",
    database ="first_demo"
)

name = input("isminizi giriniz : ")
adres = input("adresinizi giriniz : ")



mycursor = veritab.cursor()

sorgu = "INSERT INTO employees_3 (name,adres) VALUES (%s ,%s )"
deger = (name, adres)
mycursor.execute(sorgu,deger)

veritab.commit()

print(mycursor.rowcount ,"kayıt eklendi .")
