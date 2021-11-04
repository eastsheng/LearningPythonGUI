# 复选框
from tkinter import *
def printInfo():
	selection=""
	for i in checkboxes:
		if checkboxes[i].get()==True:
			selection=selection+sports[i] + "\t"
	print(selection)

root=Tk()
root.title("复选框1")
root.geometry("400x200")

labFrame = LabelFrame(root,text="请选择喜欢的运动",
	fg='blue',bg="lightyellow",width=30)

sports = {0:"美式足球",1:"棒球",2:"篮球",3:"网球"}
checkboxes = {}
for i in range(len(sports)):
	checkboxes[i] = BooleanVar()
	Checkbutton(labFrame,text=sports[i],
		variable=checkboxes[i]).grid(row=i+1,sticky=W)
labFrame.pack(ipadx=5,ipady=5,pady=10)
btn = Button(root,text="OK",width=10,command=printInfo)
btn.pack()
root.mainloop()