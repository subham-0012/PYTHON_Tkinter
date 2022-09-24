from tkinter import *
from tkinter import messagebox
top = Tk() 
L1 = Label(top, text="User Name") 
L1.pack( side = LEFT)

E1 = Entry(top, bd =5) 
E1.pack(side = LEFT)
def disp():
    messagebox.showinfo("Message to you",E1.get())
B1 = Button(top, text="display", command=disp)
B1.pack(side = RIGHT)
top.mainloop()
