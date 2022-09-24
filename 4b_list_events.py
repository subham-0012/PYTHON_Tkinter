from tkinter import *

#Create the parent container
root = Frame()
root.pack()

#Create a dictionary which is the data source for list box
d = {"Sam":123,"Linda":456,"Paulman":563,"Cay":789,"Horstmann":6174,"Cornell":234,"Ranjan":2788,"Sandy":234}

#Create and pack labels
widget1 = Label(root,text="Name will be displayed here..")
widget1.pack(side="top")
widget2 = Label(root,text="Phone Number will be displayed here..")
widget2.pack(side="top")

#Define event handler for list selection
def handleList(even):
    label = lst.get(ACTIVE) # on list click
    print(label)
    ph = d.get(label)
    #global widget1,widget2
    widget1.config(text=label)
    widget2.config(text=ph)
    
#Create and pack list box inside a scroll bar
lst = Listbox(root)
#lst.config(selectmode=EXTENDED)
sbar = Scrollbar(root)
sbar.config(command=lst.yview) # xlink sbar and list
lst.config(yscrollcommand=sbar.set) # move one moves other
sbar.pack(side=RIGHT, fill=Y) # pack first=clip last
lst.pack(side=LEFT, expand=YES, fill=BOTH)

#Bind event handler for list
lst.bind('<Double-1>', handleList)

#Insert items into list
for k,v in d.items():
    lst.insert('end',k)

#Start the loop and listen for events
root.mainloop()
