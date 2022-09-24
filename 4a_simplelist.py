from tkinter import *
top = Tk()

#Create a list box in root window
Lb1 = Listbox(top)

# Insert elements into list
Lb1.insert(1, "Python")  
Lb1.insert(2, "Perl") 
Lb1.insert(3, "C") 
Lb1.insert(4, "PHP") 
Lb1.insert(5, "JSP") 
Lb1.insert(6, "Ruby")

#Pack and listen
Lb1.pack(side=TOP)
top.mainloop()
