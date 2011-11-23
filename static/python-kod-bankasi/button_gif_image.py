gifdir = "./"
from Tkinter import *
win = Tk()
igm = PhotoImage(file=gifdir+"logo.gif")
Button(win, image=igm).pack()
win.mainloop()
