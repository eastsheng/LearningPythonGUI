# 第三章：窗口控件配置管理员
"""
实现在一个窗口创建多个控件
通过三个方法可以实现：
pack(side,fill,padx/pady,ipadx/ipady,anchor)
grid 
place
"""
from tkinter import *

window = Tk()
window.title("pack方法学习")


# anchor控制控件位置
# root=Tk()
# root.title("OK")
# root.geometry("300x180")
oklabel = Label(window,text="OK",
	font="Times 20 bold",
	fg="white",bg="blue")
oklabel.pack(anchor=S,side=LEFT,padx=10,pady=10)

nolabel = Label(window,text="NO",
	font="Times 20 bold",
	fg="white",bg="red")
nolabel.pack(anchor=S,side=LEFT,pady=10)


lab1 = Label(window,text="清华大学",
	bg="lightblue",
	width=15)
lab2 = Label(window,text="北京大学",
	bg="lightyellow",
	width=15)
lab3 = Label(window,text="上海交通大学",
	bg="lightgreen",
	width=15)

lab1.pack(side=BOTTOM,pady=50) #side控制标签的排列位置： TOP BOTTOM LEFT RIGHT
lab2.pack(side=BOTTOM,fill=X) #fill填充整个X轴
lab3.pack(side=BOTTOM,pady=50,ipadx=20) #pady控制y间距,ipadx控制文字与边框的距离

# 使用不同排列方式列出所有边框属性
Reliefs = ["flat", "groove", "raised", "solid", "sunken"]

for Relief in Reliefs:
	lab4 = Label(window,text=Relief,relief=Relief,
		fg="blue",
		bg="yellow",
		font="Times 20 bold")
	lab4.pack(side=LEFT,padx=10)


# 使用不同排列方式列出所有bitmaps位图
bitMaps = ["error","hourglass","info","questhead","question",
			"warning","gray12","gray25","gray50","gray75"]

for bitMap in bitMaps:
	lab5 = Label(window,bitmap=bitMap)
	lab5.pack(side=LEFT,padx=5,)


window.mainloop()
#2021-8-12学到46page 3-2-2 padx/pady参数