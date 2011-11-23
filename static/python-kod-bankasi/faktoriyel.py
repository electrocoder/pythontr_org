#	Project Name	:	Faktoriyel Hesapla
#	Date	        :	22-09-2010
#	Author		    :	macrocoders team
#	Contact		    :	macrocoders@gmail.com
#	Web			    :	http://visualpython.org
#	Python Ver.     :	2.6, 2.7
# -*- coding: utf-8 -*-
from Tkinter import *
from tkMessageBox import *
# -- Do not change. You may experience problems with the design file. #
form1=Tk()
form1.title('Faktoriyel')
form1.resizable(width=FALSE, height=FALSE)form1.geometry('292x273+100+100')
# -- Do not change. You may experience problems with the design file. #
# -- Do not change. You may experience problems with the design file. -- #
textBox1=Entry(font = '{MS Sans Serif} 10')
textBox1.place(relx=0.30, rely=0.08, relwidth=0.34, relheight=0.07)

# -- Do not change. You may experience problems with the design file. -- #
def button1Click():
	m=0
	m=int(textBox1.get())
	i=1
	f=1
	while i<m+1:
		f=i*f
		i=i+1
	showinfo("sayinin faktoriyeli", f)
# -- Do not change. You may experience problems with the design file. -- #
button1=Button(text='Faktoriyel Hesapla', command=button1Click)
button1.place(relx=0.17, rely=0.27, relwidth=0.60, relheight=0.33)

form1.mainloop()