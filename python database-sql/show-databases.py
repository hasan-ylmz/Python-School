import mysql.connector

veritab = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd = ""
    )

print(veritab)

yap = veritab.cursor()
yap.execute("SHOW DATABASES")

for x in yap:
    print(x)
