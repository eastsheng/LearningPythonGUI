from tkinter import *

root = Tk()
root.title("标签")
# root.geometry("300x160")
root.iconbitmap("../img/cool.ico")
# label = Label(root,text="我是一个标签").pack()
stext = "我是海绵宝宝"
html_gif = PhotoImage(file="../img/hmbb1.gif")
label = Label(root, 
	# bitmap="hourglass",
	compound="top",#与文字共存时，bitmap的位置：left right top bottom center
	# height=3,width=20,
	image=html_gif, text=stext,
	relief="raised", #边框属性：flat groove raised ridge solid sunken
	bg="lightyellow",
	padx=5,pady=10,#文字与标签距离

	


				) 

label.pack()


root.mainloop()

