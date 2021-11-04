from tkinter import *

root=Tk()
root.title("raised 复选框")

fm  = Frame(width=150,height=80,relief=RAISED,borderwidth=5)

lab = Label(fm,text="请复选常用的程序语言").pack()

python = Checkbutton(fm,text="Python").pack(anchor=W)
java = Checkbutton(fm,text="Java").pack(anchor=E)
ruby = Checkbutton(fm,text="Ruby").pack(anchor=W)
fm.pack(padx=10,pady=10)

root.mainloop()