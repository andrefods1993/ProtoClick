# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCalendarWidget,
    QCheckBox, QComboBox, QDateEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QTimeEdit,
    QToolBox, QToolButton, QVBoxLayout, QWidget)
import rc_assets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 725)
        font = QFont()
        font.setFamilies([u"Poppins"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/assets/icons/logo_p.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(92, 96, 102);")
        self.horizontalLayout = QHBoxLayout(MainWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nav = QFrame(MainWindow)
        self.nav.setObjectName(u"nav")
        self.nav.setMaximumSize(QSize(200, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(0, 113, 143, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nav.setPalette(palette)
        font1 = QFont()
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.nav.setFont(font1)
        self.nav.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QFrame{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: rgb(234, 234, 234);\n"
"  border-radius: 5px;\n"
"  padding: 10px;\n"
"  text-align: left;\n"
"  color: #00718F;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #d6d6d6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #bfbfbf;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(48, 54, 63);\n"
"	color: #fff;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"    background-color: #5e6472;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 25, 58, 255), stop:1 rgba(31, 134, 160, 255));\n"
"}\n"
"")
        self.nav.setFrameShape(QFrame.StyledPanel)
        self.nav.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.nav)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_logo = QFrame(self.nav)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo = QLabel(self.frame_logo)
        self.logo.setObjectName(u"logo")

        self.horizontalLayout_2.addWidget(self.logo)


        self.verticalLayout.addWidget(self.frame_logo)

        self.frame_menu = QFrame(self.nav)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.toolBox_menu = QToolBox(self.frame_menu)
        self.toolBox_menu.setObjectName(u"toolBox_menu")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(10)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.toolBox_menu.setFont(font2)
        self.toolBox_menu.setStyleSheet(u"QScrollBar:horizontal {\n"
"    height: 1px; /* Altura da barra de rolagem */\n"
"}")
        self.m1_menu = QWidget()
        self.m1_menu.setObjectName(u"m1_menu")
        self.m1_menu.setGeometry(QRect(0, 0, 160, 545))
        self.verticalLayout_4 = QVBoxLayout(self.m1_menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn1_home = QPushButton(self.m1_menu)
        self.btn1_home.setObjectName(u"btn1_home")
        self.btn1_home.setMaximumSize(QSize(16777215, 16777215))
        self.btn1_home.setFont(font2)
        self.btn1_home.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u":/assets/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn1_home.setIcon(icon1)
        self.btn1_home.setIconSize(QSize(18, 18))

        self.verticalLayout_4.addWidget(self.btn1_home)

        self.btn2_usuarios = QPushButton(self.m1_menu)
        self.btn2_usuarios.setObjectName(u"btn2_usuarios")
        self.btn2_usuarios.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/assets/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn2_usuarios.setIcon(icon2)
        self.btn2_usuarios.setIconSize(QSize(18, 18))

        self.verticalLayout_4.addWidget(self.btn2_usuarios)

        self.btn3_clientes = QPushButton(self.m1_menu)
        self.btn3_clientes.setObjectName(u"btn3_clientes")
        self.btn3_clientes.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/assets/icons/clientes.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn3_clientes.setIcon(icon3)
        self.btn3_clientes.setIconSize(QSize(18, 18))

        self.verticalLayout_4.addWidget(self.btn3_clientes)

        self.btn4_protocolos = QPushButton(self.m1_menu)
        self.btn4_protocolos.setObjectName(u"btn4_protocolos")
        self.btn4_protocolos.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/assets/icons/protocolos.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn4_protocolos.setIcon(icon4)
        self.btn4_protocolos.setIconSize(QSize(18, 18))

        self.verticalLayout_4.addWidget(self.btn4_protocolos)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        icon5 = QIcon()
        icon5.addFile(u":/assets/icons/grid_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_menu.addItem(self.m1_menu, icon5, u"Menu")
        self.m2_configuracoes = QWidget()
        self.m2_configuracoes.setObjectName(u"m2_configuracoes")
        self.m2_configuracoes.setGeometry(QRect(0, 0, 160, 545))
        self.verticalLayout_5 = QVBoxLayout(self.m2_configuracoes)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn1_empresa = QPushButton(self.m2_configuracoes)
        self.btn1_empresa.setObjectName(u"btn1_empresa")
        self.btn1_empresa.setFont(font2)
        icon6 = QIcon()
        icon6.addFile(u":/assets/icons/empresa.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn1_empresa.setIcon(icon6)
        self.btn1_empresa.setIconSize(QSize(18, 18))

        self.verticalLayout_5.addWidget(self.btn1_empresa)

        self.btn2_tipoAtendimento = QPushButton(self.m2_configuracoes)
        self.btn2_tipoAtendimento.setObjectName(u"btn2_tipoAtendimento")
        self.btn2_tipoAtendimento.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u":/assets/icons/tp_atendimento.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn2_tipoAtendimento.setIcon(icon7)
        self.btn2_tipoAtendimento.setIconSize(QSize(18, 18))

        self.verticalLayout_5.addWidget(self.btn2_tipoAtendimento)

        self.btn3_avisos = QPushButton(self.m2_configuracoes)
        self.btn3_avisos.setObjectName(u"btn3_avisos")
        self.btn3_avisos.setFont(font2)
        icon8 = QIcon()
        icon8.addFile(u":/assets/icons/avisos.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn3_avisos.setIcon(icon8)
        self.btn3_avisos.setIconSize(QSize(18, 18))

        self.verticalLayout_5.addWidget(self.btn3_avisos)

        self.btn4_sobre = QPushButton(self.m2_configuracoes)
        self.btn4_sobre.setObjectName(u"btn4_sobre")
        icon9 = QIcon()
        icon9.addFile(u":/assets/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn4_sobre.setIcon(icon9)
        self.btn4_sobre.setIconSize(QSize(18, 18))

        self.verticalLayout_5.addWidget(self.btn4_sobre)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.lb_copyright = QLabel(self.m2_configuracoes)
        self.lb_copyright.setObjectName(u"lb_copyright")

        self.verticalLayout_5.addWidget(self.lb_copyright)

        icon10 = QIcon()
        icon10.addFile(u":/assets/icons/configuracoes_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_menu.addItem(self.m2_configuracoes, icon10, u"Configura\u00e7\u00f5es")

        self.verticalLayout_2.addWidget(self.toolBox_menu)


        self.verticalLayout.addWidget(self.frame_menu)


        self.horizontalLayout.addWidget(self.nav)

        self.main = QFrame(MainWindow)
        self.main.setObjectName(u"main")
        self.main.setMaximumSize(QSize(16777215, 16777215))
        self.main.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCalendarWidget {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: #fff;\n"
"    border: none;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item:selected {\n"
"    background-color: #00718F;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"	color: #00718F;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:pressed {\n"
"    background-color: #d0d0d0;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 5px 20px;\n"
"}\n"
"\n"
"QMenu::item:sele"
                        "cted {\n"
"    background-color: #00718F;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QFrame{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: rgb(234, 234, 234);\n"
"  border-radius: 5px;\n"
"  padding: 5px 10px;\n"
"  text-align: left;\n"
"  color: #00718F;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #d6d6d6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #bfbfbf;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #454A52;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #F2F2F2;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #EBEBEB;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #00718F;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #F2F2F2;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #EBEBEB;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1px solid #00718"
                        "F;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"	background-color: #EBEBEB;\n"
"	border: 1px solid #BFBFBF;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	background-color: rgb(48, 54, 63);\n"
"	color: #FFFFFF;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	padding: 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #5e6472;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 25, 58, 255), stop:1 rgba(31, 134, 160, 255));\n"
"}\n"
"\n"
"QToolButton {\n"
"  background-color: rgb(234, 234, 234);\n"
"  border-radius: 5px;\n"
"  padding: 5px 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"  background-color: #d6d6d6;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"  background-color: #bfbfbf;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: #fff;\n"
"    border: 1px solid #dcdcdc;\n"
"	border-radius: 0;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    "
                        "background-color: #00718F;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QTableWidget::item:focus {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #00718F;\n"
"    outline: none;\n"
"	color: #000;\n"
"}\n"
"\n"
"QTableWidget QScrollBar:horizontal {\n"
"    border: 1px solid #CCCCCC;\n"
"    background-color: #FFF;\n"
"    height: 15px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:horizontal {\n"
"    background-color: #00718F;\n"
"    min-width: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-line:horizontal {\n"
"    background: transparent;\n"
"    width: 0px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::sub-line:horizontal {\n"
"    background: transparent;\n"
"    width: 0px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QTableWidget QScrollBar:vertical {\n"
""
                        "    border: 1px solid #CCCCCC;\n"
"    background-color: #FFF;\n"
"    width: 15px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:vertical {\n"
"    background-color: #00718F;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-line:vertical {\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::sub-line:vertical {\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked {\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"    background-color: #00718F;\n"
"    border: 2px solid #00718F;\n"
"    border-radius: 3px;\n"
"	ima"
                        "ge: url(:/assets/icons/close.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid #999;\n"
"}\n"
"\n"
"QCheckBox::indicator:pressed {\n"
"    border: 2px solid #555;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"	margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    position: absolute;\n"
"    top: -10 px;\n"
"    left: 10px; \n"
"    padding: -5px;\n"
"	margin: 5px;\n"
"}\n"
"\n"
"Line {\n"
"	background-color: #00718F;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.329545 rgba(255, 255, 255, 255), stop:0.471591 rgba(0, 113, 143, 255));\n"
"    border: 2px so"
                        "lid #00718F;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #999;\n"
"}\n"
"\n"
"QRadioButton::indicator:pressed {\n"
"    border: 2px solid #555;\n"
"}\n"
"\n"
"QDateEdit, QTimeEdit {\n"
"    padding: 5px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: #FFF;\n"
"}\n"
"\n"
"QDateEdit::down-button, QTimeEdit::down-button {\n"
"    border: 1px solid #ccc;\n"
"    background-color: #f0f0f0;\n"
"	border-bottom-left-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::up-button, QTimeEdit::up-button {\n"
"    border: 1px solid #ccc;\n"
"    background-color: #f0f0f0;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::up-arrow, QTimeEdit::up-arrow {\n"
"	image: url(:/assets/icons/up.svg);\n"
"	width: 15px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow, QTimeEdit::down-arrow {\n"
"	image: url(:/assets/icons/down.svg);\n"
"	width: 15px;\n"
"}\n"
"\n"
"QDateEdit:hover, "
                        "QTimeEdit:hover {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"QDateEdit:focus, QTimeEdit:focus {\n"
"    border: 1px solid #00718F;\n"
"}\n"
"\n"
"QDateEdit::down-button:hover, QTimeEdit::down-button:hover, QDateEdit::up-button:hover, QTimeEdit::up-button:hover, QDateTimeEdit::drop-down:hover {\n"
"	background-color: #e0e0e0;\n"
"}\n"
"\n"
"QDateEdit::down-button:pressed, QTimeEdit::down-button:pressed, QDateEdit::up-button:pressed, QTimeEdit::up-button:pressed, QDateTimeEdit::drop-down:pressed {\n"
"	background-color: #d0d0d0;\n"
"}\n"
"\n"
"QDateTimeEdit::drop-down {\n"
"    border: 1px solid #ccc;\n"
"    background-color: #f0f0f0;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    padding: 5px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: #FFF;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right;\n"
"    border-left: 1px solid #ccc;\n"
"    border-radiu"
                        "s: 3px;\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/assets/icons/down.svg);\n"
"	width: 15px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QComboBox::drop-down:pressed {\n"
"    background-color: #d0d0d0;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    scrollbar:vertical;\n"
"    background-color: #f2f2f2;\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    border: 1px solid #CCCCCC;\n"
"    background-color: #FFF;\n"
"    width: 15px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: #00718F;\n"
"    min-height: 20px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::add-line:vertical {\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QComboBox QScrollBar::sub-line:vertical {\n"
"    background: transparent;\n"
"    height: 0px;\n"
"   "
                        " subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_header = QFrame(self.main)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame1_toggleButton = QFrame(self.frame_header)
        self.frame1_toggleButton.setObjectName(u"frame1_toggleButton")
        self.frame1_toggleButton.setFrameShape(QFrame.StyledPanel)
        self.frame1_toggleButton.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame1_toggleButton)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_toggleButton = QToolButton(self.frame1_toggleButton)
        self.btn_toggleButton.setObjectName(u"btn_toggleButton")
        self.btn_toggleButton.setStyleSheet(u"padding:5px;")
        icon11 = QIcon()
        icon11.addFile(u":/assets/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggleButton.setIcon(icon11)
        self.btn_toggleButton.setIconSize(QSize(20, 20))
        self.btn_toggleButton.setCheckable(False)
        self.btn_toggleButton.setChecked(False)

        self.horizontalLayout_12.addWidget(self.btn_toggleButton)


        self.horizontalLayout_3.addWidget(self.frame1_toggleButton)

        self.frame2_socialMedia = QFrame(self.frame_header)
        self.frame2_socialMedia.setObjectName(u"frame2_socialMedia")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame2_socialMedia.sizePolicy().hasHeightForWidth())
        self.frame2_socialMedia.setSizePolicy(sizePolicy)
        self.frame2_socialMedia.setFrameShape(QFrame.StyledPanel)
        self.frame2_socialMedia.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame2_socialMedia)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_3)

        self.btn1_whatsApp = QToolButton(self.frame2_socialMedia)
        self.btn1_whatsApp.setObjectName(u"btn1_whatsApp")
        self.btn1_whatsApp.setStyleSheet(u"padding:5px;")
        icon12 = QIcon()
        icon12.addFile(u":/assets/icons/whatsapp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn1_whatsApp.setIcon(icon12)
        self.btn1_whatsApp.setIconSize(QSize(20, 20))

        self.horizontalLayout_27.addWidget(self.btn1_whatsApp)

        self.btn2_instagram = QToolButton(self.frame2_socialMedia)
        self.btn2_instagram.setObjectName(u"btn2_instagram")
        self.btn2_instagram.setStyleSheet(u"padding:5px;")
        icon13 = QIcon()
        icon13.addFile(u":/assets/icons/insta.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn2_instagram.setIcon(icon13)
        self.btn2_instagram.setIconSize(QSize(20, 20))

        self.horizontalLayout_27.addWidget(self.btn2_instagram)

        self.btn3_linkedin = QToolButton(self.frame2_socialMedia)
        self.btn3_linkedin.setObjectName(u"btn3_linkedin")
        self.btn3_linkedin.setStyleSheet(u"padding:5px;")
        icon14 = QIcon()
        icon14.addFile(u":/assets/icons/linkedin.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn3_linkedin.setIcon(icon14)
        self.btn3_linkedin.setIconSize(QSize(20, 20))

        self.horizontalLayout_27.addWidget(self.btn3_linkedin)

        self.btn4_github = QToolButton(self.frame2_socialMedia)
        self.btn4_github.setObjectName(u"btn4_github")
        self.btn4_github.setStyleSheet(u"padding:5px;")
        icon15 = QIcon()
        icon15.addFile(u":/assets/icons/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn4_github.setIcon(icon15)
        self.btn4_github.setIconSize(QSize(20, 20))

        self.horizontalLayout_27.addWidget(self.btn4_github)

        self.btn5_email = QToolButton(self.frame2_socialMedia)
        self.btn5_email.setObjectName(u"btn5_email")
        icon16 = QIcon()
        icon16.addFile(u":/assets/icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn5_email.setIcon(icon16)
        self.btn5_email.setIconSize(QSize(20, 20))

        self.horizontalLayout_27.addWidget(self.btn5_email)


        self.horizontalLayout_3.addWidget(self.frame2_socialMedia)


        self.verticalLayout_3.addWidget(self.frame_header)

        self.frame_section = QFrame(self.main)
        self.frame_section.setObjectName(u"frame_section")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_section.sizePolicy().hasHeightForWidth())
        self.frame_section.setSizePolicy(sizePolicy1)
        self.frame_section.setFont(font)
        self.frame_section.setStyleSheet(u"")
        self.frame_section.setFrameShape(QFrame.StyledPanel)
        self.frame_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_section)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.section = QStackedWidget(self.frame_section)
        self.section.setObjectName(u"section")
        self.s1_home = QWidget()
        self.s1_home.setObjectName(u"s1_home")
        self.verticalLayout_9 = QVBoxLayout(self.s1_home)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.calendario = QCalendarWidget(self.s1_home)
        self.calendario.setObjectName(u"calendario")
        self.calendario.setNavigationBarVisible(True)
        self.calendario.setDateEditEnabled(True)

        self.verticalLayout_9.addWidget(self.calendario)

        self.frame_informacao = QFrame(self.s1_home)
        self.frame_informacao.setObjectName(u"frame_informacao")
        self.frame_informacao.setFrameShape(QFrame.StyledPanel)
        self.frame_informacao.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_informacao)

        self.section.addWidget(self.s1_home)
        self.s8_sobre = QWidget()
        self.s8_sobre.setObjectName(u"s8_sobre")
        self.s8_sobre.setFont(font)
        self.verticalLayout_35 = QVBoxLayout(self.s8_sobre)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame1_headerSobre = QFrame(self.s8_sobre)
        self.frame1_headerSobre.setObjectName(u"frame1_headerSobre")
        self.frame1_headerSobre.setFrameShape(QFrame.StyledPanel)
        self.frame1_headerSobre.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame1_headerSobre)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lb_titleSobre = QLabel(self.frame1_headerSobre)
        self.lb_titleSobre.setObjectName(u"lb_titleSobre")
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.lb_titleSobre.setFont(font3)

        self.verticalLayout_7.addWidget(self.lb_titleSobre)

        self.lineSobre = QFrame(self.frame1_headerSobre)
        self.lineSobre.setObjectName(u"lineSobre")
        self.lineSobre.setStyleSheet(u"background-color: #00718F;")
        self.lineSobre.setFrameShape(QFrame.HLine)
        self.lineSobre.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.lineSobre)


        self.verticalLayout_35.addWidget(self.frame1_headerSobre)

        self.frame2_mainSobre = QFrame(self.s8_sobre)
        self.frame2_mainSobre.setObjectName(u"frame2_mainSobre")
        sizePolicy1.setHeightForWidth(self.frame2_mainSobre.sizePolicy().hasHeightForWidth())
        self.frame2_mainSobre.setSizePolicy(sizePolicy1)
        self.frame2_mainSobre.setFrameShape(QFrame.StyledPanel)
        self.frame2_mainSobre.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame2_mainSobre)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.lb1_sobre = QLabel(self.frame2_mainSobre)
        self.lb1_sobre.setObjectName(u"lb1_sobre")

        self.verticalLayout_36.addWidget(self.lb1_sobre)

        self.lb2_sobre = QLabel(self.frame2_mainSobre)
        self.lb2_sobre.setObjectName(u"lb2_sobre")

        self.verticalLayout_36.addWidget(self.lb2_sobre)

        self.lb3_sobre = QLabel(self.frame2_mainSobre)
        self.lb3_sobre.setObjectName(u"lb3_sobre")

        self.verticalLayout_36.addWidget(self.lb3_sobre)

        self.label = QLabel(self.frame2_mainSobre)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        font4.setPointSize(8)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.verticalLayout_36.addWidget(self.label)


        self.verticalLayout_35.addWidget(self.frame2_mainSobre)

        self.section.addWidget(self.s8_sobre)
        self.s7_avisos = QWidget()
        self.s7_avisos.setObjectName(u"s7_avisos")
        self.verticalLayout_34 = QVBoxLayout(self.s7_avisos)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_headerAvisos = QFrame(self.s7_avisos)
        self.frame_headerAvisos.setObjectName(u"frame_headerAvisos")
        self.frame_headerAvisos.setFrameShape(QFrame.StyledPanel)
        self.frame_headerAvisos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_headerAvisos)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lb_titleAvisos = QLabel(self.frame_headerAvisos)
        self.lb_titleAvisos.setObjectName(u"lb_titleAvisos")
        self.lb_titleAvisos.setFont(font3)

        self.verticalLayout_10.addWidget(self.lb_titleAvisos)

        self.lineAvisos = QFrame(self.frame_headerAvisos)
        self.lineAvisos.setObjectName(u"lineAvisos")
        self.lineAvisos.setStyleSheet(u"background-color: #00718F;")
        self.lineAvisos.setFrameShape(QFrame.HLine)
        self.lineAvisos.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.lineAvisos)


        self.verticalLayout_34.addWidget(self.frame_headerAvisos)

        self.aba_avisos = QTabWidget(self.s7_avisos)
        self.aba_avisos.setObjectName(u"aba_avisos")
        self.aba_avisos.setFont(font)
        self.aba1_listaAvisos = QWidget()
        self.aba1_listaAvisos.setObjectName(u"aba1_listaAvisos")
        self.verticalLayout_30 = QVBoxLayout(self.aba1_listaAvisos)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame1_listaAvisos = QFrame(self.aba1_listaAvisos)
        self.frame1_listaAvisos.setObjectName(u"frame1_listaAvisos")
        self.frame1_listaAvisos.setFrameShape(QFrame.StyledPanel)
        self.frame1_listaAvisos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame1_listaAvisos)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame1_btnAvisos = QFrame(self.frame1_listaAvisos)
        self.frame1_btnAvisos.setObjectName(u"frame1_btnAvisos")
        self.frame1_btnAvisos.setFrameShape(QFrame.StyledPanel)
        self.frame1_btnAvisos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame1_btnAvisos)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.btn1_editarAvisos = QPushButton(self.frame1_btnAvisos)
        self.btn1_editarAvisos.setObjectName(u"btn1_editarAvisos")
        self.btn1_editarAvisos.setFont(font)
        icon17 = QIcon()
        icon17.addFile(u":/assets/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn1_editarAvisos.setIcon(icon17)
        self.btn1_editarAvisos.setIconSize(QSize(18, 18))

        self.horizontalLayout_23.addWidget(self.btn1_editarAvisos)

        self.btn2_excluirAvisos = QPushButton(self.frame1_btnAvisos)
        self.btn2_excluirAvisos.setObjectName(u"btn2_excluirAvisos")
        self.btn2_excluirAvisos.setFont(font)
        icon18 = QIcon()
        icon18.addFile(u":/assets/icons/lixeira.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn2_excluirAvisos.setIcon(icon18)
        self.btn2_excluirAvisos.setIconSize(QSize(18, 18))

        self.horizontalLayout_23.addWidget(self.btn2_excluirAvisos)


        self.horizontalLayout_22.addWidget(self.frame1_btnAvisos)

        self.frame2_pesquisaAvisos = QFrame(self.frame1_listaAvisos)
        self.frame2_pesquisaAvisos.setObjectName(u"frame2_pesquisaAvisos")
        self.frame2_pesquisaAvisos.setFrameShape(QFrame.StyledPanel)
        self.frame2_pesquisaAvisos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame2_pesquisaAvisos)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.barLine_pesquisaAvisos = QLineEdit(self.frame2_pesquisaAvisos)
        self.barLine_pesquisaAvisos.setObjectName(u"barLine_pesquisaAvisos")
        self.barLine_pesquisaAvisos.setFont(font)

        self.horizontalLayout_24.addWidget(self.barLine_pesquisaAvisos)

        self.btn_pesquisaAvisos = QToolButton(self.frame2_pesquisaAvisos)
        self.btn_pesquisaAvisos.setObjectName(u"btn_pesquisaAvisos")
        icon19 = QIcon()
        icon19.addFile(u":/assets/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisaAvisos.setIcon(icon19)
        self.btn_pesquisaAvisos.setIconSize(QSize(18, 18))

        self.horizontalLayout_24.addWidget(self.btn_pesquisaAvisos)


        self.horizontalLayout_22.addWidget(self.frame2_pesquisaAvisos)


        self.verticalLayout_30.addWidget(self.frame1_listaAvisos)

        self.tabela_avisos = QTableWidget(self.aba1_listaAvisos)
        if (self.tabela_avisos.columnCount() < 4):
            self.tabela_avisos.setColumnCount(4)
        font5 = QFont()
        font5.setFamilies([u"Poppins"])
        font5.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.tabela_avisos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.tabela_avisos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.tabela_avisos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.tabela_avisos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabela_avisos.setObjectName(u"tabela_avisos")
        self.tabela_avisos.setFont(font5)
        self.tabela_avisos.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tabela_avisos.setProperty("showDropIndicator", False)
        self.tabela_avisos.setDragDropOverwriteMode(False)
        self.tabela_avisos.setAlternatingRowColors(True)
        self.tabela_avisos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_avisos.setSortingEnabled(True)
        self.tabela_avisos.horizontalHeader().setCascadingSectionResizes(False)
        self.tabela_avisos.horizontalHeader().setDefaultSectionSize(200)
        self.tabela_avisos.horizontalHeader().setHighlightSections(True)
        self.tabela_avisos.verticalHeader().setMinimumSectionSize(90)

        self.verticalLayout_30.addWidget(self.tabela_avisos)

        icon20 = QIcon()
        icon20.addFile(u":/assets/icons/lista_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_avisos.addTab(self.aba1_listaAvisos, icon20, "")
        self.aba2_cadastroAvisos = QWidget()
        self.aba2_cadastroAvisos.setObjectName(u"aba2_cadastroAvisos")
        self.verticalLayout_32 = QVBoxLayout(self.aba2_cadastroAvisos)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame1_mainCadastroAvisos = QFrame(self.aba2_cadastroAvisos)
        self.frame1_mainCadastroAvisos.setObjectName(u"frame1_mainCadastroAvisos")
        sizePolicy1.setHeightForWidth(self.frame1_mainCadastroAvisos.sizePolicy().hasHeightForWidth())
        self.frame1_mainCadastroAvisos.setSizePolicy(sizePolicy1)
        self.frame1_mainCadastroAvisos.setFrameShape(QFrame.StyledPanel)
        self.frame1_mainCadastroAvisos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame1_mainCadastroAvisos)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_idAvisos = QFrame(self.frame1_mainCadastroAvisos)
        self.frame_idAvisos.setObjectName(u"frame_idAvisos")
        self.frame_idAvisos.setFrameShape(QFrame.StyledPanel)
        self.frame_idAvisos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_idAvisos)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lb_avisosId = QLabel(self.frame_idAvisos)
        self.lb_avisosId.setObjectName(u"lb_avisosId")
        font6 = QFont()
        font6.setFamilies([u"Poppins"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.lb_avisosId.setFont(font6)
        self.lb_avisosId.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.lb_avisosId)

        self.ed_avisosId = QLineEdit(self.frame_idAvisos)
        self.ed_avisosId.setObjectName(u"ed_avisosId")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ed_avisosId.sizePolicy().hasHeightForWidth())
        self.ed_avisosId.setSizePolicy(sizePolicy2)
        self.ed_avisosId.setMaximumSize(QSize(356, 16777215))
        self.ed_avisosId.setFont(font5)
        self.ed_avisosId.setInputMethodHints(Qt.ImhNone)
        self.ed_avisosId.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.ed_avisosId)

        self.cb_avisosDesativado = QCheckBox(self.frame_idAvisos)
        self.cb_avisosDesativado.setObjectName(u"cb_avisosDesativado")
        self.cb_avisosDesativado.setEnabled(False)
        self.cb_avisosDesativado.setFont(font5)
        self.cb_avisosDesativado.setCheckable(True)

        self.horizontalLayout_25.addWidget(self.cb_avisosDesativado)


        self.verticalLayout_33.addWidget(self.frame_idAvisos, 0, Qt.AlignLeft)

        self.lb_avisosDescricao = QLabel(self.frame1_mainCadastroAvisos)
        self.lb_avisosDescricao.setObjectName(u"lb_avisosDescricao")
        self.lb_avisosDescricao.setFont(font6)
        self.lb_avisosDescricao.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.lb_avisosDescricao)

        self.ed_avisosDescricao = QLineEdit(self.frame1_mainCadastroAvisos)
        self.ed_avisosDescricao.setObjectName(u"ed_avisosDescricao")
        self.ed_avisosDescricao.setFont(font5)

        self.verticalLayout_33.addWidget(self.ed_avisosDescricao)

        self.lb_avisosMensagem = QLabel(self.frame1_mainCadastroAvisos)
        self.lb_avisosMensagem.setObjectName(u"lb_avisosMensagem")
        self.lb_avisosMensagem.setFont(font6)
        self.lb_avisosMensagem.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.lb_avisosMensagem)

        self.ed_avisosMensagem = QTextEdit(self.frame1_mainCadastroAvisos)
        self.ed_avisosMensagem.setObjectName(u"ed_avisosMensagem")
        self.ed_avisosMensagem.setFont(font5)

        self.verticalLayout_33.addWidget(self.ed_avisosMensagem)

        self.verticalSpacer_5 = QSpacerItem(20, 198, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_5)


        self.verticalLayout_32.addWidget(self.frame1_mainCadastroAvisos)

        self.frame2_btnCadastroAvisos = QFrame(self.aba2_cadastroAvisos)
        self.frame2_btnCadastroAvisos.setObjectName(u"frame2_btnCadastroAvisos")
        self.frame2_btnCadastroAvisos.setFrameShape(QFrame.StyledPanel)
        self.frame2_btnCadastroAvisos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame2_btnCadastroAvisos)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_5 = QSpacerItem(312, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_5)

        self.btn_limparCadastroAvisos = QPushButton(self.frame2_btnCadastroAvisos)
        self.btn_limparCadastroAvisos.setObjectName(u"btn_limparCadastroAvisos")
        self.btn_limparCadastroAvisos.setFont(font)
        icon21 = QIcon()
        icon21.addFile(u":/assets/icons/limpar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limparCadastroAvisos.setIcon(icon21)
        self.btn_limparCadastroAvisos.setIconSize(QSize(18, 18))

        self.horizontalLayout_26.addWidget(self.btn_limparCadastroAvisos)

        self.btn_salvarCadastroAvisos = QPushButton(self.frame2_btnCadastroAvisos)
        self.btn_salvarCadastroAvisos.setObjectName(u"btn_salvarCadastroAvisos")
        self.btn_salvarCadastroAvisos.setFont(font)
        icon22 = QIcon()
        icon22.addFile(u":/assets/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvarCadastroAvisos.setIcon(icon22)
        self.btn_salvarCadastroAvisos.setIconSize(QSize(18, 18))

        self.horizontalLayout_26.addWidget(self.btn_salvarCadastroAvisos)


        self.verticalLayout_32.addWidget(self.frame2_btnCadastroAvisos)

        icon23 = QIcon()
        icon23.addFile(u":/assets/icons/add_alt_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_avisos.addTab(self.aba2_cadastroAvisos, icon23, "")

        self.verticalLayout_34.addWidget(self.aba_avisos)

        self.section.addWidget(self.s7_avisos)
        self.s6_tipos_atendimento = QWidget()
        self.s6_tipos_atendimento.setObjectName(u"s6_tipos_atendimento")
        self.verticalLayout_31 = QVBoxLayout(self.s6_tipos_atendimento)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_headerTiposAtendimento = QFrame(self.s6_tipos_atendimento)
        self.frame_headerTiposAtendimento.setObjectName(u"frame_headerTiposAtendimento")
        self.frame_headerTiposAtendimento.setFrameShape(QFrame.StyledPanel)
        self.frame_headerTiposAtendimento.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_headerTiposAtendimento)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.lb_titleTiposAtendimento = QLabel(self.frame_headerTiposAtendimento)
        self.lb_titleTiposAtendimento.setObjectName(u"lb_titleTiposAtendimento")
        self.lb_titleTiposAtendimento.setFont(font3)

        self.verticalLayout_26.addWidget(self.lb_titleTiposAtendimento)

        self.lineTiposAtendimento = QFrame(self.frame_headerTiposAtendimento)
        self.lineTiposAtendimento.setObjectName(u"lineTiposAtendimento")
        self.lineTiposAtendimento.setStyleSheet(u"background-color: #00718F;")
        self.lineTiposAtendimento.setFrameShape(QFrame.HLine)
        self.lineTiposAtendimento.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.lineTiposAtendimento)


        self.verticalLayout_31.addWidget(self.frame_headerTiposAtendimento)

        self.aba_tipos_atendimento = QTabWidget(self.s6_tipos_atendimento)
        self.aba_tipos_atendimento.setObjectName(u"aba_tipos_atendimento")
        self.aba_tipos_atendimento.setFont(font)
        self.aba1_listaTiposAtendimento = QWidget()
        self.aba1_listaTiposAtendimento.setObjectName(u"aba1_listaTiposAtendimento")
        self.verticalLayout_27 = QVBoxLayout(self.aba1_listaTiposAtendimento)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame1_listaTiposAtendimento = QFrame(self.aba1_listaTiposAtendimento)
        self.frame1_listaTiposAtendimento.setObjectName(u"frame1_listaTiposAtendimento")
        self.frame1_listaTiposAtendimento.setFrameShape(QFrame.StyledPanel)
        self.frame1_listaTiposAtendimento.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame1_listaTiposAtendimento)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame1_btnTiposAtendimento = QFrame(self.frame1_listaTiposAtendimento)
        self.frame1_btnTiposAtendimento.setObjectName(u"frame1_btnTiposAtendimento")
        self.frame1_btnTiposAtendimento.setFrameShape(QFrame.StyledPanel)
        self.frame1_btnTiposAtendimento.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame1_btnTiposAtendimento)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn1_editarTiposAtendimento = QPushButton(self.frame1_btnTiposAtendimento)
        self.btn1_editarTiposAtendimento.setObjectName(u"btn1_editarTiposAtendimento")
        self.btn1_editarTiposAtendimento.setFont(font)
        self.btn1_editarTiposAtendimento.setIcon(icon17)
        self.btn1_editarTiposAtendimento.setIconSize(QSize(18, 18))

        self.horizontalLayout_18.addWidget(self.btn1_editarTiposAtendimento)

        self.btn2_excluirTiposAtendimento = QPushButton(self.frame1_btnTiposAtendimento)
        self.btn2_excluirTiposAtendimento.setObjectName(u"btn2_excluirTiposAtendimento")
        self.btn2_excluirTiposAtendimento.setFont(font)
        self.btn2_excluirTiposAtendimento.setIcon(icon18)
        self.btn2_excluirTiposAtendimento.setIconSize(QSize(18, 18))

        self.horizontalLayout_18.addWidget(self.btn2_excluirTiposAtendimento)


        self.horizontalLayout_15.addWidget(self.frame1_btnTiposAtendimento)

        self.frame2_pesquisaTiposAtendimento = QFrame(self.frame1_listaTiposAtendimento)
        self.frame2_pesquisaTiposAtendimento.setObjectName(u"frame2_pesquisaTiposAtendimento")
        self.frame2_pesquisaTiposAtendimento.setFrameShape(QFrame.StyledPanel)
        self.frame2_pesquisaTiposAtendimento.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame2_pesquisaTiposAtendimento)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.barLine_pesquisaTiposAtendimento = QLineEdit(self.frame2_pesquisaTiposAtendimento)
        self.barLine_pesquisaTiposAtendimento.setObjectName(u"barLine_pesquisaTiposAtendimento")
        self.barLine_pesquisaTiposAtendimento.setFont(font)

        self.horizontalLayout_19.addWidget(self.barLine_pesquisaTiposAtendimento)

        self.btn_pesquisaTiposAtendimento = QToolButton(self.frame2_pesquisaTiposAtendimento)
        self.btn_pesquisaTiposAtendimento.setObjectName(u"btn_pesquisaTiposAtendimento")
        self.btn_pesquisaTiposAtendimento.setIcon(icon19)
        self.btn_pesquisaTiposAtendimento.setIconSize(QSize(18, 18))

        self.horizontalLayout_19.addWidget(self.btn_pesquisaTiposAtendimento)


        self.horizontalLayout_15.addWidget(self.frame2_pesquisaTiposAtendimento)


        self.verticalLayout_27.addWidget(self.frame1_listaTiposAtendimento)

        self.tabela_tiposAtendimento = QTableWidget(self.aba1_listaTiposAtendimento)
        if (self.tabela_tiposAtendimento.columnCount() < 3):
            self.tabela_tiposAtendimento.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tabela_tiposAtendimento.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font5);
        self.tabela_tiposAtendimento.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self.tabela_tiposAtendimento.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tabela_tiposAtendimento.setObjectName(u"tabela_tiposAtendimento")
        self.tabela_tiposAtendimento.setFont(font5)
        self.tabela_tiposAtendimento.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_tiposAtendimento.setProperty("showDropIndicator", False)
        self.tabela_tiposAtendimento.setDragDropOverwriteMode(False)
        self.tabela_tiposAtendimento.setAlternatingRowColors(True)
        self.tabela_tiposAtendimento.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_tiposAtendimento.setSortingEnabled(True)

        self.verticalLayout_27.addWidget(self.tabela_tiposAtendimento)

        self.aba_tipos_atendimento.addTab(self.aba1_listaTiposAtendimento, icon20, "")
        self.aba2_cadastroTiposAtendimento = QWidget()
        self.aba2_cadastroTiposAtendimento.setObjectName(u"aba2_cadastroTiposAtendimento")
        self.verticalLayout_28 = QVBoxLayout(self.aba2_cadastroTiposAtendimento)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame1_mainCadastroTiposAtendimento = QFrame(self.aba2_cadastroTiposAtendimento)
        self.frame1_mainCadastroTiposAtendimento.setObjectName(u"frame1_mainCadastroTiposAtendimento")
        sizePolicy1.setHeightForWidth(self.frame1_mainCadastroTiposAtendimento.sizePolicy().hasHeightForWidth())
        self.frame1_mainCadastroTiposAtendimento.setSizePolicy(sizePolicy1)
        self.frame1_mainCadastroTiposAtendimento.setFrameShape(QFrame.StyledPanel)
        self.frame1_mainCadastroTiposAtendimento.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame1_mainCadastroTiposAtendimento)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_idTiposAtendimento = QFrame(self.frame1_mainCadastroTiposAtendimento)
        self.frame_idTiposAtendimento.setObjectName(u"frame_idTiposAtendimento")
        self.frame_idTiposAtendimento.setFrameShape(QFrame.StyledPanel)
        self.frame_idTiposAtendimento.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_idTiposAtendimento)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lb_tiposAtendimentoId = QLabel(self.frame_idTiposAtendimento)
        self.lb_tiposAtendimentoId.setObjectName(u"lb_tiposAtendimentoId")
        self.lb_tiposAtendimentoId.setFont(font6)
        self.lb_tiposAtendimentoId.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lb_tiposAtendimentoId)

        self.ed_tiposAtendimentoId = QLineEdit(self.frame_idTiposAtendimento)
        self.ed_tiposAtendimentoId.setObjectName(u"ed_tiposAtendimentoId")
        sizePolicy2.setHeightForWidth(self.ed_tiposAtendimentoId.sizePolicy().hasHeightForWidth())
        self.ed_tiposAtendimentoId.setSizePolicy(sizePolicy2)
        self.ed_tiposAtendimentoId.setMaximumSize(QSize(356, 16777215))
        self.ed_tiposAtendimentoId.setFont(font5)
        self.ed_tiposAtendimentoId.setInputMethodHints(Qt.ImhNone)
        self.ed_tiposAtendimentoId.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.ed_tiposAtendimentoId)

        self.cb_tiposAtendimentoDesativado = QCheckBox(self.frame_idTiposAtendimento)
        self.cb_tiposAtendimentoDesativado.setObjectName(u"cb_tiposAtendimentoDesativado")
        self.cb_tiposAtendimentoDesativado.setEnabled(False)
        self.cb_tiposAtendimentoDesativado.setFont(font5)
        self.cb_tiposAtendimentoDesativado.setCheckable(True)

        self.horizontalLayout_21.addWidget(self.cb_tiposAtendimentoDesativado)


        self.verticalLayout_29.addWidget(self.frame_idTiposAtendimento, 0, Qt.AlignLeft)

        self.lb_tiposAtendimentoDescricao = QLabel(self.frame1_mainCadastroTiposAtendimento)
        self.lb_tiposAtendimentoDescricao.setObjectName(u"lb_tiposAtendimentoDescricao")
        self.lb_tiposAtendimentoDescricao.setFont(font6)
        self.lb_tiposAtendimentoDescricao.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.lb_tiposAtendimentoDescricao)

        self.ed_tiposAtendimentoDescricao = QLineEdit(self.frame1_mainCadastroTiposAtendimento)
        self.ed_tiposAtendimentoDescricao.setObjectName(u"ed_tiposAtendimentoDescricao")
        font7 = QFont()
        font7.setFamilies([u"Poppins"])
        font7.setPointSize(10)
        font7.setUnderline(False)
        self.ed_tiposAtendimentoDescricao.setFont(font7)
        self.ed_tiposAtendimentoDescricao.setAlignment(Qt.AlignCenter)
        self.ed_tiposAtendimentoDescricao.setDragEnabled(False)
        self.ed_tiposAtendimentoDescricao.setReadOnly(False)
        self.ed_tiposAtendimentoDescricao.setClearButtonEnabled(True)

        self.verticalLayout_29.addWidget(self.ed_tiposAtendimentoDescricao)

        self.verticalSpacer_4 = QSpacerItem(20, 198, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_4)


        self.verticalLayout_28.addWidget(self.frame1_mainCadastroTiposAtendimento)

        self.frame2_btnCadastroTiposAtendimento = QFrame(self.aba2_cadastroTiposAtendimento)
        self.frame2_btnCadastroTiposAtendimento.setObjectName(u"frame2_btnCadastroTiposAtendimento")
        self.frame2_btnCadastroTiposAtendimento.setFrameShape(QFrame.StyledPanel)
        self.frame2_btnCadastroTiposAtendimento.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame2_btnCadastroTiposAtendimento)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_4 = QSpacerItem(312, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)

        self.btn_limparCadastroTiposAtendimento = QPushButton(self.frame2_btnCadastroTiposAtendimento)
        self.btn_limparCadastroTiposAtendimento.setObjectName(u"btn_limparCadastroTiposAtendimento")
        self.btn_limparCadastroTiposAtendimento.setFont(font)
        self.btn_limparCadastroTiposAtendimento.setIcon(icon21)
        self.btn_limparCadastroTiposAtendimento.setIconSize(QSize(18, 18))

        self.horizontalLayout_20.addWidget(self.btn_limparCadastroTiposAtendimento)

        self.btn_salvarCadastroTiposAtendimento = QPushButton(self.frame2_btnCadastroTiposAtendimento)
        self.btn_salvarCadastroTiposAtendimento.setObjectName(u"btn_salvarCadastroTiposAtendimento")
        self.btn_salvarCadastroTiposAtendimento.setFont(font)
        self.btn_salvarCadastroTiposAtendimento.setIcon(icon22)
        self.btn_salvarCadastroTiposAtendimento.setIconSize(QSize(18, 18))

        self.horizontalLayout_20.addWidget(self.btn_salvarCadastroTiposAtendimento)


        self.verticalLayout_28.addWidget(self.frame2_btnCadastroTiposAtendimento)

        self.aba_tipos_atendimento.addTab(self.aba2_cadastroTiposAtendimento, icon23, "")

        self.verticalLayout_31.addWidget(self.aba_tipos_atendimento)

        self.section.addWidget(self.s6_tipos_atendimento)
        self.s5_empresas = QWidget()
        self.s5_empresas.setObjectName(u"s5_empresas")
        self.verticalLayout_23 = QVBoxLayout(self.s5_empresas)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_headerEmpresa = QFrame(self.s5_empresas)
        self.frame_headerEmpresa.setObjectName(u"frame_headerEmpresa")
        self.frame_headerEmpresa.setFrameShape(QFrame.StyledPanel)
        self.frame_headerEmpresa.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_headerEmpresa)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.lb_titleEmpresa = QLabel(self.frame_headerEmpresa)
        self.lb_titleEmpresa.setObjectName(u"lb_titleEmpresa")
        self.lb_titleEmpresa.setFont(font3)

        self.verticalLayout_22.addWidget(self.lb_titleEmpresa)

        self.lineEmpresa = QFrame(self.frame_headerEmpresa)
        self.lineEmpresa.setObjectName(u"lineEmpresa")
        self.lineEmpresa.setStyleSheet(u"background-color: #00718F;")
        self.lineEmpresa.setFrameShape(QFrame.HLine)
        self.lineEmpresa.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_22.addWidget(self.lineEmpresa)


        self.verticalLayout_23.addWidget(self.frame_headerEmpresa)

        self.frame_mainEmpresa = QFrame(self.s5_empresas)
        self.frame_mainEmpresa.setObjectName(u"frame_mainEmpresa")
        sizePolicy1.setHeightForWidth(self.frame_mainEmpresa.sizePolicy().hasHeightForWidth())
        self.frame_mainEmpresa.setSizePolicy(sizePolicy1)
        self.frame_mainEmpresa.setFrameShape(QFrame.StyledPanel)
        self.frame_mainEmpresa.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_mainEmpresa)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame1_btnEmpresa = QFrame(self.frame_mainEmpresa)
        self.frame1_btnEmpresa.setObjectName(u"frame1_btnEmpresa")
        self.frame1_btnEmpresa.setFrameShape(QFrame.StyledPanel)
        self.frame1_btnEmpresa.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame1_btnEmpresa)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_logoEmpresa = QGroupBox(self.frame1_btnEmpresa)
        self.groupBox_logoEmpresa.setObjectName(u"groupBox_logoEmpresa")
        self.horizontalLayout_28 = QHBoxLayout(self.groupBox_logoEmpresa)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.btn_logoEmpresa = QFrame(self.groupBox_logoEmpresa)
        self.btn_logoEmpresa.setObjectName(u"btn_logoEmpresa")
        self.btn_logoEmpresa.setFrameShape(QFrame.StyledPanel)
        self.btn_logoEmpresa.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.btn_logoEmpresa)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.btn_selecionarLogoEmpresa = QPushButton(self.btn_logoEmpresa)
        self.btn_selecionarLogoEmpresa.setObjectName(u"btn_selecionarLogoEmpresa")
        icon24 = QIcon()
        icon24.addFile(u":/assets/icons/anexo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_selecionarLogoEmpresa.setIcon(icon24)
        self.btn_selecionarLogoEmpresa.setIconSize(QSize(18, 18))

        self.verticalLayout_38.addWidget(self.btn_selecionarLogoEmpresa)

        self.btn_removerLogoEmpresa = QPushButton(self.btn_logoEmpresa)
        self.btn_removerLogoEmpresa.setObjectName(u"btn_removerLogoEmpresa")
        self.btn_removerLogoEmpresa.setIcon(icon18)

        self.verticalLayout_38.addWidget(self.btn_removerLogoEmpresa)


        self.horizontalLayout_28.addWidget(self.btn_logoEmpresa)

        self.logoEmpresa = QLabel(self.groupBox_logoEmpresa)
        self.logoEmpresa.setObjectName(u"logoEmpresa")
        self.logoEmpresa.setMinimumSize(QSize(50, 50))
        self.logoEmpresa.setMaximumSize(QSize(50, 50))
        self.logoEmpresa.setFont(font)
        self.logoEmpresa.setTextFormat(Qt.AutoText)
        self.logoEmpresa.setPixmap(QPixmap(u":/assets/icons/logo_p_dark_200px.png"))
        self.logoEmpresa.setScaledContents(True)
        self.logoEmpresa.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.logoEmpresa)


        self.horizontalLayout_6.addWidget(self.groupBox_logoEmpresa)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.btn_editarEmpresa = QPushButton(self.frame1_btnEmpresa)
        self.btn_editarEmpresa.setObjectName(u"btn_editarEmpresa")
        self.btn_editarEmpresa.setIcon(icon17)
        self.btn_editarEmpresa.setIconSize(QSize(18, 18))

        self.horizontalLayout_6.addWidget(self.btn_editarEmpresa)

        self.btn_excluirEmpresa = QPushButton(self.frame1_btnEmpresa)
        self.btn_excluirEmpresa.setObjectName(u"btn_excluirEmpresa")
        self.btn_excluirEmpresa.setIcon(icon18)
        self.btn_excluirEmpresa.setIconSize(QSize(18, 18))

        self.horizontalLayout_6.addWidget(self.btn_excluirEmpresa)

        self.btn_salvarEmpresa = QPushButton(self.frame1_btnEmpresa)
        self.btn_salvarEmpresa.setObjectName(u"btn_salvarEmpresa")
        self.btn_salvarEmpresa.setIcon(icon22)
        self.btn_salvarEmpresa.setIconSize(QSize(18, 18))

        self.horizontalLayout_6.addWidget(self.btn_salvarEmpresa)


        self.verticalLayout_24.addWidget(self.frame1_btnEmpresa)

        self.frame2_formEmpresa = QFrame(self.frame_mainEmpresa)
        self.frame2_formEmpresa.setObjectName(u"frame2_formEmpresa")
        sizePolicy1.setHeightForWidth(self.frame2_formEmpresa.sizePolicy().hasHeightForWidth())
        self.frame2_formEmpresa.setSizePolicy(sizePolicy1)
        self.frame2_formEmpresa.setFrameShape(QFrame.StyledPanel)
        self.frame2_formEmpresa.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame2_formEmpresa)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.groupBox1_identificacaoEmpresa = QGroupBox(self.frame2_formEmpresa)
        self.groupBox1_identificacaoEmpresa.setObjectName(u"groupBox1_identificacaoEmpresa")
        self.gridLayout_6 = QGridLayout(self.groupBox1_identificacaoEmpresa)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lb_empresaContato = QLabel(self.groupBox1_identificacaoEmpresa)
        self.lb_empresaContato.setObjectName(u"lb_empresaContato")
        self.lb_empresaContato.setMaximumSize(QSize(80, 16777215))
        self.lb_empresaContato.setFont(font)

        self.gridLayout_6.addWidget(self.lb_empresaContato, 3, 0, 1, 1)

        self.lb_empresaId = QLabel(self.groupBox1_identificacaoEmpresa)
        self.lb_empresaId.setObjectName(u"lb_empresaId")
        self.lb_empresaId.setMaximumSize(QSize(80, 16777215))
        self.lb_empresaId.setFont(font)

        self.gridLayout_6.addWidget(self.lb_empresaId, 0, 0, 1, 1)

        self.lb_empresaRazaoSocial = QLabel(self.groupBox1_identificacaoEmpresa)
        self.lb_empresaRazaoSocial.setObjectName(u"lb_empresaRazaoSocial")
        self.lb_empresaRazaoSocial.setMaximumSize(QSize(80, 16777215))
        self.lb_empresaRazaoSocial.setFont(font)

        self.gridLayout_6.addWidget(self.lb_empresaRazaoSocial, 1, 0, 1, 1)

        self.radioButton_empresaJuridica = QRadioButton(self.groupBox1_identificacaoEmpresa)
        self.radioButton_empresaJuridica.setObjectName(u"radioButton_empresaJuridica")
        self.radioButton_empresaJuridica.setFont(font)
        self.radioButton_empresaJuridica.setAutoFillBackground(False)
        self.radioButton_empresaJuridica.setChecked(True)
        self.radioButton_empresaJuridica.setAutoRepeat(False)

        self.gridLayout_6.addWidget(self.radioButton_empresaJuridica, 0, 3, 1, 1)

        self.ed_empresaContato = QLineEdit(self.groupBox1_identificacaoEmpresa)
        self.ed_empresaContato.setObjectName(u"ed_empresaContato")
        self.ed_empresaContato.setFont(font)
        self.ed_empresaContato.setInputMethodHints(Qt.ImhPreferNumbers)
        self.ed_empresaContato.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.ed_empresaContato, 3, 1, 1, 1)

        self.lb_empresaCpfCnpj = QLabel(self.groupBox1_identificacaoEmpresa)
        self.lb_empresaCpfCnpj.setObjectName(u"lb_empresaCpfCnpj")
        self.lb_empresaCpfCnpj.setMaximumSize(QSize(80, 16777215))
        self.lb_empresaCpfCnpj.setFont(font)

        self.gridLayout_6.addWidget(self.lb_empresaCpfCnpj, 2, 0, 1, 1)

        self.radioButton_empresaFisica = QRadioButton(self.groupBox1_identificacaoEmpresa)
        self.radioButton_empresaFisica.setObjectName(u"radioButton_empresaFisica")
        self.radioButton_empresaFisica.setFont(font)

        self.gridLayout_6.addWidget(self.radioButton_empresaFisica, 0, 2, 1, 1)

        self.ed_empresaCpfCnpj = QLineEdit(self.groupBox1_identificacaoEmpresa)
        self.ed_empresaCpfCnpj.setObjectName(u"ed_empresaCpfCnpj")
        self.ed_empresaCpfCnpj.setFont(font)
        self.ed_empresaCpfCnpj.setInputMethodHints(Qt.ImhPreferNumbers)
        self.ed_empresaCpfCnpj.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.ed_empresaCpfCnpj, 2, 1, 1, 3)

        self.lb_empresaEmail = QLabel(self.groupBox1_identificacaoEmpresa)
        self.lb_empresaEmail.setObjectName(u"lb_empresaEmail")
        self.lb_empresaEmail.setFont(font)
        self.lb_empresaEmail.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.lb_empresaEmail, 3, 2, 1, 1)

        self.ed_empresaId = QLineEdit(self.groupBox1_identificacaoEmpresa)
        self.ed_empresaId.setObjectName(u"ed_empresaId")
        self.ed_empresaId.setFont(font)
        self.ed_empresaId.setReadOnly(True)

        self.gridLayout_6.addWidget(self.ed_empresaId, 0, 1, 1, 1)

        self.ed_empresaEmail = QLineEdit(self.groupBox1_identificacaoEmpresa)
        self.ed_empresaEmail.setObjectName(u"ed_empresaEmail")
        self.ed_empresaEmail.setFont(font)
        self.ed_empresaEmail.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.ed_empresaEmail.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.ed_empresaEmail, 3, 3, 1, 1)

        self.ed_empresaRazaoSocial = QLineEdit(self.groupBox1_identificacaoEmpresa)
        self.ed_empresaRazaoSocial.setObjectName(u"ed_empresaRazaoSocial")
        self.ed_empresaRazaoSocial.setFont(font)
        self.ed_empresaRazaoSocial.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.ed_empresaRazaoSocial, 1, 1, 1, 3)


        self.verticalLayout_25.addWidget(self.groupBox1_identificacaoEmpresa)

        self.groupBox2_enderecoEmpresa = QGroupBox(self.frame2_formEmpresa)
        self.groupBox2_enderecoEmpresa.setObjectName(u"groupBox2_enderecoEmpresa")
        self.gridLayout_3 = QGridLayout(self.groupBox2_enderecoEmpresa)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lb_empresaCidade = QLabel(self.groupBox2_enderecoEmpresa)
        self.lb_empresaCidade.setObjectName(u"lb_empresaCidade")
        self.lb_empresaCidade.setMaximumSize(QSize(80, 16777215))
        self.lb_empresaCidade.setFont(font)

        self.gridLayout_3.addWidget(self.lb_empresaCidade, 2, 0, 1, 1)

        self.lb_empresaNumero = QLabel(self.groupBox2_enderecoEmpresa)
        self.lb_empresaNumero.setObjectName(u"lb_empresaNumero")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lb_empresaNumero.sizePolicy().hasHeightForWidth())
        self.lb_empresaNumero.setSizePolicy(sizePolicy3)
        self.lb_empresaNumero.setMaximumSize(QSize(20, 16777215))
        self.lb_empresaNumero.setFont(font)

        self.gridLayout_3.addWidget(self.lb_empresaNumero, 0, 4, 1, 1)

        self.ed_empresaBairro = QLineEdit(self.groupBox2_enderecoEmpresa)
        self.ed_empresaBairro.setObjectName(u"ed_empresaBairro")
        self.ed_empresaBairro.setFont(font)

        self.gridLayout_3.addWidget(self.ed_empresaBairro, 1, 1, 1, 1)

        self.ed_empresaNumero = QLineEdit(self.groupBox2_enderecoEmpresa)
        self.ed_empresaNumero.setObjectName(u"ed_empresaNumero")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ed_empresaNumero.sizePolicy().hasHeightForWidth())
        self.ed_empresaNumero.setSizePolicy(sizePolicy4)
        self.ed_empresaNumero.setMinimumSize(QSize(125, 0))
        font8 = QFont()
        font8.setFamilies([u"Poppins"])
        font8.setPointSize(9)
        self.ed_empresaNumero.setFont(font8)
        self.ed_empresaNumero.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.ed_empresaNumero, 0, 5, 1, 1)

        self.ed_empresaLogradouro = QLineEdit(self.groupBox2_enderecoEmpresa)
        self.ed_empresaLogradouro.setObjectName(u"ed_empresaLogradouro")
        self.ed_empresaLogradouro.setMinimumSize(QSize(240, 0))
        self.ed_empresaLogradouro.setFont(font8)
        self.ed_empresaLogradouro.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.ed_empresaLogradouro, 0, 1, 1, 3)

        self.lb_empresaLogradoura = QLabel(self.groupBox2_enderecoEmpresa)
        self.lb_empresaLogradoura.setObjectName(u"lb_empresaLogradoura")
        self.lb_empresaLogradoura.setMaximumSize(QSize(80, 16777215))
        self.lb_empresaLogradoura.setFont(font)

        self.gridLayout_3.addWidget(self.lb_empresaLogradoura, 0, 0, 1, 1)

        self.lb_empresaCep = QLabel(self.groupBox2_enderecoEmpresa)
        self.lb_empresaCep.setObjectName(u"lb_empresaCep")
        self.lb_empresaCep.setFont(font)

        self.gridLayout_3.addWidget(self.lb_empresaCep, 1, 3, 1, 1)

        self.cb_empresaCidade = QComboBox(self.groupBox2_enderecoEmpresa)
        self.cb_empresaCidade.setObjectName(u"cb_empresaCidade")
        self.cb_empresaCidade.setMinimumSize(QSize(130, 0))
        self.cb_empresaCidade.setFont(font)

        self.gridLayout_3.addWidget(self.cb_empresaCidade, 2, 1, 1, 3)

        self.lb_empresaReferencia = QLabel(self.groupBox2_enderecoEmpresa)
        self.lb_empresaReferencia.setObjectName(u"lb_empresaReferencia")
        self.lb_empresaReferencia.setMaximumSize(QSize(80, 16777215))
        self.lb_empresaReferencia.setFont(font)

        self.gridLayout_3.addWidget(self.lb_empresaReferencia, 3, 0, 1, 1)

        self.lb_empresaBairro = QLabel(self.groupBox2_enderecoEmpresa)
        self.lb_empresaBairro.setObjectName(u"lb_empresaBairro")
        self.lb_empresaBairro.setFont(font)

        self.gridLayout_3.addWidget(self.lb_empresaBairro, 1, 0, 1, 1)

        self.cb_empresaUf = QComboBox(self.groupBox2_enderecoEmpresa)
        self.cb_empresaUf.setObjectName(u"cb_empresaUf")
        self.cb_empresaUf.setFont(font)

        self.gridLayout_3.addWidget(self.cb_empresaUf, 2, 5, 1, 1)

        self.lb_empresaUf = QLabel(self.groupBox2_enderecoEmpresa)
        self.lb_empresaUf.setObjectName(u"lb_empresaUf")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lb_empresaUf.sizePolicy().hasHeightForWidth())
        self.lb_empresaUf.setSizePolicy(sizePolicy5)
        self.lb_empresaUf.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_3.addWidget(self.lb_empresaUf, 2, 4, 1, 1)

        self.ed_empresaReferencia = QLineEdit(self.groupBox2_enderecoEmpresa)
        self.ed_empresaReferencia.setObjectName(u"ed_empresaReferencia")
        self.ed_empresaReferencia.setFont(font8)
        self.ed_empresaReferencia.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.ed_empresaReferencia, 3, 1, 1, 5)

        self.ed_empresaCep = QLineEdit(self.groupBox2_enderecoEmpresa)
        self.ed_empresaCep.setObjectName(u"ed_empresaCep")
        sizePolicy4.setHeightForWidth(self.ed_empresaCep.sizePolicy().hasHeightForWidth())
        self.ed_empresaCep.setSizePolicy(sizePolicy4)
        self.ed_empresaCep.setMinimumSize(QSize(125, 0))
        self.ed_empresaCep.setMaximumSize(QSize(200, 16777215))
        self.ed_empresaCep.setFont(font8)
        self.ed_empresaCep.setInputMethodHints(Qt.ImhPreferNumbers)
        self.ed_empresaCep.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.ed_empresaCep, 1, 4, 1, 2)


        self.verticalLayout_25.addWidget(self.groupBox2_enderecoEmpresa)


        self.verticalLayout_24.addWidget(self.frame2_formEmpresa)


        self.verticalLayout_23.addWidget(self.frame_mainEmpresa)

        self.section.addWidget(self.s5_empresas)
        self.s4_protocolos = QWidget()
        self.s4_protocolos.setObjectName(u"s4_protocolos")
        self.verticalLayout_21 = QVBoxLayout(self.s4_protocolos)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_headerProtocolos = QFrame(self.s4_protocolos)
        self.frame_headerProtocolos.setObjectName(u"frame_headerProtocolos")
        self.frame_headerProtocolos.setFrameShape(QFrame.StyledPanel)
        self.frame_headerProtocolos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_headerProtocolos)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.lb_titleProtocolos = QLabel(self.frame_headerProtocolos)
        self.lb_titleProtocolos.setObjectName(u"lb_titleProtocolos")
        self.lb_titleProtocolos.setFont(font3)

        self.verticalLayout_19.addWidget(self.lb_titleProtocolos)

        self.lineProtocolos = QFrame(self.frame_headerProtocolos)
        self.lineProtocolos.setObjectName(u"lineProtocolos")
        self.lineProtocolos.setStyleSheet(u"background-color: #00718F;")
        self.lineProtocolos.setFrameShape(QFrame.HLine)
        self.lineProtocolos.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.lineProtocolos)


        self.verticalLayout_21.addWidget(self.frame_headerProtocolos)

        self.aba_protocolos = QTabWidget(self.s4_protocolos)
        self.aba_protocolos.setObjectName(u"aba_protocolos")
        self.aba_protocolos.setFont(font)
        self.aba1_listaProtocolos = QWidget()
        self.aba1_listaProtocolos.setObjectName(u"aba1_listaProtocolos")
        self.gridLayout_5 = QGridLayout(self.aba1_listaProtocolos)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame1_listaProtocolos = QFrame(self.aba1_listaProtocolos)
        self.frame1_listaProtocolos.setObjectName(u"frame1_listaProtocolos")
        self.frame1_listaProtocolos.setFrameShape(QFrame.StyledPanel)
        self.frame1_listaProtocolos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame1_listaProtocolos)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_pesquisaProtocolos = QFrame(self.frame1_listaProtocolos)
        self.frame_pesquisaProtocolos.setObjectName(u"frame_pesquisaProtocolos")
        self.frame_pesquisaProtocolos.setFrameShape(QFrame.StyledPanel)
        self.frame_pesquisaProtocolos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_pesquisaProtocolos)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.barLine_pesquisaProtocolos = QLineEdit(self.frame_pesquisaProtocolos)
        self.barLine_pesquisaProtocolos.setObjectName(u"barLine_pesquisaProtocolos")
        self.barLine_pesquisaProtocolos.setFont(font)

        self.horizontalLayout_17.addWidget(self.barLine_pesquisaProtocolos)

        self.btn_pesquisaProtocolos = QToolButton(self.frame_pesquisaProtocolos)
        self.btn_pesquisaProtocolos.setObjectName(u"btn_pesquisaProtocolos")
        self.btn_pesquisaProtocolos.setIcon(icon19)
        self.btn_pesquisaProtocolos.setIconSize(QSize(18, 18))

        self.horizontalLayout_17.addWidget(self.btn_pesquisaProtocolos)


        self.horizontalLayout_11.addWidget(self.frame_pesquisaProtocolos)


        self.gridLayout_5.addWidget(self.frame1_listaProtocolos, 0, 0, 1, 3)

        self.frame2_listaProtocolos = QFrame(self.aba1_listaProtocolos)
        self.frame2_listaProtocolos.setObjectName(u"frame2_listaProtocolos")
        self.frame2_listaProtocolos.setFrameShape(QFrame.StyledPanel)
        self.frame2_listaProtocolos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame2_listaProtocolos)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.btn1_editarProtocolos = QPushButton(self.frame2_listaProtocolos)
        self.btn1_editarProtocolos.setObjectName(u"btn1_editarProtocolos")
        self.btn1_editarProtocolos.setFont(font)
        self.btn1_editarProtocolos.setIcon(icon17)
        self.btn1_editarProtocolos.setIconSize(QSize(18, 18))

        self.verticalLayout_18.addWidget(self.btn1_editarProtocolos)

        self.btn2_excluirProtocolos = QPushButton(self.frame2_listaProtocolos)
        self.btn2_excluirProtocolos.setObjectName(u"btn2_excluirProtocolos")
        self.btn2_excluirProtocolos.setFont(font)
        self.btn2_excluirProtocolos.setIcon(icon18)
        self.btn2_excluirProtocolos.setIconSize(QSize(18, 18))

        self.verticalLayout_18.addWidget(self.btn2_excluirProtocolos)

        self.btn4_pdfProtocolos = QPushButton(self.frame2_listaProtocolos)
        self.btn4_pdfProtocolos.setObjectName(u"btn4_pdfProtocolos")
        icon25 = QIcon()
        icon25.addFile(u":/assets/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn4_pdfProtocolos.setIcon(icon25)
        self.btn4_pdfProtocolos.setIconSize(QSize(18, 18))

        self.verticalLayout_18.addWidget(self.btn4_pdfProtocolos)

        self.btn5_wordProtocolos = QPushButton(self.frame2_listaProtocolos)
        self.btn5_wordProtocolos.setObjectName(u"btn5_wordProtocolos")
        self.btn5_wordProtocolos.setIcon(icon25)
        self.btn5_wordProtocolos.setIconSize(QSize(18, 18))

        self.verticalLayout_18.addWidget(self.btn5_wordProtocolos)

        self.btn6_whatsappProtocolos = QPushButton(self.frame2_listaProtocolos)
        self.btn6_whatsappProtocolos.setObjectName(u"btn6_whatsappProtocolos")
        self.btn6_whatsappProtocolos.setIcon(icon12)
        self.btn6_whatsappProtocolos.setIconSize(QSize(18, 18))

        self.verticalLayout_18.addWidget(self.btn6_whatsappProtocolos)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_3)


        self.gridLayout_5.addWidget(self.frame2_listaProtocolos, 1, 0, 1, 1)

        self.tabela_protocolos = QTableWidget(self.aba1_listaProtocolos)
        if (self.tabela_protocolos.columnCount() < 10):
            self.tabela_protocolos.setColumnCount(10)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font5);
        self.tabela_protocolos.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font5);
        self.tabela_protocolos.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font5);
        self.tabela_protocolos.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        self.tabela_protocolos.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font5);
        self.tabela_protocolos.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font5);
        self.tabela_protocolos.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font5);
        self.tabela_protocolos.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font5);
        self.tabela_protocolos.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.tabela_protocolos.setHorizontalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font5);
        self.tabela_protocolos.setHorizontalHeaderItem(9, __qtablewidgetitem16)
        self.tabela_protocolos.setObjectName(u"tabela_protocolos")
        self.tabela_protocolos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_protocolos.setProperty("showDropIndicator", False)
        self.tabela_protocolos.setDragDropOverwriteMode(False)
        self.tabela_protocolos.setAlternatingRowColors(True)
        self.tabela_protocolos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_protocolos.setSortingEnabled(True)

        self.gridLayout_5.addWidget(self.tabela_protocolos, 1, 2, 1, 1)

        self.aba_protocolos.addTab(self.aba1_listaProtocolos, icon20, "")
        self.aba2_cadastroProtocolos = QWidget()
        self.aba2_cadastroProtocolos.setObjectName(u"aba2_cadastroProtocolos")
        self.verticalLayout_37 = QVBoxLayout(self.aba2_cadastroProtocolos)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame1_mainCadastroProtocolos = QFrame(self.aba2_cadastroProtocolos)
        self.frame1_mainCadastroProtocolos.setObjectName(u"frame1_mainCadastroProtocolos")
        sizePolicy1.setHeightForWidth(self.frame1_mainCadastroProtocolos.sizePolicy().hasHeightForWidth())
        self.frame1_mainCadastroProtocolos.setSizePolicy(sizePolicy1)
        self.frame1_mainCadastroProtocolos.setFrameShape(QFrame.StyledPanel)
        self.frame1_mainCadastroProtocolos.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame1_mainCadastroProtocolos)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.date_protocolosTermino = QTimeEdit(self.frame1_mainCadastroProtocolos)
        self.date_protocolosTermino.setObjectName(u"date_protocolosTermino")
        self.date_protocolosTermino.setMaximumSize(QSize(16777215, 30))
        self.date_protocolosTermino.setFont(font)
        self.date_protocolosTermino.setTime(QTime(17, 0, 0))

        self.gridLayout_11.addWidget(self.date_protocolosTermino, 4, 4, 1, 1)

        self.date_protocolosData = QDateEdit(self.frame1_mainCadastroProtocolos)
        self.date_protocolosData.setObjectName(u"date_protocolosData")
        self.date_protocolosData.setMaximumSize(QSize(16777215, 30))
        self.date_protocolosData.setFont(font)
        self.date_protocolosData.setAccelerated(False)
        self.date_protocolosData.setProperty("showGroupSeparator", False)
        self.date_protocolosData.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(18, 0, 0)))
        self.date_protocolosData.setCalendarPopup(True)
        self.date_protocolosData.setDate(QDate(2024, 1, 1))

        self.gridLayout_11.addWidget(self.date_protocolosData, 2, 4, 1, 1)

        self.cb_protocolosConsultor = QComboBox(self.frame1_mainCadastroProtocolos)
        self.cb_protocolosConsultor.setObjectName(u"cb_protocolosConsultor")
        self.cb_protocolosConsultor.setFont(font)

        self.gridLayout_11.addWidget(self.cb_protocolosConsultor, 2, 1, 1, 2)

        self.lb_protocolosTermino = QLabel(self.frame1_mainCadastroProtocolos)
        self.lb_protocolosTermino.setObjectName(u"lb_protocolosTermino")
        self.lb_protocolosTermino.setMaximumSize(QSize(60, 16777215))
        self.lb_protocolosTermino.setFont(font5)
        self.lb_protocolosTermino.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.lb_protocolosTermino, 4, 3, 1, 1)

        self.lb_protocolosConsultor = QLabel(self.frame1_mainCadastroProtocolos)
        self.lb_protocolosConsultor.setObjectName(u"lb_protocolosConsultor")
        self.lb_protocolosConsultor.setMaximumSize(QSize(85, 16777215))
        self.lb_protocolosConsultor.setFont(font5)

        self.gridLayout_11.addWidget(self.lb_protocolosConsultor, 2, 0, 1, 1)

        self.ed_protocolosDescricao = QTextEdit(self.frame1_mainCadastroProtocolos)
        self.ed_protocolosDescricao.setObjectName(u"ed_protocolosDescricao")

        self.gridLayout_11.addWidget(self.ed_protocolosDescricao, 8, 0, 1, 5)

        self.cb_protocolosSolicitante = QComboBox(self.frame1_mainCadastroProtocolos)
        self.cb_protocolosSolicitante.setObjectName(u"cb_protocolosSolicitante")
        self.cb_protocolosSolicitante.setFont(font)

        self.gridLayout_11.addWidget(self.cb_protocolosSolicitante, 4, 1, 1, 2)

        self.lb_protocolosCliente = QLabel(self.frame1_mainCadastroProtocolos)
        self.lb_protocolosCliente.setObjectName(u"lb_protocolosCliente")
        self.lb_protocolosCliente.setMaximumSize(QSize(85, 16777215))
        self.lb_protocolosCliente.setFont(font5)

        self.gridLayout_11.addWidget(self.lb_protocolosCliente, 3, 0, 1, 1)

        self.lb_protocolosSolicitante = QLabel(self.frame1_mainCadastroProtocolos)
        self.lb_protocolosSolicitante.setObjectName(u"lb_protocolosSolicitante")
        self.lb_protocolosSolicitante.setMaximumSize(QSize(85, 16777215))
        self.lb_protocolosSolicitante.setFont(font5)

        self.gridLayout_11.addWidget(self.lb_protocolosSolicitante, 4, 0, 1, 1)

        self.lb_protocolosData = QLabel(self.frame1_mainCadastroProtocolos)
        self.lb_protocolosData.setObjectName(u"lb_protocolosData")
        self.lb_protocolosData.setMaximumSize(QSize(60, 16777215))
        self.lb_protocolosData.setFont(font5)
        self.lb_protocolosData.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.lb_protocolosData, 2, 3, 1, 1)

        self.cb_protocolosCliente = QComboBox(self.frame1_mainCadastroProtocolos)
        self.cb_protocolosCliente.setObjectName(u"cb_protocolosCliente")
        self.cb_protocolosCliente.setFont(font)

        self.gridLayout_11.addWidget(self.cb_protocolosCliente, 3, 1, 1, 2)

        self.lb_protocolosInicio = QLabel(self.frame1_mainCadastroProtocolos)
        self.lb_protocolosInicio.setObjectName(u"lb_protocolosInicio")
        self.lb_protocolosInicio.setMaximumSize(QSize(60, 16777215))
        self.lb_protocolosInicio.setFont(font5)
        self.lb_protocolosInicio.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.lb_protocolosInicio, 3, 3, 1, 1)

        self.lb_protocolosAtendimento = QLabel(self.frame1_mainCadastroProtocolos)
        self.lb_protocolosAtendimento.setObjectName(u"lb_protocolosAtendimento")
        self.lb_protocolosAtendimento.setMaximumSize(QSize(85, 16777215))
        self.lb_protocolosAtendimento.setFont(font5)

        self.gridLayout_11.addWidget(self.lb_protocolosAtendimento, 1, 0, 1, 1)

        self.date_protocolosInicio = QTimeEdit(self.frame1_mainCadastroProtocolos)
        self.date_protocolosInicio.setObjectName(u"date_protocolosInicio")
        self.date_protocolosInicio.setMinimumSize(QSize(0, 0))
        self.date_protocolosInicio.setMaximumSize(QSize(16777215, 30))
        self.date_protocolosInicio.setFont(font)
        self.date_protocolosInicio.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.date_protocolosInicio.setAccelerated(False)
        self.date_protocolosInicio.setCalendarPopup(False)
        self.date_protocolosInicio.setTime(QTime(8, 0, 0))

        self.gridLayout_11.addWidget(self.date_protocolosInicio, 3, 4, 1, 1)

        self.btn_protocolosRobot = QPushButton(self.frame1_mainCadastroProtocolos)
        self.btn_protocolosRobot.setObjectName(u"btn_protocolosRobot")
        icon26 = QIcon()
        icon26.addFile(u":/assets/icons/robot.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_protocolosRobot.setIcon(icon26)
        self.btn_protocolosRobot.setIconSize(QSize(18, 18))

        self.gridLayout_11.addWidget(self.btn_protocolosRobot, 7, 4, 1, 1, Qt.AlignRight)

        self.lb_protocolosDescricao = QLabel(self.frame1_mainCadastroProtocolos)
        self.lb_protocolosDescricao.setObjectName(u"lb_protocolosDescricao")
        self.lb_protocolosDescricao.setMaximumSize(QSize(16777215, 16777215))
        font9 = QFont()
        font9.setFamilies([u"Poppins"])
        font9.setPointSize(10)
        font9.setBold(True)
        self.lb_protocolosDescricao.setFont(font9)

        self.gridLayout_11.addWidget(self.lb_protocolosDescricao, 7, 0, 1, 4)

        self.lb_protocolosId = QLabel(self.frame1_mainCadastroProtocolos)
        self.lb_protocolosId.setObjectName(u"lb_protocolosId")
        self.lb_protocolosId.setFont(font5)

        self.gridLayout_11.addWidget(self.lb_protocolosId, 0, 0, 1, 1)

        self.cb_protocolosCancelado = QCheckBox(self.frame1_mainCadastroProtocolos)
        self.cb_protocolosCancelado.setObjectName(u"cb_protocolosCancelado")
        self.cb_protocolosCancelado.setEnabled(False)

        self.gridLayout_11.addWidget(self.cb_protocolosCancelado, 0, 4, 1, 1)

        self.cb_protocolosAtendimento = QComboBox(self.frame1_mainCadastroProtocolos)
        self.cb_protocolosAtendimento.setObjectName(u"cb_protocolosAtendimento")
        self.cb_protocolosAtendimento.setFont(font)

        self.gridLayout_11.addWidget(self.cb_protocolosAtendimento, 1, 1, 1, 4)

        self.ed_protocolosId = QLineEdit(self.frame1_mainCadastroProtocolos)
        self.ed_protocolosId.setObjectName(u"ed_protocolosId")
        self.ed_protocolosId.setReadOnly(True)

        self.gridLayout_11.addWidget(self.ed_protocolosId, 0, 1, 1, 3)


        self.verticalLayout_37.addWidget(self.frame1_mainCadastroProtocolos)

        self.frame2_btnCadastroProtocolos = QFrame(self.aba2_cadastroProtocolos)
        self.frame2_btnCadastroProtocolos.setObjectName(u"frame2_btnCadastroProtocolos")
        self.frame2_btnCadastroProtocolos.setFrameShape(QFrame.StyledPanel)
        self.frame2_btnCadastroProtocolos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame2_btnCadastroProtocolos)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer_6 = QSpacerItem(296, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_6)

        self.btn_limparCadastroProtocolos = QPushButton(self.frame2_btnCadastroProtocolos)
        self.btn_limparCadastroProtocolos.setObjectName(u"btn_limparCadastroProtocolos")
        self.btn_limparCadastroProtocolos.setFont(font)
        self.btn_limparCadastroProtocolos.setIcon(icon21)
        self.btn_limparCadastroProtocolos.setIconSize(QSize(18, 18))

        self.horizontalLayout_32.addWidget(self.btn_limparCadastroProtocolos)

        self.btn_salvarCadastroProtocolos = QPushButton(self.frame2_btnCadastroProtocolos)
        self.btn_salvarCadastroProtocolos.setObjectName(u"btn_salvarCadastroProtocolos")
        self.btn_salvarCadastroProtocolos.setFont(font)
        self.btn_salvarCadastroProtocolos.setIcon(icon22)
        self.btn_salvarCadastroProtocolos.setIconSize(QSize(18, 18))

        self.horizontalLayout_32.addWidget(self.btn_salvarCadastroProtocolos)


        self.verticalLayout_37.addWidget(self.frame2_btnCadastroProtocolos)

        icon27 = QIcon()
        icon27.addFile(u":/assets/icons/doc_add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_protocolos.addTab(self.aba2_cadastroProtocolos, icon27, "")

        self.verticalLayout_21.addWidget(self.aba_protocolos)

        self.section.addWidget(self.s4_protocolos)
        self.s3_clientes = QWidget()
        self.s3_clientes.setObjectName(u"s3_clientes")
        self.verticalLayout_17 = QVBoxLayout(self.s3_clientes)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_headerClientes = QFrame(self.s3_clientes)
        self.frame_headerClientes.setObjectName(u"frame_headerClientes")
        self.frame_headerClientes.setFrameShape(QFrame.StyledPanel)
        self.frame_headerClientes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_headerClientes)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.lb_titleClientes = QLabel(self.frame_headerClientes)
        self.lb_titleClientes.setObjectName(u"lb_titleClientes")
        self.lb_titleClientes.setFont(font3)

        self.verticalLayout_16.addWidget(self.lb_titleClientes)

        self.lineClientes = QFrame(self.frame_headerClientes)
        self.lineClientes.setObjectName(u"lineClientes")
        self.lineClientes.setStyleSheet(u"background-color: #00718F;")
        self.lineClientes.setFrameShape(QFrame.HLine)
        self.lineClientes.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.lineClientes)


        self.verticalLayout_17.addWidget(self.frame_headerClientes)

        self.aba_clientes = QTabWidget(self.s3_clientes)
        self.aba_clientes.setObjectName(u"aba_clientes")
        self.aba_clientes.setFont(font)
        self.aba1_listaClientes = QWidget()
        self.aba1_listaClientes.setObjectName(u"aba1_listaClientes")
        self.verticalLayout_20 = QVBoxLayout(self.aba1_listaClientes)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame1_listaClientes = QFrame(self.aba1_listaClientes)
        self.frame1_listaClientes.setObjectName(u"frame1_listaClientes")
        self.frame1_listaClientes.setFrameShape(QFrame.StyledPanel)
        self.frame1_listaClientes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame1_listaClientes)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame1_btnClientes = QFrame(self.frame1_listaClientes)
        self.frame1_btnClientes.setObjectName(u"frame1_btnClientes")
        self.frame1_btnClientes.setFrameShape(QFrame.StyledPanel)
        self.frame1_btnClientes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame1_btnClientes)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn1_editarClientes = QPushButton(self.frame1_btnClientes)
        self.btn1_editarClientes.setObjectName(u"btn1_editarClientes")
        self.btn1_editarClientes.setFont(font)
        self.btn1_editarClientes.setIcon(icon17)
        self.btn1_editarClientes.setIconSize(QSize(18, 18))

        self.horizontalLayout_9.addWidget(self.btn1_editarClientes)

        self.btn2_excluirClientes = QPushButton(self.frame1_btnClientes)
        self.btn2_excluirClientes.setObjectName(u"btn2_excluirClientes")
        self.btn2_excluirClientes.setFont(font)
        self.btn2_excluirClientes.setIcon(icon18)
        self.btn2_excluirClientes.setIconSize(QSize(18, 18))

        self.horizontalLayout_9.addWidget(self.btn2_excluirClientes)


        self.horizontalLayout_10.addWidget(self.frame1_btnClientes)

        self.frame2_pesquisaClientes = QFrame(self.frame1_listaClientes)
        self.frame2_pesquisaClientes.setObjectName(u"frame2_pesquisaClientes")
        self.frame2_pesquisaClientes.setFrameShape(QFrame.StyledPanel)
        self.frame2_pesquisaClientes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame2_pesquisaClientes)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.barLine_pesquisaClientes = QLineEdit(self.frame2_pesquisaClientes)
        self.barLine_pesquisaClientes.setObjectName(u"barLine_pesquisaClientes")
        self.barLine_pesquisaClientes.setFont(font)

        self.horizontalLayout_16.addWidget(self.barLine_pesquisaClientes)

        self.btn_pesquisaClientes = QToolButton(self.frame2_pesquisaClientes)
        self.btn_pesquisaClientes.setObjectName(u"btn_pesquisaClientes")
        self.btn_pesquisaClientes.setIcon(icon19)
        self.btn_pesquisaClientes.setIconSize(QSize(18, 18))

        self.horizontalLayout_16.addWidget(self.btn_pesquisaClientes)


        self.horizontalLayout_10.addWidget(self.frame2_pesquisaClientes)


        self.verticalLayout_20.addWidget(self.frame1_listaClientes)

        self.tabela_clientes = QTableWidget(self.aba1_listaClientes)
        if (self.tabela_clientes.columnCount() < 15):
            self.tabela_clientes.setColumnCount(15)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(6, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(7, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(8, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(9, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(10, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(11, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(12, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(13, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font5);
        self.tabela_clientes.setHorizontalHeaderItem(14, __qtablewidgetitem31)
        self.tabela_clientes.setObjectName(u"tabela_clientes")
        self.tabela_clientes.setFont(font5)
        self.tabela_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_clientes.setProperty("showDropIndicator", False)
        self.tabela_clientes.setDragDropOverwriteMode(False)
        self.tabela_clientes.setAlternatingRowColors(True)
        self.tabela_clientes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_clientes.setSortingEnabled(True)

        self.verticalLayout_20.addWidget(self.tabela_clientes)

        self.aba_clientes.addTab(self.aba1_listaClientes, icon20, "")
        self.aba2_cadastroClientes = QWidget()
        self.aba2_cadastroClientes.setObjectName(u"aba2_cadastroClientes")
        self.verticalLayout_13 = QVBoxLayout(self.aba2_cadastroClientes)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame1_mainCadastroClientes = QFrame(self.aba2_cadastroClientes)
        self.frame1_mainCadastroClientes.setObjectName(u"frame1_mainCadastroClientes")
        sizePolicy1.setHeightForWidth(self.frame1_mainCadastroClientes.sizePolicy().hasHeightForWidth())
        self.frame1_mainCadastroClientes.setSizePolicy(sizePolicy1)
        self.frame1_mainCadastroClientes.setStyleSheet(u"padding:0;")
        self.frame1_mainCadastroClientes.setFrameShape(QFrame.StyledPanel)
        self.frame1_mainCadastroClientes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame1_mainCadastroClientes)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox1_identificacaoCadastroClientes = QGroupBox(self.frame1_mainCadastroClientes)
        self.groupBox1_identificacaoCadastroClientes.setObjectName(u"groupBox1_identificacaoCadastroClientes")
        self.groupBox1_identificacaoCadastroClientes.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox1_identificacaoCadastroClientes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_clientesContato = QLabel(self.groupBox1_identificacaoCadastroClientes)
        self.lb_clientesContato.setObjectName(u"lb_clientesContato")
        sizePolicy5.setHeightForWidth(self.lb_clientesContato.sizePolicy().hasHeightForWidth())
        self.lb_clientesContato.setSizePolicy(sizePolicy5)
        self.lb_clientesContato.setMinimumSize(QSize(80, 0))
        self.lb_clientesContato.setFont(font)

        self.gridLayout.addWidget(self.lb_clientesContato, 7, 0, 1, 1)

        self.lb_clientesId = QLabel(self.groupBox1_identificacaoCadastroClientes)
        self.lb_clientesId.setObjectName(u"lb_clientesId")
        sizePolicy5.setHeightForWidth(self.lb_clientesId.sizePolicy().hasHeightForWidth())
        self.lb_clientesId.setSizePolicy(sizePolicy5)
        self.lb_clientesId.setMinimumSize(QSize(80, 0))
        self.lb_clientesId.setFont(font)

        self.gridLayout.addWidget(self.lb_clientesId, 0, 0, 1, 1)

        self.lb_clientesRazaoSocial = QLabel(self.groupBox1_identificacaoCadastroClientes)
        self.lb_clientesRazaoSocial.setObjectName(u"lb_clientesRazaoSocial")
        sizePolicy5.setHeightForWidth(self.lb_clientesRazaoSocial.sizePolicy().hasHeightForWidth())
        self.lb_clientesRazaoSocial.setSizePolicy(sizePolicy5)
        self.lb_clientesRazaoSocial.setMinimumSize(QSize(80, 0))
        self.lb_clientesRazaoSocial.setFont(font)

        self.gridLayout.addWidget(self.lb_clientesRazaoSocial, 4, 0, 1, 1)

        self.lb_clientesCpfCnpj = QLabel(self.groupBox1_identificacaoCadastroClientes)
        self.lb_clientesCpfCnpj.setObjectName(u"lb_clientesCpfCnpj")
        sizePolicy5.setHeightForWidth(self.lb_clientesCpfCnpj.sizePolicy().hasHeightForWidth())
        self.lb_clientesCpfCnpj.setSizePolicy(sizePolicy5)
        self.lb_clientesCpfCnpj.setMinimumSize(QSize(80, 0))
        self.lb_clientesCpfCnpj.setFont(font)

        self.gridLayout.addWidget(self.lb_clientesCpfCnpj, 6, 0, 1, 1)

        self.rd_clientesFisica = QRadioButton(self.groupBox1_identificacaoCadastroClientes)
        self.rd_clientesFisica.setObjectName(u"rd_clientesFisica")
        self.rd_clientesFisica.setFont(font8)
        self.rd_clientesFisica.setChecked(False)

        self.gridLayout.addWidget(self.rd_clientesFisica, 6, 3, 1, 1, Qt.AlignRight)

        self.rd_clientesJuridica = QRadioButton(self.groupBox1_identificacaoCadastroClientes)
        self.rd_clientesJuridica.setObjectName(u"rd_clientesJuridica")
        self.rd_clientesJuridica.setFont(font8)
        self.rd_clientesJuridica.setChecked(True)

        self.gridLayout.addWidget(self.rd_clientesJuridica, 6, 5, 1, 1)

        self.ed_clientesContato = QLineEdit(self.groupBox1_identificacaoCadastroClientes)
        self.ed_clientesContato.setObjectName(u"ed_clientesContato")
        self.ed_clientesContato.setMinimumSize(QSize(160, 0))
        self.ed_clientesContato.setMaximumSize(QSize(16777215, 16777215))
        self.ed_clientesContato.setFont(font8)
        self.ed_clientesContato.setInputMethodHints(Qt.ImhPreferNumbers)
        self.ed_clientesContato.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.ed_clientesContato, 7, 1, 1, 1)

        self.ed_clientesId = QLineEdit(self.groupBox1_identificacaoCadastroClientes)
        self.ed_clientesId.setObjectName(u"ed_clientesId")
        self.ed_clientesId.setEnabled(True)
        self.ed_clientesId.setFont(font)
        self.ed_clientesId.setReadOnly(True)

        self.gridLayout.addWidget(self.ed_clientesId, 0, 1, 1, 1)

        self.lv_clientesEmail = QLabel(self.groupBox1_identificacaoCadastroClientes)
        self.lv_clientesEmail.setObjectName(u"lv_clientesEmail")
        self.lv_clientesEmail.setFont(font)

        self.gridLayout.addWidget(self.lv_clientesEmail, 7, 2, 1, 1)

        self.cd_clientesDesativado = QCheckBox(self.groupBox1_identificacaoCadastroClientes)
        self.cd_clientesDesativado.setObjectName(u"cd_clientesDesativado")
        self.cd_clientesDesativado.setEnabled(False)
        self.cd_clientesDesativado.setFont(font)

        self.gridLayout.addWidget(self.cd_clientesDesativado, 0, 3, 1, 1)

        self.ed_clientesRazaoSocial = QLineEdit(self.groupBox1_identificacaoCadastroClientes)
        self.ed_clientesRazaoSocial.setObjectName(u"ed_clientesRazaoSocial")
        self.ed_clientesRazaoSocial.setFont(font8)
        self.ed_clientesRazaoSocial.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.ed_clientesRazaoSocial, 4, 1, 1, 5)

        self.ed_clientesCpfCnpj = QLineEdit(self.groupBox1_identificacaoCadastroClientes)
        self.ed_clientesCpfCnpj.setObjectName(u"ed_clientesCpfCnpj")
        sizePolicy2.setHeightForWidth(self.ed_clientesCpfCnpj.sizePolicy().hasHeightForWidth())
        self.ed_clientesCpfCnpj.setSizePolicy(sizePolicy2)
        self.ed_clientesCpfCnpj.setMaximumSize(QSize(16777215, 16777215))
        self.ed_clientesCpfCnpj.setFont(font8)
        self.ed_clientesCpfCnpj.setInputMethodHints(Qt.ImhPreferNumbers)
        self.ed_clientesCpfCnpj.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.ed_clientesCpfCnpj, 6, 1, 1, 2)

        self.ed_clientesEmail = QLineEdit(self.groupBox1_identificacaoCadastroClientes)
        self.ed_clientesEmail.setObjectName(u"ed_clientesEmail")
        self.ed_clientesEmail.setFont(font8)
        self.ed_clientesEmail.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.ed_clientesEmail.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.ed_clientesEmail, 7, 3, 1, 3)


        self.verticalLayout_8.addWidget(self.groupBox1_identificacaoCadastroClientes)

        self.groupBox2_enderecoCadastroClientes = QGroupBox(self.frame1_mainCadastroClientes)
        self.groupBox2_enderecoCadastroClientes.setObjectName(u"groupBox2_enderecoCadastroClientes")
        self.groupBox2_enderecoCadastroClientes.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox2_enderecoCadastroClientes)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ed_enderecoClientesLodradouro = QLineEdit(self.groupBox2_enderecoCadastroClientes)
        self.ed_enderecoClientesLodradouro.setObjectName(u"ed_enderecoClientesLodradouro")
        self.ed_enderecoClientesLodradouro.setFont(font8)
        self.ed_enderecoClientesLodradouro.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.ed_enderecoClientesLodradouro, 0, 1, 1, 3)

        self.lb_enderecoClientesCidade = QLabel(self.groupBox2_enderecoCadastroClientes)
        self.lb_enderecoClientesCidade.setObjectName(u"lb_enderecoClientesCidade")
        sizePolicy5.setHeightForWidth(self.lb_enderecoClientesCidade.sizePolicy().hasHeightForWidth())
        self.lb_enderecoClientesCidade.setSizePolicy(sizePolicy5)
        self.lb_enderecoClientesCidade.setMinimumSize(QSize(80, 0))
        self.lb_enderecoClientesCidade.setFont(font)

        self.gridLayout_2.addWidget(self.lb_enderecoClientesCidade, 3, 0, 1, 1)

        self.lb_enderecoClientesNumero = QLabel(self.groupBox2_enderecoCadastroClientes)
        self.lb_enderecoClientesNumero.setObjectName(u"lb_enderecoClientesNumero")

        self.gridLayout_2.addWidget(self.lb_enderecoClientesNumero, 0, 4, 1, 1)

        self.lb_enderecoClientesReferencia = QLabel(self.groupBox2_enderecoCadastroClientes)
        self.lb_enderecoClientesReferencia.setObjectName(u"lb_enderecoClientesReferencia")
        sizePolicy5.setHeightForWidth(self.lb_enderecoClientesReferencia.sizePolicy().hasHeightForWidth())
        self.lb_enderecoClientesReferencia.setSizePolicy(sizePolicy5)
        self.lb_enderecoClientesReferencia.setMinimumSize(QSize(80, 0))
        self.lb_enderecoClientesReferencia.setFont(font)

        self.gridLayout_2.addWidget(self.lb_enderecoClientesReferencia, 5, 0, 1, 1)

        self.lb_enderecoClientesLogradouro = QLabel(self.groupBox2_enderecoCadastroClientes)
        self.lb_enderecoClientesLogradouro.setObjectName(u"lb_enderecoClientesLogradouro")
        sizePolicy5.setHeightForWidth(self.lb_enderecoClientesLogradouro.sizePolicy().hasHeightForWidth())
        self.lb_enderecoClientesLogradouro.setSizePolicy(sizePolicy5)
        self.lb_enderecoClientesLogradouro.setMinimumSize(QSize(80, 0))
        self.lb_enderecoClientesLogradouro.setFont(font)

        self.gridLayout_2.addWidget(self.lb_enderecoClientesLogradouro, 0, 0, 1, 1)

        self.ed_enderecoClientesNumeros = QLineEdit(self.groupBox2_enderecoCadastroClientes)
        self.ed_enderecoClientesNumeros.setObjectName(u"ed_enderecoClientesNumeros")
        sizePolicy4.setHeightForWidth(self.ed_enderecoClientesNumeros.sizePolicy().hasHeightForWidth())
        self.ed_enderecoClientesNumeros.setSizePolicy(sizePolicy4)
        self.ed_enderecoClientesNumeros.setMinimumSize(QSize(125, 0))
        self.ed_enderecoClientesNumeros.setFont(font8)
        self.ed_enderecoClientesNumeros.setMaxLength(10)
        self.ed_enderecoClientesNumeros.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.ed_enderecoClientesNumeros, 0, 5, 1, 1)

        self.lb_enderecoClienteBairro = QLabel(self.groupBox2_enderecoCadastroClientes)
        self.lb_enderecoClienteBairro.setObjectName(u"lb_enderecoClienteBairro")
        sizePolicy5.setHeightForWidth(self.lb_enderecoClienteBairro.sizePolicy().hasHeightForWidth())
        self.lb_enderecoClienteBairro.setSizePolicy(sizePolicy5)
        self.lb_enderecoClienteBairro.setMinimumSize(QSize(80, 0))
        self.lb_enderecoClienteBairro.setFont(font)

        self.gridLayout_2.addWidget(self.lb_enderecoClienteBairro, 1, 0, 1, 1)

        self.ed_enderecoClienteBairro = QLineEdit(self.groupBox2_enderecoCadastroClientes)
        self.ed_enderecoClienteBairro.setObjectName(u"ed_enderecoClienteBairro")

        self.gridLayout_2.addWidget(self.ed_enderecoClienteBairro, 1, 1, 1, 1)

        self.lb_enderecoClientesCep = QLabel(self.groupBox2_enderecoCadastroClientes)
        self.lb_enderecoClientesCep.setObjectName(u"lb_enderecoClientesCep")
        self.lb_enderecoClientesCep.setFont(font)

        self.gridLayout_2.addWidget(self.lb_enderecoClientesCep, 1, 3, 1, 1)

        self.ed_enderecoClientesCep = QLineEdit(self.groupBox2_enderecoCadastroClientes)
        self.ed_enderecoClientesCep.setObjectName(u"ed_enderecoClientesCep")
        sizePolicy4.setHeightForWidth(self.ed_enderecoClientesCep.sizePolicy().hasHeightForWidth())
        self.ed_enderecoClientesCep.setSizePolicy(sizePolicy4)
        self.ed_enderecoClientesCep.setMinimumSize(QSize(125, 0))
        self.ed_enderecoClientesCep.setMaximumSize(QSize(200, 16777215))
        self.ed_enderecoClientesCep.setFont(font8)
        self.ed_enderecoClientesCep.setInputMethodHints(Qt.ImhPreferNumbers)
        self.ed_enderecoClientesCep.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.ed_enderecoClientesCep, 1, 4, 1, 2)

        self.cb_enderecoClientesUF = QComboBox(self.groupBox2_enderecoCadastroClientes)
        self.cb_enderecoClientesUF.setObjectName(u"cb_enderecoClientesUF")
        self.cb_enderecoClientesUF.setFont(font)

        self.gridLayout_2.addWidget(self.cb_enderecoClientesUF, 3, 5, 1, 1)

        self.lb_enderecoClientesUF = QLabel(self.groupBox2_enderecoCadastroClientes)
        self.lb_enderecoClientesUF.setObjectName(u"lb_enderecoClientesUF")

        self.gridLayout_2.addWidget(self.lb_enderecoClientesUF, 3, 4, 1, 1)

        self.cb_enderecoClientesCidade = QComboBox(self.groupBox2_enderecoCadastroClientes)
        self.cb_enderecoClientesCidade.setObjectName(u"cb_enderecoClientesCidade")
        self.cb_enderecoClientesCidade.setFont(font)

        self.gridLayout_2.addWidget(self.cb_enderecoClientesCidade, 3, 1, 1, 3)

        self.ed_enderecoClientesReferencia = QLineEdit(self.groupBox2_enderecoCadastroClientes)
        self.ed_enderecoClientesReferencia.setObjectName(u"ed_enderecoClientesReferencia")
        self.ed_enderecoClientesReferencia.setFont(font8)
        self.ed_enderecoClientesReferencia.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.ed_enderecoClientesReferencia, 5, 1, 1, 5)


        self.verticalLayout_8.addWidget(self.groupBox2_enderecoCadastroClientes)


        self.verticalLayout_13.addWidget(self.frame1_mainCadastroClientes)

        self.frame2_btnCadastroClientes = QFrame(self.aba2_cadastroClientes)
        self.frame2_btnCadastroClientes.setObjectName(u"frame2_btnCadastroClientes")
        self.frame2_btnCadastroClientes.setFrameShape(QFrame.StyledPanel)
        self.frame2_btnCadastroClientes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame2_btnCadastroClientes)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.groupBox3_solicitanteCadastroClientes = QGroupBox(self.frame2_btnCadastroClientes)
        self.groupBox3_solicitanteCadastroClientes.setObjectName(u"groupBox3_solicitanteCadastroClientes")
        sizePolicy.setHeightForWidth(self.groupBox3_solicitanteCadastroClientes.sizePolicy().hasHeightForWidth())
        self.groupBox3_solicitanteCadastroClientes.setSizePolicy(sizePolicy)
        self.groupBox3_solicitanteCadastroClientes.setFont(font)
        self.verticalLayout_39 = QVBoxLayout(self.groupBox3_solicitanteCadastroClientes)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.ed_clientesSolicitante = QLineEdit(self.groupBox3_solicitanteCadastroClientes)
        self.ed_clientesSolicitante.setObjectName(u"ed_clientesSolicitante")

        self.verticalLayout_39.addWidget(self.ed_clientesSolicitante)


        self.horizontalLayout_13.addWidget(self.groupBox3_solicitanteCadastroClientes)

        self.btn_limparCadastroClientes = QPushButton(self.frame2_btnCadastroClientes)
        self.btn_limparCadastroClientes.setObjectName(u"btn_limparCadastroClientes")
        self.btn_limparCadastroClientes.setFont(font)
        self.btn_limparCadastroClientes.setIcon(icon21)
        self.btn_limparCadastroClientes.setIconSize(QSize(18, 18))

        self.horizontalLayout_13.addWidget(self.btn_limparCadastroClientes)

        self.btn_salvarCadastroClientes = QPushButton(self.frame2_btnCadastroClientes)
        self.btn_salvarCadastroClientes.setObjectName(u"btn_salvarCadastroClientes")
        self.btn_salvarCadastroClientes.setFont(font)
        self.btn_salvarCadastroClientes.setIcon(icon22)
        self.btn_salvarCadastroClientes.setIconSize(QSize(18, 18))

        self.horizontalLayout_13.addWidget(self.btn_salvarCadastroClientes)


        self.verticalLayout_13.addWidget(self.frame2_btnCadastroClientes)

        icon28 = QIcon()
        icon28.addFile(u":/assets/icons/user_add_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_clientes.addTab(self.aba2_cadastroClientes, icon28, "")

        self.verticalLayout_17.addWidget(self.aba_clientes)

        self.section.addWidget(self.s3_clientes)
        self.s2_usuarios = QWidget()
        self.s2_usuarios.setObjectName(u"s2_usuarios")
        self.verticalLayout_12 = QVBoxLayout(self.s2_usuarios)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_headerUsuario = QFrame(self.s2_usuarios)
        self.frame_headerUsuario.setObjectName(u"frame_headerUsuario")
        self.frame_headerUsuario.setFrameShape(QFrame.StyledPanel)
        self.frame_headerUsuario.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_headerUsuario)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lb_titleUsuarios = QLabel(self.frame_headerUsuario)
        self.lb_titleUsuarios.setObjectName(u"lb_titleUsuarios")
        self.lb_titleUsuarios.setFont(font3)
        self.lb_titleUsuarios.setLayoutDirection(Qt.LeftToRight)
        self.lb_titleUsuarios.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.lb_titleUsuarios)

        self.lineUsuarios = QFrame(self.frame_headerUsuario)
        self.lineUsuarios.setObjectName(u"lineUsuarios")
        self.lineUsuarios.setStyleSheet(u"background-color: #00718F;")
        self.lineUsuarios.setFrameShape(QFrame.HLine)
        self.lineUsuarios.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.lineUsuarios)


        self.verticalLayout_12.addWidget(self.frame_headerUsuario)

        self.aba_usuarios = QTabWidget(self.s2_usuarios)
        self.aba_usuarios.setObjectName(u"aba_usuarios")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.aba_usuarios.setPalette(palette1)
        self.aba_usuarios.setFont(font)
        self.aba_usuarios.setStyleSheet(u"")
        self.aba_usuarios.setIconSize(QSize(16, 16))
        self.aba1_listaUsuarios = QWidget()
        self.aba1_listaUsuarios.setObjectName(u"aba1_listaUsuarios")
        self.verticalLayout_15 = QVBoxLayout(self.aba1_listaUsuarios)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame1_listaUsuarios = QFrame(self.aba1_listaUsuarios)
        self.frame1_listaUsuarios.setObjectName(u"frame1_listaUsuarios")
        self.frame1_listaUsuarios.setFrameShape(QFrame.StyledPanel)
        self.frame1_listaUsuarios.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame1_listaUsuarios)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame1_btnUsuarios = QFrame(self.frame1_listaUsuarios)
        self.frame1_btnUsuarios.setObjectName(u"frame1_btnUsuarios")
        self.frame1_btnUsuarios.setFrameShape(QFrame.StyledPanel)
        self.frame1_btnUsuarios.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame1_btnUsuarios)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn1_editarUsuarios = QPushButton(self.frame1_btnUsuarios)
        self.btn1_editarUsuarios.setObjectName(u"btn1_editarUsuarios")
        self.btn1_editarUsuarios.setFont(font)
        self.btn1_editarUsuarios.setIcon(icon17)
        self.btn1_editarUsuarios.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.btn1_editarUsuarios)

        self.btn2_excluirUsuarios = QPushButton(self.frame1_btnUsuarios)
        self.btn2_excluirUsuarios.setObjectName(u"btn2_excluirUsuarios")
        self.btn2_excluirUsuarios.setFont(font)
        self.btn2_excluirUsuarios.setIcon(icon18)
        self.btn2_excluirUsuarios.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.btn2_excluirUsuarios)


        self.horizontalLayout_7.addWidget(self.frame1_btnUsuarios)

        self.frame2_pesquisaUsuarios = QFrame(self.frame1_listaUsuarios)
        self.frame2_pesquisaUsuarios.setObjectName(u"frame2_pesquisaUsuarios")
        self.frame2_pesquisaUsuarios.setFrameShape(QFrame.StyledPanel)
        self.frame2_pesquisaUsuarios.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame2_pesquisaUsuarios)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.barLine_pesquisaUsuarios = QLineEdit(self.frame2_pesquisaUsuarios)
        self.barLine_pesquisaUsuarios.setObjectName(u"barLine_pesquisaUsuarios")
        self.barLine_pesquisaUsuarios.setFont(font)

        self.horizontalLayout_5.addWidget(self.barLine_pesquisaUsuarios)

        self.btn_pesquisaUsuarios = QToolButton(self.frame2_pesquisaUsuarios)
        self.btn_pesquisaUsuarios.setObjectName(u"btn_pesquisaUsuarios")
        self.btn_pesquisaUsuarios.setIcon(icon19)
        self.btn_pesquisaUsuarios.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.btn_pesquisaUsuarios)


        self.horizontalLayout_7.addWidget(self.frame2_pesquisaUsuarios)


        self.verticalLayout_15.addWidget(self.frame1_listaUsuarios)

        self.tabela_usuarios = QTableWidget(self.aba1_listaUsuarios)
        if (self.tabela_usuarios.columnCount() < 6):
            self.tabela_usuarios.setColumnCount(6)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font5);
        self.tabela_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font5);
        self.tabela_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font5);
        self.tabela_usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font5);
        self.tabela_usuarios.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font5);
        self.tabela_usuarios.setHorizontalHeaderItem(4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font5);
        self.tabela_usuarios.setHorizontalHeaderItem(5, __qtablewidgetitem37)
        self.tabela_usuarios.setObjectName(u"tabela_usuarios")
        font10 = QFont()
        font10.setFamilies([u"Poppins"])
        font10.setPointSize(10)
        font10.setBold(False)
        font10.setItalic(False)
        self.tabela_usuarios.setFont(font10)
        self.tabela_usuarios.setAutoScroll(True)
        self.tabela_usuarios.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_usuarios.setProperty("showDropIndicator", False)
        self.tabela_usuarios.setDragEnabled(False)
        self.tabela_usuarios.setDragDropOverwriteMode(False)
        self.tabela_usuarios.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tabela_usuarios.setAlternatingRowColors(True)
        self.tabela_usuarios.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela_usuarios.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_usuarios.setTextElideMode(Qt.ElideRight)
        self.tabela_usuarios.setShowGrid(True)
        self.tabela_usuarios.setSortingEnabled(True)
        self.tabela_usuarios.setWordWrap(True)
        self.tabela_usuarios.setCornerButtonEnabled(True)
        self.tabela_usuarios.horizontalHeader().setVisible(True)
        self.tabela_usuarios.horizontalHeader().setCascadingSectionResizes(False)
        self.tabela_usuarios.horizontalHeader().setProperty("showSortIndicator", True)
        self.tabela_usuarios.verticalHeader().setCascadingSectionResizes(False)
        self.tabela_usuarios.verticalHeader().setProperty("showSortIndicator", False)
        self.tabela_usuarios.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_15.addWidget(self.tabela_usuarios)

        self.aba_usuarios.addTab(self.aba1_listaUsuarios, icon20, "")
        self.aba2_cadastroUsuarios = QWidget()
        self.aba2_cadastroUsuarios.setObjectName(u"aba2_cadastroUsuarios")
        self.verticalLayout_6 = QVBoxLayout(self.aba2_cadastroUsuarios)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame1_mainCadastroUsuarios = QFrame(self.aba2_cadastroUsuarios)
        self.frame1_mainCadastroUsuarios.setObjectName(u"frame1_mainCadastroUsuarios")
        self.frame1_mainCadastroUsuarios.setFrameShape(QFrame.StyledPanel)
        self.frame1_mainCadastroUsuarios.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame1_mainCadastroUsuarios)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ed_usuariosNome = QLineEdit(self.frame1_mainCadastroUsuarios)
        self.ed_usuariosNome.setObjectName(u"ed_usuariosNome")
        self.ed_usuariosNome.setFont(font7)
        self.ed_usuariosNome.setAlignment(Qt.AlignCenter)
        self.ed_usuariosNome.setDragEnabled(False)
        self.ed_usuariosNome.setReadOnly(False)
        self.ed_usuariosNome.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.ed_usuariosNome, 2, 0, 1, 4)

        self.ed_usuariosFuncao = QLineEdit(self.frame1_mainCadastroUsuarios)
        self.ed_usuariosFuncao.setObjectName(u"ed_usuariosFuncao")
        self.ed_usuariosFuncao.setFont(font5)
        self.ed_usuariosFuncao.setAlignment(Qt.AlignCenter)
        self.ed_usuariosFuncao.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.ed_usuariosFuncao, 8, 0, 1, 4)

        self.lb_usuariosFuncao = QLabel(self.frame1_mainCadastroUsuarios)
        self.lb_usuariosFuncao.setObjectName(u"lb_usuariosFuncao")
        self.lb_usuariosFuncao.setFont(font6)
        self.lb_usuariosFuncao.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_usuariosFuncao, 7, 0, 1, 4)

        self.ed_usuariosContato = QLineEdit(self.frame1_mainCadastroUsuarios)
        self.ed_usuariosContato.setObjectName(u"ed_usuariosContato")
        self.ed_usuariosContato.setFont(font5)
        self.ed_usuariosContato.setInputMethodHints(Qt.ImhPreferNumbers)
        self.ed_usuariosContato.setAlignment(Qt.AlignCenter)
        self.ed_usuariosContato.setReadOnly(False)
        self.ed_usuariosContato.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.ed_usuariosContato, 4, 0, 1, 4)

        self.lb_usuariosContato = QLabel(self.frame1_mainCadastroUsuarios)
        self.lb_usuariosContato.setObjectName(u"lb_usuariosContato")
        self.lb_usuariosContato.setFont(font6)
        self.lb_usuariosContato.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_usuariosContato, 3, 0, 1, 4)

        self.ed_usuariosEmail = QLineEdit(self.frame1_mainCadastroUsuarios)
        self.ed_usuariosEmail.setObjectName(u"ed_usuariosEmail")
        self.ed_usuariosEmail.setFont(font5)
        self.ed_usuariosEmail.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.ed_usuariosEmail.setAlignment(Qt.AlignCenter)
        self.ed_usuariosEmail.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.ed_usuariosEmail, 6, 0, 1, 4)

        self.lb_usuariosEmail = QLabel(self.frame1_mainCadastroUsuarios)
        self.lb_usuariosEmail.setObjectName(u"lb_usuariosEmail")
        self.lb_usuariosEmail.setFont(font6)
        self.lb_usuariosEmail.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_usuariosEmail, 5, 0, 1, 4)

        self.lb_usuariosNome = QLabel(self.frame1_mainCadastroUsuarios)
        self.lb_usuariosNome.setObjectName(u"lb_usuariosNome")
        self.lb_usuariosNome.setFont(font6)
        self.lb_usuariosNome.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_usuariosNome, 1, 0, 1, 4)

        self.lb_usuariosId = QLabel(self.frame1_mainCadastroUsuarios)
        self.lb_usuariosId.setObjectName(u"lb_usuariosId")
        self.lb_usuariosId.setFont(font6)

        self.gridLayout_4.addWidget(self.lb_usuariosId, 0, 0, 1, 1, Qt.AlignLeft)

        self.ed_usuarioId = QLineEdit(self.frame1_mainCadastroUsuarios)
        self.ed_usuarioId.setObjectName(u"ed_usuarioId")
        sizePolicy2.setHeightForWidth(self.ed_usuarioId.sizePolicy().hasHeightForWidth())
        self.ed_usuarioId.setSizePolicy(sizePolicy2)
        self.ed_usuarioId.setMaximumSize(QSize(356, 16777215))
        self.ed_usuarioId.setFont(font5)
        self.ed_usuarioId.setInputMethodHints(Qt.ImhNone)
        self.ed_usuarioId.setReadOnly(True)

        self.gridLayout_4.addWidget(self.ed_usuarioId, 0, 1, 1, 1)

        self.cb_usuariosDesativado = QCheckBox(self.frame1_mainCadastroUsuarios)
        self.cb_usuariosDesativado.setObjectName(u"cb_usuariosDesativado")
        self.cb_usuariosDesativado.setEnabled(False)
        self.cb_usuariosDesativado.setFont(font5)
        self.cb_usuariosDesativado.setCheckable(True)

        self.gridLayout_4.addWidget(self.cb_usuariosDesativado, 0, 2, 1, 2)


        self.verticalLayout_6.addWidget(self.frame1_mainCadastroUsuarios)

        self.frame2_btnCadastroUsuarios = QFrame(self.aba2_cadastroUsuarios)
        self.frame2_btnCadastroUsuarios.setObjectName(u"frame2_btnCadastroUsuarios")
        self.frame2_btnCadastroUsuarios.setFrameShape(QFrame.StyledPanel)
        self.frame2_btnCadastroUsuarios.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame2_btnCadastroUsuarios)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.btn_limparCadastroUsuarios = QPushButton(self.frame2_btnCadastroUsuarios)
        self.btn_limparCadastroUsuarios.setObjectName(u"btn_limparCadastroUsuarios")
        self.btn_limparCadastroUsuarios.setFont(font)
        self.btn_limparCadastroUsuarios.setIcon(icon21)
        self.btn_limparCadastroUsuarios.setIconSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.btn_limparCadastroUsuarios)

        self.btn_salvarCadastroUsurios = QPushButton(self.frame2_btnCadastroUsuarios)
        self.btn_salvarCadastroUsurios.setObjectName(u"btn_salvarCadastroUsurios")
        self.btn_salvarCadastroUsurios.setFont(font)
        self.btn_salvarCadastroUsurios.setIcon(icon22)
        self.btn_salvarCadastroUsurios.setIconSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.btn_salvarCadastroUsurios)


        self.verticalLayout_6.addWidget(self.frame2_btnCadastroUsuarios)

        self.aba_usuarios.addTab(self.aba2_cadastroUsuarios, icon28, "")

        self.verticalLayout_12.addWidget(self.aba_usuarios)

        self.section.addWidget(self.s2_usuarios)

        self.verticalLayout_11.addWidget(self.section)


        self.verticalLayout_3.addWidget(self.frame_section)


        self.horizontalLayout.addWidget(self.main)

        QWidget.setTabOrder(self.btn_toggleButton, self.btn1_whatsApp)
        QWidget.setTabOrder(self.btn1_whatsApp, self.btn2_instagram)
        QWidget.setTabOrder(self.btn2_instagram, self.btn3_linkedin)
        QWidget.setTabOrder(self.btn3_linkedin, self.btn4_github)
        QWidget.setTabOrder(self.btn4_github, self.btn5_email)
        QWidget.setTabOrder(self.btn5_email, self.btn1_home)
        QWidget.setTabOrder(self.btn1_home, self.btn2_usuarios)
        QWidget.setTabOrder(self.btn2_usuarios, self.btn3_clientes)
        QWidget.setTabOrder(self.btn3_clientes, self.btn4_protocolos)
        QWidget.setTabOrder(self.btn4_protocolos, self.calendario)
        QWidget.setTabOrder(self.calendario, self.btn1_editarUsuarios)
        QWidget.setTabOrder(self.btn1_editarUsuarios, self.btn2_excluirUsuarios)
        QWidget.setTabOrder(self.btn2_excluirUsuarios, self.barLine_pesquisaUsuarios)
        QWidget.setTabOrder(self.barLine_pesquisaUsuarios, self.btn_pesquisaUsuarios)
        QWidget.setTabOrder(self.btn_pesquisaUsuarios, self.tabela_usuarios)
        QWidget.setTabOrder(self.tabela_usuarios, self.aba_usuarios)
        QWidget.setTabOrder(self.aba_usuarios, self.ed_usuarioId)
        QWidget.setTabOrder(self.ed_usuarioId, self.cb_usuariosDesativado)
        QWidget.setTabOrder(self.cb_usuariosDesativado, self.ed_usuariosNome)
        QWidget.setTabOrder(self.ed_usuariosNome, self.ed_usuariosContato)
        QWidget.setTabOrder(self.ed_usuariosContato, self.ed_usuariosEmail)
        QWidget.setTabOrder(self.ed_usuariosEmail, self.ed_usuariosFuncao)
        QWidget.setTabOrder(self.ed_usuariosFuncao, self.btn_limparCadastroUsuarios)
        QWidget.setTabOrder(self.btn_limparCadastroUsuarios, self.btn_salvarCadastroUsurios)
        QWidget.setTabOrder(self.btn_salvarCadastroUsurios, self.aba_clientes)
        QWidget.setTabOrder(self.aba_clientes, self.btn1_editarClientes)
        QWidget.setTabOrder(self.btn1_editarClientes, self.btn2_excluirClientes)
        QWidget.setTabOrder(self.btn2_excluirClientes, self.barLine_pesquisaClientes)
        QWidget.setTabOrder(self.barLine_pesquisaClientes, self.btn_pesquisaClientes)
        QWidget.setTabOrder(self.btn_pesquisaClientes, self.tabela_clientes)
        QWidget.setTabOrder(self.tabela_clientes, self.ed_clientesId)
        QWidget.setTabOrder(self.ed_clientesId, self.cd_clientesDesativado)
        QWidget.setTabOrder(self.cd_clientesDesativado, self.ed_clientesRazaoSocial)
        QWidget.setTabOrder(self.ed_clientesRazaoSocial, self.ed_clientesCpfCnpj)
        QWidget.setTabOrder(self.ed_clientesCpfCnpj, self.rd_clientesFisica)
        QWidget.setTabOrder(self.rd_clientesFisica, self.rd_clientesJuridica)
        QWidget.setTabOrder(self.rd_clientesJuridica, self.ed_clientesContato)
        QWidget.setTabOrder(self.ed_clientesContato, self.ed_clientesEmail)
        QWidget.setTabOrder(self.ed_clientesEmail, self.ed_enderecoClientesLodradouro)
        QWidget.setTabOrder(self.ed_enderecoClientesLodradouro, self.ed_enderecoClientesNumeros)
        QWidget.setTabOrder(self.ed_enderecoClientesNumeros, self.ed_enderecoClienteBairro)
        QWidget.setTabOrder(self.ed_enderecoClienteBairro, self.ed_enderecoClientesCep)
        QWidget.setTabOrder(self.ed_enderecoClientesCep, self.cb_enderecoClientesUF)
        QWidget.setTabOrder(self.cb_enderecoClientesUF, self.cb_enderecoClientesCidade)
        QWidget.setTabOrder(self.cb_enderecoClientesCidade, self.ed_enderecoClientesReferencia)
        QWidget.setTabOrder(self.ed_enderecoClientesReferencia, self.ed_clientesSolicitante)
        QWidget.setTabOrder(self.ed_clientesSolicitante, self.btn_limparCadastroClientes)
        QWidget.setTabOrder(self.btn_limparCadastroClientes, self.btn_salvarCadastroClientes)
        QWidget.setTabOrder(self.btn_salvarCadastroClientes, self.aba_protocolos)
        QWidget.setTabOrder(self.aba_protocolos, self.barLine_pesquisaProtocolos)
        QWidget.setTabOrder(self.barLine_pesquisaProtocolos, self.btn_pesquisaProtocolos)
        QWidget.setTabOrder(self.btn_pesquisaProtocolos, self.btn1_editarProtocolos)
        QWidget.setTabOrder(self.btn1_editarProtocolos, self.btn2_excluirProtocolos)
        QWidget.setTabOrder(self.btn2_excluirProtocolos, self.btn4_pdfProtocolos)
        QWidget.setTabOrder(self.btn4_pdfProtocolos, self.btn5_wordProtocolos)
        QWidget.setTabOrder(self.btn5_wordProtocolos, self.btn6_whatsappProtocolos)
        QWidget.setTabOrder(self.btn6_whatsappProtocolos, self.tabela_protocolos)
        QWidget.setTabOrder(self.tabela_protocolos, self.ed_protocolosId)
        QWidget.setTabOrder(self.ed_protocolosId, self.cb_protocolosCancelado)
        QWidget.setTabOrder(self.cb_protocolosCancelado, self.cb_protocolosAtendimento)
        QWidget.setTabOrder(self.cb_protocolosAtendimento, self.cb_protocolosConsultor)
        QWidget.setTabOrder(self.cb_protocolosConsultor, self.cb_protocolosCliente)
        QWidget.setTabOrder(self.cb_protocolosCliente, self.cb_protocolosSolicitante)
        QWidget.setTabOrder(self.cb_protocolosSolicitante, self.date_protocolosData)
        QWidget.setTabOrder(self.date_protocolosData, self.date_protocolosInicio)
        QWidget.setTabOrder(self.date_protocolosInicio, self.date_protocolosTermino)
        QWidget.setTabOrder(self.date_protocolosTermino, self.ed_protocolosDescricao)
        QWidget.setTabOrder(self.ed_protocolosDescricao, self.btn_protocolosRobot)
        QWidget.setTabOrder(self.btn_protocolosRobot, self.btn_limparCadastroProtocolos)
        QWidget.setTabOrder(self.btn_limparCadastroProtocolos, self.btn_salvarCadastroProtocolos)
        QWidget.setTabOrder(self.btn_salvarCadastroProtocolos, self.btn_selecionarLogoEmpresa)
        QWidget.setTabOrder(self.btn_selecionarLogoEmpresa, self.btn_removerLogoEmpresa)
        QWidget.setTabOrder(self.btn_removerLogoEmpresa, self.btn_editarEmpresa)
        QWidget.setTabOrder(self.btn_editarEmpresa, self.btn_excluirEmpresa)
        QWidget.setTabOrder(self.btn_excluirEmpresa, self.btn_salvarEmpresa)
        QWidget.setTabOrder(self.btn_salvarEmpresa, self.ed_empresaId)
        QWidget.setTabOrder(self.ed_empresaId, self.radioButton_empresaFisica)
        QWidget.setTabOrder(self.radioButton_empresaFisica, self.radioButton_empresaJuridica)
        QWidget.setTabOrder(self.radioButton_empresaJuridica, self.ed_empresaRazaoSocial)
        QWidget.setTabOrder(self.ed_empresaRazaoSocial, self.ed_empresaCpfCnpj)
        QWidget.setTabOrder(self.ed_empresaCpfCnpj, self.ed_empresaContato)
        QWidget.setTabOrder(self.ed_empresaContato, self.ed_empresaEmail)
        QWidget.setTabOrder(self.ed_empresaEmail, self.ed_empresaLogradouro)
        QWidget.setTabOrder(self.ed_empresaLogradouro, self.ed_empresaNumero)
        QWidget.setTabOrder(self.ed_empresaNumero, self.ed_empresaBairro)
        QWidget.setTabOrder(self.ed_empresaBairro, self.ed_empresaCep)
        QWidget.setTabOrder(self.ed_empresaCep, self.cb_empresaCidade)
        QWidget.setTabOrder(self.cb_empresaCidade, self.cb_empresaUf)
        QWidget.setTabOrder(self.cb_empresaUf, self.ed_empresaReferencia)
        QWidget.setTabOrder(self.ed_empresaReferencia, self.aba_tipos_atendimento)
        QWidget.setTabOrder(self.aba_tipos_atendimento, self.btn1_editarTiposAtendimento)
        QWidget.setTabOrder(self.btn1_editarTiposAtendimento, self.btn2_excluirTiposAtendimento)
        QWidget.setTabOrder(self.btn2_excluirTiposAtendimento, self.barLine_pesquisaTiposAtendimento)
        QWidget.setTabOrder(self.barLine_pesquisaTiposAtendimento, self.btn_pesquisaTiposAtendimento)
        QWidget.setTabOrder(self.btn_pesquisaTiposAtendimento, self.tabela_tiposAtendimento)
        QWidget.setTabOrder(self.tabela_tiposAtendimento, self.ed_tiposAtendimentoId)
        QWidget.setTabOrder(self.ed_tiposAtendimentoId, self.cb_tiposAtendimentoDesativado)
        QWidget.setTabOrder(self.cb_tiposAtendimentoDesativado, self.ed_tiposAtendimentoDescricao)
        QWidget.setTabOrder(self.ed_tiposAtendimentoDescricao, self.btn_limparCadastroTiposAtendimento)
        QWidget.setTabOrder(self.btn_limparCadastroTiposAtendimento, self.btn_salvarCadastroTiposAtendimento)
        QWidget.setTabOrder(self.btn_salvarCadastroTiposAtendimento, self.aba_avisos)
        QWidget.setTabOrder(self.aba_avisos, self.btn1_editarAvisos)
        QWidget.setTabOrder(self.btn1_editarAvisos, self.btn2_excluirAvisos)
        QWidget.setTabOrder(self.btn2_excluirAvisos, self.barLine_pesquisaAvisos)
        QWidget.setTabOrder(self.barLine_pesquisaAvisos, self.btn_pesquisaAvisos)
        QWidget.setTabOrder(self.btn_pesquisaAvisos, self.tabela_avisos)
        QWidget.setTabOrder(self.tabela_avisos, self.ed_avisosId)
        QWidget.setTabOrder(self.ed_avisosId, self.cb_avisosDesativado)
        QWidget.setTabOrder(self.cb_avisosDesativado, self.ed_avisosDescricao)
        QWidget.setTabOrder(self.ed_avisosDescricao, self.ed_avisosMensagem)
        QWidget.setTabOrder(self.ed_avisosMensagem, self.btn_limparCadastroAvisos)
        QWidget.setTabOrder(self.btn_limparCadastroAvisos, self.btn_salvarCadastroAvisos)
        QWidget.setTabOrder(self.btn_salvarCadastroAvisos, self.btn4_sobre)
        QWidget.setTabOrder(self.btn4_sobre, self.btn2_tipoAtendimento)
        QWidget.setTabOrder(self.btn2_tipoAtendimento, self.btn1_empresa)
        QWidget.setTabOrder(self.btn1_empresa, self.btn3_avisos)

        self.retranslateUi(MainWindow)

        self.toolBox_menu.setCurrentIndex(0)
        self.section.setCurrentIndex(0)
        self.aba_avisos.setCurrentIndex(0)
        self.aba_tipos_atendimento.setCurrentIndex(0)
        self.aba_protocolos.setCurrentIndex(0)
        self.aba_clientes.setCurrentIndex(0)
        self.aba_usuarios.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ProtoClick - Protocolo Inteligente", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/assets/icons/logo_protoclick.png\"/></p></body></html>", None))
        self.btn1_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn2_usuarios.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.btn3_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn4_protocolos.setText(QCoreApplication.translate("MainWindow", u"Protocolos", None))
        self.toolBox_menu.setItemText(self.toolBox_menu.indexOf(self.m1_menu), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn1_empresa.setText(QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.btn2_tipoAtendimento.setText(QCoreApplication.translate("MainWindow", u"Tipos", None))
        self.btn3_avisos.setText(QCoreApplication.translate("MainWindow", u"Avisos", None))
        self.btn4_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.lb_copyright.setText(QCoreApplication.translate("MainWindow", u"\u00a9 ProtoClick 2024", None))
        self.toolBox_menu.setItemText(self.toolBox_menu.indexOf(self.m2_configuracoes), QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.btn_toggleButton.setText("")
        self.btn1_whatsApp.setText("")
        self.btn2_instagram.setText("")
        self.btn3_linkedin.setText("")
        self.btn4_github.setText("")
        self.btn5_email.setText("")
        self.lb_titleSobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.lb1_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Bem-vindo ao </span><span style=\" font-size:10pt; font-weight:700;\">ProtoClick</span><span style=\" font-size:10pt;\">, a solu\u00e7\u00e3o definitiva para simplificar e</span></p><p align=\"center\"><span style=\" font-size:10pt;\">aprimorar o gerenciamento de protocolos de atendimento aos</span></p><p align=\"center\"><span style=\" font-size:10pt;\">clientes. Com nossa tecnologia avan\u00e7ada e recursos inovadores,</span></p><p align=\"center\"><span style=\" font-size:10pt;\">voc\u00ea ter\u00e1 todas as ferramentas necess\u00e1rias para organizar,</span></p><p align=\"center\"><span style=\" font-size:10pt;\">automatizar e otimizar seus processos de atendimento,</span></p><p align=\"center\"><span style=\" font-size:10pt;\">proporcionando uma experi\u00eancia excepcional para seus clientes.</span></p></body></html>", None))
        self.lb2_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; text-decoration: underline;\">Principais Recursos:</span></p><p align=\"center\"><span style=\" font-weight:700;\">Automatiza\u00e7\u00e3o Inteligente:</span> Economize tempo e esfor\u00e7o com a automatiza\u00e7\u00e3o</p><p align=\"center\">da cria\u00e7\u00e3o de protocolos, permitindo que voc\u00ea se concentre em tarefas estrat\u00e9gicas.</p><p align=\"center\"><span style=\" font-weight:700;\">Consist\u00eancia e Precis\u00e3o: </span>Utilize a intelig\u00eancia artificial para garantir a consist\u00eancia e precis\u00e3o</p><p align=\"center\">das informa\u00e7\u00f5es nos protocolos, com sugest\u00f5es autom\u00e1ticas para completar campos relevantes.</p><p align=\"center\"><span style=\" font-weight:700;\">Gest\u00e3o Eficiente: </span>Organize e categorize os protocolos de forma inteligente, facilitando</p><p align=\"center\">a gest\u00e3o de m\u00faltiplos casos simultaneamente, com filtros e ferramentas de busca avan\u00e7adas"
                        ".</p></body></html>", None))
        self.lb3_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/><span style=\" font-size:10pt; font-style:italic;\">Experimente agora mesmo o Software de Protocolo Inteligente da ProtoClick</span></p><p align=\"center\"><span style=\" font-size:10pt; font-style:italic;\">e eleve o seu atendimento ao pr\u00f3ximo n\u00edvel!</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Vers\u00e3o 1.0 - 24 de Mar\u00e7o de 2024", None))
        self.lb_titleAvisos.setText(QCoreApplication.translate("MainWindow", u"Avisos", None))
        self.btn1_editarAvisos.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn2_excluirAvisos.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.barLine_pesquisaAvisos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.btn_pesquisaAvisos.setText("")
        ___qtablewidgetitem = self.tabela_avisos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tabela_avisos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem2 = self.tabela_avisos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Mensagem", None));
        ___qtablewidgetitem3 = self.tabela_avisos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Desativado", None));
        self.aba_avisos.setTabText(self.aba_avisos.indexOf(self.aba1_listaAvisos), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.lb_avisosId.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.cb_avisosDesativado.setText(QCoreApplication.translate("MainWindow", u"Desativado", None))
        self.lb_avisosDescricao.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.lb_avisosMensagem.setText(QCoreApplication.translate("MainWindow", u"Mensagem", None))
        self.btn_limparCadastroAvisos.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btn_salvarCadastroAvisos.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.aba_avisos.setTabText(self.aba_avisos.indexOf(self.aba2_cadastroAvisos), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.lb_titleTiposAtendimento.setText(QCoreApplication.translate("MainWindow", u"Tipos de Atendimento", None))
        self.btn1_editarTiposAtendimento.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn2_excluirTiposAtendimento.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.barLine_pesquisaTiposAtendimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.btn_pesquisaTiposAtendimento.setText("")
        ___qtablewidgetitem4 = self.tabela_tiposAtendimento.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem5 = self.tabela_tiposAtendimento.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem6 = self.tabela_tiposAtendimento.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Desativado", None));
        self.aba_tipos_atendimento.setTabText(self.aba_tipos_atendimento.indexOf(self.aba1_listaTiposAtendimento), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.lb_tiposAtendimentoId.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.cb_tiposAtendimentoDesativado.setText(QCoreApplication.translate("MainWindow", u"Desativado", None))
        self.lb_tiposAtendimentoDescricao.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.ed_tiposAtendimentoDescricao.setInputMask("")
        self.ed_tiposAtendimentoDescricao.setText("")
        self.btn_limparCadastroTiposAtendimento.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btn_salvarCadastroTiposAtendimento.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.aba_tipos_atendimento.setTabText(self.aba_tipos_atendimento.indexOf(self.aba2_cadastroTiposAtendimento), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.lb_titleEmpresa.setText(QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.groupBox_logoEmpresa.setTitle(QCoreApplication.translate("MainWindow", u"Logo", None))
        self.btn_selecionarLogoEmpresa.setText(QCoreApplication.translate("MainWindow", u"Selecionar", None))
        self.btn_removerLogoEmpresa.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.logoEmpresa.setText("")
        self.btn_editarEmpresa.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_excluirEmpresa.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_salvarEmpresa.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.groupBox1_identificacaoEmpresa.setTitle(QCoreApplication.translate("MainWindow", u"Identifica\u00e7\u00e3o", None))
        self.lb_empresaContato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.lb_empresaId.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.lb_empresaRazaoSocial.setText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o Social", None))
        self.radioButton_empresaJuridica.setText(QCoreApplication.translate("MainWindow", u"Jur\u00eddica", None))
        self.ed_empresaContato.setInputMask(QCoreApplication.translate("MainWindow", u"+55 (00) 0 0000-0000", None))
        self.lb_empresaCpfCnpj.setText(QCoreApplication.translate("MainWindow", u"CPF / CNPJ", None))
        self.radioButton_empresaFisica.setText(QCoreApplication.translate("MainWindow", u"F\u00edsica", None))
        self.ed_empresaCpfCnpj.setInputMask(QCoreApplication.translate("MainWindow", u"00000000000000", None))
        self.ed_empresaCpfCnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00.000.000/0001-00", None))
        self.lb_empresaEmail.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.ed_empresaEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email@email.com.br", None))
        self.groupBox2_enderecoEmpresa.setTitle(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.lb_empresaCidade.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.lb_empresaNumero.setText(QCoreApplication.translate("MainWindow", u"N\u00ba", None))
        self.ed_empresaNumero.setPlaceholderText("")
        self.lb_empresaLogradoura.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.lb_empresaCep.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.lb_empresaReferencia.setText(QCoreApplication.translate("MainWindow", u"Refer\u00eancia", None))
        self.lb_empresaBairro.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.lb_empresaUf.setText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.ed_empresaCep.setInputMask(QCoreApplication.translate("MainWindow", u"00.000-000", None))
        self.lb_titleProtocolos.setText(QCoreApplication.translate("MainWindow", u"Protocolos", None))
        self.barLine_pesquisaProtocolos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.btn_pesquisaProtocolos.setText("")
        self.btn1_editarProtocolos.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn2_excluirProtocolos.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn4_pdfProtocolos.setText(QCoreApplication.translate("MainWindow", u"PDV", None))
        self.btn5_wordProtocolos.setText(QCoreApplication.translate("MainWindow", u"Word", None))
        self.btn6_whatsappProtocolos.setText(QCoreApplication.translate("MainWindow", u"WhatsApp", None))
        ___qtablewidgetitem7 = self.tabela_protocolos.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem8 = self.tabela_protocolos.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem9 = self.tabela_protocolos.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem10 = self.tabela_protocolos.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Solicitante", None));
        ___qtablewidgetitem11 = self.tabela_protocolos.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtablewidgetitem12 = self.tabela_protocolos.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Tipo de Atendimento", None));
        ___qtablewidgetitem13 = self.tabela_protocolos.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None));
        ___qtablewidgetitem14 = self.tabela_protocolos.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None));
        ___qtablewidgetitem15 = self.tabela_protocolos.horizontalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"T\u00e9minio", None));
        ___qtablewidgetitem16 = self.tabela_protocolos.horizontalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Cancelado", None));
        self.aba_protocolos.setTabText(self.aba_protocolos.indexOf(self.aba1_listaProtocolos), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.lb_protocolosTermino.setText(QCoreApplication.translate("MainWindow", u"T\u00e9rmino", None))
        self.lb_protocolosConsultor.setText(QCoreApplication.translate("MainWindow", u"Consultor", None))
        self.lb_protocolosCliente.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.lb_protocolosSolicitante.setText(QCoreApplication.translate("MainWindow", u"Solicitante", None))
        self.lb_protocolosData.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.lb_protocolosInicio.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.lb_protocolosAtendimento.setText(QCoreApplication.translate("MainWindow", u"Atendimento", None))
        self.btn_protocolosRobot.setText(QCoreApplication.translate("MainWindow", u"Aprimorar", None))
        self.lb_protocolosDescricao.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.lb_protocolosId.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.cb_protocolosCancelado.setText(QCoreApplication.translate("MainWindow", u"Cancelado", None))
        self.btn_limparCadastroProtocolos.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btn_salvarCadastroProtocolos.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.aba_protocolos.setTabText(self.aba_protocolos.indexOf(self.aba2_cadastroProtocolos), QCoreApplication.translate("MainWindow", u"Protocolo", None))
        self.lb_titleClientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn1_editarClientes.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn2_excluirClientes.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.barLine_pesquisaClientes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.btn_pesquisaClientes.setText("")
        ___qtablewidgetitem17 = self.tabela_clientes.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem18 = self.tabela_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o Social", None));
        ___qtablewidgetitem19 = self.tabela_clientes.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"CPF / CNPJ", None));
        ___qtablewidgetitem20 = self.tabela_clientes.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Natureza Social", None));
        ___qtablewidgetitem21 = self.tabela_clientes.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Contato", None));
        ___qtablewidgetitem22 = self.tabela_clientes.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem23 = self.tabela_clientes.horizontalHeaderItem(6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Solicitante", None));
        ___qtablewidgetitem24 = self.tabela_clientes.horizontalHeaderItem(7)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem25 = self.tabela_clientes.horizontalHeaderItem(8)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None));
        ___qtablewidgetitem26 = self.tabela_clientes.horizontalHeaderItem(9)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None));
        ___qtablewidgetitem27 = self.tabela_clientes.horizontalHeaderItem(10)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem28 = self.tabela_clientes.horizontalHeaderItem(11)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem29 = self.tabela_clientes.horizontalHeaderItem(12)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem30 = self.tabela_clientes.horizontalHeaderItem(13)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Refer\u00eancia", None));
        ___qtablewidgetitem31 = self.tabela_clientes.horizontalHeaderItem(14)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Desativado", None));
        self.aba_clientes.setTabText(self.aba_clientes.indexOf(self.aba1_listaClientes), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.groupBox1_identificacaoCadastroClientes.setTitle(QCoreApplication.translate("MainWindow", u"Identifica\u00e7\u00e3o", None))
        self.lb_clientesContato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.lb_clientesId.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.lb_clientesRazaoSocial.setText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o Social", None))
        self.lb_clientesCpfCnpj.setText(QCoreApplication.translate("MainWindow", u"CPF / CNPJ", None))
        self.rd_clientesFisica.setText(QCoreApplication.translate("MainWindow", u"F\u00edsica", None))
        self.rd_clientesJuridica.setText(QCoreApplication.translate("MainWindow", u"J\u00faridica", None))
        self.ed_clientesContato.setInputMask(QCoreApplication.translate("MainWindow", u"+55 (00) 0 0000-0000", None))
        self.lv_clientesEmail.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.cd_clientesDesativado.setText(QCoreApplication.translate("MainWindow", u"Desativado", None))
        self.ed_clientesCpfCnpj.setInputMask(QCoreApplication.translate("MainWindow", u"00000000000000", None))
        self.ed_clientesCpfCnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00.000.000/0001-00", None))
        self.ed_clientesEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email@email.com.br", None))
        self.groupBox2_enderecoCadastroClientes.setTitle(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.lb_enderecoClientesCidade.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.lb_enderecoClientesNumero.setText(QCoreApplication.translate("MainWindow", u"N\u00ba", None))
        self.lb_enderecoClientesReferencia.setText(QCoreApplication.translate("MainWindow", u"Refer\u00eancia", None))
        self.lb_enderecoClientesLogradouro.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.ed_enderecoClientesNumeros.setPlaceholderText("")
        self.lb_enderecoClienteBairro.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.lb_enderecoClientesCep.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.ed_enderecoClientesCep.setInputMask(QCoreApplication.translate("MainWindow", u"00.000-000", None))
        self.lb_enderecoClientesUF.setText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.groupBox3_solicitanteCadastroClientes.setTitle(QCoreApplication.translate("MainWindow", u"Solicitante", None))
        self.btn_limparCadastroClientes.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btn_salvarCadastroClientes.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.aba_clientes.setTabText(self.aba_clientes.indexOf(self.aba2_cadastroClientes), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.lb_titleUsuarios.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.btn1_editarUsuarios.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn2_excluirUsuarios.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.barLine_pesquisaUsuarios.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.btn_pesquisaUsuarios.setText("")
        ___qtablewidgetitem32 = self.tabela_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem33 = self.tabela_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem34 = self.tabela_usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Contato", None));
        ___qtablewidgetitem35 = self.tabela_usuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem36 = self.tabela_usuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o", None));
        ___qtablewidgetitem37 = self.tabela_usuarios.horizontalHeaderItem(5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Desativado", None));
        self.aba_usuarios.setTabText(self.aba_usuarios.indexOf(self.aba1_listaUsuarios), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.ed_usuariosNome.setInputMask("")
        self.ed_usuariosNome.setText("")
        self.lb_usuariosFuncao.setText(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o", None))
        self.ed_usuariosContato.setInputMask(QCoreApplication.translate("MainWindow", u"+55 (00) 0 0000-0000", None))
        self.ed_usuariosContato.setText(QCoreApplication.translate("MainWindow", u"+55 ()  -", None))
        self.ed_usuariosContato.setPlaceholderText("")
        self.lb_usuariosContato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.ed_usuariosEmail.setInputMask("")
        self.ed_usuariosEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email@email.com.br", None))
        self.lb_usuariosEmail.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.lb_usuariosNome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lb_usuariosId.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.cb_usuariosDesativado.setText(QCoreApplication.translate("MainWindow", u"Desativado", None))
        self.btn_limparCadastroUsuarios.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btn_salvarCadastroUsurios.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.aba_usuarios.setTabText(self.aba_usuarios.indexOf(self.aba2_cadastroUsuarios), QCoreApplication.translate("MainWindow", u"Cadastro", None))
    # retranslateUi

