from tkinter import *

root=Tk()
root.title("LabelFrame")

msg = "欢迎进入tkinter系统"
sseGif = PhotoImage(file="../img/hmbb1.gif")

logo = Label(root,image=sseGif,text=msg,compound=BOTTOM)
logo.pack()

labFrame = LabelFrame(root,text="账号密码")
accountL = Label(labFrame,text="Account")
accountL.grid(row=0,column=0)

pwdL = Label(labFrame,text="Password")
pwdL.grid(row=1,column=0)
accountE = Entry(labFrame).grid(row=0,column=1)
pwdE = Entry(labFrame,show="*").grid(row=1,column=1,pady=10)

labFrame.pack(padx=10,pady=5,ipadx=5,ipady=5)
root.mainloop()