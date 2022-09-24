from Tkinter import *
import tkMessageBox
import sys
def fetch():
    n1=ent.get() # get text
    n2=ent2.get()
    sum=int(n1)+int(n2)
    ent.delete(0, END) # first, delete from start to end
    ent.insert(0, 'enter no1')
    ent2.delete(0, END) # first, delete from start to end
    ent2.insert(0, 'enter no2')
    widget.config(text='sum is '+str(sum))                                 
def endproc():
    tkMessageBox.showinfo("last window","Good bye!!!")
    sys.exit()
root = Tk()
ent = Entry(root)
ent.insert(0, 'enter no 1') # set text
ent.pack(side=TOP, fill=X) # grow horiz
ent.focus() # save a click
ent.bind('<Return>', (lambda eventname: fetch())) # on enter key


ent2 = Entry(root)
ent2.insert(0, 'enter no 2') # set text
ent2.pack(side=TOP, fill=X) # grow horiz
ent2.bind('<Return>', (lambda eventname: fetch())) # on enter key

widget = Label(root)
widget.config(text='')
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.title('addition')

btn = Button(root, text='Fetch', command=fetch) # and on button
btn.pack(side=LEFT)

Button(root, text='Quit', command=endproc).pack(side=RIGHT, expand=YES)

root.mainloop()
#destroy() just terminates the mainloop and deletes all widgets. 
