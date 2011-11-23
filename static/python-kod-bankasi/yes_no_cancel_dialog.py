
from Tkinter import *
from Dialog import Dialog

class OldDialogDemo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)  # same as self.pack()
        Button(self, text='Pop1', command=self.dialog1).pack()
        Button(self, text='Pop2', command=self.dialog2).pack()
    def dialog1(self):
        ans = Dialog(self,
                     title   = 'Title!',
                     text    = 'text'
                               'and text "quotation".',
                     bitmap  = 'questhead',
                     default = 0, strings = ('Yes', 'No', 'Cancel'))
        if ans.num == 0: self.dialog2()
    def dialog2(self):
        Dialog(self, title   = 'title',
                     text    = "text",
                     bitmap  = 'hourglass',
                     default = 0, strings = ('spam', 'SPAM'))

if __name__ == '__main__': OldDialogDemo().mainloop()
