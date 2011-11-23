from Tkinter import *

class MyApp:
  def __init__(self, parent):
    self.myParent = parent   
    self.myContainer1 = Frame(parent)
    self.myContainer1.pack()
    
    button_name = "OK"
    
    # command binding
    self.button1 = Button(self.myContainer1,
      command = lambda 
      arg1=button_name, arg2=1, arg3="Good stuff!" :
      self.buttonHandler(arg1, arg2, arg3)
      )
    
    # event binding -- passing the event as an argument
    self.button1.bind("<Return>", 
      lambda 
      event, arg1=button_name, arg2=1, arg3="Good stuff!" : 
      self.buttonHandler_a(event, arg1, arg2, arg3)
      )
         
    self.button1.configure(text=button_name, background="green")  
    self.button1.pack(side=LEFT)
    self.button1.focus_force()  # Put keyboard focus on button1    
    
    button_name = "Cancel"
    
    self.button2 = Button(self.myContainer1,
      command = lambda 
      arg1=button_name, arg2=2, arg3="Bad  stuff!": 
      self.buttonHandler(arg1, arg2, arg3)
      )

    self.button2.bind("<Return>", 
      lambda 
      event, arg1=button_name, arg2=2, arg3="Bad  stuff!" : 
      self.buttonHandler(arg1, arg2, arg3)
      )
  
    self.button2.configure(text=button_name, background="red")
    self.button2.pack(side=LEFT)   
    
    
    
   def buttonHandler_a(self, event, argument1, argument2, argument3):
    print "buttonHandler_a received event", event
    self.buttonHandler(argument1, argument2, argument3)
    
root = Tk()
myapp = MyApp(root)
root.mainloop()