import sys,os
from tkinter import *

root = Tk(  )

# Insert a menu bar on the main window
menubar = Menu(root)
root.config(menu=menubar)

# Create a menu button labeled "File" that brings up a menu
filemenu = Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)


# Create entries in the "File" menu
# simulated command functions that we want to invoke from our menus

def doSave(  ):
    val=t.get('1.0',END)
    f = open("new.txt","w")
    f.write(val)
    f.close()


filemenu.add_command(label='Save', command=doSave)
t=Text(root)
t.pack()

root.mainloop(  )
