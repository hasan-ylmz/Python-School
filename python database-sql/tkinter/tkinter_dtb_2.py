from tkinter import *
import mysql.connector


root = Tk()

root.geometry("1200x800")


veritab = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd =""
)

print(veritab)

yap = veritab.cursor()


def myClick():
    mylabel =yap.execute("CREATE DATABASE x_1_demo")
    

myButton= Button(root ,text="Click me !",command= myClick)
myButton.pack()
root.mainloop()











