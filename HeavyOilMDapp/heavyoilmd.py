# 一个处理分子动力学模拟稠油数据的可视化程序软件

from tkinter import *

def printInfo():
	print("red")
	return


root=Tk()
root.title("HeavyOil MD")

'''------------menu region------------'''
menu = Frame(width=800,height=30,relief=GROOVE,bg="lightyellow")

# button_open = Button(menu,text="Red",fg="red",command=printInfo)
# button_open.pack()

menu.grid(row=0,column=0,columnspan=2,padx=5,pady=5)
'''------------menu region end------------'''




'''------------side region------------'''
side = Frame(root,width=100,height=500,relief=RAISED,bg="lightblue")
side.grid(row=1,column=0,padx=5,pady=5)
'''------------side region end------------'''



'''------------view region------------'''
view = Frame(root,width=700,height=470,relief=RAISED,bg="lightgray")
view.grid(row=1,column=1)

'''------------view region end------------'''

root.mainloop()