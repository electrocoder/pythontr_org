from Tkinter import *                   

class Hello(Frame):                     
    def __init__(self, parent=None):    
        Frame.__init__(self, parent)
        self.pack()
        self.make_widgets()

    def make_widgets(self):             
        widget = Button(self, text='Hello world', command=self.quit)
        widget.pack(side=LEFT)
        widget.configure(state=DISABLED, background='cadetblue')
        widget.configure(state=NORMAL, background='red')

if __name__ == '__main__':  Hello().mainloop()