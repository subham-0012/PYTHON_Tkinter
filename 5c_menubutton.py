from tkinter import * 
top = Tk() 
mb= Menubutton ( top, text="Courses", relief=RAISED )
choices = Menu ( mb) 
mb.config(menu=choices)
choices.add_command(label="Python",command = top.quit)
choices.add_command(label="Java",command = top.quit)
choices.add_command(label="Haskell",command = top.quit)
mb.pack()
top.mainloop()
