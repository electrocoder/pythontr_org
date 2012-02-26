from Tkinter import *

class MyApp:
  def __init__(self, parent):
    self.myParent = parent   
    self.myContainer1 = Frame(parent)
    self.myContainer1.pack()
    
    button_name = "OK"
    self.button1 = Button(self.myContainer1,
      command=self.buttonHandler(button_name, 1, "Good stuff!"))
      
    self.button1.configure(text=button_name)  
    self.button1.pack(side=LEFT)
    self.button1.focus_force()  # Put keyboard focus on button1    
    
    button_name = "Cancel"
    self.button2 = Button(self.myContainer1, 
      command=self.buttonHandler(button_name, 2, "Bad  stuff!")) 
       
    self.button2.configure(text=button_name)
    self.button2.pack(side=LEFT)   
        
    
  def buttonHandler(self, arg1, arg2, arg3):   
         print ""  
          
   def buttonHandler_a(self, event, arg1, arg2, arg3):
         print ""    
    
root = Tk()
myapp = MyApp(root)
root.mainloop()