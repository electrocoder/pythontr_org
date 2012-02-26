from Tkinter import * 

def onCanvasClick(event):                  
    print 'Got canvas click', event.x, event.y, event.widget

root = Tk()
canv = Canvas(root, width=100, height=100)
obj1 = canv.create_text(50, 30, text='one')
obj2 = canv.create_text(50, 70, text='two')

canv.bind('<Double-1>', onCanvasClick)                  
canv.pack()
root.mainloop()
