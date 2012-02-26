from Tkinter import *

class HelloButton(Button):
    def __init__(self, parent=None, side=TOP, **config): 
        Button.__init__(self, parent, config)            
        self.pack(side=side)                             
        self.config(command=self.callback)
    def callback(self):
        print 'callback...'                   
        self.quit()
 
if __name__ == '__main__':
    HelloButton(side=LEFT, text='Hello Button').mainloop()

