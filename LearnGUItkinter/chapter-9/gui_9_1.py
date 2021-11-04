# Scale的数值输入控制
from tkinter import *

def printInfo():
	print("垂直尺度 = %d,水平尺度 = %d" 
		% (slider1.get(),slider2.get()))


window = Tk()
window.title("Scale")

slider1 = Scale(window,bg="lightyellow",from_=0,to=10)
slider1.set(5)#设定尺度初始值
slider1.pack()

slider2 = Scale(window,
	from_=0,to=10,#范围
	fg="red",#数字颜色
	width=30,#槽宽
	length=300,#scale长
	troughcolor="yellow",#槽颜色
	tickinterval=1,#刻度
	highlightbackground="green",
	highlightcolor="yellow",
	label="My Scale",
	orient=HORIZONTAL)

slider2.pack()
slider2.set(3)#设定尺度初始值

btn = Button(window,text="Print",command=printInfo)
btn.pack()
window.mainloop()