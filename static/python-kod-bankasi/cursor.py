from Tkinter import *
widget = Button(text='Spam', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='gumby')

widget.config(font=('helvetica', 20, 'underline italic'))
mainloop()
