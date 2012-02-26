from Tkinter import *

class AllTkinterWidgets:
    def __init__(self, master):
        frame = Frame(master, width=500, height=400, bd=1)
        frame.pack()

        iframe1 = Frame(frame, bd=2, relief=SUNKEN)
        Button(iframe1, text='Button').pack(side=LEFT, padx=5)
        Checkbutton(iframe1, text='CheckButton').pack(side=LEFT, padx=5)

        v=IntVar()
        Radiobutton(iframe1, text='Button 1', variable=v,
                    value=3).pack(side=RIGHT, anchor=W)
        Radiobutton(iframe1, text='Button 2', variable=v,
                    value=2).pack(side=RIGHT, anchor=W)
        Radiobutton(iframe1, text='Button 3', variable=v,
                    value=1).pack(side=RIGHT, anchor=W)
        iframe1.pack(expand=1, fill=X, pady=10, padx=5)


    
root = Tk()
all = AllTkinterWidgets(root)
root.title('Tkinter Widgets')
root.mainloop()