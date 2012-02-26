from Tkinter import *
from tkMessageBox import *
from tkFileDialog   import askopenfilename      

def callback():
    showerror('Error!', "Error")
    
    
errmsg = 'Error!'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)
mainloop()


          