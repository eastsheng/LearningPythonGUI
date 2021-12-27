from tkinter import *
def mouseMotion(event):
	x = event.x
	y = event.y
	textvar = "Mouse location - x:{},y:{}".format(x,y)
	var.set(textvar)

root =Tk()
root.title("鼠标移动")
root.geometry("300x180")

x,y = 0,0
var = StringVar()
text = "Mouse location - x:{},y:{}".format(x,y)
var.set(text)


lab = Label(root,textvariable=var)
lab.pack(anchor=S,side=RIGHT,padx=10,pady=10)
root.bind("<Motion>",mouseMotion)
root.mainloop()