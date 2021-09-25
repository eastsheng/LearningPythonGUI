# 变量类型：
"""
x = IntVar() # 整型变量，默认0
x = DoubleVar() # 浮点型变量，默认0.0
x = StringVar() # 字符串变量 默认""
x = BooleanVar() # 布尔型变量 True是1，False是0
"""
# 93page 6-2
from tkinter import *

# def btn_hit():
# 	global msg_on
# 	if msg_on == False:
# 		msg_on = True
# 		x.set("You like tkinter")
# 	else:
# 		msg_on = False
# 		x.set("No")

def btn_hit():
	# global msg_on
	# if msg_on == False:
		# msg_on = True
	if x.get() == "No":
		
		x.set("You like tkinter")
	else:
		# msg_on = False
		x.set("No")

root = Tk()
root.title("Variable")

msg_on = False
x = StringVar()

label = Label(root,textvariable=x,
					fg="blue",bg="lightyellow",
					font="Verdana 16 bold",
					width=25,height=2)
label.pack()
btn = Button(root,text="Click Me",command=btn_hit)
btn.pack()
root.mainloop()
