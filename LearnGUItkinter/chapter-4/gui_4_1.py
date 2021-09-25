# 4-1 功能按钮基本概念

from tkinter import *

# def msgShow():
# 	label["text"] = "I love Python!"
# 	label["bg"] = "lightyellow"
# 	label["fg"] = "blue"

def msgShow():
	label.config(text="I love Python!",bg="lightyellow",fg="blue")

counter = 0
def run_counter(digit):
	def counting():
		global counter 
		counter += 1
		digit.config(text=str(counter))
		digit.after(1000,counting)
	counting()

def yellow():
	root.config(bg="yellow")
def blue():
	root.config(bg="blue")

root = Tk()
root.title("Button")

digit = Label(root,bg="lightyellow",fg="blue",
	height=3,width=10,
	font="Helvetic 20 bold")
digit.pack()
run_counter(digit)


label = Label(root)

bluebtn = Button(root,text="Blue",command=blue)
yellowbtn = Button(root,text="Yellow",command=yellow)

btn1 = Button(root,text="打印消息",width=15,command=msgShow)
btn2 = Button(root,text="退出",width=15,command=root.destroy)
label.pack()

bluebtn.pack(side=LEFT)
yellowbtn.pack(side=LEFT)

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)


root.mainloop()
# 76page 