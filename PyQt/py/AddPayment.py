# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt\ui\AddPayment.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPaymentWindow(object):
    def setupUi(self, AddPaymentWindow):
        AddPaymentWindow.setObjectName("AddPaymentWindow")
        AddPaymentWindow.resize(384, 338)
        AddPaymentWindow.setStyleSheet("QLineEdit\n"
"{\n"
"background: transparent;\n"
"border: none;\n"
"border-bottom: 1px solid steelblue;\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: steelblue;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: steelblue;\n"
"    transition: all 1s;\n"
"    font: 10pt \"Comic Sans MS\";\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: white;\n"
"background: steelblue;\n"
"border-radius: 60px;\n"
"font: 12pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QComboBox{\n"
"background: transparent;\n"
"border: none;\n"
"border-bottom: 1px solid steelblue;\n"
"font: 12pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QDateEdit{\n"
"background: transparent;\n"
"border: none;\n"
"font: 14pt \"Comic Sans MS\";\n"
"color: steelblue;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(AddPaymentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_card_number = QtWidgets.QLabel(self.frame)
        self.label_card_number.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label_card_number.setObjectName("label_card_number")
        self.verticalLayout.addWidget(self.label_card_number)
        self.edit_card_number = QtWidgets.QLineEdit(self.frame)
        self.edit_card_number.setObjectName("edit_card_number")
        self.verticalLayout.addWidget(self.edit_card_number)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_card_holder = QtWidgets.QLabel(self.frame_4)
        self.label_card_holder.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label_card_holder.setObjectName("label_card_holder")
        self.verticalLayout_2.addWidget(self.label_card_holder)
        self.edit_card_holder = QtWidgets.QLineEdit(self.frame_4)
        self.edit_card_holder.setObjectName("edit_card_holder")
        self.verticalLayout_2.addWidget(self.edit_card_holder)
        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_expiration_date = QtWidgets.QLabel(self.frame_2)
        self.label_expiration_date.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label_expiration_date.setObjectName("label_expiration_date")
        self.verticalLayout_3.addWidget(self.label_expiration_date)
        self.dateEdit_expiration_date = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit_expiration_date.setStyleSheet("QDateEdit{\n"
"    color:    black;\n"
"}")
        self.dateEdit_expiration_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2099, 12, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_expiration_date.setObjectName("dateEdit_expiration_date")
        self.verticalLayout_3.addWidget(self.dateEdit_expiration_date)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_security_code = QtWidgets.QLabel(self.frame_3)
        self.label_security_code.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label_security_code.setObjectName("label_security_code")
        self.verticalLayout_4.addWidget(self.label_security_code)
        self.edit_security_code = QtWidgets.QLineEdit(self.frame_3)
        self.edit_security_code.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_security_code.setObjectName("edit_security_code")
        self.verticalLayout_4.addWidget(self.edit_security_code)
        self.gridLayout.addWidget(self.frame_3, 2, 1, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setMinimumSize(QtCore.QSize(130, 40))
        self.btn_add.setStyleSheet("QPushButton{\n"
"color: #1db954;\n"
"background:     #121212;\n"
"border-radius: 60px;\n"
"font: 12pt \"Comic Sans MS\";\n"
"}")
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 3, 0, 1, 2)
        AddPaymentWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddPaymentWindow)
        QtCore.QMetaObject.connectSlotsByName(AddPaymentWindow)

    def retranslateUi(self, AddPaymentWindow):
        _translate = QtCore.QCoreApplication.translate
        AddPaymentWindow.setWindowTitle(_translate("AddPaymentWindow", "Add payment method"))
        self.label_card_number.setText(_translate("AddPaymentWindow", "Card Number"))
        self.label_card_holder.setText(_translate("AddPaymentWindow", "Card holder"))
        self.label_expiration_date.setText(_translate("AddPaymentWindow", "Expiration date"))
        self.dateEdit_expiration_date.setDisplayFormat(_translate("AddPaymentWindow", "MM/yy"))
        self.label_security_code.setText(_translate("AddPaymentWindow", "Security code"))
        self.btn_add.setText(_translate("AddPaymentWindow", "Add"))
