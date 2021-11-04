from tkinter import *
from tkinter import messagebox

def myMsg1():
	ret = messagebox.askretrycancel("Test1","安装失败，再试一次？")
	print("安装失败",ret)

def myMsg2():
	ret = messagebox.askyesnocancel("Test2","编辑完成，是否取消？")
	print("编辑完成",ret)

def myMsg3():
	ret = messagebox.showwarning("Test3","小心病毒感染！")
	print("小心病毒",ret)
def myMsg4():
	ret = messagebox.showerror("Test4","磁盘存取错误！")
	print("磁盘存取错误",ret)

def myMsg5():
	ret = messagebox.askquestion("Test5","确定离开？")
	print("确定离开",ret)
def myMsg6():
	ret = messagebox.askokcancel("Test5","确定 or 取消？")
	print("确定取消",ret)

def myMsg7():
	ret = messagebox.askyesno("Test5","是 or 否？")
	print("是 or 否",ret)


root=Tk()
root.title("Message box")
root.geometry("360x360")

btn1 = Button(root,text="安装失败",command=myMsg1)
btn1.pack()

btn2 = Button(root,text="编辑完成",command=myMsg2)
btn2.pack()

btn3 = Button(root,text="小心病毒",command=myMsg3)
btn3.pack()
btn4 = Button(root,text="磁盘错误",command=myMsg4)
btn4.pack()

btn5 = Button(root,text="确定离开",command=myMsg5)
btn5.pack()

btn6 = Button(root,text="确定or取消",command=myMsg6)
btn6.pack()
btn7 = Button(root,text="是or否",command=myMsg7)
btn7.pack()


root.mainloop()