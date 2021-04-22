# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\configVenti_dise.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(354, 200)
        Dialog.setMouseTracking(False)
        Dialog.setAcceptDrops(False)
        Dialog.setWindowTitle("")
        Dialog.setWindowOpacity(1.0)
        Dialog.setAutoFillBackground(False)
        Dialog.setWindowFilePath("")
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setMinimumSize(QtCore.QSize(50, 50))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.dSB_tempActVenti = QtWidgets.QDoubleSpinBox(Dialog)
        self.dSB_tempActVenti.setMinimumSize(QtCore.QSize(90, 40))
        self.dSB_tempActVenti.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dSB_tempActVenti.setFont(font)
        self.dSB_tempActVenti.setAlignment(QtCore.Qt.AlignCenter)
        self.dSB_tempActVenti.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dSB_tempActVenti.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dSB_tempActVenti.setKeyboardTracking(True)
        self.dSB_tempActVenti.setProperty("showGroupSeparator", False)
        self.dSB_tempActVenti.setDecimals(1)
        self.dSB_tempActVenti.setProperty("value", 70.0)
        self.dSB_tempActVenti.setObjectName("dSB_tempActVenti")
        self.horizontalLayout.addWidget(self.dSB_tempActVenti)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.label_2.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(70, 50))
        self.label_4.setMaximumSize(QtCore.QSize(100, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("border-image: url(:/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/termo.png);")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setMinimumSize(QtCore.QSize(50, 50))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setMinimumSize(QtCore.QSize(0, 10))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(50, 50))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.btn_guardarSalir = QtWidgets.QPushButton(Dialog)
        self.btn_guardarSalir.setMinimumSize(QtCore.QSize(110, 40))
        self.btn_guardarSalir.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_guardarSalir.setStyleSheet("QPushButton:hover {\n"
"    background-color: #DDE8E8; \n"
"    border: 1px solid #DAE7E7;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #DDE8E8; \n"
"    border: 1px solid #B1BCBC;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#B8C0C0;\n"
"    border: 1px solid #B8C0C0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.btn_guardarSalir.setObjectName("btn_guardarSalir")
        self.horizontalLayout_2.addWidget(self.btn_guardarSalir)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setMinimumSize(QtCore.QSize(50, 50))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "Prender ventilador a partir de los:"))
        self.label_2.setText(_translate("Dialog", "°[C]"))
        self.btn_guardarSalir.setText(_translate("Dialog", "GUARDAR"))
import IMAG_rc
