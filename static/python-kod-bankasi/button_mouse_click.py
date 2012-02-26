
from Tkinter import *

def hello(event):
    print 'Double Click to exit'

def quit(event):       
    print 'You double clicked...'        
    import sys; sys.exit() 

widget = Button(None, text='Hello event world')
widget.pack()
widget.bind('<Button-1>', hello)             # bind left mouse clicks
widget.bind('<Double-1>', quit)              # bind double left clicks
widget.mainloop()

           