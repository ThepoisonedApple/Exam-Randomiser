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
from threading import Thread

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
		self.setCentralWidget(self.centralwidget)

		self.myclass=Db_Class()

#region maintabs ve barlar

		self.maintabs=QTabWidget(self.centralwidget)
		self.maintabs.setGeometry(QRect(100, 40, 924, 703))
		self.maintabs.setStyleSheet(Style.tabstyle)

		self.home = QWidget() 
		self.addQ = QWidget()
		self.addLS = QWidget() 
		self.settings = QWidget() 

		self.maintabs.addTab(self.home, "Home") 
		self.maintabs.addTab(self.addQ, "Soru ekle")
		self.maintabs.addTab(self.addLS, "Ders ve konu ekle")
		self.maintabs.addTab(self.settings, "Settings")
		self.maintabs.setTabVisible(0,False)
		self.maintabs.setTabVisible(1,False)
		self.maintabs.setTabVisible(2,False)
		self.maintabs.setTabVisible(3,False)
		self.maintabs.setCurrentIndex(0)

		self.menubar=QWidget(self.centralwidget)
		self.menubar.setFixedSize(100, 768)
		self.menubar.setStyleSheet("background:rgb(37, 42, 49)")

		self.topbar=QWidget(self.centralwidget)
		self.topbar.move(100,0)
		self.topbar.setFixedSize(924,40)
		self.topbar.setStyleSheet("background:rgb(37, 42, 49)")

		self.bottombar=QWidget(self.centralwidget)
		self.bottombar.move(100,743)
		self.bottombar.setFixedSize(924,25)
		self.bottombar.setStyleSheet("background:rgb(37, 42, 49)")
#endregion

#region topbar 

		self.b_exit = QtWidgets.QPushButton(self.topbar)
		self.b_exit.setStyleSheet(Style.exit_button)
		self.b_exit.setIcon(QIcon("cross.png"))
		self.b_exit.setGeometry(QRect(884,0,40,40))
		self.b_exit.clicked.connect(self.exit_onclick)

		self.p_icon = QtWidgets.QLabel(self.topbar)
		self.p_icon.setGeometry(QRect(5, 5, 30, 30))
		self.p_icon.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.p_icon.setText("")
		self.p_icon.setScaledContents(True)
		self.p_icon.setPixmap(QtGui.QPixmap("images/exam.png"))

		self.t_icon = QtWidgets.QLabel(self.topbar)
		self.t_icon.setGeometry(QRect(40, 5, 200, 30))
		self.t_icon.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.t_icon.setText("Exam Randomiser  v0.1.0")
		self.t_icon.setFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
		self.t_icon.setStyleSheet('color: White')
#endregion

#region menubar buttons
		self.isextended=0
		self.b_extendmenu = QtWidgets.QPushButton(self.menubar)
		self.b_extendmenu.setStyleSheet(Style.menu_button)
		self.b_extendmenu.setGeometry(QRect(0, 0, 100, 40))
		self.b_extendmenu.setIcon(QIcon("images/menu.png"))
		self.b_extendmenu.clicked.connect(self.extend)	

		self.b_home = QtWidgets.QPushButton(self.menubar)
		self.b_home.setStyleSheet(Style.active_menu_button)
		self.b_home.setGeometry(QRect(0, 40, 100, 100))
		self.b_home.setIcon(QIcon("images/home.png"))
		self.b_home.setIconSize(QSize(40, 40));
		self.b_home.setFont(QtGui.QFont("Verdana", 9, QtGui.QFont.Bold))
		self.b_home.clicked.connect(self.b_home_onclick)

		self.b_addQ = QtWidgets.QPushButton(self.menubar)
		self.b_addQ.setStyleSheet(Style.menu_button)
		self.b_addQ.setGeometry(QRect(0,140,100,100))
		self.b_addQ.setIcon(QIcon("images/add.png"))
		self.b_addQ.setIconSize(QSize(40, 40));
		self.b_addQ.setFont(QtGui.QFont("Verdana", 9, QtGui.QFont.Bold))
		self.b_addQ.clicked.connect(self.b_addQ_onclick)

		self.b_addLS = QtWidgets.QPushButton(self.menubar)
		self.b_addLS.setStyleSheet(Style.menu_button)
		self.b_addLS.setGeometry(QRect(0,240,100,100))
		self.b_addLS.setIcon(QIcon("images/add_1.png"))
		self.b_addLS.setIconSize(QSize(40, 40));
		self.b_addLS.setFont(QtGui.QFont("Verdana", 9, QtGui.QFont.Bold))
		self.b_addLS.clicked.connect(self.b_addLS_onclick)

		self.b_setting = QtWidgets.QPushButton(self.menubar)
		self.b_setting.setStyleSheet(Style.menu_button)
		self.b_setting.setGeometry(QRect(0,340,100,100))
		self.b_setting.setIcon(QIcon("images/settings_1.png"))
		self.b_setting.setIconSize(QSize(40, 40));
		self.b_setting.setFont(QtGui.QFont("Verdana", 9, QtGui.QFont.Bold))
		self.b_setting.clicked.connect(self.b_setting_onclick)
#endregion

#region bottombar

		self.p_checkdb = QtWidgets.QLabel(self.bottombar)
		self.p_checkdb.setGeometry(QtCore.QRect(4, 3, 20, 20))
		self.p_checkdb.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.p_checkdb.setText("")
		self.p_checkdb.setScaledContents(True)
		self.p_checkdb.setPixmap(QtGui.QPixmap("images/close.png"))

		self.t_checkdb = QtWidgets.QLabel(self.bottombar)
		self.t_checkdb.setGeometry(QtCore.QRect(28, 3, 400, 20))
		self.t_checkdb.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.t_checkdb.setText("Veritabanına Bağlanılıyor..")
		self.t_checkdb.setFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
		self.t_checkdb.setStyleSheet('color: White')

		self.t_author = QtWidgets.QLabel(self.bottombar)
		self.t_author.setGeometry(QtCore.QRect(658, 2, 300, 20))
		self.t_author.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.t_author.setText("Created by:Muhammed Ali ERDURAN")
		self.t_author.setFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
		self.t_author.setStyleSheet('color: White')

		self.checkdb()
		timer = QtCore.QTimer(self, timeout=self.checkdb, interval=6000)
		timer.start()
#endregion

#region tab=0 home page

		self.tcheckdb = QtWidgets.QLabel(self.home)
		self.tcheckdb.setGeometry(QtCore.QRect(300, 200, 400, 400))
		self.tcheckdb.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.tcheckdb.setText("Home")
		self.tcheckdb.setObjectName("tcheckdb")
		self.tcheckdb.setFont(QtGui.QFont("Verdana", 30, QtGui.QFont.Bold))
		self.tcheckdb.setStyleSheet('color: White')
#endregion

#region tab=1 soru ekle-düzenle page

		self.addQ_topframe=QtWidgets.QFrame(self.addQ)
		self.addQ_topframe.move(10,10)
		self.addQ_topframe.setFixedSize(904,353)
		self.addQ_topframe.setStyleSheet(Style.all_style)

		self.addQ_bottomtabs=QtWidgets.QTabWidget(self.addQ)
		self.addQ_bottomtabs.move(10,373)
		self.addQ_bottomtabs.setFixedSize(904,318)
		self.addQ_bottomtabs.setStyleSheet(Style.all_style)

		self.addQ_insert = QWidget() 
		self.addQ_update = QWidget() 

		self.addQ_bottomtabs.addTab(self.addQ_insert,"EKLE")
		self.addQ_bottomtabs.addTab(self.addQ_update,"GÜNCELLE")
		self.addQ_insert.setStyleSheet(Style.all_style)

		self.Q_table = QtWidgets.QTableWidget(self.addQ_topframe)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Q_table.sizePolicy().hasHeightForWidth())
		self.Q_table.setSizePolicy(sizePolicy)
		self.Q_table.setGeometry(QRect(10,10,884,300))
		self.Q_table.setFont(QtGui.QFont("Verdana", 9))
		self.Q_table.horizontalHeader().setStyleSheet("color:White")
		self.Q_table.setStyleSheet(Style.table_style)
		self.Q_table.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.Q_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.Q_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.Q_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.Q_table.setAlternatingRowColors(False)
		self.Q_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.Q_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.Q_table.setShowGrid(True)
		self.Q_table.setGridStyle(QtCore.Qt.SolidLine)
		self.Q_table.setColumnCount(4)
		self.Q_table.setRowCount(100)
		self.Q_table.horizontalHeader().setVisible(True)
		self.Q_table.horizontalHeader().setCascadingSectionResizes(True)
		self.Q_table.horizontalHeader().setDefaultSectionSize(200)
		self.Q_table.horizontalHeader().setStretchLastSection(True)
		self.Q_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
		self.Q_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
		self.Q_table.verticalHeader().setVisible(False)
		self.Q_table.verticalHeader().setCascadingSectionResizes(False)
		self.Q_table.verticalHeader().setHighlightSections(False)
		self.Q_table.verticalHeader().setStretchLastSection(True)
		self.Q_table.setHorizontalHeaderLabels(["ID","Ders Adı","Konu Adı","Soru"])
		self.Q_table.setColumnHidden(0,True)
		self.Q_table.setSortingEnabled(True)
	#region search question

		self.addQ_s_lsoru=QtWidgets.QLabel(self.addQ_topframe)
		self.addQ_s_lsoru.setGeometry(QtCore.QRect(10, 312, 120, 35))
		self.addQ_s_lsoru.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addQ_s_lsoru.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addQ_s_lsoru.setStyleSheet("color:White;")
		self.addQ_s_lsoru.setText("Soru içeriği:")
		self.addQ_s_lsoru.setScaledContents(True)
		self.addQ_s_lsoru.setObjectName("addQ_s_lsoru")

		self.addQ_s_tbsoru = QtWidgets.QLineEdit(self.addQ_topframe)
		self.addQ_s_tbsoru.setGeometry(QtCore.QRect(135, 315, 250, 30))
		self.addQ_s_tbsoru.setPlaceholderText("Soru içeriği..")
		self.addQ_s_tbsoru.setFocusPolicy(Qt.StrongFocus)
		self.addQ_s_tbsoru.setFont(QtGui.QFont("Verdana", 10))
		self.addQ_s_tbsoru.setStyleSheet(Style.lineedit_style)

		self.addQ_s_lkonu=QtWidgets.QLabel(self.addQ_topframe)
		self.addQ_s_lkonu.setGeometry(QtCore.QRect(400, 312, 90, 35))
		self.addQ_s_lkonu.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addQ_s_lkonu.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addQ_s_lkonu.setStyleSheet("color:White;")
		self.addQ_s_lkonu.setText("konu:")
		self.addQ_s_lkonu.setScaledContents(True)
		self.addQ_s_lkonu.setObjectName("addQ_s_lkonu")

		self.addQ_s_tbkonu = QtWidgets.QLineEdit(self.addQ_topframe)
		self.addQ_s_tbkonu.setGeometry(QtCore.QRect(465, 315, 250, 30))
		self.addQ_s_tbkonu.setPlaceholderText("konu adı..")
		self.addQ_s_tbkonu.setFocusPolicy(Qt.StrongFocus)
		self.addQ_s_tbkonu.setFont(QtGui.QFont("Verdana", 10))
		self.addQ_s_tbkonu.setStyleSheet(Style.lineedit_style)	

		self.addQ_i_binsert = QtWidgets.QPushButton(self.addQ_topframe)
		self.addQ_i_binsert.setGeometry(QRect(750,315,70,30))
		self.addQ_i_binsert.setStyleSheet(Style.ok_button)
		self.addQ_i_binsert.setText("Ara")
		#self.addQ_i_binsert.clicked.connect(self.Soru_ekle)

	#endregion
	#region insert question
		self.addQ_i_cbders = QtWidgets.QComboBox(self.addQ_insert)
		self.addQ_i_cbders.setGeometry(QRect(20,10,200,35))
		self.addQ_i_cbders.setFont(QtGui.QFont("Verdana", 9))
		self.addQ_i_cbders.setAutoFillBackground(False)
		self.addQ_i_cbders.setIconSize(QtCore.QSize(16, 16))
		self.addQ_i_cbders.setFrame(True)
		self.addQ_i_cbders.setStyleSheet(Style.combobox_style)
		self.addQ_i_cbders.activated['int'].connect(self.activated_addQ_i_cbders)

		self.addQ_i_cbkonu = QtWidgets.QComboBox(self.addQ_insert)
		self.addQ_i_cbkonu.setGeometry(QRect(285,10,200,35))
		self.addQ_i_cbkonu.setFont(QtGui.QFont("Verdana", 9))
		self.addQ_i_cbkonu.setAutoFillBackground(False)
		self.addQ_i_cbkonu.setStyleSheet(Style.combobox_style)
		self.addQ_i_cbkonu.setIconSize(QtCore.QSize(16, 16))
		self.addQ_i_cbkonu.setFrame(True)

		self.addQ_i_tbsoru = QtWidgets.QPlainTextEdit(self.addQ_insert)
		self.addQ_i_tbsoru.setGeometry(QRect(20, 60 ,700 ,210))
		self.addQ_i_tbsoru.setPlaceholderText("Ders ve Konuyu seçtikten sonra sorunuzu bu kısma yazınız..")
		self.addQ_i_tbsoru.setFocusPolicy(Qt.StrongFocus)
		self.addQ_i_tbsoru.setFont(QtGui.QFont("Verdana", 11))
		self.addQ_i_tbsoru.setStyleSheet(Style.plaintextedit_style)

		self.addQ_i_binsert = QtWidgets.QPushButton(self.addQ_insert)
		self.addQ_i_binsert.setGeometry(QRect(740,200,100,100))
		self.addQ_i_binsert.setStyleSheet(Style.ok_button)
		self.addQ_i_binsert.setText("ok")
		self.addQ_i_binsert.clicked.connect(self.Soru_ekle)
	#endregion
	#region update question
		
		self.Q_table.itemSelectionChanged.connect(self.fill_addQ_updatetab)

		self.addQ_u_tbid=QLineEdit(self.addQ_update)
		self.addQ_u_tbid.setGeometry(QRect(20,10,80,35))
		self.addQ_u_tbid.setFocusPolicy(Qt.StrongFocus)
		self.addQ_u_tbid.setFont(QtGui.QFont("Verdana", 11))
		self.addQ_u_tbid.setStyleSheet(Style.lineedit_style)
		self.addQ_u_tbid.setReadOnly(True)

		self.addQ_u_cbders = QtWidgets.QComboBox(self.addQ_update)
		self.addQ_u_cbders.setGeometry(QRect(120,10,200,35))
		self.addQ_u_cbders.setFont(QtGui.QFont("Verdana", 9))
		self.addQ_u_cbders.setAutoFillBackground(False)
		self.addQ_u_cbders.setIconSize(QtCore.QSize(16, 16))
		self.addQ_u_cbders.setFrame(True)
		self.addQ_u_cbders.setStyleSheet(Style.combobox_style)
		self.addQ_u_cbders.activated['int'].connect(self.activated_addQ_u_cbders)

		self.addQ_u_cbkonu = QtWidgets.QComboBox(self.addQ_update)
		self.addQ_u_cbkonu.setGeometry(QRect(385,10,200,35))
		self.addQ_u_cbkonu.setFont(QtGui.QFont("Verdana", 9))
		self.addQ_u_cbkonu.setAutoFillBackground(False)
		self.addQ_u_cbkonu.setStyleSheet(Style.combobox_style)
		self.addQ_u_cbkonu.setIconSize(QtCore.QSize(16, 16))
		self.addQ_u_cbkonu.setFrame(True)

		self.addQ_u_tbsoru = QtWidgets.QPlainTextEdit(self.addQ_update)
		self.addQ_u_tbsoru.setGeometry(QRect(20, 60 ,700 ,210))
		self.addQ_u_tbsoru.setFocusPolicy(Qt.StrongFocus)
		self.addQ_u_tbsoru.setFont(QtGui.QFont("Verdana", 11))
		self.addQ_u_tbsoru.setStyleSheet(Style.plaintextedit_style)

		self.addQ_u_binsert = QtWidgets.QPushButton(self.addQ_update)
		self.addQ_u_binsert.setGeometry(QRect(740,200,100,100))
		self.addQ_u_binsert.setStyleSheet(Style.ok_button)
		self.addQ_u_binsert.setText("ok")
		self.addQ_u_binsert.clicked.connect(self.soru_guncelle)

	#endregion
#endregion


#region tab=2 ders-konu ekle-düzenle page

	#region ders
		self.addL_frame=QtWidgets.QFrame(self.addLS)
		self.addL_frame.setGeometry(QRect(10,10,420,318))
		self.addL_frame.setStyleSheet(Style.all_style)

		self.addL_tabs=QtWidgets.QTabWidget(self.addLS)
		self.addL_tabs.move(450,10)
		self.addL_tabs.setFixedSize(454,318)
		self.addL_tabs.setStyleSheet(Style.all_style)

		self.addL_insterttab = QWidget() 
		self.addL_updatetab = QWidget()
		self.addL_searchtab = QWidget()  

		self.addL_tabs.addTab(self.addL_searchtab,"Ara")
		self.addL_tabs.addTab(self.addL_insterttab,"EKLE")
		self.addL_tabs.addTab(self.addL_updatetab,"GÜNCELLE")
		self.addL_tabs.setStyleSheet(Style.all_style)
		self.addL_tabs.setTabPosition(3)

		self.L_table = QtWidgets.QTableWidget(self.addL_frame)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.L_table.sizePolicy().hasHeightForWidth())
		self.L_table.setSizePolicy(sizePolicy)
		self.L_table.setFixedSize(400,300)
		self.L_table.move(10,10)
		self.L_table.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
		self.L_table.horizontalHeader().setStyleSheet("color:White")
		self.L_table.setStyleSheet(Style.table_style)
		self.L_table.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.L_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.L_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.L_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.L_table.setAlternatingRowColors(False)
		self.L_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.L_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.L_table.setShowGrid(True)
		self.L_table.setGridStyle(QtCore.Qt.SolidLine)
		self.L_table.setObjectName("L_table")
		self.L_table.setColumnCount(2)
		self.L_table.setRowCount(100)
		self.L_table.horizontalHeader().setVisible(True)
		self.L_table.horizontalHeader().setCascadingSectionResizes(True)
		self.L_table.horizontalHeader().setDefaultSectionSize(200)
		self.L_table.horizontalHeader().setStretchLastSection(True)
		self.L_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
		self.L_table.setHorizontalHeaderLabels(["ID","Ders Adı"])
		self.L_table.verticalHeader().setVisible(False)
		self.L_table.verticalHeader().setCascadingSectionResizes(False)
		self.L_table.verticalHeader().setHighlightSections(False)
		self.L_table.verticalHeader().setStretchLastSection(True)
		self.L_table.setSortingEnabled(True)
		self.L_table.setColumnHidden(0, True);
		#region ders ara

		self.addL_searchtab_icon = QtWidgets.QLabel(self.addL_searchtab)
		self.addL_searchtab_icon.setGeometry(QtCore.QRect(100, 30, 75, 75))
		self.addL_searchtab_icon.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addL_searchtab_icon.setText("")
		self.addL_searchtab_icon.setScaledContents(True)
		self.addL_searchtab_icon.setObjectName("addL_searchtab_icon")
		self.addL_searchtab_icon.setPixmap(QtGui.QPixmap("images/search.png"))

		self.addL_searchtab_label=QtWidgets.QLabel(self.addL_searchtab)
		self.addL_searchtab_label.setGeometry(QtCore.QRect(200, 50, 200, 45))
		self.addL_searchtab_label.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addL_searchtab_label.setFont(QtGui.QFont("Verdana", 15,QtGui.QFont.Bold))
		self.addL_searchtab_label.setStyleSheet("color:White;")
		self.addL_searchtab_label.setText("Ders Ara")
		self.addL_searchtab_label.setScaledContents(True)
		self.addL_searchtab_label.setObjectName("addL_searchtab_label")

		self.addL_searchtab_tbara=QLineEdit(self.addL_searchtab)
		self.addL_searchtab_tbara.move(100, 200)
		self.addL_searchtab_tbara.resize(200,35)
		self.addL_searchtab_tbara.setFocusPolicy(Qt.StrongFocus)
		self.addL_searchtab_tbara.setFont(QtGui.QFont("Verdana", 11))
		self.addL_searchtab_tbara.setStyleSheet(Style.lineedit_style)
		self.addL_searchtab_tbara.textEdited.connect(self.ders_ara)	

		self.addL_searchtab_bara = QtWidgets.QPushButton(self.addL_searchtab)
		self.addL_searchtab_bara.setStyleSheet(Style.borderless_button)
		self.addL_searchtab_bara.setFixedSize(35,35)
		self.addL_searchtab_bara.move(300,200)
		self.addL_searchtab_bara.setIcon(QIcon("images/search.png"))
		self.addL_searchtab_bara.clicked.connect(self.ders_ara)		

		#endregion
		#region ders insert

		self.addL_insterttab_tbname = QtWidgets.QLineEdit(self.addL_insterttab)
		self.addL_insterttab_tbname.move(20, 60)
		self.addL_insterttab_tbname.resize(200,35)
		self.addL_insterttab_tbname.setPlaceholderText("Ders adını giriniz..")
		self.addL_insterttab_tbname.setFocusPolicy(Qt.StrongFocus)
		self.addL_insterttab_tbname.setFont(QtGui.QFont("Verdana", 11))
		self.addL_insterttab_tbname.setStyleSheet(Style.lineedit_style)	

		self.addL_insterttab_binsert = QtWidgets.QPushButton(self.addL_insterttab)
		self.addL_insterttab_binsert.setStyleSheet(Style.ok_button)
		self.addL_insterttab_binsert.setText("Ekle")
		self.addL_insterttab_binsert.setFixedSize(100,50)
		self.addL_insterttab_binsert.move(100,200)
		self.addL_insterttab_binsert.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
		self.addL_insterttab_binsert.clicked.connect(self.ders_ekle)

		#endregion
		#region ders update

		self.addL_updatetab_tbid=QLineEdit(self.addL_updatetab)
		self.addL_updatetab_tbid.move(10, 120)
		self.addL_updatetab_tbid.resize(200,35)
		self.addL_updatetab_tbid.setFocusPolicy(Qt.StrongFocus)
		self.addL_updatetab_tbid.setFont(QtGui.QFont("Verdana", 11))
		self.addL_updatetab_tbid.setStyleSheet(Style.lineedit_style)
		self.addL_updatetab_tbid.setReadOnly(True)

		self.addL_updatetab_tbname=QLineEdit(self.addL_updatetab)
		self.addL_updatetab_tbname.move(10, 170)
		self.addL_updatetab_tbname.resize(200,35)
		self.addL_updatetab_tbname.setFocusPolicy(Qt.StrongFocus)
		self.addL_updatetab_tbname.setFont(QtGui.QFont("Verdana", 11))
		self.addL_updatetab_tbname.setStyleSheet(Style.lineedit_style)

		self.L_table.itemSelectionChanged.connect(self.L_table_onselected)

		self.addL_updatetab_bupdate = QtWidgets.QPushButton(self.addL_updatetab)
		self.addL_updatetab_bupdate.setStyleSheet(Style.ok_button)
		self.addL_updatetab_bupdate.setFixedSize(35,35)
		self.addL_updatetab_bupdate.move(300,200)
		self.addL_updatetab_bupdate.setText("Güncelle")
		self.addL_updatetab_bupdate.clicked.connect(self.ders_guncelle)

		#endregion


	#endregion

	#region konu

		self.addS_frame=QtWidgets.QFrame(self.addLS)
		self.addS_frame.move(10,338)
		self.addS_frame.setFixedSize(495,353)
		self.addS_frame.setStyleSheet(Style.all_style)

		self.addS_tabs=QtWidgets.QTabWidget(self.addLS)
		self.addS_tabs.move(520,338)
		self.addS_tabs.setFixedSize(394,353)
		self.addS_tabs.setStyleSheet(Style.all_style)

		self.addS_inserttab = QWidget() 
		self.addS_updatetab = QWidget()
		self.addS_searchtab = QWidget()

		self.addS_tabs.addTab(self.addS_searchtab,"ARA")
		self.addS_tabs.addTab(self.addS_inserttab,"EKLE")
		self.addS_tabs.addTab(self.addS_updatetab,"GÜNCELLE")
		self.addS_tabs.setStyleSheet(Style.all_style)
		self.addS_tabs.setTabPosition(3)

		self.S_table = QtWidgets.QTableWidget(self.addS_frame)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.S_table.sizePolicy().hasHeightForWidth())
		self.S_table.setSizePolicy(sizePolicy)
		self.S_table.setFixedSize(475,335)
		self.S_table.move(10,10)
		self.S_table.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
		self.S_table.horizontalHeader().setStyleSheet("color:White")
		self.S_table.setStyleSheet(Style.table_style)
		self.S_table.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.S_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.S_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.S_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.S_table.setAlternatingRowColors(False)
		self.S_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.S_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.S_table.setShowGrid(True)
		self.S_table.setGridStyle(QtCore.Qt.SolidLine)
		self.S_table.setObjectName("S_table")
		self.S_table.setColumnCount(4)
		self.S_table.setRowCount(100)
		self.S_table.horizontalHeader().setVisible(True)
		self.S_table.horizontalHeader().setCascadingSectionResizes(True)
		self.S_table.horizontalHeader().setDefaultSectionSize(200)
		self.S_table.horizontalHeader().setStretchLastSection(True)
		self.S_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
		self.S_table.setHorizontalHeaderLabels(["ID","Ders Adı","Donem","Konu Adı"])
		self.S_table.verticalHeader().setVisible(False)
		self.S_table.verticalHeader().setCascadingSectionResizes(False)
		self.S_table.verticalHeader().setHighlightSections(False)
		self.S_table.verticalHeader().setStretchLastSection(True)
		self.S_table.setSortingEnabled(True)
		self.S_table.setColumnHidden(0, True);

		#region konu search
		self.addS_searchtab_tbara=QLineEdit(self.addS_searchtab)
		self.addS_searchtab_tbara.move(100, 200)
		self.addS_searchtab_tbara.resize(200,35)
		self.addS_searchtab_tbara.setFocusPolicy(Qt.StrongFocus)
		self.addS_searchtab_tbara.setFont(QtGui.QFont("Verdana", 11))
		self.addS_searchtab_tbara.setStyleSheet(Style.lineedit_style)
		self.addS_searchtab_tbara.textEdited.connect(self.konu_ara)	

		self.addS_searchtab_bara = QtWidgets.QPushButton(self.addS_searchtab)
		self.addS_searchtab_bara.setStyleSheet(Style.borderless_button)
		self.addS_searchtab_bara.setFixedSize(35,35)
		self.addS_searchtab_bara.move(300,200)
		self.addS_searchtab_bara.setIcon(QIcon("images/search.png"))
		self.addS_searchtab_bara.clicked.connect(self.konu_ara)
		#endregion

		#region konu insert

		self.addS_inserttab_cbders = QtWidgets.QComboBox(self.addS_inserttab)
		self.addS_inserttab_cbders.move(20,10)
		self.addS_inserttab_cbders.setFixedSize(200,35)
		self.addS_inserttab_cbders.setFont(QtGui.QFont("Verdana", 9))
		self.addS_inserttab_cbders.setAutoFillBackground(False)
		self.addS_inserttab_cbders.setStyleSheet(Style.combobox_style)
		self.addS_inserttab_cbders.setIconSize(QtCore.QSize(16, 16))
		self.addS_inserttab_cbders.setFrame(True)

		self.addS_inserttab_cbdonem = QtWidgets.QComboBox(self.addS_inserttab)
		self.addS_inserttab_cbdonem.move(20,60)
		self.addS_inserttab_cbdonem.setFixedSize(200,35)
		self.addS_inserttab_cbdonem.setFont(QtGui.QFont("Verdana", 9))
		self.addS_inserttab_cbdonem.setAutoFillBackground(False)
		self.addS_inserttab_cbdonem.setStyleSheet(Style.combobox_style)
		self.addS_inserttab_cbdonem.setIconSize(QtCore.QSize(16, 16))
		self.addS_inserttab_cbdonem.setFrame(True)
		self.addS_inserttab_cbdonem.addItem("Vize",0)
		self.addS_inserttab_cbdonem.addItem("Final",1)

		self.addS_inserttab_tbname=QLineEdit(self.addS_inserttab)
		self.addS_inserttab_tbname.move(10, 110)
		self.addS_inserttab_tbname.resize(200,35)
		self.addS_inserttab_tbname.setFocusPolicy(Qt.StrongFocus)
		self.addS_inserttab_tbname.setFont(QtGui.QFont("Verdana", 11))
		self.addS_inserttab_tbname.setStyleSheet(Style.lineedit_style)

		self.addS_inserttab_binsert = QtWidgets.QPushButton(self.addS_inserttab)
		self.addS_inserttab_binsert.setStyleSheet(Style.ok_button)
		self.addS_inserttab_binsert.setFixedSize(35,35)
		self.addS_inserttab_binsert.move(300,200)
		self.addS_inserttab_binsert.setText("ekle")
		self.addS_inserttab_binsert.clicked.connect(self.konu_ekle)

		#endregion

		#region konu update

		self.addS_updatetab_tbid=QLineEdit(self.addS_updatetab)
		self.addS_updatetab_tbid.move(10, 120)
		self.addS_updatetab_tbid.resize(200,35)
		self.addS_updatetab_tbid.setFocusPolicy(Qt.StrongFocus)
		self.addS_updatetab_tbid.setFont(QtGui.QFont("Verdana", 11))
		self.addS_updatetab_tbid.setStyleSheet(Style.lineedit_style)
		self.addS_updatetab_tbid.setReadOnly(True)

		self.addS_updatetab_cbders = QtWidgets.QComboBox(self.addS_updatetab)
		self.addS_updatetab_cbders.move(20,10)
		self.addS_updatetab_cbders.setFixedSize(200,35)
		self.addS_updatetab_cbders.setFont(QtGui.QFont("Verdana", 9))
		self.addS_updatetab_cbders.setAutoFillBackground(False)
		self.addS_updatetab_cbders.setStyleSheet(Style.combobox_style)
		self.addS_updatetab_cbders.setIconSize(QtCore.QSize(16, 16))
		self.addS_updatetab_cbders.setFrame(True)

		self.addS_updatetab_cbdonem = QtWidgets.QComboBox(self.addS_updatetab)
		self.addS_updatetab_cbdonem.move(20,60)
		self.addS_updatetab_cbdonem.setFixedSize(200,35)
		self.addS_updatetab_cbdonem.setFont(QtGui.QFont("Verdana", 9))
		self.addS_updatetab_cbdonem.setAutoFillBackground(False)
		self.addS_updatetab_cbdonem.setStyleSheet(Style.combobox_style)
		self.addS_updatetab_cbdonem.setIconSize(QtCore.QSize(16, 16))
		self.addS_updatetab_cbdonem.setFrame(True)
		self.addS_updatetab_cbdonem.addItem("Vize",0)
		self.addS_updatetab_cbdonem.addItem("Final",1)

		self.addS_updatetab_tbname=QLineEdit(self.addS_updatetab)
		self.addS_updatetab_tbname.move(10, 170)
		self.addS_updatetab_tbname.resize(200,35)
		self.addS_updatetab_tbname.setFocusPolicy(Qt.StrongFocus)
		self.addS_updatetab_tbname.setFont(QtGui.QFont("Verdana", 11))
		self.addS_updatetab_tbname.setStyleSheet(Style.lineedit_style)

		self.S_table.itemSelectionChanged.connect(self.fill_addS_updatetab)

		self.addS_updatetab_bupdate = QtWidgets.QPushButton(self.addS_updatetab)
		self.addS_updatetab_bupdate.setStyleSheet(Style.ok_button)
		self.addS_updatetab_bupdate.setFixedSize(35,35)
		self.addS_updatetab_bupdate.move(300,200)
		self.addS_updatetab_bupdate.setText("Güncelle")
		self.addS_updatetab_bupdate.clicked.connect(self.konu_guncelle)

		#endregion
	#endregion
#endregion


#region tab=3 settings page
		

		self.p_setting = QtWidgets.QLabel(self.settings)
		self.p_setting.setGeometry(QtCore.QRect(387, 20, 150, 150))
		self.p_setting.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.p_setting.setText("")
		self.p_setting.setScaledContents(True)
		self.p_setting.setObjectName("p_setting")
		self.p_setting.setPixmap(QtGui.QPixmap("images/settings.png"))

		self.t_setting = QtWidgets.QLabel(self.settings)
		self.t_setting.setGeometry(QtCore.QRect(387, 200, 185, 35))
		self.t_setting.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.t_setting.setText("Ayarlar")
		self.t_setting.setObjectName("t_setting")
		self.t_setting.setFont(QtGui.QFont("Verdana", 16, QtGui.QFont.Bold))
		self.t_setting.setStyleSheet('color: White;')

		self.setting_frame=QtWidgets.QFrame(self.settings)
		self.setting_frame.setGeometry(QtCore.QRect(175, 300, 500, 353))
		self.setting_frame.setStyleSheet(Style.all_style+Style.rounded_frame)

		self.setting_tip = QtWidgets.QLabel(self.setting_frame)
		self.setting_tip.setGeometry(QtCore.QRect(25, 25, 185, 35))
		self.setting_tip.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.setting_tip.setText("Veritabanı ip:")
		self.setting_tip.setObjectName("t_ip")
		self.setting_tip.setFont(QtGui.QFont("Verdana", 14, QtGui.QFont.Bold))
		self.setting_tip.setStyleSheet('color: White;')

		self.setting_tbip = QtWidgets.QLineEdit(self.setting_frame)
		self.setting_tbip.move(215, 25)
		self.setting_tbip.resize(240,35)
		self.setting_tbip.setFocusPolicy(Qt.StrongFocus)
		self.setting_tbip.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
		self.setting_tbip.setStyleSheet(Style.lineedit_style)
		self.setting_tbip.setText(self.myclass.Host)

		self.setting_tuser = QtWidgets.QLabel(self.setting_frame)
		self.setting_tuser.setGeometry(QtCore.QRect(25, 100, 185, 35))
		self.setting_tuser.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.setting_tuser.setText("Kullanıcı Adı:")
		self.setting_tuser.setObjectName("t_user")
		self.setting_tuser.setFont(QtGui.QFont("Verdana", 14, QtGui.QFont.Bold))
		self.setting_tuser.setStyleSheet('color: White;')

		self.setting_tbuser = QtWidgets.QLineEdit(self.setting_frame)
		self.setting_tbuser.move(215, 100)
		self.setting_tbuser.resize(240,35)
		self.setting_tbuser.setFocusPolicy(Qt.StrongFocus)
		self.setting_tbuser.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
		self.setting_tbuser.setStyleSheet(Style.lineedit_style)
		self.setting_tbuser.setText(self.myclass.User)

		self.setting_tpass = QtWidgets.QLabel(self.setting_frame)
		self.setting_tpass.setGeometry(QtCore.QRect(25, 175, 185, 35))
		self.setting_tpass.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.setting_tpass.setText("Şifre:")
		self.setting_tpass.setObjectName("t_pass")
		self.setting_tpass.setFont(QtGui.QFont("Verdana", 14, QtGui.QFont.Bold))
		self.setting_tpass.setStyleSheet('color: White;')

		self.setting_tbpass = QLineEdit(self.setting_frame)
		self.setting_tbpass.move(215, 175)
		self.setting_tbpass.resize(240,35)
		self.setting_tbpass.setEchoMode(QLineEdit.Password)
		self.setting_tbpass.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
		self.setting_tbpass.setStyleSheet(Style.lineedit_style)

		self.setting_bupdate = QtWidgets.QPushButton(self.setting_frame)
		self.setting_bupdate.setStyleSheet(Style.ok_button)
		self.setting_bupdate.setText("Onayla")
		self.setting_bupdate.setFixedSize(100,50)
		self.setting_bupdate.move(300,250)
		self.setting_bupdate.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
		self.setting_bupdate.clicked.connect(self.Write_Config)

#endregion


		self.old_Pos = None
		self.show()

#region çerçevesiz frame için gerekli fonksiyonlar 
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
	def exit_onclick(self):
		quit()
#endregion

#region menu buttons extend functions
	def extend(self):
		if self.isextended==0:
			self.menubar.setFixedSize(200,768)
			self.b_home.setFixedSize(200,100)
			self.b_home.setStyleSheet(Style.extended)
			self.b_home.setText(" Ana Sayfa")
			self.b_addQ.setFixedSize(200,100)
			self.b_addQ.setStyleSheet(Style.extended)
			self.b_addQ.setText(" Soru \n Ekle-Düzenle")
			self.b_addLS.setFixedSize(200,100)
			self.b_addLS.setStyleSheet(Style.extended)
			self.b_addLS.setText(" Ders ve Konu \n Ekle-Düzenle")
			self.b_setting.setFixedSize(200,100)
			self.b_setting.setStyleSheet(Style.extended)
			self.b_setting.setText(" Ayarlar")
			self.isextended=1
			if self.maintabs.currentIndex()==0:
				self.b_home.setStyleSheet(Style.extended_active)
			elif self.maintabs.currentIndex()==1:
				self.b_addQ.setStyleSheet(Style.extended_active)
			elif self.maintabs.currentIndex()==2:
				self.b_addLS.setStyleSheet(Style.extended_active)
			else:
				self.b_setting.setStyleSheet(Style.extended_active)
		else:
			self.unextend()
	def unextend(self):
		self.menubar.setFixedSize(100,768)
		self.b_home.setFixedSize(100,100)
		self.b_home.setStyleSheet(Style.menu_button)
		self.b_home.setText("")
		self.b_addQ.setFixedSize(100,100)
		self.b_addQ.setStyleSheet(Style.menu_button)
		self.b_addQ.setText("")
		self.b_addLS.setFixedSize(100,100)
		self.b_addLS.setStyleSheet(Style.menu_button)
		self.b_addLS.setText("")
		self.b_setting.setFixedSize(100,100)
		self.b_setting.setStyleSheet(Style.menu_button)
		self.b_setting.setText("")
		self.isextended=0
		if self.maintabs.currentIndex()==0:
			self.b_home.setStyleSheet(Style.active_menu_button)
		elif self.maintabs.currentIndex()==1:
			self.b_addQ.setStyleSheet(Style.active_menu_button)
		elif self.maintabs.currentIndex()==2:
			self.b_addLS.setStyleSheet(Style.active_menu_button)
		else:
			self.b_setting.setStyleSheet(Style.active_menu_button)
#endregion

#region db connection check functions
	def checkdb(self):
		if self.myclass.Db_Status!=1:
			self.p_checkdb.setPixmap(QtGui.QPixmap("images/loading.png"))
			self.t_checkdb.setText("Veritabanına Bağlanılıyor.")
		Thread(target=self.checkdb_1).start()

	def checkdb_1(self):
		self.myclass.Check_Db_Status()
		if self.myclass.Db_Status==1: 
			self.p_checkdb.setPixmap(QtGui.QPixmap("images/check.png"))
			self.t_checkdb.setText("Veritabanına Bağlanıldı.")
		elif self.myclass.Db_Status==-1:
			time.sleep(1)
			self.p_checkdb.setPixmap(QtGui.QPixmap("images/close.png"))
			self.t_checkdb.setText("Veritabanına Bağlanılamadı.")
		elif self.myclass.Db_Status==0:
			time.sleep(1)
			self.p_checkdb.setPixmap(QtGui.QPixmap("images/close.png"))
			self.t_checkdb.setText("Bağlantı var.Gerekli tabloları oluşturunuz.")
		else:
			time.sleep(1)
			self.p_checkdb.setPixmap(QtGui.QPixmap("images/close.png"))
			self.t_checkdb.setText("Hata! Veritabanı bağlantısını kontrol ediniz.")

	def Write_Config(self):
		self.myclass.Host=self.setting_tbip.text()
		self.myclass.User=self.setting_tbuser.text()
		self.myclass.Pw=self.setting_tbpass.text()
		self.myclass.Create_Config()
		self.myclass.Get_Config()
		self.checkdb()
#endregion

#region menu buttons tab pass functions

	def b_home_onclick(self):
		self.maintabs.setCurrentIndex(0)
		if self.isextended==1:
			self.unextend()
		self.b_home.setStyleSheet(Style.active_menu_button)
		self.b_addQ.setStyleSheet(Style.menu_button)
		self.b_addLS.setStyleSheet(Style.menu_button)
		self.b_setting.setStyleSheet(Style.menu_button)
	def b_addQ_onclick(self):
		self.maintabs.setCurrentIndex(1)
		if self.isextended==1:
			self.unextend()
		self.b_home.setStyleSheet(Style.menu_button)
		self.b_addQ.setStyleSheet(Style.active_menu_button)
		self.b_addLS.setStyleSheet(Style.menu_button)
		self.b_setting.setStyleSheet(Style.menu_button)
		if self.myclass.Db_Status==1:
			self.get_data()
			self.fill_table_soru_onstart()
			self.fill_cbders(self.addQ_i_cbders)
			self.fill_cbkonu(self.addQ_i_cbkonu,self.addQ_i_cbders)
			self.fill_cbders(self.addQ_u_cbders)
			self.fill_cbkonu(self.addQ_u_cbkonu,self.addQ_u_cbders)
	def b_addLS_onclick(self):
		self.maintabs.setCurrentIndex(2)
		if self.isextended==1:
			self.unextend()
		self.b_home.setStyleSheet(Style.menu_button)
		self.b_addQ.setStyleSheet(Style.menu_button)
		self.b_addLS.setStyleSheet(Style.active_menu_button)
		self.b_setting.setStyleSheet(Style.menu_button)
		if self.myclass.Db_Status==1:
			self.LStable_fillonstart()
			self.fill_cbders(self.addS_inserttab_cbders)
			self.fill_cbders(self.addS_updatetab_cbders)
	def b_setting_onclick(self):
		self.maintabs.setCurrentIndex(3)
		if self.isextended==1:
			self.unextend()
		self.b_home.setStyleSheet(Style.menu_button)
		self.b_addQ.setStyleSheet(Style.menu_button)
		self.b_addLS.setStyleSheet(Style.menu_button)
		self.b_setting.setStyleSheet(Style.active_menu_button)
#endregion

#region table fill functions
	def get_data(self):
		self.List_Ders=self.myclass.Ders_get_all()
		self.List_Konu=self.myclass.Konu_get_all()

	def LStable_fillonstart(self):
		self.get_data()
		self.fill_table_ders(self.List_Ders)
		self.fill_table_konu(self.List_Konu)

	def fill_table_ders(self,mylist):
		self.L_table.setSortingEnabled(False)
		self.L_table.setRowCount(len(mylist)+1)
		if len(mylist)>=1:
			for i in range(len(mylist)):
				x=QtWidgets.QTableWidgetItem(str(mylist[i][0]) )
				x.setForeground(QBrush(QColor(255, 255, 255)))
				self.L_table.setItem(i , 0 , x)
				x=QtWidgets.QTableWidgetItem(str(mylist[i][1]) )
				x.setForeground(QBrush(QColor(255, 255, 255)))
				self.L_table.setItem(i , 1 , x )
		self.L_table.setSortingEnabled(True)
	def fill_table_konu(self,mylist):
		self.S_table.setSortingEnabled(False)
		self.S_table.setRowCount(len(mylist)+1)
		if len(mylist)>=1:
			for i in range(len(mylist)):
				x=QtWidgets.QTableWidgetItem(str(mylist[i][0]) )
				x.setForeground(QBrush(QColor(255, 255, 255)))
				self.S_table.setItem(i , 0 , x)
				x=QtWidgets.QTableWidgetItem(str(mylist[i][1]) )
				x.setForeground(QBrush(QColor(255, 255, 255)))
				self.S_table.setItem(i , 1 , x )
				if mylist[i][2]==0:
					x=QtWidgets.QTableWidgetItem("Vize")
				else:
					x=QtWidgets.QTableWidgetItem("Final")
				x.setForeground(QBrush(QColor(255, 255, 255)))
				self.S_table.setItem(i , 2 , x )
				x=QtWidgets.QTableWidgetItem(str(mylist[i][3]) )
				x.setForeground(QBrush(QColor(255, 255, 255)))
				self.S_table.setItem(i , 3 , x )
		self.S_table.setSortingEnabled(True)
	def fill_table_soru(self,sorular):
		self.Q_table.setSortingEnabled(False)
		if len(sorular)>=1:
			self.Q_table.setRowCount(len(sorular)+1)
			for i in range(len(sorular)):
				x=QtWidgets.QTableWidgetItem(str(sorular[i][0]) )
				x.setForeground(QBrush(QColor(255, 255, 255)))
				self.Q_table.setItem(i , 0 , x)
				x=QtWidgets.QTableWidgetItem(str(sorular[i][1]) )
				x.setForeground(QBrush(QColor(255, 255, 255)))
				self.Q_table.setItem(i , 1 , x )
				x=QtWidgets.QTableWidgetItem(str(sorular[i][2]) )
				x.setForeground(QBrush(QColor(255, 255, 255)))
				self.Q_table.setItem(i , 2 , x)
				x=QtWidgets.QTableWidgetItem(str(sorular[i][3]) )
				x.setForeground(QBrush(QColor(255, 255, 255)))
				self.Q_table.setItem(i , 3 , x )
			del sorular
		self.Q_table.setSortingEnabled(True)
	def fill_table_soru_onstart(self):
		sorular=self.myclass.Soru_get_all()
		self.fill_table_soru(sorular)

#endregion

#region ders functions

	def L_table_onselected(self):
		if self.L_table.item(self.L_table.currentRow(),0) != None:
			self.addL_updatetab_tbid.setText(self.L_table.item(self.L_table.currentRow(),0).text())
			self.addL_updatetab_tbname.setText(self.L_table.item(self.L_table.currentRow(),1).text())

	def ders_ara(self):
		self.L_table.clear()
		self.L_table.setHorizontalHeaderLabels(["ID","Ders Adı"])
		Ders_searchresault=self.myclass.Ders_search(self.addL_searchtab_tbara.text())
		self.fill_table_ders(Ders_searchresault)

	def ders_guncelle(self):
		if self.L_table.item(self.L_table.currentRow(),0) != None and self.L_table.item(self.L_table.currentRow(),1) != None:
			self.myclass.Ders_update(self.addL_updatetab_tbid.text(),self.addL_updatetab_tbname.text())
			self.get_data()
			self.fill_table_ders(self.List_Ders)

	def ders_ekle(self):
		if self.addL_insterttab_tbname.text() != None:
			self.myclass.Ders_insert(self.addL_insterttab_tbname.text())
			self.get_data()
			self.fill_table_ders(self.List_Ders)
#endregion

#region konu functions

	def konu_ara(self):
		self.S_table.clear()
		self.S_table.setHorizontalHeaderLabels(["ID","Ders Adı","Donem","Konu Adı"])
		mylist=self.myclass.Konu_search(self.addS_searchtab_tbara.text())
		self.S_table.setRowCount(len(mylist)+1)
		self.fill_table_konu(mylist)

	def konu_ekle(self):
		if self.addS_inserttab_tbname.text() == None:
			return "error"
		else:
			self.myclass.Konu_insert(self.addS_inserttab_cbders.currentData(),self.addS_inserttab_cbdonem.currentData(),self.addS_inserttab_tbname.text())
			self.konu_ara()
	def fill_addS_updatetab(self):
		if self.S_table.item(self.S_table.currentRow(),0) != None:
			self.addS_updatetab_tbid.setText(self.S_table.item(self.S_table.currentRow(),0).text())
			if self.S_table.item(self.S_table.currentRow(),2).text()=="Final":
				self.addS_updatetab_cbdonem.setCurrentIndex(1)
			else:
				self.addS_updatetab_cbdonem.setCurrentIndex(0)
			x=self.addS_updatetab_cbders.findText(self.S_table.item(self.S_table.currentRow(),1).text())
			self.addS_updatetab_cbders.setCurrentIndex(x)
			self.addS_updatetab_tbname.setText(self.S_table.item(self.S_table.currentRow(),3).text())
	def konu_guncelle(self):
		if self.addS_updatetab_tbname.text() != "":
			self.myclass.Konu_update(self.addS_updatetab_tbid.text(),self.addS_updatetab_cbders.currentData(),self.addS_updatetab_cbdonem.currentData(),self.addS_updatetab_tbname.text())
			self.b_addLS_onclick()
#endregion

#region soru functions
	def Soru_ekle(self):
		self.myclass.Soru_insert(self.addQ_i_cbkonu.currentData(),self.addQ_i_tbsoru.toPlainText())
	def fill_addQ_updatetab(self):
		if self.Q_table.item(self.Q_table.currentRow(),0) != None:
			self.addQ_u_tbid.setText(self.Q_table.item(self.Q_table.currentRow(),0).text())
			x=self.addQ_u_cbders.findText(self.Q_table.item(self.Q_table.currentRow(),1).text())
			self.addQ_u_cbders.setCurrentIndex(x)
			self.fill_cbkonu(self.addQ_u_cbkonu,self.addQ_u_cbders)
			x=self.addQ_u_cbkonu.findText(self.Q_table.item(self.Q_table.currentRow(),2).text())
			self.addQ_u_cbkonu.setCurrentIndex(x)
			self.addQ_u_tbsoru.setPlainText(self.Q_table.item(self.Q_table.currentRow(),3).text())
	def soru_guncelle(self):
		if self.addQ_u_tbid.text() != "" and self.addQ_u_tbsoru.toPlainText() != "" and self.addQ_u_cbkonu.currentData()!=-1 and self.addQ_u_cbders.currentData()!=-1:
			self.myclass.Soru_update(self.addQ_u_tbid.text(),self.addQ_u_cbkonu.currentData(),self.addQ_u_tbsoru.toPlainText())
			self.addQ_u_cbders.setCurrentIndex(0)
			self.addQ_u_cbkonu.setCurrentIndex(0)
			self.addQ_u_tbsoru.setPlainText("")
			self.addQ_u_tbid.setText("")
			self.activated_addQ_u_cbders()
			self.b_addQ_onclick()

#endregion

#region fill comboboxes

	def fill_cbders(self,cb):
		if self.myclass.Db_Status != 1:
			return
		if len(self.List_Ders) >= 1:
			for i in self.List_Ders:
				cb.addItem(i[1],i[0])
		else:
			cb.addItem("Ders Ekleyiniz..",-1)

	def fill_cbkonu(self,targetcb,triggercb):
		if self.myclass.Db_Status == 1 and len(self.List_Ders)>=1 and triggercb.currentData()!=-1:
			List_Ders_Konu=self.myclass.Konu_get(triggercb.currentData())
			if len(List_Ders_Konu) >= 1:
				for i in List_Ders_Konu:
					targetcb.addItem(i[1],i[0])
			else:
				targetcb.addItem("Konu Ekleyiniz",-1)
	def activated_addQ_i_cbders(self):
		self.addQ_i_cbkonu.clear()
		self.fill_cbkonu(self.addQ_i_cbkonu,self.addQ_i_cbders)
	def activated_addQ_u_cbders(self):
		self.addQ_u_cbkonu.clear()
		self.fill_cbkonu(self.addQ_u_cbkonu,self.addQ_u_cbders)

#endregion

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow(MainWindow)
sys.exit(app.exec_())