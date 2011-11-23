from Tkinter import *
import tkMessageBox
       
def a():       
    filename = "a.txt"
    try:
        fp = open(filename)
    except:
        tkMessageBox.showwarning(
            "Open file",
            "Cannot open this file\n(%s)" % filename
        )
        return
a()
