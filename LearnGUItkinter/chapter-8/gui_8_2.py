from tkinter import *

root=Tk()
root.title("More Frames")

frameUpper = Frame(root,relief=GROOVE,bg="lightyellow")
frameUpper.pack()

btnRed = Button(frameUpper,relief=RAISED,text="Red",fg="red")
btnRed.pack(side=LEFT,padx=5,pady=5)

btnGreen = Button(frameUpper,relief=GROOVE,text="Green",fg="green")
btnGreen.pack(side=LEFT,padx=5,pady=5)

btnBlue = Button(frameUpper,relief=RIDGE,text="Blue",fg="blue")
btnBlue.pack(side=LEFT,padx=5,pady=5)

frameLower = Frame(root,relief=GROOVE,bg="lightblue")
frameLower.pack()

btnPurple = Button(frameLower,relief=RIDGE,text="Purple",fg="purple")
btnPurple.pack(side=LEFT,padx=5,pady=5)
root.mainloop()


