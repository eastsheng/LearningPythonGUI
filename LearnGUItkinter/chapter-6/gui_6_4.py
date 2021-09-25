from tkinter import *

def callbackW(name,index,mode):
	xL.set(xE.get())
	print("name = %r,index = %r,mode = %r" % (name,index,mode))


root = Tk()
root.title("调用")
xE = StringVar()

entry = Entry(root,textvariable=xE)
entry.pack(padx=20,pady=10)
xE.trace("w",callbackW)

xL = StringVar()
label = Label(root,textvariable=xL)
label.pack(padx=20,pady=10)
xL.set("同步显示")

root.mainloop()