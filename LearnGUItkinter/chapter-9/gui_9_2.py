from tkinter import *

def bgUpdate(source):#这里source可以替换为任意字符
	"""窗口颜色"""
	r = rSlider.get()
	g = gSlider.get()
	b = bSlider.get()
	print("R=%d,G=%d,B=%d" % (r,g,b))
	myColor = "#%02x%02x%02x" %(r,g,b)
	root.config(bg=myColor)

root=Tk()
root.title("Scale")
root.geometry("360x240")

rSlider = Scale(root,from_=0,to=255,command=bgUpdate)
gSlider = Scale(root,from_=0,to=255,command=bgUpdate)
bSlider = Scale(root,from_=0,to=255,command=bgUpdate)

bSlider.set(120)

rSlider.grid(row=0,column=0)
gSlider.grid(row=0,column=1)
bSlider.grid(row=0,column=3)


root.mainloop()