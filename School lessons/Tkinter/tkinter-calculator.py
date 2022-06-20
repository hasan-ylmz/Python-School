from tkinter import *
import math

ekran = Tk()
ekran.title("Calculator")
ekran.geometry("600x180")
ekran.wm_attributes("-alpha",0.9)
ekran.resizable(False,False)

sayıbir= Label(text="Birinci sayı", bg="blue",fg="white")
sayıbir.place(x=30, y=10)

girdibir=Entry()
girdibir.place(x=100,y=10)


sayıiki= Label(text="İkinci sayı ", bg="blue",fg="white")
sayıiki.place(x=30, y=50)

girdiiki=Entry()
girdiiki.place(x=100,y=50)

sonuc=Label(text="Sonuç" ,bg="black",fg="white")
sonuc.place(x=30,y=90)

girdiüc=Entry()
girdiüc.place(x=100,y=90)

def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text=" +",command=topla)
toplama.place(x=275, y=10)


def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text=" - ",command=topla)
toplama.place(x=275, y=50)


def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text=" / ",command=topla)
toplama.place(x=275, y=90)


def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text=" * ",command=topla)
toplama.place(x=325, y=10)

def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text=" sec ",command=topla)
toplama.place(x=325, y=50)

def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text=" ! ",command=topla)
toplama.place(x=325, y=90)



def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text=" tan ",command=topla)
toplama.place(x=375, y=10)

def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text=" cot ",command=topla)
toplama.place(x=375, y=50)


def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text="  sin ",command=topla)
toplama.place(x=375, y=90)

def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text=" cos ",command=topla)
toplama.place(x=425, y=10)

def topla():
    yazı["text"]=girdibir.get() 
toplama=Button(text=" cot ",command=topla)
toplama.place(x=425, y=50)

def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text="  csc ",command=topla)
toplama.place(x=425, y=90)

def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text="  x² ",command=topla)
toplama.place(x=490, y=10)

def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text="  x³ ",command=topla)
toplama.place(x=490, y=50)

def topla():
    yazı["text"]=girdibir.get()
toplama=Button(text="  log ",command=topla)
toplama.place(x=490, y=90)














