from Tkinter import *
from tkMessageBox import *
from tkFileDialog   import askopenfilename      

def callback():
    askquestion('Warning', 'Line "quotation"\n Line 2 ?')
    
    
errmsg = 'Error!'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)
mainloop()

