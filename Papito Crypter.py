# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import base64
top = Tk()
top.geometry("750x500")
top.title("X")
def ac():
    y = x.get()
    if var.get() == 1 and boolVar.get() == 0:#Base64 encode
        t.delete('1.0', END)
        t.insert(INSERT, base64.b64encode(y.encode('utf-8')))
    elif var.get() == 2 and boolVar.get() == 0:#Base32 encode
        t.delete('1.0', END)
        t.insert(INSERT, base64.b32encode(y.encode('utf-8')))
    elif var.get() == 3 and boolVar.get() == 0:#Base16 encode
        t.delete('1.0', END)
        t.insert(INSERT, base64.b16encode(y.encode('utf-8')))
    elif var.get() == 4 and boolVar.get() == 0:#b85 encode
        t.delete('1.0', END)
        t.insert(INSERT, base64.b85encode(y.encode('utf-8')))
    elif var.get() == 5 and boolVar.get() == 0:#a85 encode
        t.delete('1.0', END)
        t.insert(INSERT, base64.a85encode(y.encode('utf-8')))
    elif var.get() == 1 and boolVar.get() == 1:#Base64 decode
        t.delete('1.0', END)
        t.insert(INSERT, base64.b64decode(y.encode('utf-8')))
    elif var.get() == 2 and boolVar.get() == 1:#Base32 decode
        t.delete('1.0', END)
        t.insert(INSERT, base64.b32decode(y.encode('utf-8')))
    elif var.get() == 3 and boolVar.get() == 1:#Base16 decode
        t.delete('1.0', END)
        t.insert(INSERT, base64.b16decode(y.encode('utf-8')))
    elif var.get() == 4 and boolVar.get() == 1:#b85 decode
        t.delete('1.0', END)
        t.insert(INSERT, base64.b85decode(y.encode('utf-8')))
    elif var.get() == 5 and boolVar.get() == 1:#a85 decode
        t.delete('1.0', END)
        t.insert(INSERT, base64.a85decode(y.encode('utf-8')))




P = StringVar()
strVar = StringVar()
var = IntVar()
boolVar = IntVar()
R1 = Radiobutton(top, text="Base64", variable=var, value=1)
R1.pack( anchor = W )

R2 = Radiobutton(top, text="Base32", variable=var, value=2)
R2.pack( anchor = W)

R3 = Radiobutton(top, text="Base16", variable=var, value=3)
R3.pack( anchor = W )

R4 = Radiobutton(top, text="B85", variable=var, value=4)
R4.pack( anchor = W)

R5 = Radiobutton(top, text="A85", variable=var, value=5)
R5.pack( anchor = W)

R6 = Radiobutton(top, text="Encode", variable=boolVar, value=0)
R6.pack( anchor = W)

R7 = Radiobutton(top, text="Decode", variable=boolVar, value=1)
R7.pack( anchor = W)

label = Label(top)
label.pack()


t = Text(top, height = 25, width = 100)
t.place(x = 5, y = 265)
x = Entry(top)
x.place(x = 5, y = 205)
B = Button(top, text = "Do it", command = ac)
B.place(x = 5,y = 235)
top.mainloop()
