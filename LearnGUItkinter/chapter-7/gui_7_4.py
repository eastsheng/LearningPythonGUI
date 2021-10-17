# 盒子按钮indicatoron
from tkinter import *

def printSelection():
	print(cities[var.get()])
	label.config(text="Your favourite city is "+cities[var.get()]+"!")

root=Tk()
root.title("盒子按钮")

cities = {
	0:"北京",1:"南京",2:"西安",3:"东京",4:"郑州"
}

var = IntVar()
var.set(0)

label=Label(root,text="Chose you favourite city ! ",
	fg="blue",bg="lightyellow",width=30)
label.pack()
for val, city in cities.items():
	Radiobutton(root,text=city,
		width=30,
		indicatoron=0,
		variable = var,
		value=val,
		command=printSelection).pack()


root.mainloop()