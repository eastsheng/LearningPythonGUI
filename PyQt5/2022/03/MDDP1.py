# coding:utf-8
'''
MD Data Processing(MDDP)
A LAMMPS-based MD simulation initial file generation and visualization program for data post-processing software
writed by Dongsheng Chen
2022/02/10
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MDDP(QMainWindow):
	"""MD Data Processing(MDDP)"""
	def __init__(self):
		super().__init__()
		self.initUI()
		
	def initUI(self):
		self.setWindowTitle("MD-Data-Processing")
		self.resize(1000,600)
		self.move(5,200)
		self.menu_and_status()
		# self.box_layout()
		self.grid_layout()

	def menu_and_status(self):
		# set a status messages text.
		self.statusBar().showMessage("This is a post-processing software for MD.")

		menu = self.menuBar() # Create a menu bar
		file_menu = menu.addMenu("文件F") # Create a file menu
		view_menu = menu.addMenu("视图V") # Create a view menu
		edit_menu = menu.addMenu("编辑E") # Create a edit menu
		help_menu = menu.addMenu("帮助H") # Create a help menu


		new_action = QAction('NEW新文件',self) # Create a action
		file_menu.addAction(new_action) # Add a action to file menu

		new_action.setStatusTip("新的文件") # Update the status messages text.

		exit_action = QAction('退出',self)
		exit_action.setStatusTip("Ctrl+Q点击退出应用程序")
		exit_action.triggered.connect(self.close)
		exit_action.setShortcut('Ctrl+Q') #set shortcut key
		file_menu.addAction(exit_action)


	def box_layout(self):
		
		lab1 = QLabel("标签1",self)
		lab2 = QLabel("标签2",self)

		button1 = QPushButton("按钮1",self)
		button2 = QPushButton("按钮2",self)

		hbox1 = QHBoxLayout()
		hbox2 = QHBoxLayout()
		hbox1.addWidget(lab1)
		hbox1.addWidget(button1)
		hbox2.addWidget(lab2)
		hbox2.addWidget(button2)


		vbox = QVBoxLayout()
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)

		layout_widget = QWidget()
		layout_widget.setLayout(vbox)
		self.setCentralWidget(layout_widget)

	def grid_layout(self):
		label_1 = QLabel('第一个标签')
		label_2 = QLabel('第二个标签')
		button_1 = QPushButton('第一个按钮')
		button_2 = QPushButton('第二个按钮')
		button_3 = QPushButton('第三个按钮')

		grid_layout = QGridLayout()

		grid_layout.addWidget(label_1,0,0) 
		grid_layout.addWidget(button_1,0,1)
		grid_layout.addWidget(label_2,1,0)
		grid_layout.addWidget(button_2,1,1)

		grid_layout.addWidget(button_3,2,1,1,5) #占用第3行的第2个位置 并占1行5列大小


		grid_layout.setAlignment(Qt.AlignTop)
		grid_layout.setAlignment(label_1,Qt.AlignCenter)
		grid_layout.setAlignment(label_2,Qt.AlignCenter)

		layout_widget = QWidget()
		layout_widget.setLayout(grid_layout)
		self.setCentralWidget(layout_widget)



if __name__ =='__main__':
	app = QApplication(sys.argv)
	gui = MDDP()
	gui.show()
	sys.exit(app.exec_())



