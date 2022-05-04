from PyQt5 import QtCore,QtWidgets,QtGui
import MyFirstQtGUI as mfqg
import sys
import time
import pyqtgraph as pg

class DragDropButton(QtWidgets.QPushButton):
    
    def __init__(self, text, parent):
        super().__init__(text, parent)       
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        self.setText(event.mimeData().text())


class MainWindow(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = mfqg.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.pushButton.hide()
        self.pushButton = DragDropButton("拖放按钮",MainWindow)
        self.ui.horizontalLayout_2.addWidget(self.pushButton)

        # self.ui.verticalLayout_3.addWidget(self.pushButton)
        self.update_date()
        self.update_calendar()
        self.set_lcd()
        self.set_dial()
        # self.zero_process()
        # self.update_process()
        # self.click_radio3()
        self.update_processbar()
        self.set_font()
        MainWindow.show()
        sys.exit(app.exec_())
    # 修改日期修改器数值
    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    # 日历信号槽
    def update_calendar(self):
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)

    # 设置LCD数字
    def set_lcd(self):
        self.ui.lcdNumber.display(self.ui.dial.value())
    # 刻度盘信号槽
    def set_dial(self):
        self.ui.dial.valueChanged['int'].connect(self.set_lcd)


    def zero_process(self):
        self.ui.radioButton_2.clicked.connect(self.ui.progressBar.reset)
    # 更新进度栏
    def update_process(self):
        value = self.ui.lcdNumber.value()
        self.ui.progressBar.setValue(value)
     # 点击按钮3
    def click_radio3(self):
        self.ui.radioButton_3.clicked.connect(self.update_process)


    def update_processbar(self):
        self.ui.radioButton.clicked.connect(self.start_progressbar)
        self.ui.radioButton_2.clicked.connect(self.stop_progressbar)
        self.ui.radioButton_3.clicked.connect(self.reset_progressbar)
        self.progress_value=0
        self.stop_progress=False

    def start_progressbar(self):
        self.stop_progress = False
        self.progress_value = self.ui.progressBar.value()
        self.progressbar_counter(self.progress_value)
       
        # while (self.progress_value<=101) and not (self.stop_progress):
        #     self.ui.progressBar.setValue(self.progress_value)
        #     self.progress_value += 1
        #     time.sleep(0.5)
        #     QtWidgets.QApplication.processEvents()

    def stop_progressbar(self):
        self.stop_progress = True
        try:
            self.run_thread.stop()
        except:
            pass

    def reset_progressbar(self):
        self.progress_value=0
        self.ui.progressBar.reset()
        self.stop_progress=False

    def progressbar_counter(self,start_value=0):
        self.run_thread = RunThread(parent=None,counter_value=start_value)
        self.run_thread.start()
        self.run_thread.counter_value.connect(self.reset_progressbar)
    def set_progressbar(self,counter):
        if not self.stop_progress:
            self.ui.progressBar.setValue(counter)

    def set_font(self):        
        self.ui.fontComboBox.activated['QString'].connect(self.ui.label.setText)


class RunThread(QtCore.QThread):
    """docstring for RunThread"""
    counter_value = QtCore.pyqtSignal(int)

    def __init__(self, parent=None,counter_value=0):
        super(RunThread, self).__init__(parent)
        self.counter = counter_value
        self.is_running = True
    def run(self):
        while self.counter<100 and self.is_running == True:
            time.sleep(0.1)
            self.counter += 1
            print(self.counter)
            self.counter_value.emit(self.counter)
    def stop(self):
        self.is_running = False
        print("线程终止中......")
        self.terminate()
        



if __name__ == "__main__":
    MainWindow()