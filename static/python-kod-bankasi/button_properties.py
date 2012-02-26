from Tkinter import *

class MyApp:
  def __init__(self, parent):
    self.myContainer1 = Frame(parent)
    self.myContainer1.pack()
    
    self.button1 = Button(self.myContainer1)
    self.button1["text"] = "aaa"   
    self.button1["background"] = "green"      
    self.button1.pack()  

    self.button2 = Button(self.myContainer1)
    self.button2.configure(text="bbb") 
    self.button2.configure(background="tan")               
    self.button2.pack()  
    

    self.button3 = Button(self.myContainer1)
    self.button3.configure(text="ccc", background="cyan")  
    self.button3.pack()  
      
    self.button4 = Button(self.myContainer1, text="ddd", background="red")
    self.button4.pack()  
  
    
root = Tk()
myapp = MyApp(root)
root.mainloop()