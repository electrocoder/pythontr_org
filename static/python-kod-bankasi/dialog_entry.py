

from Tkinter import *
from tkMessageBox import *
from tkColorChooser import askcolor              
from tkMessageBox   import askquestion, showerror
from tkSimpleDialog import askfloat
from tkFileDialog   import askopenfilename      

def callback():
    askfloat('Entry', 'Input field')
    
    
errmsg = 'Error!'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)
mainloop()
