from tkinter import *

root=Tk()
root.title("Toplevel_1")

tl = Toplevel()
tl.title("Toplevel")
tl.geometry("300x180")

lab = Label(tl,text="I am a Toplevel")
lab.pack()

root.mainloop()