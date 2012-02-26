# -*- coding: utf-8-*-
# Projenin Adi : alarm clock-windows
# Tarih : 05-02-2011
# Yazar : pythontr.org ekibi
# Kontak : admin@pythontr.org
# Web : http://www.pythontr.org
# Python Versiyonu : 2.x-3.x
# Amaci : Bilgisayarınızda ayarladıgınız zaman diliminde uyarı mesajı görüntüler.
#            Çalar saat programı olarak kullanılır.
#
#         Eklemek isteginiz kodlar icin irtibat kurunuz...
#         http://www.pythontr.org


from Tkinter import *
from tkMessageBox import *
import time

MainWindow=Tk()
MainWindow.title("Alarm Clock")
MainWindow.resizable(width=FALSE, height=FALSE)
MainWindow.geometry("500x220+250+120")

clock_q = ''
Day=time.strftime("%d")
Moon=time.strftime("%m")
Year=time.strftime("%Y")

Label1=Label(text="    Day  Moon   Year          Hour    Minute")
Label1.place(relx=0.19035, rely=0.0765, relwidth=0.73, relheight=0.175)

Label2=Label(text="Please Enter Reminder...")
Label2.place(relx=0.0, rely=0.2065, relwidth=0.4, relheight=0.175)

Entry3=Entry(width=2)
Entry3.place(relx=0.405, rely=0.2065, relwidth=0.05, relheight=0.125)

Entry4=Entry()
Entry4.place(relx=0.455, rely=0.2065, relwidth=0.05, relheight=0.125)

Entry5=Entry()
Entry5.place(relx=0.5, rely=0.2065, relwidth=0.06, relheight=0.125)

Entry6=Entry()
Entry6.place(relx=0.6005, rely=0.2065, relwidth=0.05, relheight=0.125)

Entry7=Entry()
Entry7.place(relx=0.6705, rely=0.2065, relwidth=0.05, relheight=0.125)

Entry1=Entry()
#Entry1.place(relx=0.435, rely=0.5065, relwidth=0.53, relheight=0.175)

Label3=Label(text="Please Enter your note Reminder")
Label3.place(relx=0, rely=0.4465, relwidth=0.4, relheight=0.175)

Entry2=Entry()
Entry2.place(relx=0.405, rely=0.4465, relwidth=0.53, relheight=0.125)

Entry3.insert(0,Day)
Entry4.insert(0,Moon)
Entry5.insert(0,Year)

def mytime():
    global clock_q
    timenew = time.strftime("%d.%m.%Y %H:%M")
    if timenew != clock_q:
        clock_q = timenew
        Entry1.delete(0,END)
        Entry1.insert(END,clock_q)
        al=Entry1.get()
        al2=Entry2.get()
        al3=Entry3.get()
        al4=Entry4.get()
        al5=Entry5.get()
        al6=Entry6.get()
        al7=Entry7.get()
        al8=(al3+"."+al4+"."+al5+" "+al6+":"+al7)
        if al==al8:
            showinfo("Warning...",al2)
            MainWindow.quit()
    Entry1.after(200, mytime)
    MainWindow.geometry("500x207+2220+120")
    
buton1=Button(text="OK",command=mytime)
buton1.place(relx=0.395, rely=0.6565, relwidth=0.23, relheight=0.155)
    
Label4=Label(text="http://pythontr.org")
Label4.place(relx=0.22, rely=0.825, relwidth=0.57, relheight=0.145)
Entry6.focus_set()
MainWindow.mainloop()
