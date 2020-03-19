from PyQt5 import QtWidgets, QtCore
import sys
from view.authView import authView
from view.mainView import mainView


def main():
    app = QtWidgets.QApplication([])
    application = authView()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()