
from Tkinter import *

class MyApp:
  def __init__(self, parent):
    self.myLastButtonInvoked = None    
    self.myParent = parent   
    self.myContainer1 = Frame(parent)
    self.myContainer1.pack()
    
    self.yellowButton = Button(self.myContainer1, command=self.yellowButtonClick)   
    self.yellowButton.configure(text="YELLOW")     
    self.yellowButton.pack(side=LEFT)

    self.redButton = Button(self.myContainer1, command=self.redButtonClick)  
    self.redButton.configure(text="RED")
    self.redButton.pack(side=LEFT)  
    
    self.whiteButton = Button(self.myContainer1, command=self.whiteButtonClick)   
    self.whiteButton.configure(text="WHITE")     
    self.whiteButton.pack(side=LEFT)
    
  def redButtonClick(self):   
    print "RED button clicked.  Previous button invoked was", self.myLastButtonInvoked  ### 2
    self.myLastButtonInvoked = "RED" 
    
  def yellowButtonClick(self):  
    print "YELLOW button clicked.  Previous button invoked was", self.myLastButtonInvoked ### 2
    self.myLastButtonInvoked = "YELLOW" 
        
  def whiteButtonClick(self):  
    print "WHITE  button clicked.  Previous button invoked was", self.myLastButtonInvoked ### 2
    self.myLastButtonInvoked = "WHITE" 
       
    
root = Tk()
myapp = MyApp(root)
root.mainloop()
