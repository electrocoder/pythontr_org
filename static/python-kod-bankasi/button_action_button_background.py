from Tkinter import *

class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
    if self.hi_there["background"] == "green":  
      self.hi_there["background"] = "yellow"
    else:
      self.hi_there["background"] = "green"

root = Tk()

app = App(root)

root.mainloop()