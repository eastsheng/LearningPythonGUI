from tkinter import *

root=Tk()
root.title("More Frames")

fms = {
	"red":"cross",
	"green":"boat",
	"blue":"clock"
}

for fmColor in fms:
	print(fmColor,fms[fmColor])

	Frame(root,bg=fmColor,cursor=fms[fmColor],
		height=50,width=200).pack(side=LEFT)

root.mainloop()


