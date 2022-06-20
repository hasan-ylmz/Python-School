import mysql.connector

veritab = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd =""
)

print(veritab)

yap = veritab.cursor()

yap.execute("CREATE DATABASE person")
