from tkinter import *

root = Tk()
root.title("Hello")

"""-----窗口-----"""
# root.geometry("300x160")
# root.geometry("300x160+200+200")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
print(screenWidth,screenHeight)
w = 300
h = 160
x = (screenWidth-w)/2#200
y = (screenHeight-h)/2#200
root.geometry("%dx%d+%d+%d" % (w,h,x,y))

# root.configure(bg='grey')
root.configure(bg='#fffff0')
root.iconbitmap("../img/cool.ico")
root.mainloop()