# grid方法建立彩色标签
from tkinter import *

root = Tk()
root.title("彩色标签")
Colors = ["red","orange","yellow","green","blue","purple"]

# root.rowconfigure(5,weight=1)
# root.columnconfigure(0,weight=1)
r = 0

for color in Colors:
	lab1 = Label(root,text=color,relief="groove",width=20)
	lab1.grid(row=r,column=0)
	lab2 = Label(root,bg=color,relief="ridge",width=20)
	lab2.grid(row=r,column=1)
	r += 1

root.mainloop()