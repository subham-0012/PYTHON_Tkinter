import sys
from tkinter import *

root = Tk()

# Insert a menu bar on the main window
menubar = Menu(root)
root.config(menu=menubar)

# Create a menu button labeled "File" that brings up a menu
filemenu = Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
helpmenu = Menu(menubar)
menubar.add_cascade(label='Help', menu=helpmenu)

# Create entries in the "File" menu
# simulated command functions that we want to invoke from our menus
def doPrint(): print('doPrint')
def doSave(): print('doSave')
def dohelp(): print('dohelp')
filemenu.add_command(label='Print', command=doPrint)
filemenu.add_command(label='Save', command=doSave)
filemenu.add_separator(  )
filemenu.add_command(label='Quit', command=sys.exit)
helpmenu.add_command(label='queries', command=dohelp)
helpmenu.add_separator(  )
helpmenu.add_command(label='Save', command=doSave)
root.mainloop()
