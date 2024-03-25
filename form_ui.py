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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCalendarWidget, QCheckBox,
    QComboBox, QDateEdit, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QTimeEdit, QToolBox,
    QToolButton, QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 650)
        font = QFont()
        font.setFamilies([u"Poppins"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/p_logo.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.toolBox_menu.setStyleSheet(u"")
        self.m1_menu = QWidget()
        self.m1_menu.setObjectName(u"m1_menu")
        self.m1_menu.setGeometry(QRect(0, 0, 160, 470))
        self.verticalLayout_4 = QVBoxLayout(self.m1_menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn1_home = QPushButton(self.m1_menu)
        self.btn1_home.setObjectName(u"btn1_home")
        self.btn1_home.setFont(font2)
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
        self.m2_configuracoes.setGeometry(QRect(0, 0, 160, 470))
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
"    border-radiu"
                        "s: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"    background-color: #00718F;\n"
"    border: 2px solid #00718F;\n"
"    border-radius: 3px;\n"
"	image: url(:/icons/icons/close.svg);\n"
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
"    background-color: #00718F;\n"
"    color: #ffffff;\n"
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
"    to"
                        "p: -10 px;\n"
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
"    border: 2px solid #00718F;\n"
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
"QComboBox {\n"
"    padding: 5px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: #FFF;\n"
"}\n"
"\n"
"QComboBox::dro"
                        "p-down {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right;\n"
"    border-left: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/caret-down.svg);\n"
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
"	border-top-ri"
                        "ght-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::up-arrow, QTimeEdit::up-arrow {\n"
"	image: url(:/icons/icons/caret-up.svg);\n"
"	width: 15px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow, QTimeEdit::down-arrow {\n"
"	image: url(:/icons/icons/caret-down.svg);\n"
"	width: 15px;\n"
"}\n"
"\n"
"QDateEdit:hover, QTimeEdit:hover {\n"
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

        self.btn4_email = QToolButton(self.frame2_socialMedia)
        self.btn4_email.setObjectName(u"btn4_email")
        self.btn4_email.setStyleSheet(u"padding:5px;")
        icon15 = QIcon()
        icon15.addFile(u":/assets/icons/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn4_email.setIcon(icon15)
        self.btn4_email.setIconSize(QSize(20, 20))

        self.horizontalLayout_27.addWidget(self.btn4_email)

        self.toolButton = QToolButton(self.frame2_socialMedia)
        self.toolButton.setObjectName(u"toolButton")
        icon16 = QIcon()
        icon16.addFile(u":/assets/icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon16)
        self.toolButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_27.addWidget(self.toolButton)


        self.horizontalLayout_3.addWidget(self.frame2_socialMedia)


        self.verticalLayout_3.addWidget(self.frame_header)

        self.section = QFrame(self.main)
        self.section.setObjectName(u"section")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.section.sizePolicy().hasHeightForWidth())
        self.section.setSizePolicy(sizePolicy1)
        self.section.setFont(font)
        self.section.setStyleSheet(u"")
        self.section.setFrameShape(QFrame.StyledPanel)
        self.section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.section)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.stackedWidget = QStackedWidget(self.section)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.s1_home = QWidget()
        self.s1_home.setObjectName(u"s1_home")
        self.verticalLayout_9 = QVBoxLayout(self.s1_home)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.calendarWidget = QCalendarWidget(self.s1_home)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)

        self.verticalLayout_9.addWidget(self.calendarWidget)

        self.frame_30 = QFrame(self.s1_home)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_30)

        self.stackedWidget.addWidget(self.s1_home)
        self.s8_sobre = QWidget()
        self.s8_sobre.setObjectName(u"s8_sobre")
        self.verticalLayout_35 = QVBoxLayout(self.s8_sobre)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_23 = QFrame(self.s8_sobre)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_23)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lb_title_clientes_6 = QLabel(self.frame_23)
        self.lb_title_clientes_6.setObjectName(u"lb_title_clientes_6")
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.lb_title_clientes_6.setFont(font3)

        self.verticalLayout_7.addWidget(self.lb_title_clientes_6)

        self.line_clientes_6 = QFrame(self.frame_23)
        self.line_clientes_6.setObjectName(u"line_clientes_6")
        self.line_clientes_6.setStyleSheet(u"background-color: #00718F;")
        self.line_clientes_6.setFrameShape(QFrame.HLine)
        self.line_clientes_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_clientes_6)


        self.verticalLayout_35.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.s8_sobre)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy1.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy1)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_24)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_26 = QLabel(self.frame_24)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_36.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_24)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_36.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_24)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_36.addWidget(self.label_28)


        self.verticalLayout_35.addWidget(self.frame_24)

        self.stackedWidget.addWidget(self.s8_sobre)
        self.s7_avisos = QWidget()
        self.s7_avisos.setObjectName(u"s7_avisos")
        self.verticalLayout_34 = QVBoxLayout(self.s7_avisos)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_18 = QFrame(self.s7_avisos)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lb_title_clientes_5 = QLabel(self.frame_18)
        self.lb_title_clientes_5.setObjectName(u"lb_title_clientes_5")
        self.lb_title_clientes_5.setFont(font3)

        self.verticalLayout_10.addWidget(self.lb_title_clientes_5)

        self.line_clientes_5 = QFrame(self.frame_18)
        self.line_clientes_5.setObjectName(u"line_clientes_5")
        self.line_clientes_5.setStyleSheet(u"background-color: #00718F;")
        self.line_clientes_5.setFrameShape(QFrame.HLine)
        self.line_clientes_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_clientes_5)


        self.verticalLayout_34.addWidget(self.frame_18)

        self.tabWidget_5 = QTabWidget(self.s7_avisos)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.lista_clientes_3 = QWidget()
        self.lista_clientes_3.setObjectName(u"lista_clientes_3")
        self.verticalLayout_30 = QVBoxLayout(self.lista_clientes_3)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_19 = QFrame(self.lista_clientes_3)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_btn_lista_clientes_4 = QFrame(self.frame_19)
        self.frame_btn_lista_clientes_4.setObjectName(u"frame_btn_lista_clientes_4")
        self.frame_btn_lista_clientes_4.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_lista_clientes_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_btn_lista_clientes_4)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.btn_editar_clientes_4 = QPushButton(self.frame_btn_lista_clientes_4)
        self.btn_editar_clientes_4.setObjectName(u"btn_editar_clientes_4")
        self.btn_editar_clientes_4.setFont(font)
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editar_clientes_4.setIcon(icon17)
        self.btn_editar_clientes_4.setIconSize(QSize(18, 18))

        self.horizontalLayout_23.addWidget(self.btn_editar_clientes_4)

        self.btn_excluir_clientes_4 = QPushButton(self.frame_btn_lista_clientes_4)
        self.btn_excluir_clientes_4.setObjectName(u"btn_excluir_clientes_4")
        self.btn_excluir_clientes_4.setFont(font)
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/excluir.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir_clientes_4.setIcon(icon18)
        self.btn_excluir_clientes_4.setIconSize(QSize(18, 18))

        self.horizontalLayout_23.addWidget(self.btn_excluir_clientes_4)


        self.horizontalLayout_22.addWidget(self.frame_btn_lista_clientes_4)

        self.frame_barra_pesquisa_clientes_4 = QFrame(self.frame_19)
        self.frame_barra_pesquisa_clientes_4.setObjectName(u"frame_barra_pesquisa_clientes_4")
        self.frame_barra_pesquisa_clientes_4.setFrameShape(QFrame.StyledPanel)
        self.frame_barra_pesquisa_clientes_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_barra_pesquisa_clientes_4)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.ed_barra_pesquisa_clientes_4 = QLineEdit(self.frame_barra_pesquisa_clientes_4)
        self.ed_barra_pesquisa_clientes_4.setObjectName(u"ed_barra_pesquisa_clientes_4")
        self.ed_barra_pesquisa_clientes_4.setFont(font)

        self.horizontalLayout_24.addWidget(self.ed_barra_pesquisa_clientes_4)

        self.btn_pesquisa_clientes_4 = QToolButton(self.frame_barra_pesquisa_clientes_4)
        self.btn_pesquisa_clientes_4.setObjectName(u"btn_pesquisa_clientes_4")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisa_clientes_4.setIcon(icon19)
        self.btn_pesquisa_clientes_4.setIconSize(QSize(18, 18))

        self.horizontalLayout_24.addWidget(self.btn_pesquisa_clientes_4)


        self.horizontalLayout_22.addWidget(self.frame_barra_pesquisa_clientes_4)


        self.verticalLayout_30.addWidget(self.frame_19)

        self.tableWidget_4 = QTableWidget(self.lista_clientes_3)
        if (self.tableWidget_4.columnCount() < 3):
            self.tableWidget_4.setColumnCount(3)
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        font4.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setFont(font4)

        self.verticalLayout_30.addWidget(self.tableWidget_4)

        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/lista-branco.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget_5.addTab(self.lista_clientes_3, icon20, "")
        self.cadastro_clientes_3 = QWidget()
        self.cadastro_clientes_3.setObjectName(u"cadastro_clientes_3")
        self.verticalLayout_32 = QVBoxLayout(self.cadastro_clientes_3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_20 = QFrame(self.cadastro_clientes_3)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy1.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy1)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_20)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lb_usuarios_id_3 = QLabel(self.frame_21)
        self.lb_usuarios_id_3.setObjectName(u"lb_usuarios_id_3")
        font5 = QFont()
        font5.setFamilies([u"Poppins"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.lb_usuarios_id_3.setFont(font5)
        self.lb_usuarios_id_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.lb_usuarios_id_3)

        self.ed_usuario_id_3 = QLineEdit(self.frame_21)
        self.ed_usuario_id_3.setObjectName(u"ed_usuario_id_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ed_usuario_id_3.sizePolicy().hasHeightForWidth())
        self.ed_usuario_id_3.setSizePolicy(sizePolicy2)
        self.ed_usuario_id_3.setMaximumSize(QSize(356, 16777215))
        self.ed_usuario_id_3.setFont(font4)
        self.ed_usuario_id_3.setInputMethodHints(Qt.ImhNone)
        self.ed_usuario_id_3.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.ed_usuario_id_3)

        self.cb_usuarios_desativado_3 = QCheckBox(self.frame_21)
        self.cb_usuarios_desativado_3.setObjectName(u"cb_usuarios_desativado_3")
        self.cb_usuarios_desativado_3.setEnabled(True)
        self.cb_usuarios_desativado_3.setFont(font4)
        self.cb_usuarios_desativado_3.setCheckable(True)

        self.horizontalLayout_25.addWidget(self.cb_usuarios_desativado_3)


        self.verticalLayout_33.addWidget(self.frame_21, 0, Qt.AlignLeft)

        self.lb_usuarios_nome_3 = QLabel(self.frame_20)
        self.lb_usuarios_nome_3.setObjectName(u"lb_usuarios_nome_3")
        self.lb_usuarios_nome_3.setFont(font5)
        self.lb_usuarios_nome_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.lb_usuarios_nome_3)

        self.textEdit = QTextEdit(self.frame_20)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_33.addWidget(self.textEdit)

        self.verticalSpacer_5 = QSpacerItem(20, 198, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_5)


        self.verticalLayout_32.addWidget(self.frame_20)

        self.frame_22 = QFrame(self.cadastro_clientes_3)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_5 = QSpacerItem(312, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_5)

        self.btn_limpar_cd_usuarios_4 = QPushButton(self.frame_22)
        self.btn_limpar_cd_usuarios_4.setObjectName(u"btn_limpar_cd_usuarios_4")
        self.btn_limpar_cd_usuarios_4.setFont(font)
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/limpar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_cd_usuarios_4.setIcon(icon21)
        self.btn_limpar_cd_usuarios_4.setIconSize(QSize(18, 18))

        self.horizontalLayout_26.addWidget(self.btn_limpar_cd_usuarios_4)

        self.btn_cadastrar_cd_usurios_4 = QPushButton(self.frame_22)
        self.btn_cadastrar_cd_usurios_4.setObjectName(u"btn_cadastrar_cd_usurios_4")
        self.btn_cadastrar_cd_usurios_4.setFont(font)
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/adicionar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_cd_usurios_4.setIcon(icon22)
        self.btn_cadastrar_cd_usurios_4.setIconSize(QSize(18, 18))

        self.horizontalLayout_26.addWidget(self.btn_cadastrar_cd_usurios_4)


        self.verticalLayout_32.addWidget(self.frame_22)

        icon23 = QIcon()
        icon23.addFile(u":/icons/icons/cadastrar_alt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget_5.addTab(self.cadastro_clientes_3, icon23, "")

        self.verticalLayout_34.addWidget(self.tabWidget_5)

        self.stackedWidget.addWidget(self.s7_avisos)
        self.s6_tipos_atendimentos = QWidget()
        self.s6_tipos_atendimentos.setObjectName(u"s6_tipos_atendimentos")
        self.verticalLayout_31 = QVBoxLayout(self.s6_tipos_atendimentos)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_14 = QFrame(self.s6_tipos_atendimentos)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_14)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.lb_title_clientes_4 = QLabel(self.frame_14)
        self.lb_title_clientes_4.setObjectName(u"lb_title_clientes_4")
        self.lb_title_clientes_4.setFont(font3)

        self.verticalLayout_26.addWidget(self.lb_title_clientes_4)

        self.line_clientes_4 = QFrame(self.frame_14)
        self.line_clientes_4.setObjectName(u"line_clientes_4")
        self.line_clientes_4.setStyleSheet(u"background-color: #00718F;")
        self.line_clientes_4.setFrameShape(QFrame.HLine)
        self.line_clientes_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.line_clientes_4)


        self.verticalLayout_31.addWidget(self.frame_14)

        self.tabWidget_4 = QTabWidget(self.s6_tipos_atendimentos)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.lista_clientes_2 = QWidget()
        self.lista_clientes_2.setObjectName(u"lista_clientes_2")
        self.verticalLayout_27 = QVBoxLayout(self.lista_clientes_2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_15 = QFrame(self.lista_clientes_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_btn_lista_clientes_3 = QFrame(self.frame_15)
        self.frame_btn_lista_clientes_3.setObjectName(u"frame_btn_lista_clientes_3")
        self.frame_btn_lista_clientes_3.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_lista_clientes_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_btn_lista_clientes_3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_editar_clientes_3 = QPushButton(self.frame_btn_lista_clientes_3)
        self.btn_editar_clientes_3.setObjectName(u"btn_editar_clientes_3")
        self.btn_editar_clientes_3.setFont(font)
        self.btn_editar_clientes_3.setIcon(icon17)
        self.btn_editar_clientes_3.setIconSize(QSize(18, 18))

        self.horizontalLayout_18.addWidget(self.btn_editar_clientes_3)

        self.btn_excluir_clientes_3 = QPushButton(self.frame_btn_lista_clientes_3)
        self.btn_excluir_clientes_3.setObjectName(u"btn_excluir_clientes_3")
        self.btn_excluir_clientes_3.setFont(font)
        self.btn_excluir_clientes_3.setIcon(icon18)
        self.btn_excluir_clientes_3.setIconSize(QSize(18, 18))

        self.horizontalLayout_18.addWidget(self.btn_excluir_clientes_3)


        self.horizontalLayout_15.addWidget(self.frame_btn_lista_clientes_3)

        self.frame_barra_pesquisa_clientes_3 = QFrame(self.frame_15)
        self.frame_barra_pesquisa_clientes_3.setObjectName(u"frame_barra_pesquisa_clientes_3")
        self.frame_barra_pesquisa_clientes_3.setFrameShape(QFrame.StyledPanel)
        self.frame_barra_pesquisa_clientes_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_barra_pesquisa_clientes_3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.ed_barra_pesquisa_clientes_3 = QLineEdit(self.frame_barra_pesquisa_clientes_3)
        self.ed_barra_pesquisa_clientes_3.setObjectName(u"ed_barra_pesquisa_clientes_3")
        self.ed_barra_pesquisa_clientes_3.setFont(font)

        self.horizontalLayout_19.addWidget(self.ed_barra_pesquisa_clientes_3)

        self.btn_pesquisa_clientes_3 = QToolButton(self.frame_barra_pesquisa_clientes_3)
        self.btn_pesquisa_clientes_3.setObjectName(u"btn_pesquisa_clientes_3")
        self.btn_pesquisa_clientes_3.setIcon(icon19)
        self.btn_pesquisa_clientes_3.setIconSize(QSize(18, 18))

        self.horizontalLayout_19.addWidget(self.btn_pesquisa_clientes_3)


        self.horizontalLayout_15.addWidget(self.frame_barra_pesquisa_clientes_3)


        self.verticalLayout_27.addWidget(self.frame_15)

        self.tableWidget_3 = QTableWidget(self.lista_clientes_2)
        if (self.tableWidget_3.columnCount() < 3):
            self.tableWidget_3.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setFont(font4)

        self.verticalLayout_27.addWidget(self.tableWidget_3)

        self.tabWidget_4.addTab(self.lista_clientes_2, icon20, "")
        self.cadastro_clientes_2 = QWidget()
        self.cadastro_clientes_2.setObjectName(u"cadastro_clientes_2")
        self.verticalLayout_28 = QVBoxLayout(self.cadastro_clientes_2)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_13 = QFrame(self.cadastro_clientes_2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_13)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lb_usuarios_id_2 = QLabel(self.frame_17)
        self.lb_usuarios_id_2.setObjectName(u"lb_usuarios_id_2")
        self.lb_usuarios_id_2.setFont(font5)
        self.lb_usuarios_id_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lb_usuarios_id_2)

        self.ed_usuario_id_2 = QLineEdit(self.frame_17)
        self.ed_usuario_id_2.setObjectName(u"ed_usuario_id_2")
        sizePolicy2.setHeightForWidth(self.ed_usuario_id_2.sizePolicy().hasHeightForWidth())
        self.ed_usuario_id_2.setSizePolicy(sizePolicy2)
        self.ed_usuario_id_2.setMaximumSize(QSize(356, 16777215))
        self.ed_usuario_id_2.setFont(font4)
        self.ed_usuario_id_2.setInputMethodHints(Qt.ImhNone)
        self.ed_usuario_id_2.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.ed_usuario_id_2)

        self.cb_usuarios_desativado_2 = QCheckBox(self.frame_17)
        self.cb_usuarios_desativado_2.setObjectName(u"cb_usuarios_desativado_2")
        self.cb_usuarios_desativado_2.setEnabled(True)
        self.cb_usuarios_desativado_2.setFont(font4)
        self.cb_usuarios_desativado_2.setCheckable(True)

        self.horizontalLayout_21.addWidget(self.cb_usuarios_desativado_2)


        self.verticalLayout_29.addWidget(self.frame_17, 0, Qt.AlignLeft)

        self.lb_usuarios_nome_2 = QLabel(self.frame_13)
        self.lb_usuarios_nome_2.setObjectName(u"lb_usuarios_nome_2")
        self.lb_usuarios_nome_2.setFont(font5)
        self.lb_usuarios_nome_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.lb_usuarios_nome_2)

        self.ed_usuarios_nome_2 = QLineEdit(self.frame_13)
        self.ed_usuarios_nome_2.setObjectName(u"ed_usuarios_nome_2")
        font6 = QFont()
        font6.setFamilies([u"Poppins"])
        font6.setPointSize(10)
        font6.setUnderline(False)
        self.ed_usuarios_nome_2.setFont(font6)
        self.ed_usuarios_nome_2.setAlignment(Qt.AlignCenter)
        self.ed_usuarios_nome_2.setDragEnabled(False)
        self.ed_usuarios_nome_2.setReadOnly(False)
        self.ed_usuarios_nome_2.setClearButtonEnabled(True)

        self.verticalLayout_29.addWidget(self.ed_usuarios_nome_2)

        self.verticalSpacer_4 = QSpacerItem(20, 198, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_4)


        self.verticalLayout_28.addWidget(self.frame_13)

        self.frame_16 = QFrame(self.cadastro_clientes_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_4 = QSpacerItem(312, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)

        self.btn_limpar_cd_usuarios_3 = QPushButton(self.frame_16)
        self.btn_limpar_cd_usuarios_3.setObjectName(u"btn_limpar_cd_usuarios_3")
        self.btn_limpar_cd_usuarios_3.setFont(font)
        self.btn_limpar_cd_usuarios_3.setIcon(icon21)
        self.btn_limpar_cd_usuarios_3.setIconSize(QSize(18, 18))

        self.horizontalLayout_20.addWidget(self.btn_limpar_cd_usuarios_3)

        self.btn_cadastrar_cd_usurios_3 = QPushButton(self.frame_16)
        self.btn_cadastrar_cd_usurios_3.setObjectName(u"btn_cadastrar_cd_usurios_3")
        self.btn_cadastrar_cd_usurios_3.setFont(font)
        self.btn_cadastrar_cd_usurios_3.setIcon(icon22)
        self.btn_cadastrar_cd_usurios_3.setIconSize(QSize(18, 18))

        self.horizontalLayout_20.addWidget(self.btn_cadastrar_cd_usurios_3)


        self.verticalLayout_28.addWidget(self.frame_16)

        self.tabWidget_4.addTab(self.cadastro_clientes_2, icon23, "")

        self.verticalLayout_31.addWidget(self.tabWidget_4)

        self.stackedWidget.addWidget(self.s6_tipos_atendimentos)
        self.s5_empresas = QWidget()
        self.s5_empresas.setObjectName(u"s5_empresas")
        self.verticalLayout_23 = QVBoxLayout(self.s5_empresas)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_8 = QFrame(self.s5_empresas)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_8)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.lb_title_clientes_3 = QLabel(self.frame_8)
        self.lb_title_clientes_3.setObjectName(u"lb_title_clientes_3")
        self.lb_title_clientes_3.setFont(font3)

        self.verticalLayout_22.addWidget(self.lb_title_clientes_3)

        self.line_clientes_3 = QFrame(self.frame_8)
        self.line_clientes_3.setObjectName(u"line_clientes_3")
        self.line_clientes_3.setStyleSheet(u"background-color: #00718F;")
        self.line_clientes_3.setFrameShape(QFrame.HLine)
        self.line_clientes_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_22.addWidget(self.line_clientes_3)


        self.verticalLayout_23.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.s5_empresas)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_9)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_11 = QPushButton(self.frame_12)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon24 = QIcon()
        icon24.addFile(u":/icons/icons/anexo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon24)
        self.pushButton_11.setIconSize(QSize(18, 18))

        self.horizontalLayout_14.addWidget(self.pushButton_11, 0, Qt.AlignRight)

        self.label_25 = QLabel(self.frame_12)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(50, 50))
        self.label_25.setMaximumSize(QSize(50, 50))
        self.label_25.setFont(font)
        self.label_25.setPixmap(QPixmap(u":/icons/icons/p_logo_200px.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_25)


        self.horizontalLayout_6.addWidget(self.frame_12)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.pushButton_9 = QPushButton(self.frame_11)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon17)
        self.pushButton_9.setIconSize(QSize(18, 18))

        self.horizontalLayout_6.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_11)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon25 = QIcon()
        icon25.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon25)
        self.pushButton_10.setIconSize(QSize(18, 18))

        self.horizontalLayout_6.addWidget(self.pushButton_10)


        self.verticalLayout_24.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.groupBox_4 = QGroupBox(self.frame_10)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.groupBox_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_11, 0, 1, 1, 1)

        self.radioButton_3 = QRadioButton(self.groupBox_4)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font)

        self.gridLayout_6.addWidget(self.radioButton_3, 0, 2, 1, 1)

        self.radioButton_4 = QRadioButton(self.groupBox_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font)
        self.radioButton_4.setAutoFillBackground(False)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setAutoRepeat(False)

        self.gridLayout_6.addWidget(self.radioButton_4, 0, 3, 1, 1)

        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout_6.addWidget(self.label_15, 1, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_12, 1, 1, 1, 3)

        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_6.addWidget(self.label_16, 2, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout_6.addWidget(self.label_17, 3, 0, 1, 1)

        self.lineEdit_14 = QLineEdit(self.groupBox_4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_14.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_14, 3, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.gridLayout_6.addWidget(self.label_18, 3, 2, 1, 1)

        self.lineEdit_15 = QLineEdit(self.groupBox_4)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.lineEdit_15.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_15, 3, 3, 1, 1)

        self.lineEdit_13 = QLineEdit(self.groupBox_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_13.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_13, 2, 1, 1, 3)


        self.verticalLayout_25.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame_10)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_24 = QLabel(self.groupBox_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.gridLayout_7.addWidget(self.label_24, 1, 0, 1, 1)

        self.lineEdit_19 = QLineEdit(self.groupBox_5)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        font7 = QFont()
        font7.setFamilies([u"Poppins"])
        font7.setPointSize(9)
        self.lineEdit_19.setFont(font7)
        self.lineEdit_19.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.lineEdit_19, 0, 5, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox_5)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setFont(font)

        self.gridLayout_7.addWidget(self.comboBox_3, 1, 1, 1, 1)

        self.lineEdit_16 = QLineEdit(self.groupBox_5)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setFont(font7)
        self.lineEdit_16.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.lineEdit_16, 0, 1, 1, 3)

        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 1, 2, 1, 1)

        self.label_20 = QLabel(self.groupBox_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout_7.addWidget(self.label_20, 0, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.groupBox_5)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setFont(font)

        self.gridLayout_7.addWidget(self.comboBox_4, 1, 3, 1, 1)

        self.lineEdit_17 = QLineEdit(self.groupBox_5)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setFont(font7)
        self.lineEdit_17.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_17.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.lineEdit_17, 1, 5, 1, 1)

        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.gridLayout_7.addWidget(self.label_21, 2, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.gridLayout_7.addWidget(self.label_23, 0, 4, 1, 1)

        self.lineEdit_18 = QLineEdit(self.groupBox_5)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setFont(font7)
        self.lineEdit_18.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.lineEdit_18, 2, 1, 1, 5)

        self.label_22 = QLabel(self.groupBox_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.gridLayout_7.addWidget(self.label_22, 1, 4, 1, 1)


        self.verticalLayout_25.addWidget(self.groupBox_5)


        self.verticalLayout_24.addWidget(self.frame_10)


        self.verticalLayout_23.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.s5_empresas)
        self.s4_protocolos = QWidget()
        self.s4_protocolos.setObjectName(u"s4_protocolos")
        self.verticalLayout_21 = QVBoxLayout(self.s4_protocolos)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_6 = QFrame(self.s4_protocolos)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.lb_title_clientes_2 = QLabel(self.frame_6)
        self.lb_title_clientes_2.setObjectName(u"lb_title_clientes_2")
        self.lb_title_clientes_2.setFont(font3)

        self.verticalLayout_19.addWidget(self.lb_title_clientes_2)

        self.line_clientes_2 = QFrame(self.frame_6)
        self.line_clientes_2.setObjectName(u"line_clientes_2")
        self.line_clientes_2.setStyleSheet(u"background-color: #00718F;")
        self.line_clientes_2.setFrameShape(QFrame.HLine)
        self.line_clientes_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_clientes_2)


        self.verticalLayout_21.addWidget(self.frame_6)

        self.tabWidget_3 = QTabWidget(self.s4_protocolos)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableWidget_2 = QTableWidget(self.tab)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_5.addWidget(self.tableWidget_2, 1, 2, 1, 1)

        self.frame_btn_lista_clientes_2 = QFrame(self.tab)
        self.frame_btn_lista_clientes_2.setObjectName(u"frame_btn_lista_clientes_2")
        self.frame_btn_lista_clientes_2.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_lista_clientes_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_btn_lista_clientes_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.btn_editar_clientes_2 = QPushButton(self.frame_btn_lista_clientes_2)
        self.btn_editar_clientes_2.setObjectName(u"btn_editar_clientes_2")
        self.btn_editar_clientes_2.setFont(font)
        self.btn_editar_clientes_2.setIcon(icon17)
        self.btn_editar_clientes_2.setIconSize(QSize(18, 18))

        self.verticalLayout_18.addWidget(self.btn_editar_clientes_2)

        self.btn_excluir_clientes_2 = QPushButton(self.frame_btn_lista_clientes_2)
        self.btn_excluir_clientes_2.setObjectName(u"btn_excluir_clientes_2")
        self.btn_excluir_clientes_2.setFont(font)
        self.btn_excluir_clientes_2.setIcon(icon18)
        self.btn_excluir_clientes_2.setIconSize(QSize(18, 18))

        self.verticalLayout_18.addWidget(self.btn_excluir_clientes_2)

        self.pushButton_4 = QPushButton(self.frame_btn_lista_clientes_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon26 = QIcon()
        icon26.addFile(u":/icons/icons/print.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon26)
        self.pushButton_4.setIconSize(QSize(18, 18))

        self.verticalLayout_18.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_btn_lista_clientes_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setIcon(icon25)
        self.pushButton_5.setIconSize(QSize(18, 18))

        self.verticalLayout_18.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_btn_lista_clientes_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon25)
        self.pushButton_6.setIconSize(QSize(18, 18))

        self.verticalLayout_18.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_btn_lista_clientes_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon27 = QIcon()
        icon27.addFile(u":/icons/icons/logo-whatsapp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon27)
        self.pushButton_7.setIconSize(QSize(18, 18))

        self.verticalLayout_18.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_btn_lista_clientes_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon28 = QIcon()
        icon28.addFile(u":/icons/icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon28)
        self.pushButton_8.setIconSize(QSize(18, 18))

        self.verticalLayout_18.addWidget(self.pushButton_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_3)


        self.gridLayout_5.addWidget(self.frame_btn_lista_clientes_2, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.tab)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_barra_pesquisa_clientes_2 = QFrame(self.frame_7)
        self.frame_barra_pesquisa_clientes_2.setObjectName(u"frame_barra_pesquisa_clientes_2")
        self.frame_barra_pesquisa_clientes_2.setFrameShape(QFrame.StyledPanel)
        self.frame_barra_pesquisa_clientes_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_barra_pesquisa_clientes_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.ed_barra_pesquisa_clientes_2 = QLineEdit(self.frame_barra_pesquisa_clientes_2)
        self.ed_barra_pesquisa_clientes_2.setObjectName(u"ed_barra_pesquisa_clientes_2")
        self.ed_barra_pesquisa_clientes_2.setFont(font)

        self.horizontalLayout_17.addWidget(self.ed_barra_pesquisa_clientes_2)

        self.btn_pesquisa_clientes_2 = QToolButton(self.frame_barra_pesquisa_clientes_2)
        self.btn_pesquisa_clientes_2.setObjectName(u"btn_pesquisa_clientes_2")
        self.btn_pesquisa_clientes_2.setIcon(icon19)
        self.btn_pesquisa_clientes_2.setIconSize(QSize(18, 18))

        self.horizontalLayout_17.addWidget(self.btn_pesquisa_clientes_2)


        self.horizontalLayout_11.addWidget(self.frame_barra_pesquisa_clientes_2)


        self.gridLayout_5.addWidget(self.frame_7, 0, 0, 1, 3)

        self.tabWidget_3.addTab(self.tab, icon20, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_37 = QVBoxLayout(self.tab_2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_25 = QFrame(self.tab_2)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_25)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.comboBox_6 = QComboBox(self.frame_25)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setFont(font)

        self.gridLayout_11.addWidget(self.comboBox_6, 1, 1, 1, 2)

        self.label_33 = QLabel(self.frame_25)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(85, 16777215))
        self.label_33.setFont(font4)

        self.gridLayout_11.addWidget(self.label_33, 3, 0, 1, 1)

        self.timeEdit = QTimeEdit(self.frame_25)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(0, 0))
        self.timeEdit.setMaximumSize(QSize(16777215, 30))
        self.timeEdit.setFont(font)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.timeEdit.setAccelerated(False)
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setTime(QTime(8, 0, 0))

        self.gridLayout_11.addWidget(self.timeEdit, 2, 4, 1, 1)

        self.label_34 = QLabel(self.frame_25)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(60, 16777215))
        self.label_34.setFont(font4)
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_34, 2, 3, 1, 1)

        self.comboBox_7 = QComboBox(self.frame_25)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setFont(font)

        self.gridLayout_11.addWidget(self.comboBox_7, 2, 1, 1, 2)

        self.timeEdit_2 = QTimeEdit(self.frame_25)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setMaximumSize(QSize(16777215, 30))
        self.timeEdit_2.setFont(font)
        self.timeEdit_2.setTime(QTime(17, 0, 0))

        self.gridLayout_11.addWidget(self.timeEdit_2, 3, 4, 1, 1)

        self.dateEdit = QDateEdit(self.frame_25)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMaximumSize(QSize(16777215, 30))
        self.dateEdit.setFont(font)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.gridLayout_11.addWidget(self.dateEdit, 1, 4, 1, 1)

        self.label_29 = QLabel(self.frame_25)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(85, 16777215))
        self.label_29.setFont(font4)

        self.gridLayout_11.addWidget(self.label_29, 0, 0, 1, 1)

        self.label_35 = QLabel(self.frame_25)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(60, 16777215))
        self.label_35.setFont(font4)
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_35, 3, 3, 1, 1)

        self.comboBox_5 = QComboBox(self.frame_25)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setFont(font)

        self.gridLayout_11.addWidget(self.comboBox_5, 0, 1, 1, 4)

        self.textEdit_2 = QTextEdit(self.frame_25)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout_11.addWidget(self.textEdit_2, 7, 0, 1, 5)

        self.label_32 = QLabel(self.frame_25)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(85, 16777215))
        self.label_32.setFont(font4)

        self.gridLayout_11.addWidget(self.label_32, 2, 0, 1, 1)

        self.label_30 = QLabel(self.frame_25)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(85, 16777215))
        self.label_30.setFont(font4)

        self.gridLayout_11.addWidget(self.label_30, 1, 0, 1, 1)

        self.comboBox_8 = QComboBox(self.frame_25)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setFont(font)

        self.gridLayout_11.addWidget(self.comboBox_8, 3, 1, 1, 2)

        self.label_31 = QLabel(self.frame_25)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(60, 16777215))
        self.label_31.setFont(font4)
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_31, 1, 3, 1, 1)

        self.pushButton = QPushButton(self.frame_25)
        self.pushButton.setObjectName(u"pushButton")
        icon29 = QIcon()
        icon29.addFile(u":/icons/icons/robot.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon29)
        self.pushButton.setIconSize(QSize(18, 18))

        self.gridLayout_11.addWidget(self.pushButton, 6, 4, 1, 1, Qt.AlignRight)

        self.label_36 = QLabel(self.frame_25)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Poppins"])
        font8.setPointSize(10)
        font8.setBold(True)
        self.label_36.setFont(font8)

        self.gridLayout_11.addWidget(self.label_36, 6, 0, 1, 4)


        self.verticalLayout_37.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.tab_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.groupBox_9 = QGroupBox(self.frame_26)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_33 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.checkBox_3 = QCheckBox(self.groupBox_9)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setIcon(icon26)

        self.horizontalLayout_33.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.groupBox_9)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setIcon(icon25)

        self.horizontalLayout_33.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.groupBox_9)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setIcon(icon27)

        self.horizontalLayout_33.addWidget(self.checkBox_5)


        self.horizontalLayout_32.addWidget(self.groupBox_9)

        self.horizontalSpacer_6 = QSpacerItem(296, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_6)

        self.pushButton_15 = QPushButton(self.frame_26)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font)
        self.pushButton_15.setIcon(icon21)
        self.pushButton_15.setIconSize(QSize(18, 18))

        self.horizontalLayout_32.addWidget(self.pushButton_15)

        self.pushButton_14 = QPushButton(self.frame_26)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font)
        self.pushButton_14.setIcon(icon22)
        self.pushButton_14.setIconSize(QSize(18, 18))

        self.horizontalLayout_32.addWidget(self.pushButton_14)


        self.verticalLayout_37.addWidget(self.frame_26)

        icon30 = QIcon()
        icon30.addFile(u":/icons/icons/doc-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget_3.addTab(self.tab_2, icon30, "")

        self.verticalLayout_21.addWidget(self.tabWidget_3)

        self.stackedWidget.addWidget(self.s4_protocolos)
        self.s3_clientes = QWidget()
        self.s3_clientes.setObjectName(u"s3_clientes")
        self.verticalLayout_17 = QVBoxLayout(self.s3_clientes)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.title_clientes = QFrame(self.s3_clientes)
        self.title_clientes.setObjectName(u"title_clientes")
        self.title_clientes.setFrameShape(QFrame.StyledPanel)
        self.title_clientes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.title_clientes)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.lb_title_clientes = QLabel(self.title_clientes)
        self.lb_title_clientes.setObjectName(u"lb_title_clientes")
        self.lb_title_clientes.setFont(font3)

        self.verticalLayout_16.addWidget(self.lb_title_clientes)

        self.line_clientes = QFrame(self.title_clientes)
        self.line_clientes.setObjectName(u"line_clientes")
        self.line_clientes.setStyleSheet(u"background-color: #00718F;")
        self.line_clientes.setFrameShape(QFrame.HLine)
        self.line_clientes.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line_clientes)


        self.verticalLayout_17.addWidget(self.title_clientes)

        self.tabWidget_2 = QTabWidget(self.s3_clientes)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.lista_clientes = QWidget()
        self.lista_clientes.setObjectName(u"lista_clientes")
        self.verticalLayout_20 = QVBoxLayout(self.lista_clientes)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame = QFrame(self.lista_clientes)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_btn_lista_clientes = QFrame(self.frame)
        self.frame_btn_lista_clientes.setObjectName(u"frame_btn_lista_clientes")
        self.frame_btn_lista_clientes.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_lista_clientes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_btn_lista_clientes)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_editar_clientes = QPushButton(self.frame_btn_lista_clientes)
        self.btn_editar_clientes.setObjectName(u"btn_editar_clientes")
        self.btn_editar_clientes.setFont(font)
        self.btn_editar_clientes.setIcon(icon17)
        self.btn_editar_clientes.setIconSize(QSize(18, 18))

        self.horizontalLayout_9.addWidget(self.btn_editar_clientes)

        self.btn_excluir_clientes = QPushButton(self.frame_btn_lista_clientes)
        self.btn_excluir_clientes.setObjectName(u"btn_excluir_clientes")
        self.btn_excluir_clientes.setFont(font)
        self.btn_excluir_clientes.setIcon(icon18)
        self.btn_excluir_clientes.setIconSize(QSize(18, 18))

        self.horizontalLayout_9.addWidget(self.btn_excluir_clientes)


        self.horizontalLayout_10.addWidget(self.frame_btn_lista_clientes)

        self.frame_barra_pesquisa_clientes = QFrame(self.frame)
        self.frame_barra_pesquisa_clientes.setObjectName(u"frame_barra_pesquisa_clientes")
        self.frame_barra_pesquisa_clientes.setFrameShape(QFrame.StyledPanel)
        self.frame_barra_pesquisa_clientes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_barra_pesquisa_clientes)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.ed_barra_pesquisa_clientes = QLineEdit(self.frame_barra_pesquisa_clientes)
        self.ed_barra_pesquisa_clientes.setObjectName(u"ed_barra_pesquisa_clientes")
        self.ed_barra_pesquisa_clientes.setFont(font)

        self.horizontalLayout_16.addWidget(self.ed_barra_pesquisa_clientes)

        self.btn_pesquisa_clientes = QToolButton(self.frame_barra_pesquisa_clientes)
        self.btn_pesquisa_clientes.setObjectName(u"btn_pesquisa_clientes")
        self.btn_pesquisa_clientes.setIcon(icon19)
        self.btn_pesquisa_clientes.setIconSize(QSize(18, 18))

        self.horizontalLayout_16.addWidget(self.btn_pesquisa_clientes)


        self.horizontalLayout_10.addWidget(self.frame_barra_pesquisa_clientes)


        self.verticalLayout_20.addWidget(self.frame)

        self.tableWidget = QTableWidget(self.lista_clientes)
        if (self.tableWidget.columnCount() < 13):
            self.tableWidget.setColumnCount(13)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem18)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font4)

        self.verticalLayout_20.addWidget(self.tableWidget)

        self.tabWidget_2.addTab(self.lista_clientes, icon20, "")
        self.cadastro_clientes = QWidget()
        self.cadastro_clientes.setObjectName(u"cadastro_clientes")
        self.verticalLayout_13 = QVBoxLayout(self.cadastro_clientes)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_2 = QFrame(self.cadastro_clientes)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"padding:0;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font7)
        self.lineEdit_2.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_2, 7, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setEnabled(True)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_10, 0, 2, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font7)
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit, 4, 2, 1, 4)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)

        self.gridLayout.addWidget(self.checkBox, 0, 5, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font7)
        self.lineEdit_3.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_3.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_3, 6, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 6, 3, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font7)
        self.lineEdit_4.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.lineEdit_4.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_4, 6, 4, 1, 2)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font7)
        self.radioButton_2.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_2, 7, 5, 1, 1)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font7)
        self.radioButton.setChecked(False)

        self.gridLayout.addWidget(self.radioButton, 7, 4, 1, 1)


        self.verticalLayout_8.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font)

        self.gridLayout_2.addWidget(self.comboBox_2, 1, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 1, 4, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font7)
        self.lineEdit_6.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 1, 1, 3)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 1, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font7)
        self.lineEdit_7.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 5, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setFont(font7)
        self.lineEdit_8.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_8, 2, 1, 1, 5)

        self.lineEdit_5 = QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font7)
        self.lineEdit_5.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_5.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_5, 1, 5, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 0, 4, 1, 1)


        self.verticalLayout_8.addWidget(self.groupBox_2)


        self.verticalLayout_13.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.cadastro_clientes)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setIcon(icon21)
        self.pushButton_2.setIconSize(QSize(18, 18))

        self.gridLayout_3.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.lineEdit_9 = QLineEdit(self.groupBox_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setFont(font7)
        self.lineEdit_9.setClearButtonEnabled(True)

        self.horizontalLayout_13.addWidget(self.lineEdit_9)


        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setIcon(icon22)
        self.pushButton_3.setIconSize(QSize(18, 18))

        self.gridLayout_3.addWidget(self.pushButton_3, 0, 3, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_3)

        icon31 = QIcon()
        icon31.addFile(u":/icons/icons/cadastrar-branco.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget_2.addTab(self.cadastro_clientes, icon31, "")

        self.verticalLayout_17.addWidget(self.tabWidget_2)

        self.stackedWidget.addWidget(self.s3_clientes)
        self.s2_usuarios = QWidget()
        self.s2_usuarios.setObjectName(u"s2_usuarios")
        self.verticalLayout_12 = QVBoxLayout(self.s2_usuarios)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.title_usuarios = QFrame(self.s2_usuarios)
        self.title_usuarios.setObjectName(u"title_usuarios")
        self.title_usuarios.setFrameShape(QFrame.StyledPanel)
        self.title_usuarios.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.title_usuarios)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lb_title_usuarios = QLabel(self.title_usuarios)
        self.lb_title_usuarios.setObjectName(u"lb_title_usuarios")
        self.lb_title_usuarios.setFont(font3)
        self.lb_title_usuarios.setLayoutDirection(Qt.LeftToRight)
        self.lb_title_usuarios.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.lb_title_usuarios)

        self.line_usuarios = QFrame(self.title_usuarios)
        self.line_usuarios.setObjectName(u"line_usuarios")
        self.line_usuarios.setStyleSheet(u"background-color: #00718F;")
        self.line_usuarios.setFrameShape(QFrame.HLine)
        self.line_usuarios.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_usuarios)


        self.verticalLayout_12.addWidget(self.title_usuarios)

        self.tabWidget = QTabWidget(self.s2_usuarios)
        self.tabWidget.setObjectName(u"tabWidget")
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
        self.tabWidget.setPalette(palette1)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tab_lista_usuarios = QWidget()
        self.tab_lista_usuarios.setObjectName(u"tab_lista_usuarios")
        self.verticalLayout_15 = QVBoxLayout(self.tab_lista_usuarios)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.header_lista_usuarios = QFrame(self.tab_lista_usuarios)
        self.header_lista_usuarios.setObjectName(u"header_lista_usuarios")
        self.header_lista_usuarios.setFrameShape(QFrame.StyledPanel)
        self.header_lista_usuarios.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.header_lista_usuarios)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_btn_usuarios = QFrame(self.header_lista_usuarios)
        self.frame_btn_usuarios.setObjectName(u"frame_btn_usuarios")
        self.frame_btn_usuarios.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_usuarios.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_btn_usuarios)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_editar = QPushButton(self.frame_btn_usuarios)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setFont(font)
        self.btn_editar.setIcon(icon17)
        self.btn_editar.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.btn_editar)

        self.btn_excluir = QPushButton(self.frame_btn_usuarios)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setFont(font)
        self.btn_excluir.setIcon(icon18)
        self.btn_excluir.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.btn_excluir)


        self.horizontalLayout_7.addWidget(self.frame_btn_usuarios)

        self.frame_pesquisa_usuarios = QFrame(self.header_lista_usuarios)
        self.frame_pesquisa_usuarios.setObjectName(u"frame_pesquisa_usuarios")
        self.frame_pesquisa_usuarios.setFrameShape(QFrame.StyledPanel)
        self.frame_pesquisa_usuarios.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_pesquisa_usuarios)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.barra_pesquisa_usuarios = QLineEdit(self.frame_pesquisa_usuarios)
        self.barra_pesquisa_usuarios.setObjectName(u"barra_pesquisa_usuarios")
        self.barra_pesquisa_usuarios.setFont(font)

        self.horizontalLayout_5.addWidget(self.barra_pesquisa_usuarios)

        self.btn_pesquisa_usuarios = QToolButton(self.frame_pesquisa_usuarios)
        self.btn_pesquisa_usuarios.setObjectName(u"btn_pesquisa_usuarios")
        self.btn_pesquisa_usuarios.setIcon(icon19)
        self.btn_pesquisa_usuarios.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.btn_pesquisa_usuarios)


        self.horizontalLayout_7.addWidget(self.frame_pesquisa_usuarios)


        self.verticalLayout_15.addWidget(self.header_lista_usuarios)

        self.tabela_usuarios = QTableWidget(self.tab_lista_usuarios)
        if (self.tabela_usuarios.columnCount() < 6):
            self.tabela_usuarios.setColumnCount(6)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font4);
        self.tabela_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font4);
        self.tabela_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font4);
        self.tabela_usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font4);
        self.tabela_usuarios.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font4);
        self.tabela_usuarios.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font4);
        self.tabela_usuarios.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        self.tabela_usuarios.setObjectName(u"tabela_usuarios")
        self.tabela_usuarios.setFont(font4)

        self.verticalLayout_15.addWidget(self.tabela_usuarios)

        self.tabWidget.addTab(self.tab_lista_usuarios, icon20, "")
        self.tab_cadastrar_usuarios = QWidget()
        self.tab_cadastrar_usuarios.setObjectName(u"tab_cadastrar_usuarios")
        self.verticalLayout_6 = QVBoxLayout(self.tab_cadastrar_usuarios)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.cadastro_usuarios = QFrame(self.tab_cadastrar_usuarios)
        self.cadastro_usuarios.setObjectName(u"cadastro_usuarios")
        self.cadastro_usuarios.setFrameShape(QFrame.StyledPanel)
        self.cadastro_usuarios.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.cadastro_usuarios)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ed_usuarios_nome = QLineEdit(self.cadastro_usuarios)
        self.ed_usuarios_nome.setObjectName(u"ed_usuarios_nome")
        self.ed_usuarios_nome.setFont(font6)
        self.ed_usuarios_nome.setAlignment(Qt.AlignCenter)
        self.ed_usuarios_nome.setDragEnabled(False)
        self.ed_usuarios_nome.setReadOnly(False)
        self.ed_usuarios_nome.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.ed_usuarios_nome, 2, 0, 1, 4)

        self.ed_usuarios_funcao = QLineEdit(self.cadastro_usuarios)
        self.ed_usuarios_funcao.setObjectName(u"ed_usuarios_funcao")
        self.ed_usuarios_funcao.setFont(font4)
        self.ed_usuarios_funcao.setAlignment(Qt.AlignCenter)
        self.ed_usuarios_funcao.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.ed_usuarios_funcao, 8, 0, 1, 4)

        self.lb_usuarios_funcao = QLabel(self.cadastro_usuarios)
        self.lb_usuarios_funcao.setObjectName(u"lb_usuarios_funcao")
        self.lb_usuarios_funcao.setFont(font5)
        self.lb_usuarios_funcao.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_usuarios_funcao, 7, 0, 1, 4)

        self.ed_usuarios_contato = QLineEdit(self.cadastro_usuarios)
        self.ed_usuarios_contato.setObjectName(u"ed_usuarios_contato")
        self.ed_usuarios_contato.setFont(font4)
        self.ed_usuarios_contato.setInputMethodHints(Qt.ImhPreferNumbers)
        self.ed_usuarios_contato.setAlignment(Qt.AlignCenter)
        self.ed_usuarios_contato.setReadOnly(False)
        self.ed_usuarios_contato.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.ed_usuarios_contato, 4, 0, 1, 4)

        self.lb_usuarios_contato = QLabel(self.cadastro_usuarios)
        self.lb_usuarios_contato.setObjectName(u"lb_usuarios_contato")
        self.lb_usuarios_contato.setFont(font5)
        self.lb_usuarios_contato.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_usuarios_contato, 3, 0, 1, 4)

        self.ed_usuarios_email = QLineEdit(self.cadastro_usuarios)
        self.ed_usuarios_email.setObjectName(u"ed_usuarios_email")
        self.ed_usuarios_email.setFont(font4)
        self.ed_usuarios_email.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.ed_usuarios_email.setAlignment(Qt.AlignCenter)
        self.ed_usuarios_email.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.ed_usuarios_email, 6, 0, 1, 4)

        self.lb_usuarios_email = QLabel(self.cadastro_usuarios)
        self.lb_usuarios_email.setObjectName(u"lb_usuarios_email")
        self.lb_usuarios_email.setFont(font5)
        self.lb_usuarios_email.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_usuarios_email, 5, 0, 1, 4)

        self.lb_usuarios_nome = QLabel(self.cadastro_usuarios)
        self.lb_usuarios_nome.setObjectName(u"lb_usuarios_nome")
        self.lb_usuarios_nome.setFont(font5)
        self.lb_usuarios_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_usuarios_nome, 1, 0, 1, 4)

        self.lb_usuarios_id = QLabel(self.cadastro_usuarios)
        self.lb_usuarios_id.setObjectName(u"lb_usuarios_id")
        self.lb_usuarios_id.setFont(font5)

        self.gridLayout_4.addWidget(self.lb_usuarios_id, 0, 0, 1, 1, Qt.AlignLeft)

        self.ed_usuario_id = QLineEdit(self.cadastro_usuarios)
        self.ed_usuario_id.setObjectName(u"ed_usuario_id")
        sizePolicy2.setHeightForWidth(self.ed_usuario_id.sizePolicy().hasHeightForWidth())
        self.ed_usuario_id.setSizePolicy(sizePolicy2)
        self.ed_usuario_id.setMaximumSize(QSize(356, 16777215))
        self.ed_usuario_id.setFont(font4)
        self.ed_usuario_id.setInputMethodHints(Qt.ImhNone)
        self.ed_usuario_id.setReadOnly(True)

        self.gridLayout_4.addWidget(self.ed_usuario_id, 0, 1, 1, 1)

        self.cb_usuarios_desativado = QCheckBox(self.cadastro_usuarios)
        self.cb_usuarios_desativado.setObjectName(u"cb_usuarios_desativado")
        self.cb_usuarios_desativado.setEnabled(True)
        self.cb_usuarios_desativado.setFont(font4)
        self.cb_usuarios_desativado.setCheckable(True)

        self.gridLayout_4.addWidget(self.cb_usuarios_desativado, 0, 2, 1, 2)


        self.verticalLayout_6.addWidget(self.cadastro_usuarios)

        self.btn_cadastro_usuarios = QFrame(self.tab_cadastrar_usuarios)
        self.btn_cadastro_usuarios.setObjectName(u"btn_cadastro_usuarios")
        self.btn_cadastro_usuarios.setFrameShape(QFrame.StyledPanel)
        self.btn_cadastro_usuarios.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.btn_cadastro_usuarios)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.btn_limpar_cd_usuarios = QPushButton(self.btn_cadastro_usuarios)
        self.btn_limpar_cd_usuarios.setObjectName(u"btn_limpar_cd_usuarios")
        self.btn_limpar_cd_usuarios.setFont(font)
        self.btn_limpar_cd_usuarios.setIcon(icon21)
        self.btn_limpar_cd_usuarios.setIconSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.btn_limpar_cd_usuarios)

        self.btn_cadastrar_cd_usurios = QPushButton(self.btn_cadastro_usuarios)
        self.btn_cadastrar_cd_usurios.setObjectName(u"btn_cadastrar_cd_usurios")
        self.btn_cadastrar_cd_usurios.setFont(font)
        self.btn_cadastrar_cd_usurios.setIcon(icon22)
        self.btn_cadastrar_cd_usurios.setIconSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.btn_cadastrar_cd_usurios)


        self.verticalLayout_6.addWidget(self.btn_cadastro_usuarios)

        self.tabWidget.addTab(self.tab_cadastrar_usuarios, icon31, "")

        self.verticalLayout_12.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.s2_usuarios)

        self.verticalLayout_11.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.section)


        self.horizontalLayout.addWidget(self.main)


        self.retranslateUi(MainWindow)

        self.toolBox_menu.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


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
        self.btn4_email.setText("")
        self.toolButton.setText("")
        self.lb_title_clientes_6.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Bem-vindo ao </span><span style=\" font-size:10pt; font-weight:700;\">ProtoClick</span><span style=\" font-size:10pt;\">, a solu\u00e7\u00e3o definitiva para simplificar e</span></p><p align=\"center\"><span style=\" font-size:10pt;\">aprimorar o gerenciamento de protocolos de atendimento aos</span></p><p align=\"center\"><span style=\" font-size:10pt;\">clientes. Com nossa tecnologia avan\u00e7ada e recursos inovadores,</span></p><p align=\"center\"><span style=\" font-size:10pt;\">voc\u00ea ter\u00e1 todas as ferramentas necess\u00e1rias para organizar,</span></p><p align=\"center\"><span style=\" font-size:10pt;\">automatizar e otimizar seus processos de atendimento,</span></p><p align=\"center\"><span style=\" font-size:10pt;\">proporcionando uma experi\u00eancia excepcional para seus clientes.</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; text-decoration: underline;\">Principais Recursos:</span></p><p align=\"center\"><span style=\" font-weight:700;\">Automatiza\u00e7\u00e3o Inteligente:</span> Economize tempo e esfor\u00e7o com a automatiza\u00e7\u00e3o</p><p align=\"center\">da cria\u00e7\u00e3o de protocolos, permitindo que voc\u00ea se concentre em tarefas estrat\u00e9gicas.</p><p align=\"center\"><span style=\" font-weight:700;\">Consist\u00eancia e Precis\u00e3o: </span>Utilize a intelig\u00eancia artificial para garantir a consist\u00eancia e precis\u00e3o</p><p align=\"center\">das informa\u00e7\u00f5es nos protocolos, com sugest\u00f5es autom\u00e1ticas para completar campos relevantes.</p><p align=\"center\"><span style=\" font-weight:700;\">Gest\u00e3o Eficiente: </span>Organize e categorize os protocolos de forma inteligente, facilitando</p><p align=\"center\">a gest\u00e3o de m\u00faltiplos casos simultaneamente, com filtros e ferramentas de busca avan\u00e7adas"
                        ".</p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/><span style=\" font-size:10pt; font-style:italic;\">Experimente agora mesmo o Software de Protocolo Inteligente da ProtoClick</span></p><p align=\"center\"><span style=\" font-size:10pt; font-style:italic;\">e eleve o seu atendimento ao pr\u00f3ximo n\u00edvel!</span></p></body></html>", None))
        self.lb_title_clientes_5.setText(QCoreApplication.translate("MainWindow", u"Avisos", None))
        self.btn_editar_clientes_4.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_excluir_clientes_4.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.ed_barra_pesquisa_clientes_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.btn_pesquisa_clientes_4.setText("")
        ___qtablewidgetitem = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem2 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Desativado", None));
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.lista_clientes_3), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.lb_usuarios_id_3.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.cb_usuarios_desativado_3.setText(QCoreApplication.translate("MainWindow", u"Desativado", None))
        self.lb_usuarios_nome_3.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.btn_limpar_cd_usuarios_4.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btn_cadastrar_cd_usurios_4.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.cadastro_clientes_3), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.lb_title_clientes_4.setText(QCoreApplication.translate("MainWindow", u"Tipos de Atendimento", None))
        self.btn_editar_clientes_3.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_excluir_clientes_3.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.ed_barra_pesquisa_clientes_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.btn_pesquisa_clientes_3.setText("")
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem4 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Desativado", None));
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.lista_clientes_2), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.lb_usuarios_id_2.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.cb_usuarios_desativado_2.setText(QCoreApplication.translate("MainWindow", u"Desativado", None))
        self.lb_usuarios_nome_2.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.ed_usuarios_nome_2.setInputMask("")
        self.ed_usuarios_nome_2.setText("")
        self.btn_limpar_cd_usuarios_3.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btn_cadastrar_cd_usurios_3.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.cadastro_clientes_2), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.lb_title_clientes_3.setText(QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Selecionar o Logo", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Identifica\u00e7\u00e3o", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"F\u00edsica", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Jur\u00eddica", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o Social", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"CPF / CNPJ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.lineEdit_14.setInputMask(QCoreApplication.translate("MainWindow", u"+55 (00) 0 0000-0000", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email@email.com.br", None))
        self.lineEdit_13.setInputMask(QCoreApplication.translate("MainWindow", u"00.000.000/0000/00", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.lineEdit_19.setPlaceholderText("")
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Teixeira de Freitas", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Prado", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Bahia", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Minas Gerais", None))

        self.lineEdit_17.setInputMask(QCoreApplication.translate("MainWindow", u"00.000-000", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Refer\u00eancia", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"N\u00ba", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.lb_title_clientes_2.setText(QCoreApplication.translate("MainWindow", u"Protocolos", None))
        self.btn_editar_clientes_2.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_excluir_clientes_2.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PDV", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Word", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"WhatsApp", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.ed_barra_pesquisa_clientes_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.btn_pesquisa_clientes_2.setText("")
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Solicitante", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Atendimento", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"T\u00e9rmino", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Consultor", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Aprimorar", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Ap\u00f3s Salvar?", None))
        self.checkBox_3.setText("")
        self.checkBox_4.setText("")
        self.checkBox_5.setText("")
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Protocolo", None))
        self.lb_title_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_editar_clientes.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_excluir_clientes.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.ed_barra_pesquisa_clientes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.btn_pesquisa_clientes.setText("")
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o Social", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CPF / CNPJ", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Natureza Social", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Contato", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Desativado", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.lista_clientes), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Identifica\u00e7\u00e3o", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.lineEdit_2.setInputMask(QCoreApplication.translate("MainWindow", u"00.000.000/0000-00", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPF / CNPJ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o Social", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Desativado", None))
        self.lineEdit_3.setInputMask(QCoreApplication.translate("MainWindow", u"+55 (00) 0 0000-0000", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email@email.com.br", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"J\u00faridica", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"F\u00edsica", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Teixeira de Freitas", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Prado", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Bahia", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Minas Gerais", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Refer\u00eancia", None))
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_5.setInputMask(QCoreApplication.translate("MainWindow", u"00.000-000", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"N\u00ba", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Solicitante", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.cadastro_clientes), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.lb_title_usuarios.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.barra_pesquisa_usuarios.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar...", None))
        self.btn_pesquisa_usuarios.setText("")
        ___qtablewidgetitem19 = self.tabela_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem20 = self.tabela_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem21 = self.tabela_usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Contato", None));
        ___qtablewidgetitem22 = self.tabela_usuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem23 = self.tabela_usuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o", None));
        ___qtablewidgetitem24 = self.tabela_usuarios.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Desativado", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_lista_usuarios), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.ed_usuarios_nome.setInputMask("")
        self.ed_usuarios_nome.setText("")
        self.lb_usuarios_funcao.setText(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o", None))
        self.ed_usuarios_contato.setInputMask(QCoreApplication.translate("MainWindow", u"+55 (00) 0 0000-0000", None))
        self.ed_usuarios_contato.setText(QCoreApplication.translate("MainWindow", u"+55 ()  -", None))
        self.ed_usuarios_contato.setPlaceholderText("")
        self.lb_usuarios_contato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.ed_usuarios_email.setInputMask("")
        self.ed_usuarios_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email@email.com.br", None))
        self.lb_usuarios_email.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.lb_usuarios_nome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lb_usuarios_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.cb_usuarios_desativado.setText(QCoreApplication.translate("MainWindow", u"Desativado", None))
        self.btn_limpar_cd_usuarios.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btn_cadastrar_cd_usurios.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cadastrar_usuarios), QCoreApplication.translate("MainWindow", u"Cadastro", None))
    # retranslateUi

