from PyQt5.QtWidgets import QWidget,QDesktopWidget, QMainWindow,QLineEdit,QTabWidget,QMessageBox
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QBrush, QColor,QPen
from PyQt5.QtCore import Qt, QPoint,QSize,QRect
from PyQt5.QtChart import QChart,QChartView,QPieSeries
import sys,time,math,datetime
from Db_class import Db_Class
from ui_styles import Style
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
		self.setWindowIcon(QIcon("images/exam.png"))

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
		self.b_exit.setStyleSheet(Style.delete_button)
		self.b_exit.setIcon(QIcon("images/cross.png"))
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

		self.checkdb_1()
		timer = QtCore.QTimer(self, timeout=self.checkdb, interval=6000)
		timer.start()
#endregion

#region tab=0 home page
		self.home.setStyleSheet(Style.all_style)

		self.mypiel=QtWidgets.QWidget(self.home)
		self.mypiel.setGeometry(QRect(10,10,450,450))
		self.mypiel.setContentsMargins(QtCore.QMargins(0,0,0,0))
		#self.seriesl=self.get_pie_series()
		self.seriesl=QPieSeries()
		self.seriesl.setLabelsVisible(True)
		self.seriesl.setLabelsPosition(0)
		#self.seriesl.slices()[0].setExploded(True)
		self.seriesl.clicked.connect(self.slice_clicked)
		self.chartl=QChart()
		self.chartl.addSeries(self.seriesl)
		self.chartl.setTheme(0)
		self.chartl.setBackgroundBrush(QBrush(QColor(179, 187, 201), Qt.SolidPattern))
		self.chartl.setPlotAreaBackgroundPen(QPen(QColor(179, 187, 201), Qt.SolidPattern))
		self.chartl.setContentsMargins(0,0,0,0)
		self.chartl.setAnimationOptions(QChart.SeriesAnimations)
		self.chartl.legend().hide()
		self.chartviewl=QChartView(self.chartl,self.mypiel)
		self.chartviewl.setGeometry(QRect(0,0,450,450))


		self.mypies=QtWidgets.QWidget(self.home)
		self.mypies.setGeometry(QRect(460,10,450,450))
		self.mypies.setContentsMargins(QtCore.QMargins(0,0,0,0))
		#self.seriess=self.get_pie_seriess(self.seriesl.slices()[0].label())
		self.seriess=QPieSeries()
		self.seriess.setLabelsVisible(True)
		self.seriess.setLabelsPosition(0)
		self.seriess.clicked.connect(self.slices_clicked)
		self.charts=QChart()
		self.charts.addSeries(self.seriess)
		self.charts.setTheme(0)
		self.charts.setBackgroundBrush(QBrush(QColor(179, 187, 201), Qt.SolidPattern))
		self.charts.setPlotAreaBackgroundPen(QPen(QColor(179, 187, 201), Qt.SolidPattern))
		self.charts.setContentsMargins(0,0,0,0)
		self.charts.setAnimationOptions(QChart.SeriesAnimations)
		self.charts.legend().hide()
		self.chartviews=QChartView(self.charts,self.mypies)
		self.chartviews.setGeometry(QRect(0,0,450,450))


		self.home_lders=QtWidgets.QLabel(self.home)
		self.home_lders.setGeometry(QtCore.QRect(20, 500, 150, 35))
		self.home_lders.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.home_lders.setFont(QtGui.QFont("Verdana", 11,QtGui.QFont.Bold))
		self.home_lders.setStyleSheet("color:White;")
		self.home_lders.setText("Ders Adı         :")
		self.home_lders.setScaledContents(True)
		self.home_lders.setObjectName("home_lders")

		self.home_cbders = QtWidgets.QComboBox(self.home)
		self.home_cbders.setGeometry(QRect(180,500,200,35))
		self.home_cbders.setFont(QtGui.QFont("Verdana", 9))
		self.home_cbders.setAutoFillBackground(False)
		self.home_cbders.setIconSize(QtCore.QSize(16, 16))
		self.home_cbders.setFrame(True)
		self.home_cbders.setStyleSheet(Style.combobox_style)

		self.home_lsinav=QtWidgets.QLabel(self.home)
		self.home_lsinav.setGeometry(QtCore.QRect(470, 500, 150, 35))
		self.home_lsinav.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.home_lsinav.setFont(QtGui.QFont("Verdana", 11,QtGui.QFont.Bold))
		self.home_lsinav.setStyleSheet("color:White;")
		self.home_lsinav.setText("Sınav Tipi    :")
		self.home_lsinav.setScaledContents(True)
		self.home_lsinav.setObjectName("home_lsinav")

		self.home_cbsinav = QtWidgets.QComboBox(self.home)
		self.home_cbsinav.setGeometry(QRect(610,500,200,35))
		self.home_cbsinav.setFont(QtGui.QFont("Verdana", 9))
		self.home_cbsinav.setAutoFillBackground(False)
		self.home_cbsinav.setStyleSheet(Style.combobox_style)
		self.home_cbsinav.setIconSize(QtCore.QSize(16, 16))
		self.home_cbsinav.setFrame(True)
		self.home_cbsinav.addItem("Vize",0)
		self.home_cbsinav.addItem("Final",1)
		self.home_cbsinav.addItem("Bütünleme",2)

		self.home_ltype=QtWidgets.QLabel(self.home)
		self.home_ltype.setGeometry(QtCore.QRect(20, 550, 150, 35))
		self.home_ltype.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.home_ltype.setFont(QtGui.QFont("Verdana", 11,QtGui.QFont.Bold))
		self.home_ltype.setStyleSheet("color:White;")
		self.home_ltype.setText("Soru Dağılımı :")
		self.home_ltype.setScaledContents(True)
		self.home_ltype.setObjectName("home_lsinav")

		self.home_cbtype = QtWidgets.QComboBox(self.home)
		self.home_cbtype.setGeometry(QRect(180,550,200,35))
		self.home_cbtype.setFont(QtGui.QFont("Verdana", 9))
		self.home_cbtype.setAutoFillBackground(False)
		self.home_cbtype.setStyleSheet(Style.combobox_style)
		self.home_cbtype.setIconSize(QtCore.QSize(16, 16))
		self.home_cbtype.setFrame(True)
		self.home_cbtype.addItem("Rastgele",0)
		self.home_cbtype.addItem("Eşit Dağılım",1)

		self.home_lsayi=QtWidgets.QLabel(self.home)
		self.home_lsayi.setGeometry(QtCore.QRect(470, 550, 150, 35))
		self.home_lsayi.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.home_lsayi.setFont(QtGui.QFont("Verdana", 11,QtGui.QFont.Bold))
		self.home_lsayi.setStyleSheet("color:White;")
		self.home_lsayi.setText("Soru Sayısı  :")
		self.home_lsayi.setScaledContents(True)
		self.home_lsayi.setObjectName("home_lsayi")

		self.home_tbsayi = QtWidgets.QLineEdit(self.home)
		self.home_tbsayi.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('\d{1,3}')))
		self.home_tbsayi.setGeometry(QtCore.QRect(610, 550, 200, 35))
		self.home_tbsayi.setPlaceholderText("Soru sayısı..")
		self.home_tbsayi.setFocusPolicy(Qt.StrongFocus)
		self.home_tbsayi.setFont(QtGui.QFont("Verdana", 11))
		self.home_tbsayi.setStyleSheet(Style.lineedit_style)


		self.home_bsinavcreate = QtWidgets.QPushButton(self.home)
		self.home_bsinavcreate.setGeometry(QRect(610,620,200,50))
		self.home_bsinavcreate.setStyleSheet(Style.ok_button)
		self.home_bsinavcreate.setText("Sınav Oluştur")
		self.home_bsinavcreate.setFont(QtGui.QFont("Verdana", 11,QtGui.QFont.Bold))
		self.home_bsinavcreate.clicked.connect(self.create_exam)

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
		self.addQ_bottomtabs.addTab(self.addQ_update,"GÜNCELLE-SİL")
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
		self.addQ_s_lsoru.setGeometry(QtCore.QRect(10, 312, 130, 35))
		self.addQ_s_lsoru.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addQ_s_lsoru.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addQ_s_lsoru.setStyleSheet("color:White;")
		self.addQ_s_lsoru.setText("Soru İçeriği  :")
		self.addQ_s_lsoru.setScaledContents(True)
		self.addQ_s_lsoru.setObjectName("addQ_s_lsoru")

		self.addQ_s_tbsoru = QtWidgets.QLineEdit(self.addQ_topframe)
		self.addQ_s_tbsoru.setGeometry(QtCore.QRect(150, 315, 250, 30))
		self.addQ_s_tbsoru.setPlaceholderText("Soru içeriği..")
		self.addQ_s_tbsoru.setFocusPolicy(Qt.StrongFocus)
		self.addQ_s_tbsoru.setFont(QtGui.QFont("Verdana", 10))
		self.addQ_s_tbsoru.setStyleSheet(Style.lineedit_style)

		self.addQ_s_lkonu=QtWidgets.QLabel(self.addQ_topframe)
		self.addQ_s_lkonu.setGeometry(QtCore.QRect(450, 312, 90, 35))
		self.addQ_s_lkonu.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addQ_s_lkonu.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addQ_s_lkonu.setStyleSheet("color:White;")
		self.addQ_s_lkonu.setText("Konu  :")
		self.addQ_s_lkonu.setScaledContents(True)
		self.addQ_s_lkonu.setObjectName("addQ_s_lkonu")

		self.addQ_s_tbkonu = QtWidgets.QLineEdit(self.addQ_topframe)
		self.addQ_s_tbkonu.setGeometry(QtCore.QRect(525, 315, 250, 30))
		self.addQ_s_tbkonu.setPlaceholderText("Konu adı..")
		self.addQ_s_tbkonu.setFocusPolicy(Qt.StrongFocus)
		self.addQ_s_tbkonu.setFont(QtGui.QFont("Verdana", 10))
		self.addQ_s_tbkonu.setStyleSheet(Style.lineedit_style)	

		self.addQ_i_binsert = QtWidgets.QPushButton(self.addQ_topframe)
		self.addQ_i_binsert.setGeometry(QRect(825,315,70,30))
		self.addQ_i_binsert.setStyleSheet(Style.borderless_button)
		self.addQ_i_binsert.setIcon(QIcon("images/search.png"))
		self.addQ_i_binsert.setText("Ara")
		self.addQ_i_binsert.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addQ_i_binsert.clicked.connect(self.soru_ara)


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
		self.addQ_i_binsert.setGeometry(QRect(750,180,130,80))
		self.addQ_i_binsert.setStyleSheet(Style.ok_button)
		self.addQ_i_binsert.setText("Ekle")
		self.addQ_i_binsert.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
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
		self.addQ_u_tbid.setVisible(False)

		self.addQ_u_cbders = QtWidgets.QComboBox(self.addQ_update)
		self.addQ_u_cbders.setGeometry(QRect(20,10,200,35))
		self.addQ_u_cbders.setFont(QtGui.QFont("Verdana", 9))
		self.addQ_u_cbders.setAutoFillBackground(False)
		self.addQ_u_cbders.setIconSize(QtCore.QSize(16, 16))
		self.addQ_u_cbders.setFrame(True)
		self.addQ_u_cbders.setStyleSheet(Style.combobox_style)
		self.addQ_u_cbders.activated['int'].connect(self.activated_addQ_u_cbders)

		self.addQ_u_cbkonu = QtWidgets.QComboBox(self.addQ_update)
		self.addQ_u_cbkonu.setGeometry(QRect(285,10,200,35))
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
		self.addQ_u_binsert.setGeometry(QRect(750,180,130,80))
		self.addQ_u_binsert.setStyleSheet(Style.ok_button)
		self.addQ_u_binsert.setText("Kaydet")
		self.addQ_u_binsert.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addQ_u_binsert.clicked.connect(self.soru_guncelle)

		self.addQ_u_bdelete = QtWidgets.QPushButton(self.addQ_update)
		self.addQ_u_bdelete.setGeometry(QRect(750,70,130,80))
		self.addQ_u_bdelete.setStyleSheet(Style.delete_button)
		self.addQ_u_bdelete.setText("Sil")
		self.addQ_u_bdelete.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addQ_u_bdelete.clicked.connect(self.soru_sil)

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

		self.addL_tabs.addTab(self.addL_insterttab,"EKLE")
		self.addL_tabs.addTab(self.addL_updatetab,"GÜNCELLE-SİL")
		self.addL_tabs.setStyleSheet(Style.all_style)
		self.addL_tabs.setTabPosition(3)

		self.L_table = QtWidgets.QTableWidget(self.addL_frame)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.L_table.sizePolicy().hasHeightForWidth())
		self.L_table.setSizePolicy(sizePolicy)
		self.L_table.setFixedSize(400,268)
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

		self.addL_searchtab_label=QtWidgets.QLabel(self.addL_frame)
		self.addL_searchtab_label.setGeometry(QtCore.QRect(20, 280, 200, 35))
		self.addL_searchtab_label.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addL_searchtab_label.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addL_searchtab_label.setStyleSheet("color:White;")
		self.addL_searchtab_label.setText("Ders Adı  :")
		self.addL_searchtab_label.setScaledContents(True)
		self.addL_searchtab_label.setObjectName("addL_searchtab_label")

		self.addL_searchtab_tbara=QLineEdit(self.addL_frame)
		self.addL_searchtab_tbara.move(130, 280)
		self.addL_searchtab_tbara.resize(200,35)
		self.addL_searchtab_tbara.setFocusPolicy(Qt.StrongFocus)
		self.addL_searchtab_tbara.setFont(QtGui.QFont("Verdana", 11))
		self.addL_searchtab_tbara.setStyleSheet(Style.lineedit_style)
		self.addL_searchtab_tbara.textEdited.connect(self.ders_ara)	

		self.addL_searchtab_bara = QtWidgets.QPushButton(self.addL_frame)
		self.addL_searchtab_bara.setStyleSheet(Style.borderless_button)
		self.addL_searchtab_bara.setFixedSize(80,35)
		self.addL_searchtab_bara.move(330,280)
		self.addL_searchtab_bara.setIcon(QIcon("images/search.png"))
		self.addL_searchtab_bara.setText(" Ara")
		self.addL_searchtab_bara.setFont(QtGui.QFont("Verdana", 9,QtGui.QFont.Bold))
		self.addL_searchtab_bara.clicked.connect(self.ders_ara)		

		#endregion
		#region ders insert
		self.addL_insterttab_ltitle=QtWidgets.QLabel(self.addL_insterttab)
		self.addL_insterttab_ltitle.setGeometry(QtCore.QRect(160, 40, 400, 50))
		self.addL_insterttab_ltitle.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addL_insterttab_ltitle.setFont(QtGui.QFont("Verdana", 15,QtGui.QFont.Bold))
		self.addL_insterttab_ltitle.setStyleSheet("color:White;")
		self.addL_insterttab_ltitle.setText("Ders Ekle")
		self.addL_insterttab_ltitle.setScaledContents(True)
		self.addL_insterttab_ltitle.setObjectName("addL_insterttab_ltitle")

		self.addL_insterttab_lname=QtWidgets.QLabel(self.addL_insterttab)
		self.addL_insterttab_lname.setGeometry(QtCore.QRect(40, 120, 200, 35))
		self.addL_insterttab_lname.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addL_insterttab_lname.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addL_insterttab_lname.setStyleSheet("color:White;")
		self.addL_insterttab_lname.setText("Ders Adı  :")
		self.addL_insterttab_lname.setScaledContents(True)
		self.addL_insterttab_lname.setObjectName("addL_insterttab_lname")

		self.addL_insterttab_tbname = QtWidgets.QLineEdit(self.addL_insterttab)
		self.addL_insterttab_tbname.move(40, 180)
		self.addL_insterttab_tbname.resize(200,35)
		self.addL_insterttab_tbname.setPlaceholderText("Ders adını giriniz..")
		self.addL_insterttab_tbname.setFocusPolicy(Qt.StrongFocus)
		self.addL_insterttab_tbname.setFont(QtGui.QFont("Verdana", 11))
		self.addL_insterttab_tbname.setStyleSheet(Style.lineedit_style)	

		self.addL_insterttab_binsert = QtWidgets.QPushButton(self.addL_insterttab)
		self.addL_insterttab_binsert.setStyleSheet(Style.ok_button)
		self.addL_insterttab_binsert.setText("Ekle")
		self.addL_insterttab_binsert.setFixedSize(100,40)
		self.addL_insterttab_binsert.move(270,230)
		self.addL_insterttab_binsert.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
		self.addL_insterttab_binsert.clicked.connect(self.ders_ekle)

		#endregion
		#region ders update

		self.addL_updatetab_ltitle=QtWidgets.QLabel(self.addL_updatetab)
		self.addL_updatetab_ltitle.setGeometry(QtCore.QRect(130, 40, 400, 50))
		self.addL_updatetab_ltitle.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addL_updatetab_ltitle.setFont(QtGui.QFont("Verdana", 15,QtGui.QFont.Bold))
		self.addL_updatetab_ltitle.setStyleSheet("color:White;")
		self.addL_updatetab_ltitle.setText("Ders Güncelle")
		self.addL_updatetab_ltitle.setScaledContents(True)
		self.addL_updatetab_ltitle.setObjectName("addL_updatetab_ltitle")

		self.addL_updatetab_lid=QtWidgets.QLabel(self.addL_updatetab)
		self.addL_updatetab_lid.setGeometry(QtCore.QRect(40, 120, 200, 35))
		self.addL_updatetab_lid.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addL_updatetab_lid.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addL_updatetab_lid.setStyleSheet("color:White;")
		self.addL_updatetab_lid.setText("Ders Id  :")
		self.addL_updatetab_lid.setScaledContents(True)
		self.addL_updatetab_lid.setObjectName("addL_updatetab_lid")

		self.addL_updatetab_lname=QtWidgets.QLabel(self.addL_updatetab)
		self.addL_updatetab_lname.setGeometry(QtCore.QRect(40, 200, 200, 35))
		self.addL_updatetab_lname.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addL_updatetab_lname.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addL_updatetab_lname.setStyleSheet("color:White;")
		self.addL_updatetab_lname.setText("Ders Adı  :")
		self.addL_updatetab_lname.setScaledContents(True)
		self.addL_updatetab_lname.setObjectName("addL_updatetab_lname")

		self.addL_updatetab_tbid=QLineEdit(self.addL_updatetab)
		self.addL_updatetab_tbid.move(40, 150)
		self.addL_updatetab_tbid.resize(150,35)
		self.addL_updatetab_tbid.setFocusPolicy(Qt.StrongFocus)
		self.addL_updatetab_tbid.setFont(QtGui.QFont("Verdana", 11))
		self.addL_updatetab_tbid.setStyleSheet(Style.lineedit_style)
		self.addL_updatetab_tbid.setReadOnly(True)

		self.addL_updatetab_tbname=QLineEdit(self.addL_updatetab)
		self.addL_updatetab_tbname.move(40, 235)
		self.addL_updatetab_tbname.resize(200,35)
		self.addL_updatetab_tbname.setFocusPolicy(Qt.StrongFocus)
		self.addL_updatetab_tbname.setFont(QtGui.QFont("Verdana", 11))
		self.addL_updatetab_tbname.setStyleSheet(Style.lineedit_style)

		self.L_table.itemSelectionChanged.connect(self.L_table_onselected)

		self.addL_updatetab_bupdate = QtWidgets.QPushButton(self.addL_updatetab)
		self.addL_updatetab_bupdate.setStyleSheet(Style.ok_button)
		self.addL_updatetab_bupdate.setFixedSize(90,45)
		self.addL_updatetab_bupdate.move(270,230)
		self.addL_updatetab_bupdate.setText("Güncelle")
		self.addL_updatetab_bupdate.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addL_updatetab_bupdate.clicked.connect(self.ders_guncelle)

		self.addL_updatetab_bdelete = QtWidgets.QPushButton(self.addL_updatetab)
		self.addL_updatetab_bdelete.setGeometry(QRect(270,145,90,45))
		self.addL_updatetab_bdelete.setStyleSheet(Style.delete_button)
		self.addL_updatetab_bdelete.setText("Sil")
		self.addL_updatetab_bdelete.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addL_updatetab_bdelete.clicked.connect(self.ders_sil)

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

		self.addS_tabs.addTab(self.addS_inserttab,"EKLE")
		self.addS_tabs.addTab(self.addS_updatetab,"GÜNCELLE-SİL")
		self.addS_tabs.setStyleSheet(Style.all_style)
		self.addS_tabs.setTabPosition(3)

		self.S_table = QtWidgets.QTableWidget(self.addS_frame)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.S_table.sizePolicy().hasHeightForWidth())
		self.S_table.setSizePolicy(sizePolicy)
		self.S_table.setFixedSize(475,305)
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
		self.S_table.setHorizontalHeaderLabels(["ID","Ders Adı","Dönem","Konu Adı"])
		self.S_table.verticalHeader().setVisible(False)
		self.S_table.verticalHeader().setCascadingSectionResizes(False)
		self.S_table.verticalHeader().setHighlightSections(False)
		self.S_table.verticalHeader().setStretchLastSection(True)
		self.S_table.setSortingEnabled(True)
		self.S_table.setColumnHidden(0, True);

		#region konu search
		self.addS_searchtab_label=QtWidgets.QLabel(self.addS_frame)
		self.addS_searchtab_label.setGeometry(QtCore.QRect(10, 315, 210, 35))
		self.addS_searchtab_label.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addS_searchtab_label.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addS_searchtab_label.setStyleSheet("color:White;")
		self.addS_searchtab_label.setText("Ders veya Konu Adı  :")
		self.addS_searchtab_label.setScaledContents(True)
		self.addS_searchtab_label.setObjectName("addS_searchtab_label")

		self.addS_searchtab_tbara=QLineEdit(self.addS_frame)
		self.addS_searchtab_tbara.move(220, 315)
		self.addS_searchtab_tbara.resize(200,35)
		self.addS_searchtab_tbara.setFocusPolicy(Qt.StrongFocus)
		self.addS_searchtab_tbara.setFont(QtGui.QFont("Verdana", 11))
		self.addS_searchtab_tbara.setStyleSheet(Style.lineedit_style)
		self.addS_searchtab_tbara.textEdited.connect(self.konu_ara)	

		self.addS_searchtab_bara = QtWidgets.QPushButton(self.addS_frame)
		self.addS_searchtab_bara.setStyleSheet(Style.borderless_button)
		self.addS_searchtab_bara.setFixedSize(65,35)
		self.addS_searchtab_bara.move(420,315)
		self.addS_searchtab_bara.setText("Ara")
		self.addS_searchtab_bara.setFont(QtGui.QFont("Verdana", 9,QtGui.QFont.Bold))
		self.addS_searchtab_bara.setIcon(QIcon("images/search.png"))
		self.addS_searchtab_bara.clicked.connect(self.konu_ara)
		#endregion

		#region konu insert

		self.addS_inserttab_ltitle=QtWidgets.QLabel(self.addS_inserttab)
		self.addS_inserttab_ltitle.setGeometry(QtCore.QRect(130, 20, 400, 50))
		self.addS_inserttab_ltitle.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addS_inserttab_ltitle.setFont(QtGui.QFont("Verdana", 14,QtGui.QFont.Bold))
		self.addS_inserttab_ltitle.setStyleSheet("color:White;")
		self.addS_inserttab_ltitle.setText("Konu Ekle")
		self.addS_inserttab_ltitle.setScaledContents(True)
		self.addS_inserttab_ltitle.setObjectName("addS_inserttab_ltitle")

		self.addS_inserttab_lders=QtWidgets.QLabel(self.addS_inserttab)
		self.addS_inserttab_lders.setGeometry(QtCore.QRect(30, 80, 200, 35))
		self.addS_inserttab_lders.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addS_inserttab_lders.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addS_inserttab_lders.setStyleSheet("color:White;")
		self.addS_inserttab_lders.setText("Ders :")
		self.addS_inserttab_lders.setScaledContents(True)
		self.addS_inserttab_lders.setObjectName("addS_inserttab_lders")

		self.addS_inserttab_cbders = QtWidgets.QComboBox(self.addS_inserttab)
		self.addS_inserttab_cbders.move(30,120)
		self.addS_inserttab_cbders.setFixedSize(200,35)
		self.addS_inserttab_cbders.setFont(QtGui.QFont("Verdana", 9))
		self.addS_inserttab_cbders.setAutoFillBackground(False)
		self.addS_inserttab_cbders.setStyleSheet(Style.combobox_style)
		self.addS_inserttab_cbders.setIconSize(QtCore.QSize(16, 16))
		self.addS_inserttab_cbders.setFrame(True)

		self.addS_inserttab_ldonem=QtWidgets.QLabel(self.addS_inserttab)
		self.addS_inserttab_ldonem.setGeometry(QtCore.QRect(30, 160, 200, 35))
		self.addS_inserttab_ldonem.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addS_inserttab_ldonem.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addS_inserttab_ldonem.setStyleSheet("color:White;")
		self.addS_inserttab_ldonem.setText("Dönem :")
		self.addS_inserttab_ldonem.setScaledContents(True)
		self.addS_inserttab_ldonem.setObjectName("addS_inserttab_ldonem")

		self.addS_inserttab_cbdonem = QtWidgets.QComboBox(self.addS_inserttab)
		self.addS_inserttab_cbdonem.move(30,200)
		self.addS_inserttab_cbdonem.setFixedSize(200,35)
		self.addS_inserttab_cbdonem.setFont(QtGui.QFont("Verdana", 9))
		self.addS_inserttab_cbdonem.setAutoFillBackground(False)
		self.addS_inserttab_cbdonem.setStyleSheet(Style.combobox_style)
		self.addS_inserttab_cbdonem.setIconSize(QtCore.QSize(16, 16))
		self.addS_inserttab_cbdonem.setFrame(True)
		self.addS_inserttab_cbdonem.addItem("Vize",0)
		self.addS_inserttab_cbdonem.addItem("Final",1)

		self.addS_inserttab_lname=QtWidgets.QLabel(self.addS_inserttab)
		self.addS_inserttab_lname.setGeometry(QtCore.QRect(30, 240, 200, 35))
		self.addS_inserttab_lname.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addS_inserttab_lname.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addS_inserttab_lname.setStyleSheet("color:White;")
		self.addS_inserttab_lname.setText("Konu Adı :")
		self.addS_inserttab_lname.setScaledContents(True)
		self.addS_inserttab_lname.setObjectName("addS_inserttab_lname")

		self.addS_inserttab_tbname=QLineEdit(self.addS_inserttab)
		self.addS_inserttab_tbname.move(30, 280)
		self.addS_inserttab_tbname.resize(200,35)
		self.addS_inserttab_tbname.setFocusPolicy(Qt.StrongFocus)
		self.addS_inserttab_tbname.setFont(QtGui.QFont("Verdana", 11))
		self.addS_inserttab_tbname.setStyleSheet(Style.lineedit_style)

		self.addS_inserttab_binsert = QtWidgets.QPushButton(self.addS_inserttab)
		self.addS_inserttab_binsert.setStyleSheet(Style.ok_button)
		self.addS_inserttab_binsert.setFixedSize(75,45)
		self.addS_inserttab_binsert.move(260,275)
		self.addS_inserttab_binsert.setText("Ekle")
		self.addS_inserttab_binsert.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addS_inserttab_binsert.clicked.connect(self.konu_ekle)

		#endregion

		#region konu update
		self.addS_updatetab_ltitle=QtWidgets.QLabel(self.addS_updatetab)
		self.addS_updatetab_ltitle.setGeometry(QtCore.QRect(130, 20, 400, 50))
		self.addS_updatetab_ltitle.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addS_updatetab_ltitle.setFont(QtGui.QFont("Verdana", 14,QtGui.QFont.Bold))
		self.addS_updatetab_ltitle.setStyleSheet("color:White;")
		self.addS_updatetab_ltitle.setText("Konu Ekle")
		self.addS_updatetab_ltitle.setScaledContents(True)
		self.addS_updatetab_ltitle.setObjectName("addS_updatetab_ltitle")

		self.addS_updatetab_lders=QtWidgets.QLabel(self.addS_updatetab)
		self.addS_updatetab_lders.setGeometry(QtCore.QRect(30, 80, 200, 35))
		self.addS_updatetab_lders.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addS_updatetab_lders.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addS_updatetab_lders.setStyleSheet("color:White;")
		self.addS_updatetab_lders.setText("Ders :")
		self.addS_updatetab_lders.setScaledContents(True)
		self.addS_updatetab_lders.setObjectName("addS_updatetab_lders")

		self.addS_updatetab_tbid=QLineEdit(self.addS_updatetab)
		self.addS_updatetab_tbid.move(30, 120)
		self.addS_updatetab_tbid.resize(200,35)
		self.addS_updatetab_tbid.setFocusPolicy(Qt.StrongFocus)
		self.addS_updatetab_tbid.setFont(QtGui.QFont("Verdana", 11))
		self.addS_updatetab_tbid.setStyleSheet(Style.lineedit_style)
		self.addS_updatetab_tbid.setReadOnly(True)
		self.addS_updatetab_tbid.setVisible(False)

		self.addS_updatetab_cbders = QtWidgets.QComboBox(self.addS_updatetab)
		self.addS_updatetab_cbders.move(30,120)
		self.addS_updatetab_cbders.setFixedSize(200,35)
		self.addS_updatetab_cbders.setFont(QtGui.QFont("Verdana", 9))
		self.addS_updatetab_cbders.setAutoFillBackground(False)
		self.addS_updatetab_cbders.setStyleSheet(Style.combobox_style)
		self.addS_updatetab_cbders.setIconSize(QtCore.QSize(16, 16))
		self.addS_updatetab_cbders.setFrame(True)

		self.addS_updatetab_ldonem=QtWidgets.QLabel(self.addS_updatetab)
		self.addS_updatetab_ldonem.setGeometry(QtCore.QRect(30, 160, 200, 35))
		self.addS_updatetab_ldonem.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addS_updatetab_ldonem.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addS_updatetab_ldonem.setStyleSheet("color:White;")
		self.addS_updatetab_ldonem.setText("Dönem :")
		self.addS_updatetab_ldonem.setScaledContents(True)
		self.addS_updatetab_ldonem.setObjectName("addS_updatetab_ldonem")

		self.addS_updatetab_cbdonem = QtWidgets.QComboBox(self.addS_updatetab)
		self.addS_updatetab_cbdonem.move(30,200)
		self.addS_updatetab_cbdonem.setFixedSize(200,35)
		self.addS_updatetab_cbdonem.setFont(QtGui.QFont("Verdana", 9))
		self.addS_updatetab_cbdonem.setAutoFillBackground(False)
		self.addS_updatetab_cbdonem.setStyleSheet(Style.combobox_style)
		self.addS_updatetab_cbdonem.setIconSize(QtCore.QSize(16, 16))
		self.addS_updatetab_cbdonem.setFrame(True)
		self.addS_updatetab_cbdonem.addItem("Vize",0)
		self.addS_updatetab_cbdonem.addItem("Final",1)

		self.addS_updatetab_lname=QtWidgets.QLabel(self.addS_updatetab)
		self.addS_updatetab_lname.setGeometry(QtCore.QRect(30, 240, 200, 35))
		self.addS_updatetab_lname.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.addS_updatetab_lname.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addS_updatetab_lname.setStyleSheet("color:White;")
		self.addS_updatetab_lname.setText("Konu Adı :")
		self.addS_updatetab_lname.setScaledContents(True)
		self.addS_updatetab_lname.setObjectName("addS_updatetab_lname")

		self.addS_updatetab_tbname=QLineEdit(self.addS_updatetab)
		self.addS_updatetab_tbname.move(30, 280)
		self.addS_updatetab_tbname.resize(200,35)
		self.addS_updatetab_tbname.setFocusPolicy(Qt.StrongFocus)
		self.addS_updatetab_tbname.setFont(QtGui.QFont("Verdana", 11))
		self.addS_updatetab_tbname.setStyleSheet(Style.lineedit_style)

		self.S_table.itemSelectionChanged.connect(self.fill_addS_updatetab)

		self.addS_updatetab_bupdate = QtWidgets.QPushButton(self.addS_updatetab)
		self.addS_updatetab_bupdate.setStyleSheet(Style.ok_button)
		self.addS_updatetab_bupdate.setFixedSize(85,45)
		self.addS_updatetab_bupdate.move(260,275)
		self.addS_updatetab_bupdate.setText("Güncelle")
		self.addS_updatetab_bupdate.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addS_updatetab_bupdate.clicked.connect(self.konu_guncelle)

		self.addS_updatetab_bdelete = QtWidgets.QPushButton(self.addS_updatetab)
		self.addS_updatetab_bdelete.setGeometry(QRect(260,185,85,45))
		self.addS_updatetab_bdelete.setStyleSheet(Style.delete_button)
		self.addS_updatetab_bdelete.setText("Sil")
		self.addS_updatetab_bdelete.setFont(QtGui.QFont("Verdana", 10,QtGui.QFont.Bold))
		self.addS_updatetab_bdelete.clicked.connect(self.konu_sil)

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
		self.setting_bupdate.setText("Ayarları\n Kaydet")
		self.setting_bupdate.setFixedSize(150,60)
		self.setting_bupdate.move(290,250)
		self.setting_bupdate.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
		self.setting_bupdate.clicked.connect(self.Write_Config)

		self.setting_bupdate = QtWidgets.QPushButton(self.setting_frame)
		self.setting_bupdate.setStyleSheet(Style.warning_button)
		self.setting_bupdate.setText("Veritabanı\n oluştur")
		self.setting_bupdate.setFixedSize(150,60)
		self.setting_bupdate.move(70,250)
		self.setting_bupdate.setFont(QtGui.QFont("Verdana", 11, QtGui.QFont.Bold))
		self.setting_bupdate.clicked.connect(self.create_db)
#endregion

		self.b_home_onclick()
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
	def create_db(self):
		if self.myclass.Db_Status==0:
			self.myclass.Db_Create()
			self.myclass.Check_Db_Status()
			self.myclass.Import_Db()
		else:
			self.show_warning_popup("Bağlantı kurulamadı veya veritabanı zaten var.")
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
		if self.myclass.Db_Status==1:
			self.get_data()
			self.fill_cbders(self.home_cbders)
			if len(self.List_Ders)>1 and len(self.List_Konu)>1 and len(self.myclass.Soru_get_all())>1:
				self.update_piechartl()
				self.update_piecharts()
			else:
				self.show_warning_popup("Sayfa pie chart içermektedir ve gösterebilmek için yeterli kayıt bulunmamaktadır.")
				self.charts.removeAllSeries()
				self.chartl.removeAllSeries()
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
		self.S_table.setHorizontalHeaderLabels(["ID","Ders Adı","Dönem","Konu Adı"])
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
			self.Q_table.setRowCount(len(sorular))
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
			self.addL_tabs.setCurrentIndex(1)
			self.addL_updatetab_tbid.setText(self.L_table.item(self.L_table.currentRow(),0).text())
			self.addL_updatetab_tbname.setText(self.L_table.item(self.L_table.currentRow(),1).text())

	def ders_ara(self):
		self.L_table.clear()
		self.L_table.setHorizontalHeaderLabels(["ID","Ders Adı"])
		Ders_searchresault=self.myclass.Ders_search(self.addL_searchtab_tbara.text())
		self.fill_table_ders(Ders_searchresault)

	def ders_guncelle(self):
		if self.addL_updatetab_tbid.text() != "" and self.L_table.item(self.L_table.currentRow(),1) != None and self.addL_updatetab_tbname.text() != "":
			self.myclass.Ders_update(self.addL_updatetab_tbid.text(),self.addL_updatetab_tbname.text())
			self.get_data()
			self.fill_table_ders(self.List_Ders)
			self.show_success_popup("Ders başarıyla güncellendi.")
		else:
			if self.addL_updatetab_tbname=="":
				self.show_warning_popup("Ders adı boş olamaz.")
			else:
				self.show_warning_popup("Listeden ders seçiniz.")
	def ders_ekle(self):
		if self.addL_insterttab_tbname.text() != None and self.addL_insterttab_tbname.text() != "":
			self.myclass.Ders_insert(self.addL_insterttab_tbname.text())
			self.get_data()
			self.fill_table_ders(self.List_Ders)
			self.show_success_popup("Ders başarıyla eklendi.")
			self.b_addLS_onclick()
		else:
			self.show_warning_popup("Ders adı boş olamaz.")
	def ders_sil(self):
		if self.addL_updatetab_tbid.text() != "" or self.L_table.item(self.L_table.currentRow(),1) != None:
			self.show_delete_popup("{} adlı dersi silmek istediğinize eminmisiniz.".format(self.addL_updatetab_tbname.text()),self.popup_deleteders_button)
		else:
			self.show_warning_popup("Listeden ders seçiniz.")
	def ders_sil_onay(self,result):
		if result.strip()=="OK":
			x=self.myclass.delete_ders(int(self.addL_updatetab_tbid.text()))
			self.L_table.clear()
			self.get_data()
			self.fill_table_ders(self.List_Ders)
			if x==1:
				self.show_success_popup("Ders başarıyla silindi")
				self.b_addLS_onclick()
			else:
				self.show_warning_popup(str(x))
#endregion

#region konu functions

	def konu_ara(self):
		self.S_table.clear()
		self.S_table.setHorizontalHeaderLabels(["ID","Ders Adı","Dönem","Konu Adı"])
		mylist=self.myclass.Konu_search(self.addS_searchtab_tbara.text())
		self.S_table.setRowCount(len(mylist)+1)
		self.fill_table_konu(mylist)

	def konu_ekle(self):
		if self.addS_inserttab_tbname.text() == None or self.addS_inserttab_tbname.text() == "":
			self.show_warning_popup("Konu adı boş olamaz.")
		else:
			self.myclass.Konu_insert(self.addS_inserttab_cbders.currentData(),self.addS_inserttab_cbdonem.currentData(),self.addS_inserttab_tbname.text())
			self.konu_ara()
			self.show_success_popup("Konu başarıyla eklendi.")
			self.b_addLS_onclick()
	def fill_addS_updatetab(self):
		self.addS_tabs.setCurrentIndex(1)
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
		if self.addS_updatetab_tbname.text() != "" and self.addS_updatetab_tbname.text() != None:
			self.myclass.Konu_update(self.addS_updatetab_tbid.text(),self.addS_updatetab_cbders.currentData(),self.addS_updatetab_cbdonem.currentData(),self.addS_updatetab_tbname.text())
			self.b_addLS_onclick()
			self.show_success_popup("Konu başarıyla güncellendi.")
		else:
			if self.addS_updatetab_tbname.text() == "":
				self.show_warning_popup("Konu adı boş olamaz.")
			else:
				self.show_warning_popup("Listeden konu seçiniz.")
	def konu_sil(self):
		if self.addS_updatetab_tbname.text() != "" and self.addS_updatetab_tbname.text() != None:
			self.show_delete_popup("{} adlı konuyu içindeki sorularla beraber silmek istediğinize eminmisiniz.".format(self.addS_updatetab_tbname.text()),self.popup_deletekonu_button)
		else:
			self.show_warning_popup("Listeden konu seçmelisiniz.")
	def konu_sil_onay(self,result):
		if result.strip()=="OK":
			x=self.myclass.delete_konu(int(self.addS_updatetab_tbid.text()))
			self.S_table.clear()
			self.get_data()
			self.fill_table_konu(self.List_Konu)
			if x==1:
				self.show_success_popup("Konu başarıyla silindi")
				self.b_addLS_onclick()
			else:

				self.show_warning_popup(str(x))
#endregion

#region soru functions
	def Soru_ekle(self):
		if self.addQ_i_tbsoru.toPlainText() != "" and self.addQ_i_cbkonu.currentData()!=-1 and self.addQ_i_cbders.currentData()!=-1:
			self.myclass.Soru_insert(self.addQ_i_cbkonu.currentData(),self.addQ_i_tbsoru.toPlainText())
			self.show_success_popup("Soru başarıyla eklendi.")
			self.addQ_i_cbders.setCurrentIndex(0)
			self.addQ_i_cbkonu.setCurrentIndex(0)
			self.addQ_i_tbsoru.setPlainText("")
			self.fill_table_soru_onstart()
		else:
			self.show_warning_popup("bütün alanları doldurmadınız.")
	def fill_addQ_updatetab(self):
		self.addQ_bottomtabs.setCurrentIndex(1)
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
		else:
			if self.addQ_u_tbsoru.toPlainText() == "":
				self.show_warning_popup("Boş soru eklenemez.")
			else:
				self.show_warning_popup("Listeden soru seçmelisiniz.")
	def soru_ara(self):
		self.Q_table.clear()
		self.Q_table.setHorizontalHeaderLabels(["ID","Ders Adı","Konu Adı","Soru"])

		if self.addQ_s_tbkonu.text()=="":
			konutext="%"
		else:
			konutext='%'+str(self.addQ_s_tbkonu.text())+'%'
		if self.addQ_s_tbsoru.text()=="":
			sorutext="%"
		else:
			sorutext='%'+str(self.addQ_s_tbsoru.text())+'%'
		sorular=self.myclass.Soru_search(sorutext,konutext)
		self.Q_table.setRowCount(len(sorular)+1)
		self.fill_table_soru(sorular)
	def soru_sil(self):
		if self.addQ_u_tbid.text()!="":
			self.show_delete_popup("{}... ile başlayan soruyu silmek istediğinize eminmisiniz?".format(self.addQ_u_tbsoru.toPlainText()[0:30]),self.popup_deletesoru_button)
		else:
			self.show_warning_popup("Listeden soru seçmelisiniz.")
	def soru_sil_onay(self,result):
		if result.strip()=="OK":
			x=self.myclass.delete_soru(int(self.addQ_u_tbid.text()))
			self.Q_table.clear()
			self.fill_table_soru_onstart()
			if x==1:
				self.show_success_popup("Soru başarıyla silindi")
			else:
				self.show_warning_popup(str(x))
#endregion

#region fill comboboxes

	def fill_cbders(self,cb):
		if self.myclass.Db_Status != 1:
			return
		if len(self.List_Ders) >= 1:
			cb.clear()
			for i in self.List_Ders:
				cb.addItem(i[1],i[0])
		else:
			cb.clear()
			cb.addItem("Ders Ekleyiniz..",-1)

	def fill_cbkonu(self,targetcb,triggercb):
		if self.myclass.Db_Status == 1 and len(self.List_Ders)>=1 and triggercb.currentData()!=-1:
			List_Ders_Konu=self.myclass.Konu_get(triggercb.currentData())
			if len(List_Ders_Konu) >= 1:
				targetcb.clear()
				for i in List_Ders_Konu:
					targetcb.addItem(i[1],i[0])
			else:
				targetcb.clear()
				targetcb.addItem("Konu Ekleyiniz",-1)
	def activated_addQ_i_cbders(self):
		self.addQ_i_cbkonu.clear()
		self.fill_cbkonu(self.addQ_i_cbkonu,self.addQ_i_cbders)
	def activated_addQ_u_cbders(self):
		self.addQ_u_cbkonu.clear()
		self.fill_cbkonu(self.addQ_u_cbkonu,self.addQ_u_cbders)

#endregion
#region anasayfa
	def create_exam(self):
		sinav=[]
		mystr=""
		already_selected=[]
		try:
			edonem=self.home_cbsinav.currentData()
			etype=self.home_cbtype.currentData()
			eders=self.home_cbders.currentData()
			if eders==-1:
				self.show_warning_popup("Sınav oluşturmak için ders seçmelisiniz.")
			qcount=int(self.home_tbsayi.text())
		except Exception as e:
			self.show_detailed_warning_popup("Bazı alanları doğru bir şekilde doldurmadınız",str(e))
			return
		ders_soru_sayisi=self.myclass.check_exam_is_suitable(eders,edonem)
		if qcount==0 or qcount==None:
			self.show_detailed_warning_popup("soru sayısını belirleyiniz","Soru sayısı belirlenmediğinden veya 0 girildiğinden dolayı işleme devam edilememektedir.")
			return
		elif qcount>ders_soru_sayisi:
			self.show_detailed_warning_popup("Soru sayısı geçersiz.","{} tane soru içeren sınav oluşturulamadı.Seçtiğiniz ders {} tane soruya sahip.".format(qcount,ders_soru_sayisi))
			return
		else:	
			if etype==0:
				sinav=self.myclass.get_random_exam(eders,edonem,qcount)
				self.write_exam_to_file(self.home_cbders.currentText(),sinav)
			else:
				check_sub=True
				x=self.myclass.Konu_count(int(eders),int(edonem))
				subjectsqcount=math.floor(qcount/x)
				y=self.myclass.get_exams_subjects(int(eders),int(edonem))
				if int(x)>qcount:
					dtext="konu sayınız {} iken istediğiniz soru sayısı {} dir.Eşit dağılım yapılabilmesi için en az {} soru sayısı girilmelidir.".format(x,qcount,x)
					self.show_detailed_warning_popup("Eşit soru dağılımlı sınav oluşturma başarısız..",dtext)
					return
				for i in y:
					z=self.myclass.Soru_count(int(i[0]))
					if z<subjectsqcount:
						mystr+="{} isimli konu minimum {} tane soru içermesi gerekirken {} tane soru içermektedir.\n".format(i[1],subjectsqcount,z)
						check_sub=False
				if not check_sub:
					self.show_detailed_warning_popup("Eşit soru dağılımlı sınav oluşturma başarısız..",mystr)
					return
				else:
					for i in y:
						sinav+=self.myclass.get_random_exam(i[0],subjectsqcount)
					if len(sinav)<qcount:
						for i in sinav:
							already_selected.append(i[1])
						sinav+=self.myclass.get_random_exam(eders,qcount-len(sinav),already_selected)
					self.write_exam_to_file(self.home_cbders.currentText(),sinav)
	def write_exam_to_file(self,dersad,questions):
		self.home_cbders.setCurrentIndex(0)
		self.home_cbsinav.setCurrentIndex(0)
		self.home_cbtype.setCurrentIndex(0)
		self.home_tbsayi.setText("")
		filename="ExamFor"+dersad+"_"+datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")+".txt"
		with open(str(filename),"w") as f:
			for i in range(len(questions)):
				f.write(str(i+1)+"-)\n"+questions[i][0]+"\n\n")
		self.show_success_popup("Sınavınız başarıyla oluşturuldu.")
	def get_pie_series(self):
		series=QPieSeries()
		data=self.myclass.Soru_count()
		for i in data:
			series.append(i[1],i[0])
		return series
	def slice_clicked(self,slice):
		self.get_data()
		for i in self.seriesl.slices():
			i.setExploded(False)
			i.setLabelPosition(0)
			i.setLabelColor(QColor(44, 49, 60))
			i.setLabelFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
		slice.setLabelColor(QColor(255, 255, 255))
		slice.setLabelFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
		slice.setExploded(True)
		slice.setLabelPosition(1)
		#slice.setLabel("{}{:.1f}%".format(slice.label(),100 * slice.percentage()))
		self.seriess=self.get_pie_seriess(slice.label())
		self.seriess.setLabelsVisible(True)
		self.seriess.setLabelsPosition(0)
		for i in self.seriess.slices():
			i.setBorderColor(QColor(179, 187, 201))
			i.setLabelColor(QColor(44, 49, 60))
			i.setLabelFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
		self.seriess.clicked.connect(self.slices_clicked)
		self.charts.removeAllSeries()
		self.charts.addSeries(self.seriess)
		self.charts.update()
	def get_pie_seriess(self,kad):
		series=QPieSeries()
		data=self.myclass.Konu_count(kad)
		for i in data:
			series.append(i[1],i[0])
		return series
	def slices_clicked(self,slice):
		for i in self.seriess.slices():
			i.setExploded(False)
			i.setLabelPosition(0)
			i.setLabelColor(QColor(44, 49, 60))
			i.setLabelFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
		slice.setExploded(True)
		slice.setLabelPosition(1)
		slice.setLabelColor(QColor(255, 255, 255))
		slice.setLabelFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
	def update_piechartl(self):
		self.seriesl=self.get_pie_series()
		self.seriesl.setLabelsVisible(True)
		self.seriesl.setLabelsPosition(0)
		for i in self.seriesl.slices():
			i.setBorderColor(QColor(179, 187, 201))
			i.setLabelColor(QColor(44, 49, 60))
			i.setLabelFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
		self.seriesl.slices()[0].setExploded(True)
		self.seriesl.clicked.connect(self.slice_clicked)
		self.chartl.removeAllSeries()
		self.chartl.addSeries(self.seriesl)
		self.chartl.update()
	def update_piecharts(self):
		self.seriess=self.get_pie_seriess(self.seriesl.slices()[0].label())
		self.seriess.setLabelsVisible(True)
		self.seriess.setLabelsPosition(0)
		for i in self.seriess.slices():
			i.setBorderColor(QColor(179, 187, 201))
			i.setLabelColor(QColor(44, 49, 60))
			i.setLabelFont(QtGui.QFont("Verdana", 8, QtGui.QFont.Bold))
		self.seriess.slices()[0].setExploded(True)
		self.seriess.clicked.connect(self.slices_clicked)
		self.charts.removeAllSeries()
		self.charts.addSeries(self.seriess)
		self.charts.update()
#endregion

#region popup messages
	def show_delete_popup(self,mytext,mybutton):
		msg = QMessageBox()
		msg.setWindowTitle("Uyarı")
		msg.setText("Silmek istediğinize emin misiniz?")
		msg.setIcon(QMessageBox.Critical)
		msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
		msg.setDefaultButton(QMessageBox.Cancel)
		msg.setInformativeText(mytext)
		msg.buttonClicked.connect(mybutton)
		msg.setWindowIcon(QIcon("images/exam.png"))
		x=msg.exec_()		
	def popup_deleteders_button(self,i):
		self.ders_sil_onay(i.text())
	def popup_deletekonu_button(self,i):
		self.konu_sil_onay(i.text())
	def popup_deletesoru_button(self,i):
		self.soru_sil_onay(i.text())
	def show_success_popup(self,mytext):
		msg = QMessageBox()
		msg.setWindowTitle("Bilgilendirme")
		msg.setText("İşlem başarılı.")
		msg.setIcon(QMessageBox.Information)
		msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
		msg.setDefaultButton(QMessageBox.Ok)
		msg.setInformativeText(mytext)
		msg.setWindowIcon(QIcon("images/exam.png"))
		x=msg.exec_()		
	def show_warning_popup(self,mytext):
		msg = QMessageBox()
		msg.setWindowTitle("Uyarı")
		msg.setText("İşlem başarısız.")
		msg.setIcon(QMessageBox.Warning)
		msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
		msg.setDefaultButton(QMessageBox.Ok)
		msg.setInformativeText(mytext)
		msg.setWindowIcon(QIcon("images/exam.png"))
		x=msg.exec_()	
	def show_detailed_warning_popup(self,mytext,mydetailedtext):
		msg = QMessageBox()
		msg.setWindowTitle("Uyarı")
		msg.setText("İşlem başarısız")
		msg.setIcon(QMessageBox.Warning)
		msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
		msg.setDefaultButton(QMessageBox.Ok)
		msg.setInformativeText(mytext)
		msg.setDetailedText(mydetailedtext)
		msg.setWindowIcon(QIcon("images/exam.png"))
		x=msg.exec_()
#endregion

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow(MainWindow)
sys.exit(app.exec_())