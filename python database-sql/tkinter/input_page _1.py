from tkinter import *
import mysql.connector

veritab = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = "first_demo"
)

root = Tk()

root.geometry("1200x800")

name = Label(text = "İsminizi yazın").place(x = 40, y = 40) 
job = Label(text = "İşyerindeki pozisyonunuzu yazınız ").place(x = 40, y = 80) 
experience = Label(text = "Kaç yıl deneyiminiz var ? ").place(x = 40, y = 120) 
salary = Label(text = "Maaşınızı yazınız :").place(x = 40, y = 160) 

e1 = Entry().place(x = 300, y = 40)
e2 = Entry().place(x = 300, y = 80)
e3 = Entry().place(x = 300, y = 120)
e4 = Entry().place(x = 300, y = 160)

print(veritab)

mycursor = veritab.cursor()


def myClick():
    mylabel =sorgu = "INSERT INTO employees_2 (name,Job,Level,Salary) VALUES (%s ,%s ,%s ,%s )"
    deger = (e1,e2,e3,e4)
    mycursor.execute(sorgu,deger)

veritab.commit()

print(mycursor.rowcount ,"kayıt eklendi .")

    

myButton= Button(root ,text="Click me !",command= myClick)
myButton.pack()
root.mainloop()











