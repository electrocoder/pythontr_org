from Tkinter import *

root = Tk()
 
myContainer1 = Frame(root)
myContainer1.pack()

button1 = Button(myContainer1)      
button1["text"]= "Hello, World!"    
button1["background"] = "green"     
button1.pack()                      

root.mainloop()