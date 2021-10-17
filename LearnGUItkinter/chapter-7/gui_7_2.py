from tkinter import *
def printSelection():
	# 输出变量值
	label.config(text="You are "+var.get()+"!")


root=Tk()
root.title("选项")

var = StringVar() #设置变量
var.set("Boy")#变量默认值

# 输出默认值
label=Label(root,text="Default Value",bg="lightyellow",width=30)
label.pack()
# 按钮1，变量，函数
rbman = Radiobutton(root,text="Boy",variable=var,value="Boy",
	command=printSelection)
rbman.pack()

rbwoman = Radiobutton(root,text="Girl",variable=var,value="Girl",
	command=printSelection)
rbwoman.pack()


root.mainloop()

