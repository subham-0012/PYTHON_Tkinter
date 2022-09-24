from Tkinter import *

fields = 'Name', 'Job', 'Pay'
def fetch(ents):
    for entry in ents:
        print('Input => "%s"' % entry.get()) # get text
def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root) # make a new row
        lab = Label(row, width=5, text=field) # add label, entry
        ent = Entry(row)
        row.pack(side=TOP,expand=YES, fill=X) # pack row on top
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X) # grow horizontal
        entries.append(ent)
    return entries
root = Tk()
ents = makeform(root, fields)
root.bind('<Return>', (lambda event: fetch(ents)))
Button(root, text='Fetch',command=lambda:fetch(ents)).pack(side=LEFT)
Button(root, text='Quit', command=root.quit).pack(side=RIGHT, expand=YES,fill=X)

root.mainloop()
