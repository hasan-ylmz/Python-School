import mysql.connector

veritab = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "first_database"
)

# Bu sefer şirket isimli belirli bir veri tabanına ulaşıp , o veri tabanına tablo ekleyeceğiz


mycursor = veritab.cursor()

mycursor.execute("ALTER TABLE Urun  ADD COLUMN İD  INT AUTO_INCREMENT PRIMARY KEY ")
