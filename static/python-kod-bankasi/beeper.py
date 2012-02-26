from Tkinter import *

class Alarm(Frame):
    def __init__(self):              
        Frame.__init__(self)
        self.bell()                  

if __name__ == '__main__': 
    Alarm().mainloop()
