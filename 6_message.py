from tkinter import * 
root = Tk() 
var = StringVar() 
msg = Message( root, textvariable=var, relief=RAISED )
var.set("Hey!? How are you doing?")
msg.config(bg='pink',font=('time',16,'italic'))
msg.pack(fill=Y,expand=1) 
root.mainloop()
