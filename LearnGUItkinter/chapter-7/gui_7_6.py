# build the choose button with picture and text

from tkinter import *
def printSelection():
	label.config(text="你的选择是 "+var.get())

root=Tk()
root.title("图像和文字")

imgStar = PhotoImage(file="../img/star.gif")
imgMoon = PhotoImage(file="../img/moon.gif")
imgSun = PhotoImage(file="../img/sun.gif")

var = StringVar()
var.set("星星")

label=Label(root,text="默认值，尚未选择",bg="lightblue",width=30)
label.pack()

rbStar = Radiobutton(root,image=imgStar,text="星星",compound=RIGHT,indicatoron=0,
	variable=var,value="星星",command=printSelection).pack()
rbMoon = Radiobutton(root,image=imgMoon,text="月亮",compound=RIGHT,indicatoron=0,
	variable=var,value="月亮",command=printSelection).pack()
rbSun = Radiobutton(root,image=imgSun,text="太阳",compound=RIGHT,indicatoron=0,
	variable=var,value="太阳",command=printSelection).pack()

root.mainloop()