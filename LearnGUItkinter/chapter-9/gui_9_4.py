from tkinter import *
from tkinter.colorchooser import *

def bgUpdate(source):#这里source可以替换为任意字符
	"""窗口颜色"""
	r = rSlider.get()
	g = gSlider.get()
	b = bSlider.get()
	print("R=%d,G=%d,B=%d" % (r,g,b))
	myColor = "#%02x%02x%02x" %(r,g,b)
	root.config(bg=myColor)

def bgChoose():
	"""窗口颜色"""
	myColor = askcolor()
	print(type(myColor),myColor)
	root.config(bg=myColor[1])




root=Tk()
root.title("Scale")
root.geometry("360x240")

fm = Frame(root)
fm.pack()
rSlider = Scale(fm,from_=0,to=255,command=bgUpdate)
gSlider = Scale(fm,from_=0,to=255,command=bgUpdate)
bSlider = Scale(fm,from_=0,to=255,command=bgUpdate)
bSlider.set(120)

rSlider.grid(row=0,column=0)
gSlider.grid(row=0,column=1)
bSlider.grid(row=0,column=3)

btn = Button(fm,text="Select Color",command=bgChoose)
btn.grid(row=1,column=1)

root.mainloop()