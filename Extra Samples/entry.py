from Tkinter import *

def fetch():
    print('Input => "%s"' % ent.get()) # get text
    ent.delete(0, END) # first, delete from start to end
    ent.insert(0, 'some text')
def fetch2():
    print('Input => "%s"' % ent.get()) # get text
    ent.insert(END, 'x')
    ent.insert(0, 'x')
root = Tk()
ent = Entry(root)
ent.insert(0, 'Type words here') # set text
ent.pack(side=TOP, fill=X) # grow horiz
ent.focus() # save a click
ent.bind('<Return>', (lambda eventname: fetch())) # on enter key
btn = Button(root, text='Fetch', command=fetch) # and on button
btn.pack(side=LEFT)
btn2 = Button(root, text='Fetch2', command=fetch2) # and on button
btn2.pack(side=LEFT)
Button(root, text='Quit', command=root.quit).pack(side=RIGHT, expand=YES,fill=X)

root.mainloop()
#destroy() just terminates the mainloop and deletes all widgets. 
