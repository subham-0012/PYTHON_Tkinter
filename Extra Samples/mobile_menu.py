import sys
from tkinter import *
from tkinter import messagebox

root = Tk()

# Insert a menu bar on the main window
menubar = Menu(root)
root.config(menu=menubar)

# Create a menu button labeled "File" that brings up a menu
marutimenu = Menu(menubar)
menubar.add_cascade(label='Maruti', menu=marutimenu)
fordmenu = Menu(menubar)
menubar.add_cascade(label='Ford', menu=fordmenu)

def disp(msg):
    messagebox.showinfo("Price",msg)
    

# Create entries in the "File" menu
# simulated command functions that we want to invoke from our menus
def printBaleno(): disp('The price of the car Maruti Baleno is 8.5L')
def printSwift(): disp('The price of the car Maruti Swift is 9.5L')
def printDezire(): disp('The price of the car Maruti Dezire is 7.5L')
marutimenu.add_command(label='Baleno', command=printBaleno)
marutimenu.add_command(label='Swift', command=printSwift)
marutimenu.add_command(label='Dezire', command=printDezire)
marutimenu.add_separator(  )
marutimenu.add_command(label='Quit', command=sys.exit)

def printMustang(): disp('The price of the car Ford Mustang is 65L')
def printEndeavor(): disp('The price of the car Ford Mustang is 17L')
def printAspire(): disp('The price of the car Ford Mustang is 13L')
fordmenu.add_command(label='Mustang', command=printMustang)
fordmenu.add_command(label='Endeavor', command=printEndeavor)
fordmenu.add_command(label='Aspire', command=printAspire)
fordmenu.add_separator(  )
fordmenu.add_command(label='Quit', command=sys.exit)


root.mainloop()
