import mysql.connector

veritab= mysql.connector.connect(
    host = "localhost",
    user ="root",
    passwd = "",
    database = "first_demo"
    )

# Tablo oluştururken her kayıt için birincil anahtar içeren bir sütun da oluşturmanız gerekir .
# Bu bir primary key tanımlayarak yapılabilir .

print(veritab)

mycursor = veritab.cursor()

mycursor.execute("CREATE TABLE employees_3 (id INT AUTO_INCREMENT PRIMARY KEY , name VARCHAR(255), address VARCHAR(255))")
