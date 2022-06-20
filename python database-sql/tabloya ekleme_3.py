import mysql.connector

veritab = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "first_demo"
)

# Bu sefer şirket isimli belirli bir veri tabanına ulaşıp , o veri tabanına tablo ekleyeceğiz


mycursor = veritab.cursor()

mycursor.execute("CREATE TABLE employees_2 (Name VARCHAR(255), Job VARCHAR(255) , Level VARCHAR(255))")

# mycursor.execute komutundan sonra tüm mysql komutları kullanılabilir .
