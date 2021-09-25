from tkinter import *

root = Tk()
root.title("pack方法学习")
root.geometry("300x200")
print("执行前",root.pack_slaves())#列出执行前后控件中的内容
lab1 = Label(root, text="刘备",bg='red',fg='white',
	font='华文楷体 24 bold')
lab2 = Label(root, text="张飞",bg='blue',fg='white',
	font='华文楷体 24 bold')
lab3 = Label(root, text="关羽",bg='green',fg='white',
	font='华文楷体 24 bold')


lab1.pack(side=LEFT,fill=Y)
lab2.pack(fill=X)
lab3.pack(fill=BOTH,expand=True)
print("执行后",root.pack_slaves())
root.mainloop()