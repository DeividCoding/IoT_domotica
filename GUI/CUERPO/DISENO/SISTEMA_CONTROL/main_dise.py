# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainNew3_dise.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 478)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/RoniHernandez99_IoT_domotica_128px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/RoniHernandez99_IoT_domotica_128px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/RoniHernandez99_IoT_domotica_128px.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/RoniHernandez99_IoT_domotica_128px.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/RoniHernandez99_IoT_domotica_128px.ico"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/RoniHernandez99_IoT_domotica_128px.ico"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/RoniHernandez99_IoT_domotica_128px.ico"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/RoniHernandez99_IoT_domotica_128px.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Form{    \n"
"border:1px solid white;\n"
"background-color: #193b58;\n"
"padding:0px\n"
"}\n"
"\n"
"")
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QtCore.QSize(320, 420))
        self.widget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.bel_temp = QtWidgets.QLabel(self.widget)
        self.bel_temp.setMinimumSize(QtCore.QSize(50, 25))
        self.bel_temp.setMaximumSize(QtCore.QSize(70, 50))
        self.bel_temp.setSizeIncrement(QtCore.QSize(60, 0))
        self.bel_temp.setBaseSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setFamily("LucidaGrande")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bel_temp.setFont(font)
        self.bel_temp.setStyleSheet("  width: 48px;\n"
"  height: 17px;\n"
" /* margin: 0 14px 10px 0;*/\n"
"  font-family: LucidaGrande;\n"
"  font-size: 14px;\n"
"  font-weight: normal;\n"
"  font-stretch: normal;\n"
"  font-style: normal;\n"
"  line-height: normal;\n"
"  letter-spacing: normal;\n"
"  color: #ffffff;\n"
"")
        self.bel_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_temp.setObjectName("bel_temp")
        self.horizontalLayout_11.addWidget(self.bel_temp)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setMinimumSize(QtCore.QSize(40, 25))
        self.label_11.setMaximumSize(QtCore.QSize(60, 50))
        self.label_11.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_11.setBaseSize(QtCore.QSize(40, 25))
        font = QtGui.QFont()
        font.setFamily("LucidaGrande")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("  width: 48px;\n"
"  height: 17px;\n"
"  /*margin: 0 14px 10px 0;*/\n"
"  font-family: LucidaGrande;\n"
"  font-size: 14px;\n"
"  font-weight: normal;\n"
"  font-stretch: normal;\n"
"  font-style: normal;\n"
"  line-height: normal;\n"
"  letter-spacing: normal;\n"
"  color: #ffffff;\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setMinimumSize(QtCore.QSize(0, 5))
        self.label_17.setMaximumSize(QtCore.QSize(100, 5))
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_7.addWidget(self.label_17)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(27, 27))
        self.label_4.setMaximumSize(QtCore.QSize(35, 35))
        self.label_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_4.setBaseSize(QtCore.QSize(27, 27))
        self.label_4.setStyleSheet("border-image:url(:/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/termo.png);\n"
"padding:0px;\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.label_39 = QtWidgets.QLabel(self.widget)
        self.label_39.setMinimumSize(QtCore.QSize(100, 10))
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.verticalLayout.addWidget(self.label_39)
        self.timeEdit_tiempo = QtWidgets.QTimeEdit(self.widget)
        self.timeEdit_tiempo.setMinimumSize(QtCore.QSize(228, 94))
        self.timeEdit_tiempo.setMaximumSize(QtCore.QSize(600, 100))
        self.timeEdit_tiempo.setSizeIncrement(QtCore.QSize(0, 0))
        self.timeEdit_tiempo.setBaseSize(QtCore.QSize(225, 90))
        font = QtGui.QFont()
        font.setFamily("LucidaGrande")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.timeEdit_tiempo.setFont(font)
        self.timeEdit_tiempo.setStyleSheet("QTimeEdit{ \n"
"  opacity: 0.53;\n"
"  font-family: LucidaGrande;\n"
"  font-size: 58px;\n"
"   padding:0px;\n"
"  color: #979797;\n"
"  border: 1px solid  #193b58;\n"
"background-color: #193b58;\n"
"}\n"
"\n"
"")
        self.timeEdit_tiempo.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.timeEdit_tiempo.setWrapping(False)
        self.timeEdit_tiempo.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit_tiempo.setReadOnly(True)
        self.timeEdit_tiempo.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit_tiempo.setAccelerated(False)
        self.timeEdit_tiempo.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.timeEdit_tiempo.setKeyboardTracking(True)
        self.timeEdit_tiempo.setProperty("showGroupSeparator", False)
        self.timeEdit_tiempo.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(21, 0, 0)))
        self.timeEdit_tiempo.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit_tiempo.setCalendarPopup(False)
        self.timeEdit_tiempo.setTime(QtCore.QTime(21, 0, 0))
        self.timeEdit_tiempo.setObjectName("timeEdit_tiempo")
        self.verticalLayout.addWidget(self.timeEdit_tiempo)
        self.dateEdit_fecha = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_fecha.setMinimumSize(QtCore.QSize(200, 40))
        self.dateEdit_fecha.setMaximumSize(QtCore.QSize(600, 60))
        self.dateEdit_fecha.setSizeIncrement(QtCore.QSize(0, 0))
        self.dateEdit_fecha.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("LucidaGrande")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateEdit_fecha.setFont(font)
        self.dateEdit_fecha.setStyleSheet("  font-family: LucidaGrande;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  font-stretch: normal;\n"
"  font-style: normal;\n"
"  line-height: normal;\n"
"  letter-spacing: normal;\n"
"  color: #ffffff;\n"
"  border: 1px solid  #193b58; \n"
"background-color: #193b58;\n"
"")
        self.dateEdit_fecha.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.dateEdit_fecha.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_fecha.setReadOnly(True)
        self.dateEdit_fecha.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_fecha.setProperty("showGroupSeparator", False)
        self.dateEdit_fecha.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 9, 13), QtCore.QTime(0, 0, 0)))
        self.dateEdit_fecha.setCalendarPopup(False)
        self.dateEdit_fecha.setObjectName("dateEdit_fecha")
        self.verticalLayout.addWidget(self.dateEdit_fecha)
        self.label_41 = QtWidgets.QLabel(self.widget)
        self.label_41.setMinimumSize(QtCore.QSize(100, 10))
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.verticalLayout.addWidget(self.label_41)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.btn_info = QtWidgets.QPushButton(self.widget)
        self.btn_info.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_info.setMaximumSize(QtCore.QSize(35, 35))
        self.btn_info.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_info.setBaseSize(QtCore.QSize(25, 25))
        self.btn_info.setStyleSheet("QPushButton {\n"
"border-image: url(:/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/info_off.png);\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/info_on.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/info_off.png);\n"
"}\n"
"")
        self.btn_info.setText("")
        self.btn_info.setObjectName("btn_info")
        self.horizontalLayout_14.addWidget(self.btn_info)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_14.addWidget(self.label_18)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.rb_controlManual = QtWidgets.QRadioButton(self.widget)
        self.rb_controlManual.setMinimumSize(QtCore.QSize(20, 20))
        self.rb_controlManual.setMaximumSize(QtCore.QSize(30, 30))
        self.rb_controlManual.setSizeIncrement(QtCore.QSize(0, 0))
        self.rb_controlManual.setBaseSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rb_controlManual.setFont(font)
        self.rb_controlManual.setStyleSheet("QRadioButton {\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:          9px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:        #8c2b2b; \n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       #193b58;\n"
"    border:                 2px solid white;\n"
"}\n"
"")
        self.rb_controlManual.setText("")
        self.rb_controlManual.setObjectName("rb_controlManual")
        self.verticalLayout_5.addWidget(self.rb_controlManual, 0, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(70, 20))
        self.label_6.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setFamily("LucidaGrande")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"  width: 35px;\n"
"  height: 12px;\n"
"  /*margin: 3px 8px 0 0;*/\n"
"  font-family: LucidaGrande;\n"
"  font-size: 10px;\n"
"  font-weight: normal;\n"
"  font-stretch: normal;\n"
"  font-style: normal;\n"
"  line-height: normal;\n"
"  letter-spacing: normal;\n"
"  color: #ffffff;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.horizontalLayout_14.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.rb_controlAutomatico = QtWidgets.QRadioButton(self.widget)
        self.rb_controlAutomatico.setMinimumSize(QtCore.QSize(20, 20))
        self.rb_controlAutomatico.setMaximumSize(QtCore.QSize(30, 30))
        self.rb_controlAutomatico.setSizeIncrement(QtCore.QSize(0, 0))
        self.rb_controlAutomatico.setBaseSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rb_controlAutomatico.setFont(font)
        self.rb_controlAutomatico.setStyleSheet("QRadioButton {\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:          9px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:        #8c2b2b; \n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       #193b58; ;\n"
"    border:                 2px solid white;\n"
"}\n"
"")
        self.rb_controlAutomatico.setText("")
        self.rb_controlAutomatico.setChecked(True)
        self.rb_controlAutomatico.setObjectName("rb_controlAutomatico")
        self.verticalLayout_6.addWidget(self.rb_controlAutomatico, 0, QtCore.Qt.AlignHCenter)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setMinimumSize(QtCore.QSize(70, 20))
        self.label_10.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setFamily("LucidaGrande")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("\n"
"  width: 35px;\n"
"  height: 12px;\n"
"  /*margin: 3px 8px 0 0;*/\n"
"  font-family: LucidaGrande;\n"
"  font-size: 10px;\n"
"  font-weight: normal;\n"
"  font-stretch: normal;\n"
"  font-style: normal;\n"
"  line-height: normal;\n"
"  letter-spacing: normal;\n"
"  color: #ffffff;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.horizontalLayout_14.addLayout(self.verticalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_3.addWidget(self.widget)
        self.widget_alarmasNotas = QtWidgets.QWidget(Form)
        self.widget_alarmasNotas.setMinimumSize(QtCore.QSize(430, 410))
        self.widget_alarmasNotas.setStyleSheet("#widget_alarmasNotas{\n"
"margin:0px;\n"
"background-color:#d8d8d8;\n"
"padding: 50px 50px 50px 50px;\n"
"}")
        self.widget_alarmasNotas.setObjectName("widget_alarmasNotas")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_alarmasNotas)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(26, 26, 26, 26)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stack_alarmas = QtWidgets.QStackedWidget(self.widget_alarmasNotas)
        self.stack_alarmas.setMinimumSize(QtCore.QSize(380, 160))
        self.stack_alarmas.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stack_alarmas.setSizeIncrement(QtCore.QSize(0, 0))
        self.stack_alarmas.setBaseSize(QtCore.QSize(380, 160))
        self.stack_alarmas.setToolTipDuration(0)
        self.stack_alarmas.setStyleSheet("QStackedWidget#stack_notas{\n"
"padding:0px;\n"
"background-color: #d8d8d8;\n"
"/*border-radius: 20%;*/\n"
"margin: 0px;\n"
"}\n"
"\n"
"\n"
"/*QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}*/\n"
"\n"
"*{\n"
"background-color: #d8d8d8;\n"
"/*border-radius: 20%*/;\n"
"margin: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.stack_alarmas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stack_alarmas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stack_alarmas.setObjectName("stack_alarmas")
        self.verticalLayout_2.addWidget(self.stack_alarmas)
        self.stack_notas = QtWidgets.QStackedWidget(self.widget_alarmasNotas)
        self.stack_notas.setMinimumSize(QtCore.QSize(380, 160))
        self.stack_notas.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stack_notas.setBaseSize(QtCore.QSize(380, 160))
        self.stack_notas.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stack_notas.setToolTipDuration(0)
        self.stack_notas.setStyleSheet("QStackedWidget#stack_notas{\n"
"padding:0px;\n"
"background-color: #d8d8d8;\n"
"/*border-radius: 20%;*/\n"
"margin: 0px;\n"
"}\n"
"\n"
"\n"
"/*QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}*/\n"
"\n"
"*{\n"
"background-color: #d8d8d8;\n"
"/*border-radius: 20%*/;\n"
"margin: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.stack_notas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stack_notas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stack_notas.setObjectName("stack_notas")
        self.verticalLayout_2.addWidget(self.stack_notas)
        self.horizontalLayout_3.addWidget(self.widget_alarmasNotas)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setMinimumSize(QtCore.QSize(120, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setMinimumSize(QtCore.QSize(100, 160))
        self.widget_3.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.widget_3.setBaseSize(QtCore.QSize(100, 160))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_14 = QtWidgets.QLabel(self.widget_3)
        self.label_14.setMaximumSize(QtCore.QSize(100, 30))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_18.addWidget(self.label_14)
        self.btn_configFoco = QtWidgets.QPushButton(self.widget_3)
        self.btn_configFoco.setMinimumSize(QtCore.QSize(28, 28))
        self.btn_configFoco.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_configFoco.setBaseSize(QtCore.QSize(28, 28))
        self.btn_configFoco.setStyleSheet("QPushButton {\n"
"border-image: url(:/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/rueda1_blanco.png);\n"
"\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/rrueda1_blanco.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/rueda1_blanco.png);\n"
"}")
        self.btn_configFoco.setText("")
        self.btn_configFoco.setObjectName("btn_configFoco")
        self.horizontalLayout_18.addWidget(self.btn_configFoco)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.bel_estadoFoco = QtWidgets.QLabel(self.widget_3)
        self.bel_estadoFoco.setMinimumSize(QtCore.QSize(70, 60))
        self.bel_estadoFoco.setMaximumSize(QtCore.QSize(160, 150))
        self.bel_estadoFoco.setSizeIncrement(QtCore.QSize(0, 0))
        self.bel_estadoFoco.setBaseSize(QtCore.QSize(60, 50))
        self.bel_estadoFoco.setStyleSheet("border-image: url(:/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/foco8_default.png);")
        self.bel_estadoFoco.setText("")
        self.bel_estadoFoco.setObjectName("bel_estadoFoco")
        self.verticalLayout_3.addWidget(self.bel_estadoFoco)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.widget_3)
        self.label_16.setMinimumSize(QtCore.QSize(0, 20))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.hoSli_foco = QtWidgets.QSlider(self.widget_3)
        self.hoSli_foco.setMinimumSize(QtCore.QSize(45, 35))
        self.hoSli_foco.setMaximumSize(QtCore.QSize(80, 16777215))
        self.hoSli_foco.setBaseSize(QtCore.QSize(45, 35))
        self.hoSli_foco.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 15px; /*ALTURA DE LA BARRA*/\n"
"border-radius: 4px;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: rgb(33, 139, 14);/*qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);*/\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;   /*COLOR DE BARRA A LA IZQUIERDA*/\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 #eee, stop:1 #ccc); /*colo de la cosa que se mueve*/\n"
"border: 1px solid #777;\n"
"width: 20px; /* ancho de la barra que se  mueve*/\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"text:\"roni\";\n"
"}")
        self.hoSli_foco.setMaximum(1)
        self.hoSli_foco.setSingleStep(1)
        self.hoSli_foco.setPageStep(1)
        self.hoSli_foco.setTracking(True)
        self.hoSli_foco.setOrientation(QtCore.Qt.Horizontal)
        self.hoSli_foco.setObjectName("hoSli_foco")
        self.horizontalLayout_2.addWidget(self.hoSli_foco)
        self.label_19 = QtWidgets.QLabel(self.widget_3)
        self.label_19.setMinimumSize(QtCore.QSize(0, 20))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMinimumSize(QtCore.QSize(0, 110))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setMinimumSize(QtCore.QSize(100, 160))
        self.widget_5.setSizeIncrement(QtCore.QSize(100, 160))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.bel_estadoVenti = QtWidgets.QLabel(self.widget_5)
        self.bel_estadoVenti.setMinimumSize(QtCore.QSize(63, 63))
        self.bel_estadoVenti.setMaximumSize(QtCore.QSize(150, 150))
        self.bel_estadoVenti.setBaseSize(QtCore.QSize(63, 63))
        self.bel_estadoVenti.setStyleSheet("border-image: url(:/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/ventilador_off.png);\n"
"")
        self.bel_estadoVenti.setText("")
        self.bel_estadoVenti.setObjectName("bel_estadoVenti")
        self.verticalLayout_8.addWidget(self.bel_estadoVenti)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.btn_configVenti = QtWidgets.QPushButton(self.widget_5)
        self.btn_configVenti.setMinimumSize(QtCore.QSize(52, 21))
        self.btn_configVenti.setMaximumSize(QtCore.QSize(100, 40))
        self.btn_configVenti.setBaseSize(QtCore.QSize(52, 21))
        font = QtGui.QFont()
        font.setFamily("LucidaGrande")
        font.setPointSize(-1)
        self.btn_configVenti.setFont(font)
        self.btn_configVenti.setStyleSheet("QPushButton:hover {\n"
"    background-color: #DDE8E8; \n"
"    border: 1px solid #DAE7E7;\n"
"    border-radius: 7px;\n"
"  font-family: LucidaGrande;\n"
"  font-size: 11px;\n"
"  color:black;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    /*#background-color: #DDE8E8; */\n"
"    background-color:white;  \n"
"   border: 1px solid #B1BCBC;\n"
"    border-radius: 7px;\n"
"  font-family: LucidaGrande;\n"
"  font-size: 11px;\n"
" color:black;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#B8C0C0;\n"
"    border: 1px solid #B8C0C0;\n"
"    border-radius: 7px;\n"
"  font-family: LucidaGrande;\n"
"  font-size: 11px;\n"
"  color:black;\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.btn_configVenti.setObjectName("btn_configVenti")
        self.horizontalLayout_15.addWidget(self.btn_configVenti)
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setMinimumSize(QtCore.QSize(21, 21))
        self.label_7.setMaximumSize(QtCore.QSize(35, 35))
        self.label_7.setBaseSize(QtCore.QSize(21, 21))
        self.label_7.setStyleSheet("border-image:url(:/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/termo.png);\n"
"padding:0px;\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_15.addWidget(self.label_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setMinimumSize(QtCore.QSize(0, 20))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.hoSli_venti = QtWidgets.QSlider(self.widget_5)
        self.hoSli_venti.setMinimumSize(QtCore.QSize(45, 35))
        self.hoSli_venti.setMaximumSize(QtCore.QSize(80, 16777215))
        self.hoSli_venti.setBaseSize(QtCore.QSize(45, 35))
        self.hoSli_venti.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 15px; /*ALTURA DE LA BARRA*/\n"
"border-radius: 4px;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: rgb(33, 139, 14);/*qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);*/\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;   /*COLOR DE BARRA A LA IZQUIERDA*/\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 #eee, stop:1 #ccc); /*colo de la cosa que se mueve*/\n"
"border: 1px solid #777;\n"
"width: 20px; /* ancho de la barra que se  mueve*/\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"text:\"roni\";\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"text:\"roni\";\n"
"}")
        self.hoSli_venti.setMaximum(1)
        self.hoSli_venti.setSingleStep(1)
        self.hoSli_venti.setPageStep(1)
        self.hoSli_venti.setTracking(True)
        self.hoSli_venti.setOrientation(QtCore.Qt.Horizontal)
        self.hoSli_venti.setObjectName("hoSli_venti")
        self.horizontalLayout.addWidget(self.hoSli_venti)
        self.label_15 = QtWidgets.QLabel(self.widget_5)
        self.label_15.setMinimumSize(QtCore.QSize(0, 20))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.horizontalLayout_3.addWidget(self.widget_2)

        self.retranslateUi(Form)
        self.stack_alarmas.setCurrentIndex(-1)
        self.stack_notas.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RoniHernandez99/IoT_domotica"))
        self.bel_temp.setText(_translate("Form", "39.00"))
        self.label_11.setText(_translate("Form", "[°C]"))
        self.timeEdit_tiempo.setDisplayFormat(_translate("Form", "hh:mm a"))
        self.dateEdit_fecha.setDisplayFormat(_translate("Form", "dddd dd \'de\' MMMM "))
        self.label_6.setText(_translate("Form", "Manual"))
        self.label_10.setText(_translate("Form", "Automatico"))
        self.btn_configVenti.setText(_translate("Form", "100 [°C]"))
import IMAG_rc
