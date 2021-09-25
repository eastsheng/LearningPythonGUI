from tkinter import *
from tkinter.ttk import Separator

counter = 0
def run_counter(digit):
	def counting():
		global counter
		counter += 1
		digit.config(text=str(counter))#config()方法可以添加或更改属性，这里添加了文本
		digit.after(1000,counting) #1000代表每隔一秒调用counting
	counting() #持续调用


root = Tk()
root.title("计数")

html_gif = PhotoImage(file="../img/hmbb1.gif")
digit = Label(root,bg="yellow",fg="blue",
	compound="bottom",
	image=html_gif,
	# height=3,width=10,
	font="华文楷体 20 bold",
	padx=5,pady=10,
	cursor="heart",#光标形状:heart arrow boat icon clock dot...
	)

digit.pack()
run_counter(digit)

print(digit.keys())#输出Label所有参数

myTitle = "大家好，我是海绵宝宝"
myContent = "我住在比基尼海滩，我有一个呆呆的朋友叫派大星，我的老板是蟹老板......"

lab1 = Label(root, text=myTitle,
	font="华文楷体 20 bold")
lab1.pack(padx=10,pady=10)

sep = Separator(root,orient=HORIZONTAL)
sep.pack(fill=X,padx=10)#填满X轴

lab2 = Label(root, text=myContent,
	font="华文楷体 10 bold")
lab2.pack(padx=10,pady=10)


root.mainloop()
