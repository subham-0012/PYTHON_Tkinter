from tkinter import *
from tkinter import messagebox #Always import messagebox seperately as it a sub module
top = Tk()

L1 = Label(top, text="ST_Name") 
L1.grid(row = 1, column = 1)
E1 = Entry(top, bd =5) #Attach text box to root frame. bd refers size of the border. default is 2 pixels
E1.grid(row = 1, column = 2)

L2 = Label(top, text="Mark 1") 
L2.grid(row = 2, column = 1) 
E2 = Entry(top, bd =5) 
E2.grid(row = 2, column = 2)

L3 = Label(top, text="Mark 2") 
L3.grid(row = 3, column = 1) 
E3 = Entry(top, bd =5) 
E3.grid(row = 3, column = 2)

L4 = Label(top, text="Mark 3") 
L4.grid(row = 4, column = 1)
E4 = Entry(top, bd =5) 
E4.grid(row = 4, column = 2)


def disp():
    m1 = int(E2.get())
    m2 = int(E3.get())
    m3 = int(E4.get())
    avg = (m1+m2+m3)/3
    if avg > 90:
        grd = "A"
    elif avg >=80 and avg <= 89:
        grd = "C"
    elif avg >=70 and avg <= 79:
        grd = "C"
    elif avg >=60 and avg <= 69:
        grd = "D"
    elif avg >=50 and avg <= 59:
        grd = "E"
    else:
        grd = "Fail"
    messagebox.showinfo("Your grade is",grd)
    
B1 = Button(top, text="display", command=disp)
B1.grid(row = 5, column = 2)

top.mainloop()
