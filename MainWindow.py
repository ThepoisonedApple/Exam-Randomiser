from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar,QAbstractButton
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette,QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import pyqtSlot, QCoreApplication, Qt,QBasicTimer, QPoint, QObject, pyqtSignal, QEvent ,QSize
import sys
from Db_class import Db_Class
from ui_styles import Style

class Ui_MainWindow(QMainWindow):
    def __init__(self,MainWindow):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(1024, 768)
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

        self.pcheckdb = QtWidgets.QLabel(self.centralwidget)
        self.pcheckdb.setGeometry(QtCore.QRect(104, 746, 20, 20))
        self.pcheckdb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pcheckdb.setText("")
        self.pcheckdb.setScaledContents(True)
        self.pcheckdb.setObjectName("pcheckdb")
        self.pcheckdb.setPixmap(QtGui.QPixmap("images/close.png"))

        self.tcheckdb = QtWidgets.QLabel(self.centralwidget)
        self.tcheckdb.setGeometry(QtCore.QRect(128, 746, 400, 20))
        self.tcheckdb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tcheckdb.setText("Veritabanına Bağlanılıyor..")
        self.tcheckdb.setObjectName("tcheckdb")
        self.tcheckdb.setFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
        self.tcheckdb.setStyleSheet('color: White')

        self.checkdb()
        self.tab0 = QWidget() 
        self.tab1 = QWidget() 
        ######################################################################################
        
        ######################################################################################
        self.tab2 = QWidget() 

        self.mytabs=QtWidgets.QTabWidget(self.centralwidget)
        self.mytabs.setGeometry(QtCore.QRect(100, 40, 924, 703))

        self.mytabs.setStyleSheet(Style.tabstyle)
        self.mytabs.addTab(self.tab0, "Settings") 
        self.mytabs.addTab(self.tab1, "For") 
        self.mytabs.addTab(self.tab2, "Geeks")
        self.mytabs.setTabVisible(0,False)
        self.mytabs.setTabVisible(1,False)
        self.mytabs.setTabVisible(2,False)
        self.mytabs.setCurrentIndex(0)
        ############################################################################################################################
        # tab0= settings page
        ############################################################################################################################
        self.p_setting = QtWidgets.QLabel(self.tab0)
        self.p_setting.setGeometry(QtCore.QRect(387, 20, 150, 150))
        self.p_setting.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.p_setting.setText("")
        self.p_setting.setScaledContents(True)
        self.p_setting.setObjectName("p_setting")
        self.p_setting.setPixmap(QtGui.QPixmap("images/settings.png"))

        self.t_setting = QtWidgets.QLabel(self.tab0)
        self.t_setting.setGeometry(QtCore.QRect(387, 200, 185, 35))
        self.t_setting.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.t_setting.setText("Ayarlar")
        self.t_setting.setObjectName("t_setting")
        self.t_setting.setFont(QtGui.QFont("Verdana", 16, QtGui.QFont.Bold))
        self.t_setting.setStyleSheet('color: White;')

        self.t_ip = QtWidgets.QLabel(self.tab0)
        self.t_ip.setGeometry(QtCore.QRect(200, 325, 185, 35))
        self.t_ip.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.t_ip.setText("Veritabanı ip:")
        self.t_ip.setObjectName("t_ip")
        self.t_ip.setFont(QtGui.QFont("Verdana", 14, QtGui.QFont.Bold))
        self.t_ip.setStyleSheet('color: Black;')

        self.tb_ip = QtWidgets.QLineEdit(self.tab0)
        self.tb_ip.move(390, 325)
        self.tb_ip.resize(240,35)
        self.tb_ip.setFocusPolicy(Qt.StrongFocus)
        self.tb_ip.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
        self.tb_ip.setStyleSheet('background-color: White; border: 2px solid black;')
        self.tb_ip.setText(self.myclass.Host)

        self.t_user = QtWidgets.QLabel(self.tab0)
        self.t_user.setGeometry(QtCore.QRect(200, 400, 185, 35))
        self.t_user.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.t_user.setText("Kullanıcı Adı:")
        self.t_user.setObjectName("t_user")
        self.t_user.setFont(QtGui.QFont("Verdana", 14, QtGui.QFont.Bold))
        self.t_user.setStyleSheet('color: Black;')

        self.tb_user = QtWidgets.QLineEdit(self.tab0)
        self.tb_user.move(390, 400)
        self.tb_user.resize(240,35)
        self.tb_user.setFocusPolicy(Qt.StrongFocus)
        self.tb_user.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
        self.tb_user.setStyleSheet('background-color: White; border: 2px solid black;')
        self.tb_user.setText(self.myclass.User)

        self.t_pass = QtWidgets.QLabel(self.tab0)
        self.t_pass.setGeometry(QtCore.QRect(200, 475, 185, 35))
        self.t_pass.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.t_pass.setText("Şifre:")
        self.t_pass.setObjectName("t_pass")
        self.t_pass.setFont(QtGui.QFont("Verdana", 14, QtGui.QFont.Bold))
        self.t_pass.setStyleSheet('color: Black;')

        self.tb_pass = QLineEdit(self.tab0)
        self.tb_pass.move(390, 475)
        self.tb_pass.resize(240,35)
        self.tb_pass.setEchoMode(QLineEdit.Password)
        self.tb_pass.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
        self.tb_pass.setStyleSheet('background-color: White; border: 2px solid black;')

        self.b_db_ok = QtWidgets.QPushButton(self.tab0)
        self.b_db_ok.setStyleSheet(Style.ok_button)
        self.b_db_ok.setText("Onayla")
        self.b_db_ok.setFixedSize(100,50)
        self.b_db_ok.move(724,563)
        self.b_db_ok.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
        self.b_db_ok.clicked.connect(self.Write_Config)
        ############################################################################################################################
        # End of settings page
        #Home page :tab1
        ############################################################################################################################
        
        self.f1_tab1=QtWidgets.QFrame(self.tab1)
        self.f1_tab1.move(10,10)
        self.f1_tab1.setFixedSize(420,318)
        self.f1_tab1.setStyleSheet(Style.all_style)

        self.f2_tab1=QtWidgets.QFrame(self.tab1)
        self.f2_tab1.move(10,338)
        self.f2_tab1.setFixedSize(455,353)
        self.f2_tab1.setStyleSheet(Style.all_style)

        self.f1_tab1_tabw=QtWidgets.QTabWidget(self.tab1)
        self.f1_tab1_tabw.move(450,10)
        self.f1_tab1_tabw.setFixedSize(454,318)
        self.f1_tab1_tabw.setStyleSheet(Style.all_style)

        self.f1_tab1_tabw_instert = QWidget() 
        self.f1_tab1_tabw_update = QWidget()
        self.f1_tab1_tabw_search = QWidget()  

        self.f1_tab1_tabw.addTab(self.f1_tab1_tabw_search,"Ara")
        self.f1_tab1_tabw.addTab(self.f1_tab1_tabw_instert,"EKLE")
        self.f1_tab1_tabw.addTab(self.f1_tab1_tabw_update,"GÜNCELLE")
        self.f1_tab1_tabw_instert.setStyleSheet(Style.all_style)
        self.f1_tab1_tabw.setTabPosition(3)

        self.f2_tab1_tabw=QtWidgets.QTabWidget(self.tab1)
        self.f2_tab1_tabw.move(480,338)
        self.f2_tab1_tabw.setFixedSize(434,353)
        self.f2_tab1_tabw.setStyleSheet(Style.all_style)

        self.f2_tab1_tabw_insert = QWidget() 
        self.f2_tab1_tabw_update = QWidget()
        self.f2_tab1_tabw_search = QWidget()

        self.f2_tab1_tabw.addTab(self.f2_tab1_tabw_insert,"EKLE")
        self.f2_tab1_tabw.addTab(self.f2_tab1_tabw_update,"GÜNCELLE")
        self.f2_tab1_tabw.addTab(self.f2_tab1_tabw_search,"ARA")
        self.f2_tab1_tabw_insert.setStyleSheet(Style.all_style)
        self.f2_tab1_tabw.setTabPosition(3)

        self.tbuser1 = QtWidgets.QLineEdit(self.f1_tab1_tabw_instert)
        self.tbuser1.move(20, 60)
        self.tbuser1.resize(200,35)
        self.tbuser1.setPlaceholderText("Ders adını giriniz..")
        self.tbuser1.setFocusPolicy(Qt.StrongFocus)
        self.tbuser1.setFont(QtGui.QFont("Verdana", 11))
        self.tbuser1.setStyleSheet(Style.lineedit_style)	

        self.f1_tab1_tabw_instert_ok = QtWidgets.QPushButton(self.f1_tab1_tabw_instert)
        self.f1_tab1_tabw_instert_ok.setStyleSheet(Style.ok_button)
        self.f1_tab1_tabw_instert_ok.setText("Ekle")
        self.f1_tab1_tabw_instert_ok.setFixedSize(100,50)
        self.f1_tab1_tabw_instert_ok.move(100,200)
        self.f1_tab1_tabw_instert_ok.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
        self.f1_tab1_tabw_instert_ok.clicked.connect(self.ders_ekle)	  

        self.f1_t1_table = QtWidgets.QTableWidget(self.f1_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f1_t1_table.sizePolicy().hasHeightForWidth())
        self.f1_t1_table.setSizePolicy(sizePolicy)
        self.f1_t1_table.setFixedSize(400,300)
        self.f1_t1_table.move(10,10)
        self.f1_t1_table.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
        self.f1_t1_table.horizontalHeader().setStyleSheet("color:White")
        self.f1_t1_table.setStyleSheet(Style.table_style)
        self.f1_t1_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.f1_t1_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.f1_t1_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.f1_t1_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.f1_t1_table.setAlternatingRowColors(False)
        self.f1_t1_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.f1_t1_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.f1_t1_table.setShowGrid(True)
        self.f1_t1_table.setGridStyle(QtCore.Qt.SolidLine)
        self.f1_t1_table.setObjectName("f1_t1_table")
        self.f1_t1_table.setColumnCount(2)
        self.f1_t1_table.setRowCount(100)
        self.f1_t1_table.horizontalHeader().setVisible(True)
        self.f1_t1_table.horizontalHeader().setCascadingSectionResizes(True)
        self.f1_t1_table.horizontalHeader().setDefaultSectionSize(200)
        self.f1_t1_table.horizontalHeader().setStretchLastSection(True)
        self.f1_t1_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.f1_t1_table.setHorizontalHeaderLabels(["ID","Ders Adı"])
        self.f1_t1_table.verticalHeader().setVisible(False)
        self.f1_t1_table.verticalHeader().setCascadingSectionResizes(False)
        self.f1_t1_table.verticalHeader().setHighlightSections(False)
        self.f1_t1_table.verticalHeader().setStretchLastSection(True)
        self.f1_t1_table.setSortingEnabled(True)
        ###########################
        #ders ara tab start
        ##########################

        self.psearch_icon = QtWidgets.QLabel(self.f1_tab1_tabw_search)
        self.psearch_icon.setGeometry(QtCore.QRect(100, 30, 75, 75))
        self.psearch_icon.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.psearch_icon.setText("")
        self.psearch_icon.setScaledContents(True)
        self.psearch_icon.setObjectName("psearch_icon")
        self.psearch_icon.setPixmap(QtGui.QPixmap("images/search.png"))

        self.lsearch=QtWidgets.QLabel(self.f1_tab1_tabw_search)
        self.lsearch.setGeometry(QtCore.QRect(200, 50, 200, 45))
        self.lsearch.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lsearch.setFont(QtGui.QFont("Verdana", 15,QtGui.QFont.Bold))
        self.lsearch.setStyleSheet("color:White;")
        self.lsearch.setText("Ders Ara")
        self.lsearch.setScaledContents(True)
        self.lsearch.setObjectName("psearch_icon")

        self.f1_t1_tabw_tbara=QLineEdit(self.f1_tab1_tabw_search)
        self.f1_t1_tabw_tbara.move(100, 200)
        self.f1_t1_tabw_tbara.resize(200,35)
        self.f1_t1_tabw_tbara.setFocusPolicy(Qt.StrongFocus)
        self.f1_t1_tabw_tbara.setFont(QtGui.QFont("Verdana", 11))
        self.f1_t1_tabw_tbara.setStyleSheet(Style.lineedit_style)
        self.f1_t1_tabw_tbara.textEdited.connect(self.ders_ara)	

        self.f1_t1_tabw_bara = QtWidgets.QPushButton(self.f1_tab1_tabw_search)
        self.f1_t1_tabw_bara.setStyleSheet(Style.borderless_button)
        self.f1_t1_tabw_bara.setFixedSize(35,35)
        self.f1_t1_tabw_bara.move(300,200)
        self.f1_t1_tabw_bara.setIcon(QIcon("images/search.png"))
        self.f1_t1_tabw_bara.clicked.connect(self.ders_ara)


        ########################
        #ders ara tab end
        #ders güncelle tab start
        ########################



        self.f1_tab1_tabw_tbupdate_id=QLineEdit(self.f1_tab1_tabw_update)
        self.f1_tab1_tabw_tbupdate_id.move(10, 120)
        self.f1_tab1_tabw_tbupdate_id.resize(200,35)
        self.f1_tab1_tabw_tbupdate_id.setFocusPolicy(Qt.StrongFocus)
        self.f1_tab1_tabw_tbupdate_id.setFont(QtGui.QFont("Verdana", 11))
        self.f1_tab1_tabw_tbupdate_id.setStyleSheet(Style.lineedit_style)
        self.f1_tab1_tabw_tbupdate_id.setReadOnly(True)

        self.f1_tab1_tabw_tbupdate_name=QLineEdit(self.f1_tab1_tabw_update)
        self.f1_tab1_tabw_tbupdate_name.move(10, 170)
        self.f1_tab1_tabw_tbupdate_name.resize(200,35)
        self.f1_tab1_tabw_tbupdate_name.setFocusPolicy(Qt.StrongFocus)
        self.f1_tab1_tabw_tbupdate_name.setFont(QtGui.QFont("Verdana", 11))
        self.f1_tab1_tabw_tbupdate_name.setStyleSheet(Style.lineedit_style)

        self.f1_t1_table.itemSelectionChanged.connect(self.guncelle)

        self.f1_t1_tabw_bupdate = QtWidgets.QPushButton(self.f1_tab1_tabw_update)
        self.f1_t1_tabw_bupdate.setStyleSheet(Style.ok_button)
        self.f1_t1_tabw_bupdate.setFixedSize(35,35)
        self.f1_t1_tabw_bupdate.move(300,200)
        self.f1_t1_tabw_bupdate.setText("Güncelle")
        self.f1_t1_tabw_bupdate.clicked.connect(self.ders_guncelle)

        ########################
        #ders güncelle tab end
        ########################


        #####################################################################################
        #konu tab start
        #####################################################################################
        self.f2_t1_table = QtWidgets.QTableWidget(self.f2_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f2_t1_table.sizePolicy().hasHeightForWidth())
        self.f2_t1_table.setSizePolicy(sizePolicy)
        self.f2_t1_table.setFixedSize(435,335)
        self.f2_t1_table.move(10,10)
        self.f2_t1_table.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
        self.f2_t1_table.horizontalHeader().setStyleSheet("color:White")
        self.f2_t1_table.setStyleSheet(Style.table_style)
        self.f2_t1_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.f2_t1_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.f2_t1_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.f2_t1_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.f2_t1_table.setAlternatingRowColors(False)
        self.f2_t1_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.f2_t1_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.f2_t1_table.setShowGrid(True)
        self.f2_t1_table.setGridStyle(QtCore.Qt.SolidLine)
        self.f2_t1_table.setObjectName("f2_t1_table")
        self.f2_t1_table.setColumnCount(4)
        self.f2_t1_table.setRowCount(100)
        self.f2_t1_table.horizontalHeader().setVisible(True)
        self.f2_t1_table.horizontalHeader().setCascadingSectionResizes(True)
        self.f2_t1_table.horizontalHeader().setDefaultSectionSize(200)
        self.f2_t1_table.horizontalHeader().setStretchLastSection(True)
        self.f2_t1_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.f2_t1_table.setHorizontalHeaderLabels(["ID","Ders Adı","Donem","Konu Adı"])
        self.f2_t1_table.verticalHeader().setVisible(False)
        self.f2_t1_table.verticalHeader().setCascadingSectionResizes(False)
        self.f2_t1_table.verticalHeader().setHighlightSections(False)
        self.f2_t1_table.verticalHeader().setStretchLastSection(True)
        self.f2_t1_table.setSortingEnabled(True)

        ###########################
        #konu ekle tab start
        ###########################

        self.f2_t1_tabw_cbders = QtWidgets.QComboBox(self.f2_tab1_tabw_insert)
        self.f2_t1_tabw_cbders.move(20,10)
        self.f2_t1_tabw_cbders.setFixedSize(200,35)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.f2_t1_tabw_cbders.setFont(font)
        self.f2_t1_tabw_cbders.setAutoFillBackground(False)
        self.f2_t1_tabw_cbders.setStyleSheet(Style.combobox_style)
        self.f2_t1_tabw_cbders.setIconSize(QtCore.QSize(16, 16))
        self.f2_t1_tabw_cbders.setFrame(True)


        self.f2_t1_tabw_cbdonem = QtWidgets.QComboBox(self.f2_tab1_tabw_insert)
        self.f2_t1_tabw_cbdonem.move(20,60)
        self.f2_t1_tabw_cbdonem.setFixedSize(200,35)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.f2_t1_tabw_cbdonem.setFont(font)
        self.f2_t1_tabw_cbdonem.setAutoFillBackground(False)
        self.f2_t1_tabw_cbdonem.setStyleSheet(Style.combobox_style)
        self.f2_t1_tabw_cbdonem.setIconSize(QtCore.QSize(16, 16))
        self.f2_t1_tabw_cbdonem.setFrame(True)
        self.f2_t1_tabw_cbdonem.addItem("Vize",0)
        self.f2_t1_tabw_cbdonem.addItem("Final",1)

        self.f2_t1_tabw_name=QLineEdit(self.f2_tab1_tabw_insert)
        self.f2_t1_tabw_name.move(10, 110)
        self.f2_t1_tabw_name.resize(200,35)
        self.f2_t1_tabw_name.setFocusPolicy(Qt.StrongFocus)
        self.f2_t1_tabw_name.setFont(QtGui.QFont("Verdana", 11))
        self.f2_t1_tabw_name.setStyleSheet(Style.lineedit_style)

        self.f2_t1_tabw_binsert = QtWidgets.QPushButton(self.f2_tab1_tabw_insert)
        self.f2_t1_tabw_binsert.setStyleSheet(Style.ok_button)
        self.f2_t1_tabw_binsert.setFixedSize(35,35)
        self.f2_t1_tabw_binsert.move(300,200)
        self.f2_t1_tabw_binsert.setText("ekle")
        self.f2_t1_tabw_binsert.clicked.connect(self.konu_ekle)


        ############################
        #konu ekle tab end
        #konu ara tab start
        ############################

        self.f2_t1_tabw_tbara=QLineEdit(self.f2_tab1_tabw_search)
        self.f2_t1_tabw_tbara.move(100, 200)
        self.f2_t1_tabw_tbara.resize(200,35)
        self.f2_t1_tabw_tbara.setFocusPolicy(Qt.StrongFocus)
        self.f2_t1_tabw_tbara.setFont(QtGui.QFont("Verdana", 11))
        self.f2_t1_tabw_tbara.setStyleSheet(Style.lineedit_style)
        self.f2_t1_tabw_tbara.textEdited.connect(self.konu_ara)	

        self.f2_t1_tabw_bara = QtWidgets.QPushButton(self.f2_tab1_tabw_search)
        self.f2_t1_tabw_bara.setStyleSheet(Style.borderless_button)
        self.f2_t1_tabw_bara.setFixedSize(35,35)
        self.f2_t1_tabw_bara.move(300,200)
        self.f2_t1_tabw_bara.setIcon(QIcon("images/search.png"))
        self.f2_t1_tabw_bara.clicked.connect(self.konu_ara)



        ############################
        #konu ara tab end
        #konu güncelle tab start
        ############################

        self.f2_tab1_tabw_tbupdate_id=QLineEdit(self.f2_tab1_tabw_update)
        self.f2_tab1_tabw_tbupdate_id.move(10, 120)
        self.f2_tab1_tabw_tbupdate_id.resize(200,35)
        self.f2_tab1_tabw_tbupdate_id.setFocusPolicy(Qt.StrongFocus)
        self.f2_tab1_tabw_tbupdate_id.setFont(QtGui.QFont("Verdana", 11))
        self.f2_tab1_tabw_tbupdate_id.setStyleSheet(Style.lineedit_style)
        self.f2_tab1_tabw_tbupdate_id.setReadOnly(True)

        self.f2_tab1_tabw_tbupdate_name=QLineEdit(self.f1_tab1_tabw_update)
        self.f2_tab1_tabw_tbupdate_name.move(10, 170)
        self.f2_tab1_tabw_tbupdate_name.resize(200,35)
        self.f2_tab1_tabw_tbupdate_name.setFocusPolicy(Qt.StrongFocus)
        self.f2_tab1_tabw_tbupdate_name.setFont(QtGui.QFont("Verdana", 11))
        self.f2_tab1_tabw_tbupdate_name.setStyleSheet(Style.lineedit_style)

        self.f2_t1_table.itemSelectionChanged.connect(self.guncelle_konu)

        self.f2_t1_tabw_bupdate = QtWidgets.QPushButton(self.f1_tab1_tabw_update)
        self.f2_t1_tabw_bupdate.setStyleSheet(Style.ok_button)
        self.f2_t1_tabw_bupdate.setFixedSize(35,35)
        self.f2_t1_tabw_bupdate.move(300,200)
        self.f2_t1_tabw_bupdate.setText("Güncelle")
        #self.f2_t1_tabw_bupdate.clicked.connect(self.ders_guncelle)

        #############################
        #konu güncelle tab end
        #############################

        ############################################################################################################################
        #End of Home page
        #Start of add data page tab2
        ############################################################################################################################

        self.f1_tab2=QtWidgets.QFrame(self.tab2)
        self.f1_tab2.move(10,10)
        self.f1_tab2.setFixedSize(904,353)
        self.f1_tab2.setStyleSheet(Style.all_style)

        self.f2_tab2=QtWidgets.QTabWidget(self.tab2)
        self.f2_tab2.move(10,373)
        self.f2_tab2.setFixedSize(904,318)
        self.f2_tab2.setStyleSheet(Style.all_style)

        self.f2_tab2_insert = QWidget() 
        self.f2_tab2_update = QWidget() 

        self.f2_tab2.addTab(self.f2_tab2_insert,"EKLE")
        self.f2_tab2.addTab(self.f2_tab2_update,"GÜNCELLE")

        self.f1_t2_table = QtWidgets.QTableWidget(self.f1_tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f1_t2_table.sizePolicy().hasHeightForWidth())
        self.f1_t2_table.setSizePolicy(sizePolicy)
        self.f1_t2_table.setFixedSize(884,300)
        self.f1_t2_table.move(10,10)
        self.f1_t2_table.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
        self.f1_t2_table.horizontalHeader().setStyleSheet("color:White")
        self.f1_t2_table.setStyleSheet(Style.table_style)
        self.f1_t2_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.f1_t2_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.f1_t2_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.f1_t2_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.f1_t2_table.setAlternatingRowColors(False)
        self.f1_t2_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.f1_t2_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.f1_t2_table.setShowGrid(True)
        self.f1_t2_table.setGridStyle(QtCore.Qt.SolidLine)
        self.f1_t2_table.setObjectName("f1_t2_table")
        self.f1_t2_table.setColumnCount(4)
        self.f1_t2_table.setRowCount(100)
        self.f1_t2_table.horizontalHeader().setVisible(True)
        self.f1_t2_table.horizontalHeader().setCascadingSectionResizes(True)
        self.f1_t2_table.horizontalHeader().setDefaultSectionSize(200)
        self.f1_t2_table.horizontalHeader().setStretchLastSection(True)
        self.f1_t2_table.verticalHeader().setVisible(False)
        self.f1_t2_table.verticalHeader().setCascadingSectionResizes(False)
        self.f1_t2_table.verticalHeader().setHighlightSections(False)
        self.f1_t2_table.verticalHeader().setStretchLastSection(True)
        self.f1_t2_table.setSortingEnabled(True)
        


        self.f2_t2_cbders = QtWidgets.QComboBox(self.f2_tab2_insert)
        self.f2_t2_cbders.move(20,10)
        self.f2_t2_cbders.setFixedSize(200,35)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.f2_t2_cbders.setFont(font)
        self.f2_t2_cbders.setAutoFillBackground(False)
        self.f2_t2_cbders.setStyleSheet(Style.combobox_style)
        self.f2_t2_cbders.setIconSize(QtCore.QSize(16, 16))
        self.f2_t2_cbders.setFrame(True)
        self.f2_t2_cbders.setObjectName("f2_t2_cbders")
        self.f2_t2_cbders.activated['int'].connect(self.combo)


        self.f2_t2_cbkonu = QtWidgets.QComboBox(self.f2_tab2_insert)
        self.f2_t2_cbkonu.move(285,10)
        self.f2_t2_cbkonu.setFixedSize(200,35)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.f2_t2_cbkonu.setFont(font)
        self.f2_t2_cbkonu.setAutoFillBackground(False)
        self.f2_t2_cbkonu.setStyleSheet(Style.combobox_style)
        self.f2_t2_cbkonu.setIconSize(QtCore.QSize(16, 16))
        self.f2_t2_cbkonu.setFrame(True)
        self.f2_t2_cbkonu.setObjectName("f2_t2_cbkonu")



        self.tbuser = QtWidgets.QPlainTextEdit(self.f2_tab2_insert)
        self.tbuser.move(20, 60)
        self.tbuser.resize(700,210)
        self.tbuser.setPlaceholderText("Ders ve Konuyu seçtikten sonra sorunuzu bu kısma yazınız..")
        self.tbuser.setFocusPolicy(Qt.StrongFocus)
        self.tbuser.setFont(QtGui.QFont("Verdana", 11))
        self.tbuser.setStyleSheet(Style.plaintextedit_style)


 #       self.message=QtWidgets.QMessageBox(self.centralwidget)
        #self.message.setWindowFlags(QtCore.Qt.FramelessWindowHint)
  #      self.message.setStyleSheet("background-color:Black;")
   #     self.message.setFixedSize(500,500)
    #    self.message.move(QtCore.moveCenter)
     #   self.message.show()

        ############################################################################################################################
        #End of add data page=tab2
        ############################################################################################################################



        self.picon = QtWidgets.QLabel(self.centralwidget)
        self.picon.setGeometry(QtCore.QRect(105, 5, 30, 30))
        self.picon.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.picon.setText("")
        self.picon.setScaledContents(True)
        self.picon.setObjectName("picon")
        self.picon.setPixmap(QtGui.QPixmap("images/exam.png"))



        self.ticon = QtWidgets.QLabel(self.centralwidget)
        self.ticon.setGeometry(QtCore.QRect(140, 5, 200, 30))
        self.ticon.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ticon.setText("Exam Randomiser  v0.0.1")
        self.ticon.setObjectName("ticon")
        self.ticon.setFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
        self.ticon.setStyleSheet('color: White')

        

        self.Tauthor = QtWidgets.QLabel(self.centralwidget)
        self.Tauthor.setGeometry(QtCore.QRect(758, 746, 300, 20))
        self.Tauthor.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Tauthor.setText("Created by:Muhammed Ali ERDURAN")
        self.Tauthor.setObjectName("Tauthor")
        self.Tauthor.setFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
        self.Tauthor.setStyleSheet('color: White')

        self.bmenu = QtWidgets.QPushButton(self.centralwidget)
        self.bmenu.setStyleSheet(Style.menu_button)
        self.bmenu.setFixedSize(100,40)
        self.bmenu.move(0,0)
        self.bmenu.setIcon(QIcon("images/menu.png"))

        self.bhome = QtWidgets.QPushButton(self.centralwidget)
        self.bhome.setStyleSheet(Style.menu_button)
        self.bhome.setFixedSize(100,100)
        self.bhome.move(0,40)
        self.bhome.setIcon(QIcon("images/home.png"))
        self.bhome.setIconSize(QSize(40, 40));
        self.bhome.clicked.connect(self.home)

        self.badd = QtWidgets.QPushButton(self.centralwidget)
        self.badd.setStyleSheet(Style.menu_button)
        self.badd.setFixedSize(100,100)
        self.badd.move(0,140)
        self.badd.setIcon(QIcon("images/add.png"))
        self.badd.setIconSize(QSize(40, 40));
        self.badd.clicked.connect(self.add)

        self.badd1 = QtWidgets.QPushButton(self.centralwidget)
        self.badd1.setStyleSheet(Style.menu_button)
        self.badd1.setFixedSize(100,100)
        self.badd1.move(0,340)
        self.badd1.setIcon(QIcon("images/add_1.png"))
        self.badd1.setIconSize(QSize(40, 40));
        #self.badd1.clicked.connect(self.add1)

        self.b_setting = QtWidgets.QPushButton(self.centralwidget)
        self.b_setting.setStyleSheet(Style.active_menu_button)
        self.b_setting.setFixedSize(100,100)
        self.b_setting.move(0,240)
        self.b_setting.setIcon(QIcon("images/settings_1.png"))
        self.b_setting.setIconSize(QSize(40, 40));
        self.b_setting.clicked.connect(self.settings)

        self.bexit = QtWidgets.QPushButton(self.centralwidget)
        self.bexit.setStyleSheet(Style.exit_button)
        self.bexit.setIcon(QIcon("cross.png"))
        self.bexit.move(984, 0)
        self.bexit.resize(40,40)
        self.bexit.clicked.connect(self.exit_onclick)

        self.setCentralWidget(self.centralwidget)
        self.old_Pos = None
        self.show()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(79, 87, 101),  0.5, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(79, 87, 101), Qt.SolidPattern))
        painter.drawRoundedRect(0, 0, 1024, 768,0,0)
        painter.setPen(QPen(QColor(37, 42, 49),  0.5, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(37, 42, 49), Qt.SolidPattern))
        painter.drawRoundedRect(101, 0, 923, 40,0,0)
        painter.setPen(QPen(QColor(37, 42, 49),  0.5, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(37, 42, 49), Qt.SolidPattern))
        painter.drawRoundedRect(0, 0, 100, 768,0,0)
        painter.setPen(QPen(QColor(37, 42, 49),  0.5, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(37, 42, 49), Qt.SolidPattern))
        painter.drawRoundedRect(101, 743, 923, 25,0,0)
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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
    @pyqtSlot()
    def checkdb(self):
        self.myclass.Check_Db_Status()
        if self.myclass.Db_Status==1: 
            self.pcheckdb.setPixmap(QtGui.QPixmap("images/check.png"))
            self.tcheckdb.setText("Veritabanına Bağlanıldı.")
        elif self.myclass.Db_Status==-1:
            self.pcheckdb.setPixmap(QtGui.QPixmap("images/close.png"))
            self.tcheckdb.setText("Veritabanına Bağlanılamadı.")
        elif self.myclass.Db_Status==0:
            self.pcheckdb.setPixmap(QtGui.QPixmap("images/close.png"))
            self.tcheckdb.setText("Bağlantı var.Gerekli tabloları oluşturunuz.")
        else:
            self.pcheckdb.setPixmap(QtGui.QPixmap("images/close.png"))
            self.tcheckdb.setText("Hata! Veritabanı bağlantısını kontrol ediniz.")

    def get_ders_tocombo(self):
        if self.myclass.Db_Status != 1:
            return
        self.List_Ders=self.myclass.Ders_get_all()
        if len(self.List_Ders) >= 1:
            for i in self.List_Ders:
                self.f2_t2_cbders.addItem(i[1],i[0])
            self.f2_t1_tabw_cbders.clear()
            self.mirror_derscombo(self.f2_t1_tabw_cbders)
        else:
            self.f2_t2_cbders.addItem("Ders Ekleyiniz..")
        
    def mirror_derscombo(self,x):
        for i in self.List_Ders:
            x.addItem(i[1],i[0])
    def get_konu_tocombo(self):
        if self.myclass.Db_Status == 1 and len(self.List_Ders)>=1:
            self.List_Ders_Konu=self.myclass.Konu_get(self.f2_t2_cbders.currentData())
            if len(self.List_Ders_Konu) >= 1:
                for i in self.List_Ders_Konu:
                    self.f2_t2_cbkonu.addItem(i[1])
            else:
            	self.f2_t2_cbkonu.addItem("Konu Ekleyiniz")
    def ders_ekle(self):
        if self.tbuser1.text() != None:
            self.myclass.Ders_insert(self.tbuser1.text())
            self.f2_t2_cbders.clear()
            self.get_ders_tocombo()
            self.fill_table_ders()
    		
    def ders_ara(self):
        self.f1_t1_table.clear()
        self.f1_t1_table.setHorizontalHeaderLabels(["ID","Ders Adı"])
        self.List_Ders=self.myclass.Ders_search(self.f1_t1_tabw_tbara.text())
        self.fill_table_ders()
    def konu_ara(self):
        self.f2_t1_table.clear()
        self.f2_t1_table.setHorizontalHeaderLabels(["ID","Ders Adı","Donem","Konu Adı"])
        self.List_Konu=self.myclass.Konu_search(self.f2_t1_tabw_tbara.text())
        self.f2_t1_table.setRowCount(len(self.List_Konu)+1)
        if len(self.List_Konu)>=1:
            for i in range(len(self.List_Konu)):
                x=QtWidgets.QTableWidgetItem(str(self.List_Konu[i][0]) )
                x.setForeground(QBrush(QColor(255, 255, 255)))
                self.f2_t1_table.setItem(i , 0 , x)
                x=QtWidgets.QTableWidgetItem(str(self.List_Konu[i][1]) )
                x.setForeground(QBrush(QColor(255, 255, 255)))
                self.f2_t1_table.setItem(i , 1 , x )
                if self.List_Konu[i][2]==0:
                	x=QtWidgets.QTableWidgetItem("Vize")
                else:
                	x=QtWidgets.QTableWidgetItem("Final")
                x.setForeground(QBrush(QColor(255, 255, 255)))
                self.f2_t1_table.setItem(i , 2 , x )
                x=QtWidgets.QTableWidgetItem(str(self.List_Konu[i][3]) )
                x.setForeground(QBrush(QColor(255, 255, 255)))
                self.f2_t1_table.setItem(i , 3 , x )
    def fill_table_ders(self):
    	if len(self.List_Ders)>=1:
    		for i in range(len(self.List_Ders)):
    			x=QtWidgets.QTableWidgetItem(str(self.List_Ders[i][0]) )
    			#x.setTextAlignment(Qt.AlignHCenter)
    			x.setForeground(QBrush(QColor(255, 255, 255)))
    			self.f1_t1_table.setItem(i , 0 , x)
    			x=QtWidgets.QTableWidgetItem(str(self.List_Ders[i][1]) )
    			x.setForeground(QBrush(QColor(255, 255, 255)))
    			self.f1_t1_table.setItem(i , 1 , x )
    def fill_table_konu(self):
    	self.List_Konu=self.myclass.Konu_get_all()
    	self.f2_t1_table.setRowCount(len(self.List_Konu)+1)
    	#print(self.List_Konu[0][2])
    	if len(self.List_Konu)>=1:
    		for i in range(len(self.List_Konu)):
    			#print(i)
    			x=QtWidgets.QTableWidgetItem(str(self.List_Konu[i][0]) )
    			x.setForeground(QBrush(QColor(255, 255, 255)))
    			self.f2_t1_table.setItem(i , 0 , x)
    			x=QtWidgets.QTableWidgetItem(str(self.List_Konu[i][1]) )
    			x.setForeground(QBrush(QColor(255, 255, 255)))
    			self.f2_t1_table.setItem(i , 1 , x )

    			if self.List_Konu[i][2]==0:
    				x=QtWidgets.QTableWidgetItem("Vize")
    			else:
    				x=QtWidgets.QTableWidgetItem("Final")
    			x.setForeground(QBrush(QColor(255, 255, 255)))
    			self.f2_t1_table.setItem(i , 2 , x )
    			x=QtWidgets.QTableWidgetItem(str(self.List_Konu[i][3]) )
    			x.setForeground(QBrush(QColor(255, 255, 255)))
    			self.f2_t1_table.setItem(i , 3 , x )
    def guncelle(self):
    	if self.f1_t1_table.item(self.f1_t1_table.currentRow(),0) != None:
    		self.f1_tab1_tabw_tbupdate_id.setText(self.f1_t1_table.item(self.f1_t1_table.currentRow(),0).text())
    		self.f1_tab1_tabw_tbupdate_name.setText(self.f1_t1_table.item(self.f1_t1_table.currentRow(),1).text())
    def guncelle_konu(self):
        if self.f2_t1_table.item(self.f2_t1_table.currentRow(),0) != None:
            self.f2_tab1_tabw_tbupdate_id.setText(self.f2_t1_table.item(self.f2_t1_table.currentRow(),0).text())
    def ders_guncelle(self):
    	if self.f1_t1_table.item(self.f1_t1_table.currentRow(),0) != None and self.f1_t1_table.item(self.f1_t1_table.currentRow(),1) != None:
    		self.myclass.Ders_update(self.f1_tab1_tabw_tbupdate_id.text(),self.f1_tab1_tabw_tbupdate_name.text())
    		self.f2_t2_cbders.clear()
    		self.get_ders_tocombo()
    		self.fill_table_ders()
    def konu_ekle(self):
    	if self.f2_t1_tabw_name.text() == None:
    		return "error"
    	else:
    		self.myclass.Konu_insert(self.f2_t1_tabw_cbders.currentData(),self.f2_t1_tabw_cbdonem.currentData(),self.f2_t1_tabw_name.text())
    		self.fill_table_konu()
    def exit_onclick(self):
        quit()
    @pyqtSlot()
    def Write_Config(self):
        self.myclass.Host=self.tb_ip.text()
        self.myclass.User=self.tb_user.text()
        self.myclass.Pw=self.tb_pass.text()
        self.myclass.Create_Config()
        self.myclass.Get_Config()
        self.checkdb()
    def combo(self):
    	print("changed")
    	self.f2_t2_cbkonu.clear()

    	self.get_konu_tocombo()
    def home(self):
        self.mytabs.setCurrentIndex(1)
        self.bhome.setStyleSheet(Style.active_menu_button)
        self.b_setting.setStyleSheet(Style.menu_button)
        self.badd.setStyleSheet(Style.menu_button)
    def settings(self):
        self.mytabs.setCurrentIndex(0)
        self.b_setting.setStyleSheet(Style.active_menu_button)
        self.badd.setStyleSheet(Style.menu_button)
        self.bhome.setStyleSheet(Style.menu_button)
    def add(self):
        self.mytabs.setCurrentIndex(2)
        self.bhome.setStyleSheet(Style.menu_button)
        self.b_setting.setStyleSheet(Style.menu_button)
        self.badd.setStyleSheet(Style.active_menu_button)
        if self.f2_t2_cbders.count()==0 and self.f2_t2_cbkonu.count()==0:
        	self.get_ders_tocombo()
        	self.get_konu_tocombo()
        	self.fill_table_ders()
        	self.fill_table_konu()
    def show_onclick(self):
        if self.tbpass.echoMode()==QLineEdit.Normal:
            self.tbpass.setEchoMode(QLineEdit.Password)
        else:
            self.tbpass.setEchoMode(QLineEdit.Normal)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow(MainWindow)
sys.exit(app.exec_())