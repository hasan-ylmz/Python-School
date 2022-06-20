import mysql.connector

veritab = mysql.connector.connect(
    host = "localhost",
    user ="root",
    passwd = "",
    database = "ybs2020"    
)

# bu sefer şirket isimli belirli bir veri tabanına ulaşıp , o veri tabnına tablo ekleyeceğiz. 
