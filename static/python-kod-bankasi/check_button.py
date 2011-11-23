from Tkinter import *

class Dummy: pass
var = Dummy()

root = Tk()
root.title('Checkbutton')
for castmember, row, col, status in [
    ('A', 0,0,NORMAL), ('B', 0,1,NORMAL),
    ('C', 1,0,DISABLED), ('D', 1,1,NORMAL),
    ('E',2,0,NORMAL), ('F', 2,1,NORMAL)]:
    setattr(var, castmember, IntVar())
    Checkbutton(root, text=castmember, state=status, anchor=W,
      variable = getattr(var, castmember)).grid(row=row, column=col, sticky=W)
root.mainloop()



           