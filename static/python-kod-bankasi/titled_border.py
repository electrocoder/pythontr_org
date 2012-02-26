from Tkinter import *

root = Tk()
root.title('Buttons')
f = Frame(root, width=300, height=110)
xf = Frame(f, relief=GROOVE, borderwidth=2)
Label(xf, text="AAA").pack(pady=10)
Button(xf, text="bbb", state=DISABLED).pack(side=LEFT, padx=5, pady=8)
Button(xf, text="ccc rrr rrr rrr rrr", command=root.quit).pack(side=RIGHT, padx=5, pady=8)
xf.place(relx=0.01, rely=0.125, anchor=NW)
Label(f, text='Titled Border').place(relx=.06, rely=0.125,anchor=W)
f.pack()
root.mainloop()