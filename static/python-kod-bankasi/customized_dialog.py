
from Tkinter import *
from tkMessageBox import askyesno, showerror

class NewDialogDemo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()

    def greet(self):
        print "hi"

    def createWidgets(self):
        Label(self,  text='Label').pack(side=TOP)
        Button(self, text='Button 1', command=self.dialog1).pack()
        Button(self, text='Button 2', command=self.dialog2).pack()
        Button(self, text='Button 3',  command=self.greet  ).pack(side=LEFT)
        Button(self, text='Button 4',  command=self.quit   ).pack(side=RIGHT)

    def dialog1(self):
        ans = askyesno('Title!', 'Text')
        if ans: self.dialog2()

    def dialog2(self):
        showerror('Error title', "Text")

if __name__ == '__main__': NewDialogDemo().mainloop()