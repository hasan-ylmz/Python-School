import mysql.connector

veritab = mysql.connector.connect(
    host = "localhost",
    user ="root",
    passwd = "",
    database = "first_demo"
)
sayi= int(input(" Kaç kayıt eklemek istiyorsun "))

for i in range (sayi):
    ad =input("isminizi giriniz")
    yer = input("adresinizi giriniz ")


mycursor = veritab.cursor()

sorgu = "INSERT INTO employees_3 (name,address) VALUES (%s,%s)"

deger = [
    ("Ekrem", "İstanbul No:15"),
    ("Mansur", "Ankara No:64"),
    ("Ayşe", "İzmir No:67"),
    ("Deniz", "Bodrum No:41"),
    ("Melih", "Trabzon No:61"),
    ("Onur", "Hatay No:45"),
]

mycursor.executemany(sorgu,deger)

veritab.commit()

print(mycursor.rowcount, "Kayıt eklendi.")


