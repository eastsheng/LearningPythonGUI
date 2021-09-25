# 图像作为按钮
from tkinter import *

def msgShow():
	label.config(text='I love Python?',bg='lightyellow',fg="blue")

root = Tk()
root.title("图像按钮")
label = Label(root)

hmbb = PhotoImage(file="../img/hmbb1.gif")

btn = Button(root,image=hmbb,command=msgShow,
	text="海绵宝宝",compound=TOP) #LEFTER RIGHT CENTER

label.pack()
btn.pack(padx=5,pady=5)

root.mainloop()