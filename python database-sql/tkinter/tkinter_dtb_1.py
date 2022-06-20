from tkinter import *
import mysql.connector


root = Tk()

root.geometry("1200x800")


def myClick():
    mylabel = Label(root , text ="Welcome database :) ")
    mylabel.pack()

myButton= Button(root ,text="Click me !",command= myClick)
myButton.pack()
root.mainloop()











