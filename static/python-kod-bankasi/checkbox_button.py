from Tkinter import *

class AllTkinterWidgets:
    def __init__(self, master):
        frame = Frame(master, width=500, height=400, bd=1)
        frame.pack()

        iframe1 = Frame(frame, bd=2, relief=SUNKEN)
        Button(iframe1, text='Button').pack(side=LEFT, padx=5)
        Checkbutton(iframe1, text='CheckButton').pack(side=LEFT, padx=5)

        v=IntVar()
        Radiobutton(iframe1, text='Button', variable=v,
                    value=3).pack(side=RIGHT, anchor=W)
        Radiobutton(iframe1, text='Dio', variable=v,
                    value=2).pack(side=RIGHT, anchor=W)
        Radiobutton(iframe1, text='Ra', variable=v,
                    value=1).pack(side=RIGHT, anchor=W)
        iframe1.pack(expand=1, fill=X, pady=10, padx=5)


    
root = Tk()
#root.option_add('*font', ('verdana', 10, 'bold'))
all = AllTkinterWidgets(root)
root.title('Tkinter Widgets')
root.mainloop()
