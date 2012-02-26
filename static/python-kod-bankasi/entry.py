
#	Project Name	:	Visual Tkinter Python IDE for 2.6
#	Project Date	:	13-12-2009
#	Author		:	livetogogo
#	Contact		:	livetogogo@gmail.com
#	Web			:	http://www.blendertr.org

#!/usr/bin/env python
#-*- coding:utf-8-*-

from Tkinter import *
from tkMessageBox import *

# Do not change. You may experience problems with the design file. #
MainWindow=Tk()
MainWindow.title("Form 1")
MainWindow.resizable(width=FALSE, height=FALSE)
MainWindow.geometry("200x207+250+120")

"""TODO: Place code here."""
#Begin
e = Entry(MainWindow)
e.pack()

e.focus_set()

def callback():
    print e.get()

b = Button(MainWindow, text="get", width=10, command=callback)
b.pack()


e = Entry(MainWindow, width=50)
e.pack()

text = e.get()
#End

MainWindow.mainloop()