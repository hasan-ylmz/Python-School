import mysql.connector

veritab = mysql.connector.connect(
    host = "localhost",
    user ="root",
    passwd = "",
    database = "ybs2020"    
)

# bu sefer şirket isimli belirli bir veri tabanına ulaşıp , o veri tabnına tablo ekleyeceğiz. 
print(veritab)

yap = veritab.cursor()

yap.execute("CREATE TABLE ogrencı (isim VARCHAR(255) , adres VARCHAR(255) ogno VARCHAR(255)) ")