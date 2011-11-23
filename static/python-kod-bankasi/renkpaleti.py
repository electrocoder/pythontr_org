#! /usr/bin/env python
# -*- coding: utf-8-*-
# Projenin Adi : renkpaleti
# Tarih : 10-11-2011
# Yazar : pythontr.org ekibi
# Kontak : admin@pythontr.org
# Web : http://www.pythontr.org
# Python Versiyonu : 2.x-3.x
# Amaci : Web programlamada renklerin tanımlanması
#
#         Eklemek isteginiz kodlar icin irtibat kurunuz...
#         http://www.pythontr.org

from Tkinter import *
import webbrowser

form1 = Tk()
form1.title("renk paleti v1.0")

def setcolor(v):
    rr=((str(hex(r.get()))).split("x")[1])
    if len(rr)==1:
        rr="0"+rr
    gg=((str(hex(g.get()))).split("x")[1])
    if len(gg)==1:
        gg="0"+gg
    bb=((str(hex(b.get()))).split("x")[1])
    if len(bb)==1:
        bb="0"+bb
    button1.config(bg="#"+rr+gg+bb)
    label1.config(text="#"+rr+gg+bb)

r = Scale(from_=0, to=255, bg='red', command=setcolor)
r.grid(row=1, column=1)

g = Scale(from_=0, to=255, bg='green', command=setcolor)
g.grid(row=1, column=2)

b = Scale(from_=0, to=255, bg='blue', command=setcolor)
b.grid(row=1, column=3)

def button1def():
    webbrowser.open_new_tab("http://pythontr.org")
    
button1=Button(text="www.pythontr.org", command=button1def)
button1.grid(row=2, column=2)

label1=Label(text="#")
label1.grid(row=3, column=2)

mainloop()
