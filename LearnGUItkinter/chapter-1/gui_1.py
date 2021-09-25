from tkinter import *
print(TkVersion)

import tkinter

print(tkinter.TkVersion)

class Application(Frame):
	"""docstring for Application"""
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		
	def createWidgets(self):
		self.helloLabel = Label(self, text='你好')
		self.helloLabel.pack()
		self.quitButton = Button(self, text='退出', command=self.quit)
		self.quitButton.pack()

app = Application()
app.master.title("Hello")
app.mainloop()