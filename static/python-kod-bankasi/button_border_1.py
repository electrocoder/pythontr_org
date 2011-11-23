

from Tkinter import *

class Alarm(Frame):
    def __init__(self):              
        Frame.__init__(self)
        self.pack()
        stopper = Button(self, text='Stop the beeps!', command=self.quit)
        stopper.pack()
        stopper.config(bg='navy', fg='white', bd=8) 

if __name__ == '__main__': Alarm().mainloop()

           
       