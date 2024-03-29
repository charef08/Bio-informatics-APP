import sys
from PyQt5 import QtWidgets as QtW
from PyQt5 import QtCore as QtC
from PyQt5 import QtGui as QtG

from Interface_app import Ui_Form


class MainWindow(QtW.QWidget):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
    

if __name__ == '__main__':
    application = QtW.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(application.exec_())