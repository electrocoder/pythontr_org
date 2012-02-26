
#!/usr/bin/env python
from Tkinter import *
import math

root = Tk()     
top = Frame(root)
top.pack(side='top') 

hwframe = Frame(top)
hwframe.pack(side='top')
font = 'times 18 bold'
hwtext = Label(hwframe, text='Hello, World!', font=font)
hwtext.pack(side='top', pady=20)

rframe = Frame(top)
rframe.pack(side='top', padx=10, pady=20)

r_label = Label(rframe, text='The sine of')
r_label.pack(side='left')

r_entry = Entry(rframe, width=6)
r_entry.pack(side='left')
r_entry.insert('end', '1.2')

def comp_s(event=None):
    r = float(r_entry.get())
    s = math.sin(r)
    s_label.configure(text='%g' % s)

r_entry.bind('<Return>', comp_s)

compute = Button(rframe, text=' equals ', command=comp_s, relief='flat')
compute.pack(side='left')

s_label = Label(rframe, width=12)
s_label.pack(side='left')

def quit(event=None):
    root.destroy()
quit_button = Button(top, text='Goodbye, GUI World!', command=quit,
                     background='yellow', foreground='blue')
quit_button.pack(side='top', pady=5, fill='x')
root.bind('<q>', quit)

root.mainloop()