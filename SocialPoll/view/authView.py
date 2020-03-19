from PyQt5 import QtWidgets
from view.uiAuth import Ui_AuthWindow as AuthView


class authView(QtWidgets.QMainWindow):
    def __init__(self):
        super(authView, self).__init__()
        self.ui = AuthView()
        self.ui.setupUi(self)


