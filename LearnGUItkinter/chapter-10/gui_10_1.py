from tkinter import *

root=Tk()
root.title("Message")
root.geometry("360x360")

var = StringVar()

mytext = "3031年10月，我在宿舍学tkinter,因为实验室停电了！"

msg = Message(root,textvariable=var,
	font="times 12 italic",
	bg="lightyellow",
	fg="red",
	aspect=600,    #控件宽高比
	justify=LEFT, #对齐方式
	relief=RAISED,
	)
var.set(mytext)
msg.config(bg="yellow")
msg.pack(padx=10,pady=10)

root.mainloop()