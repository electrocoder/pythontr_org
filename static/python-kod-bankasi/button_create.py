from Tkinter import *

root = Tk()
root.title("Demonstrates creating buttons")
root.geometry("200x85")

app = Frame(root)
app.grid()

bttn1 = Button(app, text = "OK!")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Cancel")

bttn3 = Button(app)
bttn3.grid()
bttn3["text"]= "Apply"

root.mainloop()