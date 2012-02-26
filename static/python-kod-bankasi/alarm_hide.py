# -*- coding: utf-8-*-
# Projenin Adi : alarm hide
# Tarih : 05-02-2011
# Yazar : pythontr.org ekibi
# Kontak : admin@pythontr.org
# Web : http://www.pythontr.org
# Python Versiyonu : 2.x-3.x
# Amaci : Uyari mesajı açar. Bilgisayarınızız hoparlöründen sesli uyarı verir.
#
#         Eklemek isteginiz kodlar icin irtibat kurunuz...
#         http://www.pythontr.org
from Tkinter import *

class AlarmFrame(Frame):
    def repeater(self):                          
        self.bell()                              
        self.after(self.msecs, self.repeater)    
    def __init__(self, msecs=1000):              
        Frame.__init__(self)
        self.msecs = msecs
        self.pack()
        stopper = Button(self, text='Stop the beeps!', command=self.quit)
        stopper.pack()
        stopper.config(bg='red', fg='white', bd=8) 
        self.stopper = stopper
        self.repeater()

class AlarmHide(AlarmFrame):      
    def repeater(self):      
        self.bell()          
        if self.shown:
            self.stopper.pack_forget()           
        else:                                    
            self.stopper.pack()
        self.shown = not self.shown              
        self.after(self.msecs, self.repeater)    
    def __init__(self, msecs=1000):              
        self.shown = 0
        AlarmFrame.__init__(self, msecs)
 
if __name__ == '__main__': 
     AlarmHide(msecs=500).mainloop()