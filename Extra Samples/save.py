from Tkinter import *

fil=sys.argv[1]
def fetch():
    fn=ent.get()
    ptr=open(fn,'w')
    for line in fil:
        ptr.write(val+'\n')
    ptr.close()
    

root = Tk()
ent = Entry(root)
ent.insert(0, 'Type words here') # set text
ent.pack(side=TOP, fill=X) # grow horiz
ent.focus() # save a click
ent.bind('<Return>', (lambda eventname: fetch())) # on enter key
btn = Button(root, text='save', command=fetch) # and on button
btn.pack(side=LEFT)

root.mainloop()
