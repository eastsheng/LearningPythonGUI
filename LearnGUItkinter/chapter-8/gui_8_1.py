# Frame

from tkinter import *
root=Tk()
root.title("Frame")

Frame(root,bg="gray",height=50,width=250).pack()

for fm in ["red","green",'blue']:
	Frame(root,bg=fm,height=50,width=250).pack()

root.mainloop()