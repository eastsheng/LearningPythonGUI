from tkinter import *

def buttonClicked():
	lab.config(text="Button clicked")

def pythonClicked():
	if varPython.get():
		lab.config(text="Select Python")
	else:
		lab.config(text="Unselect Python")

def javaClicked():
	if varJava.get():
		lab.config(text="Select Java")
	else:
		lab.config(text="Unselect Java")


# 
root = Tk()
root.title("复习")
root.geometry("300x300")

btn = Button(root,text="Click Me",command=buttonClicked)
btn.pack(anchor=S)

varPython = BooleanVar()
cbnPython = Checkbutton(root,text="Python",varialbe=varPython,
	command=pythonClicked)


lab = Label(root,bg="lightyellow",fg="blue",height=2,width=12)
lab.pack()

root.mainloop()


