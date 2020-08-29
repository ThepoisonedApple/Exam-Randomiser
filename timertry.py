from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar,QAbstractButton
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMouseEvent,QIcon,QFont,QPixmap,QPalette,QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import pyqtSlot, QCoreApplication, Qt,QBasicTimer, QPoint, QObject, pyqtSignal, QEvent
import sys
from Db_class import Db_Class

class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()

class Ui_MainWindow(QMainWindow):
    def __init__(self,MainWindow):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent")
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.center()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.myclass=Db_Class()

        timer = QtCore.QTimer(self, timeout=self.checkdb, interval=6000)
        timer.start()

        self.bexit = PicButton(QPixmap('C:/Users/PC/Desktop/login/Exit.png'), self.centralwidget)
        self.bexit.move(780, 0)
        self.bexit.resize(20,20)
        self.bexit.clicked.connect(self.exit_onclick)

        self.bpm = QtWidgets.QPushButton(self.centralwidget)
        self.bpm.setStyleSheet("background-color:transparent;\
        border: 1px solid #000000")
        self.bpm.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
        self.bpm.setText("Pattern \n Matching")
        self.bpm.setFixedSize(100,100)
        self.bpm.move(0,39)
        self.bpm.clicked.connect(self.PM_onclick)

        self.setCentralWidget(self.centralwidget)
        self.oldPos = self.pos()
        self.show()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(127,140,141),  0.5, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(127,140,141), Qt.SolidPattern))
        painter.drawRoundedRect(0, 0, 800, 600,10,10)
        painter.setPen(QPen(QColor(44,62,80),0.5,Qt.SolidLine))        
        painter.setBrush(QBrush(QColor(44,62,80),Qt.SolidPattern))
        painter.drawRoundedRect(0, 0, 95, 600,10,10)
        painter.drawRect(80,0,20,600)
        painter.setPen(QPen(QColor(52,73,94),0.5,Qt.SolidLine))        
        painter.setBrush(QBrush(QColor(52,73,94),Qt.SolidPattern))
        painter.drawRoundedRect(0, 0, 800, 39,10,10)
        painter.drawRect(0,30,800,10)
        painter.setPen(QPen(QColor(0,0,0),1.5,Qt.SolidLine))
        painter.drawLine(99,40,800,40)
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        print(QMouseEvent.pos(event))
    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    @pyqtSlot()
    def exit_onclick(self):
        self.oldPos = QMouseEvent.pos()
        quit()
    def PM_onclick(self):
    	self.oldPos = QMouseEvent.pos()
    	print("worked")
    def checkdb(self):
        self.myclass.Check_Db_Status()
        if self.myclass.Db_Status==1:
            print("db connected")
        elif self.myclass.Db_Status==0:
            print("db connected table couldnt found")
        else:
            print("an error occurded please check db connection")



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow(MainWindow)
sys.exit(app.exec_())



        self.l1=QtWidgets.QTableWidget(self.tab1)
        self.l1.setStyleSheet(Style.table_style)
        self.l1.setFixedSize(800,500)
        self.l1.setRowCount(10)
        self.l1.setColumnCount(6)
        self.l1.verticalHeader().hide()
        tab_header=("a","b","c")
        self.l1.setHorizontalHeaderLabels(tab_header)
        x=QtWidgets.QTableWidgetItem("hello")
        self.l1.setItem(0,1,x)


                self.f2_t2_cbders= QtWidgets.QComboBox(self.f2_tab2)
        self.f2_t2_cbders.setFont(QtGui.QFont("Verdana", 10, QtGui.QFont.Bold))
        #self.f2_t2_cbders.setStyleSheet("color:White")
        self.f2_t2_cbders.setFixedSize(200,35)
        self.f2_t2_cbders.move(10,10)
        self.f2_t2_cbders.addItem("C")
        self.f2_t2_cbders.addItem("C++")
