from Tkinter import *
root = Tk()
val=1
for r in range(3):
    for c in range(4):
        wid=Label(root, text='%s'%(val),borderwidth=5 )
        wid.grid(row=r,column=c)
        val+=1
root.mainloop()
