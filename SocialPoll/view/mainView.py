from PyQt5 import QtWidgets
from view.mainUI import Ui_MainWindow


class mainView(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainView, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)