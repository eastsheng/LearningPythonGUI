# 复选框
from tkinter import *

root=Tk()
root.title("复选框1")

lab = Label(root,text="请选择喜欢的运动",
	fg='blue',bg="lightyellow",width=30)
lab.grid(row=0)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

cbtnNFL = Checkbutton(root,text="美式足球",variable=var1)
cbtnNFL.grid(row=1,sticky=W)

cbtnNFL = Checkbutton(root,text="棒球",variable=var2)
cbtnNFL.grid(row=2,sticky=W)

cbtnNFL = Checkbutton(root,text="篮球",variable=var3)
cbtnNFL.grid(row=3,sticky=W)


root.mainloop()