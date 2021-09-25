from tkinter import *

def callbackW(*args):
	xL.set(xE.get())

def callbackR(*args):
	print("warning:读取已数据！")

def hit():
	print("读取数据:",xE.get())

root = Tk()
root.title("追踪r")

xE =StringVar()
entry = Entry(root,textvariable=xE)
entry.pack(pady=10,padx=10)
xE.trace("w",callbackW)
xE.trace("r",callbackR)

xL = StringVar()
label = Label(root,textvariable=xL)
xL.set("同步显示")
label.pack(pady=5,padx=10)

btn = Button(root,text="读取",command=hit)
btn.pack(pady=5)

root.mainloop()
 