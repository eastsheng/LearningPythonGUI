# Lambda表达式
from tkinter import *

def bColor(bgColor):
	root.config(bg=bgColor)

root = Tk()
root.title("Lambda")
root.geometry("300x200")

# build 3 btn

exitbtn = Button(root,text="Exit",command=root.destroy)
bluebtn = Button(root,text="Blue",command=lambda:bColor("blue"))
yellowbtn = Button(root,text="yellow",command=lambda:bColor("yellow"))

exitbtn.pack(side=RIGHT,anchor=S,padx=5,pady=5)
bluebtn.pack(side=RIGHT,anchor=S,padx=5,pady=5)
yellowbtn.pack(side=RIGHT,anchor=S,padx=5,pady=5)

root.mainloop()