# 事件绑定
from tkinter import *
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

def buttonClicked(event):
	lab.config(text="Button clicked")


root = Tk()
root.title("事件绑定")
root.geometry("300x180")

btn = Button(root,text="Click Me")
btn.pack(anchor=W)
btn.bind("<Button-1>",buttonClicked)

varPython = BooleanVar()
cbnPython = Checkbutton(root,text="Python")


lab=Label(root,bg="yellow",fg="blue",height=2,width=12,font="Times 16 bold")
lab.pack()


root.mainloop()