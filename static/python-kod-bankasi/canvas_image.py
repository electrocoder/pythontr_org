gifdir = "./"
from sys import argv
from Tkinter import *
filename = 'logo.gif'    
win = Tk()
img = PhotoImage(file=gifdir+filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())        
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()

