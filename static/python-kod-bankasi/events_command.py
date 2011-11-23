
from Tkinter import *

class MyApp:
  def __init__(self, parent):
    self.myParent = parent   
    self.myContainer1 = Frame(parent)
    self.myContainer1.pack()
    
    self.button1 = Button(self.myContainer1, command=self.button1Click)  
    self.button1.bind("<Return>", self.button1Click_a)    
    self.button1.configure(text="OK")
    self.button1.pack(side=LEFT)
    self.button1.focus_force()       
    
    self.button2 = Button(self.myContainer1, command=self.button2Click)   
    self.button2.bind("<Return>", self.button2Click_a)    
    self.button2.configure(text="Cancel")     
    self.button2.pack(side=RIGHT)
    
  def button1Click(self):  
    print "button1Click event handler" 
    if self.button1["background"] == "green":  
      self.button1["background"] = "yellow"
    else:
      self.button1["background"] = "green"
  
  def button2Click(self): 
    print "button2Click event handler" 
    self.myParent.destroy()      
  
  def button1Click_a(self, event):  
    print "button 1 Click event" 
    self.button1Click()
        
  def button2Click_a(self, event):  
    print "button 2 Click event" 
    self.button2Click()
        
              
root = Tk()
myapp = MyApp(root)
root.mainloop()
