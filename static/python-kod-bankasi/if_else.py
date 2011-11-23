#	Project Name	:	Visual Python IDE for 2.6
#	Date	        :	13-12-2009
#	Author		    :	macrocoders team
#	Contact		    :	macrocoders@gmail.com
#	Web			    :	http://visualpython.org
#	Python Ver.     :	2.6
# -*- coding: utf-8 -*-
from Tkinter import *
from tkMessageBox import *
# -- Do not change. You may experience problems with the design file.#
form1=Tk()form1.title('form1')
form1.resizable(width=FALSE, height=FALSE)form1.geometry('292x273+100+100')
# -- Do not change. You may experience problems with the design file. #
# -- Do not change. You may experience problems with the design file. -- #
textBox1=Entry(font = '{MS Sans Serif} 10')
textBox1.place(relx=0.58, rely=0.14, relwidth=0.36, relheight=0.07)

# -- Do not change. You may experience problems with the design file. -- #
label1=Label(text='Please enter an integer:')
label1.place(relx=0.05, rely=0.13, relwidth=0.49, relheight=0.08)

# -- Do not change. You may experience problems with the design file. -- #
def button1Click():
	x = int(textBox1.get())
	if x < 0:
		x = 0
		showinfo("","Negative changed to zero")
	elif x == 0:
		showinfo("","Zero")
	elif x == 1:
		showinfo("","Single")
	else:
		showinfo("","More")

# -- Do not change. You may experience problems with the design file. -- #
button1=Button(text='button1', command=button1Click)
button1.place(relx=0.21, rely=0.49, relwidth=0.56, relheight=0.34)

form1.mainloop() 