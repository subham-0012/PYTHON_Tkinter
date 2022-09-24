from Tkinter import *
def greeting():
    print('Hello stdout world!...')
win = Frame()
win.pack()
Button(win, text='Hello', command=greeting).pack(side=LEFT,fill=Y)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT, expand=YES, fill=X)
win.mainloop()
