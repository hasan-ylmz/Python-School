import mysql.connector

veritab = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "first_demo"
)

# Bu sefer şirket isimli belirli bir veri tabanına ulaşıp , o veri tabanına tablo ekleyeceğiz

print(veritab)

mycursor =veritab.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
