# 第七章：选项按钮与复选框
# p96

from tkinter import *
def printSelection():
	num = var.get()
	if num == 1:
		label.config(text="你是男生")
	else:
		label.config(text="你是女生")
	return
root = Tk()
root.title("选项按钮")

var = IntVar()
var.set(1)

label = Label(root,text="这是预设，尚未选择",
	bg="lightyellow",width=30)
label.pack()

rbman = Radiobutton(root,text="男生",variable=var,
	value=1,command=printSelection)
rbman.pack()

rbwoman = Radiobutton(root,text="女生",variable=var,
	value=2,command=printSelection)
rbwoman.pack()

root.mainloop()
