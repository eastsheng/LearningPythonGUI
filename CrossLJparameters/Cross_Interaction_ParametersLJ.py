# A GUI program to calculate the cross interaction LJ parameters 
from tkinter import *
import numpy as np

def CrossLJE():
	ei = eval(energyi.get())
	ej = eval(energyj.get())
	eij = np.sqrt(ei*ej)
	print(eij)
	oute.configure(text="E_ij= "+str(eij)+" ev")

def CrossLJD():
	ri = eval(distancei.get())
	rj = eval(distancej.get())
	rij = (ri+rj)/2
	print(rij)
	outr.configure(text="R_ij= "+str(rij)+" Angstrom")


root = Tk()
root.title("CCILJ")
# screenWidth = root.winfo_screenwidth()
# screenHeight = root.winfo_screenheight()
# w = 555
# h = 200
# x = (screenWidth-w)/2#200
# y = (screenHeight-h)/2#200
# root.geometry("%dx%d+%d+%d" % (w,h,x,y))
label = Label(root,text="Calculate the cross interaction LJ parameters",
	font="Times 15 bold",fg="blue")
label.grid(pady=10,row=0,columnspan=4)

energyn = Label(root,text="Energy",font="Times 15 bold",fg="red")
energyn.grid(padx=5,pady=5,row=1)

energyi = Entry(root)
energyi.grid(padx=5,pady=5,row=1,column=1)
energyj = Entry(root)
energyj.grid(padx=5,pady=5,row=1,column=2)
unite =Label(root,text="ev")
unite.grid(padx=5,pady=5,row=1,column=3)


btn = Button(root,text="Calculate",command=CrossLJE,cursor="heart")
btn.grid(padx=5,pady=5,row=2,column=0)
oute =Label(root,font="Times 10 bold")
oute.grid(padx=5,pady=5,row=2,column=1,columnspan=2)


distancen = Label(root,text="Distance",font="Times 15 bold",fg="gray")
distancen.grid(row=3)

distancei = Entry(root)
distancei.grid(padx=5,pady=5,row=3,column=1)
distancej = Entry(root)
distancej.grid(padx=5,pady=5,row=3,column=2)
unitr =Label(root,text="Angstrom")
unitr.grid(padx=5,pady=5,row=3,column=3)


btn = Button(root,text="Calculate",command=CrossLJD,cursor="heart")
btn.grid(padx=5,pady=5,row=4,column=0)


outr =Label(root,font="Times 10 bold")
outr.grid(padx=5,pady=5,row=4,column=1,columnspan=2)


quit = Button(root,text="Quit",command=root.quit,cursor="heart")
quit.grid(pady=10,row=5,columnspan=4)

root.mainloop()


