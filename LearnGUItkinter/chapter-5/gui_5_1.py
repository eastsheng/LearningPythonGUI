# 第五章：文本框Entery
from tkinter import *

root = Tk()
root.title("姓名和地址")
root.geometry("240x100")

namel = Label(root,text="Name")
namel.grid(row=0)

addressl = Label(root,text="Address")
addressl.grid(row=1)

nameE = Entry(root) #文本框
addressE = Entry(root,show="*") #以*隐藏输入内容

nameE.grid(row=0,column=1)
addressE.grid(row=1,column=1)



root.mainloop()
