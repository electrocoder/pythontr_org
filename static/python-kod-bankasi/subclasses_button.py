from Tkinter import *

class HelloButton(Button):
    def __init__(self, parent=None, **config):     
        Button.__init__(self, parent, config)      
        self.pack()
        self.config(command=self.callback)
    def callback(self):                            
        print 'Hi'                   
        self.quit()
 
if __name__ == '__main__':
    HelloButton(text='Hello Button').mainloop()