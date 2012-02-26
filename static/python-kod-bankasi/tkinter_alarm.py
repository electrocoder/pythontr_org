from Tkinter import *

class Alarm(Frame):
    def repeater(self):                          
        self.bell()                              
        self.after(self.msecs, self.repeater)    
    def __init__(self):              
        Frame.__init__(self)
        self.msecs = 1000
        self.pack()
        stopper = Button(self, text='Stop the beeps!', command=self.quit)
        stopper.pack()
        stopper.config(bg='navy', fg='white', bd=8) 
        self.stopper = stopper
        self.repeater()

if __name__ == '__main__': 
   Alarm().mainloop()