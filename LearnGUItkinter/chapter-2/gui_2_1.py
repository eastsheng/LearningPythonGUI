from tkinter import *

root = Tk()
root.title("标签")
# root.geometry("300x160")
root.iconbitmap("../img/cool.ico")
# label = Label(root,text="我是一个标签").pack()
label = Label(root, text="我是一个标签啊啊啊啊啊",
				fg="yellow",bg="blue",
				height=10,width=20,
				# anchor="se", #标签位置（n, s, w, e, nw, ne, sw, se），大写时不用双引号，
				wraplength = 60, #达到40px自动换行
				# font="华文行楷 20 bold", #字体 大小 加粗
				font=("华文行楷", 20, "bold"), #也可使用元组方式：字体 大小 加粗
				justify="center", #最后一行位置:center right left

				) 

label.pack()

print(type(label))


root.mainloop()

