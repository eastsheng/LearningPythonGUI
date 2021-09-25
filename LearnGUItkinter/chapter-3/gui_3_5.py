from tkinter import *
root = Tk()
root.title("sticky")

root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)

lab1 = Label(root,text="硕士",bg="blue",fg="white")
lab1.grid(row=0,column=0,padx=5,pady=5,stick=W)

lab2 = Label(root,text="博士",bg="red",fg="white")
lab2.grid(row=0,column=1,padx=5,pady=5,stick=W)

lab3 = Label(root,text="本科",bg="black",fg="white")
# lab3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky=N+S+W+E)

# lab3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky=W+E)
# lab3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky=N+S)

lab3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky=S+W)


root.mainloop()