from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class MainWindow(QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QWidget.__init__(self)
        self.combo1 = QComboBox()
        for i in range (0,10):
            self.combo1.addItem('Combo1 label %s' %str(i))
        self.combo2 = QComboBox()
        for i in range (0,15):
            self.combo2.addItem('Combo2 label %s' %str(i))
        main_layout = QVBoxLayout()
        layout = QHBoxLayout()
        layout.addWidget(self.combo1)
        layout.addWidget(self.combo2)
        # design title bar
        title_bar = QHBoxLayout()
        title_bar.setObjectName('HeaderBar')
        title_bar.setContentsMargins(0,0,0,0)
        title = QLabel('title bar')
        btn_size = 35
        btn_close = QPushButton("x")
        btn_close.clicked.connect(self.btn_close_clicked)
        btn_close.setFixedSize(btn_size,btn_size)
        btn_close.setStyleSheet("background-color: red;")
        btn_min = QPushButton("_")
        btn_min.clicked.connect(self.btn_min_clicked)
        btn_min.setFixedSize(btn_size, btn_size)
        btn_min.setStyleSheet("background-color: gray;")
        self.btn_max = QPushButton("+")
        self.btn_max.clicked.connect(self.btn_max_clicked)
        self.btn_max.setFixedSize(btn_size, btn_size)
        self.btn_max.setStyleSheet("background-color: gray;")
        title.setAlignment(Qt.AlignCenter)
        title_bar.addWidget(title)
        title_bar.addWidget(btn_min)
        title_bar.addWidget(self.btn_max)
        title_bar.addWidget(btn_close)
        main_layout.addLayout(title_bar)
        main_layout.addLayout(layout)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setLayout(main_layout)
        self.work_with_combo = True
        self.old_Pos = None
    def mousePressEvent(self, event):
        self.old_Pos = event.globalPos()
        self.old_width = self.width()
        self.old_height = self.height()
    def mouseMoveEvent(self, event):
        if self.old_Pos:
            delta = QPoint (event.globalPos() - self.old_Pos)
            if (self.old_Pos.x() > self.x() + self.old_width - 10) or (self.old_Pos.y() > self.y() + self.old_height - 10):
                self.setFixedSize(self.old_width + delta.x(),self.old_height + delta.y())
            else:
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.old_Pos = event.globalPos()
    def mouseReleaseEvent(self, event):
        self.old_Pos = None
    def btn_close_clicked(self):
        quit()
    def btn_max_clicked(self):
        if self.isMaximized():
            self.showNormal()
            self.btn_max.setText('+')
        else:
            self.showMaximized()
            self.btn_max.setText('R')
    def btn_min_clicked(self):
        self.showMinimized()        
app = QApplication([])
mainapp = MainWindow()
mainapp.show()
app.exec_()