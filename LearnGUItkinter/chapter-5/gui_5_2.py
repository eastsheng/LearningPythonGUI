# 建立一个登录页面

from tkinter import *

root = Tk()
root.title("登陆页面")

msg = "欢迎进入海绵宝宝系统"

sseGif = PhotoImage(file="../img/hmbb1.gif")


logo = Label(root,image=sseGif,text=msg, compound=BOTTOM)
logo.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
accountL = Label(root,text="Account")
accountL.grid(row=1)
pwdL = Label(root,text="Password")
pwdL.grid(row=2)

accountE = Entry(root)
accountE.grid(row=1,column=1)
accountE.insert(0,"海绵宝宝") #在0位置插入默认文本框里的文字

pwdE = Entry(root,show="*")
pwdE.grid(row=2,column=1,pady=10)
pwdE.insert(0,"hmbb") #在0位置插入默认文本框里的文字

# LOGIN QUIT

def printInfo():
	print("Account: %s\nPassword: %s" %(accountE.get(), pwdE.get()))
	accountE.delete(0,END) #删除文本框内从0到最后的内容
	pwdE.delete(0,END) #删除文本框内从0到最后的内容

loginbtn = Button(root,text="Login",command=printInfo)
loginbtn.grid(row=3,column=0,sticky=W,padx=10,pady=10)

quitbtn = Button(root,text="Quit",command=root.quit)
quitbtn.grid(row=3,column=1,sticky=W,padx=10,pady=10)


root.mainloop()
#86