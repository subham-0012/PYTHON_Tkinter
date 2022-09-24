from Tkinter import *
#the textoption of the label is
#set after it is constructed, by assigning to the widget’s  textkey.

widget = Label()
widget['text'] = 'Hello GUI world!'
widget.pack(side=TOP)
mainloop()



