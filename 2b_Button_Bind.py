from tkinter import *
#Define handlers for event handling - button click
def hello(event): 
	print("Single Click, Button-l") 
def quit(event): 
	print("Double Click, so let's stop") 
	import sys; sys.exit()

#Create button
widget = Button(None, text='Mouse Clicks')
#None represents attach the button to root parent window.
#text attribute refers the text to be displayed 

widget.pack() 
widget.bind('<Button-1>', hello) #'<Button-1>' - Single click handler
widget.bind('<Double-1>', quit) #'<Double-1>' - Double click handler
widget.mainloop()
