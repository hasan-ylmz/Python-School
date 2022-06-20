import mysql.connector

veritab = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd ="",
    database ="first_demo"
)

name = input("Adınızı giriniz : ")
gorev= input("yerindeki pozisyonunuzu yazınız : ")
experience = input("Kaç senelik tecrübeye sahipsiniz ? ")
maas = input("Maaşınızı yazınız : ")

mycursor = veritab.cursor()

sorgu = "INSERT INTO employees_2 (name,Job,Level,Salary) VALUES (%s ,%s ,%s ,%s )"
deger = (name,gorev,experience,maas)
mycursor.execute(sorgu,deger)

veritab.commit()

print(mycursor.rowcount ,"kayıt eklendi .")
