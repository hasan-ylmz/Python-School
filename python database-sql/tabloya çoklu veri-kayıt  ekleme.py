import mysql.connector

veritab = mysql.connector.connect(
    host = "localhost",
    user ="root",
    passwd = "",
    database = "first_demo"
)

# INSERT INTO  komutu ile kayıt ekleriz . Çoklu kayıt için verilerimizi bir ilsete içine ekleriz .

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


