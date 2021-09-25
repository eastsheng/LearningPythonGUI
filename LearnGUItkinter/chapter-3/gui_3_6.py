# place方法

'''
place(height/width,relx/rely,x/y,
relheight/relwidth,bordermode,anchor)
'''
#x/y参数
'''
from tkinter import *

window = Tk()
window.title("palce 方法")
lab1 = Label(window,text="清华大学",bg="lightyellow",width=15)
lab2 = Label(window,text="北京大学",bg="lightgreen",width=15)
lab3 = Label(window,text="南京大学",bg="lightblue",width=15)

lab1.place(x=0,y=0)
lab2.place(x=30,y=50)
lab3.place(x=60,y=100)

window.mainloop()
'''

#width/height参数
'''
from tkinter import *

window = Tk()
window.title("palce 方法")
window.geometry("640x480")


hmbb = PhotoImage(file="../img/hmbb1.gif")
pdx = PhotoImage(file="../img/pdax1.gif")

lab1 = Label(window,image=hmbb)
lab2 = Label(window,image=pdx)

lab1.place(x=20,y=30,width=200,height=120)

lab2.place(x=200,y=200,width=400,height=240)


window.mainloop()
'''

#relx/rely与relwidth/reheight
# 相对位置与相对大小

from tkinter import *

window = Tk()
window.title("palce 方法")
window.geometry("640x480")


hmbb = PhotoImage(file="../img/hmbb1.gif")
pdx = PhotoImage(file="../img/pdax1.gif")

lab1 = Label(window,image=hmbb)
lab2 = Label(window,image=pdx)

lab1.place(relx=0.05,rely=0.1,relwidth=0.4,relheight=0.8)

lab2.place(relx=0.55,rely=0.1,relwidth=0.4,relheight=0.8)


window.mainloop()