import mysql.connector

veritab = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd ="",
    database ="first_demo"
)

# Tablo zaten varsa , ALTER TABLE anahtar sözcüğünü kullanarak PRIMARY KEY ekleyebiliriz .
print(veritab)

mycursor =veritab.cursor()

mycursor.execute("ALTER TABLE employees_2  ADD COLUMN Salary VARCHAR(255)")

""" Tabloya  sütun / alan ekleme """
