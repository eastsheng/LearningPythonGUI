from tkinter import *
from tkinter import messagebox

def myMsg():
	messagebox.showinfo("My Message Box","Python Tkinter你好呀")

root=Tk()
root.title("Message box")
root.geometry("360x360")

btn = Button(root,text="How are you, bro?",command=myMsg)
btn.pack()

root.mainloop()