'''
grid方法：grid(row,column,padx/pady,rowspan,columnspan, sticky)
'''

from tkinter import *

window = Tk()
window.title("Grid方法")
lab1 = Label(window,text="西游记",relief="raised",
	# bg="lightblue",
	width=15)
lab2 = Label(window,text="水浒传",relief="raised",
	bg="lightgreen",
	width=15)
lab3 = Label(window,text="红楼梦",relief="raised",
	bg="lightyellow",
	width=15)
lab4 = Label(window,text="三国志",relief="raised",
	bg="lightblue",
	width=15)


lab1.grid(row=0,column=0,padx=5,pady=5,sticky=N+S+W+E)
lab2.grid(row=0,column=1)
# lab3.grid(row=1,column=0,columnspan=2) #columnspan和第0列对应
lab3.grid(row=1,column=0)
lab4.grid(row=1,column=1)

window.mainloop()
#62page 3-3-5
