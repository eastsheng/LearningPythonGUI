# build the choose button with picture

from tkinter import *
def printSelection():
	label.config(text="你的选择是"+var.get())

root=Tk()
root.title()

imgStar = PhotoImage(file="../img/star.gif")
imgMoon = PhotoImage(file="../img/moon.gif")
imgSun = PhotoImage(file="../img/sun.gif")

var = StringVar()
var.set("星星")

label=Label(root,text="默认值，尚未选择",bg="lightyellow",width=30)
label.pack()

rbStar = Radiobutton(root,image=imgStar,variable=var,value="星星",
	command=printSelection).pack()
rbMoon = Radiobutton(root,image=imgMoon,variable=var,value="月亮",
	command=printSelection).pack()
rbSun = Radiobutton(root,image=imgSun,variable=var,value="太阳",
	command=printSelection).pack()

root.mainloop()