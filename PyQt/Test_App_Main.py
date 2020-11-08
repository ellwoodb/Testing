from PyQt5.QtWidgets import QWidget
from Test import *
import sys


class TestApp(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        # self.First_Button.clicked.connect(self.clicked_first)
        # self.Second_Button.clicked.connect(self.clicked_second)
        # self.Third_Button.clicked.connect(self.clicked_third)

    # def clicked_first(self):
    #     print("Button 1 clicked!")

    # def clicked_second(self):
    #     print("Button 2 clicked!")

    # def clicked_third(self):
    #     print("Button 3 clicked!")


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = TestApp(MainWindow)

MainWindow.show()
app.exec_()
