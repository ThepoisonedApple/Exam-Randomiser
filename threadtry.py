from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                            QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                            QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                            QTextEdit,QDialog,QFrame,QProgressBar,QAbstractButton,QTabWidget
                            )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette,QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import pyqtSlot, QCoreApplication, Qt,QBasicTimer, QPoint, QObject, pyqtSignal, QEvent ,QSize,QRect,QThread
import sys
from Db_class import Db_Class
from ui_styles import Style
import time

class Ui_MainWindow(QMainWindow):
    def __init__(self,MainWindow):
        super().__init__()
        self.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.myclass=Db_Class()
        self.thread = Worker()
        self.btnStart.clicked.connect(self.slotStart)
        self.thread.sinout.connect(self.slotAdd)
    def slotStart(self):
        self.btnStart.setEnabled(False)
        self.thread.start()

    def slotAdd(self,file_inf):
        self.listFile.addItem(file_inf)

class Worker(QThread):
    sinout=  pyqtSignal(str)
    def __init__(self, parent = None):
        super(Worker,self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while self.working == True:
            file_str = "File index {0} ".format(self.num)
            self.num += 1
            # Transmitting signal
            self.sinout.emit(file_str)
            # Thread hibernates for 2 seconds
            self.sleep(2)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWidget()
    demo.show()
    sys.exit(app.exec_())