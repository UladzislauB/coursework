# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt\ui\Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(417, 486)
        RegisterWindow.setStyleSheet("QLineEdit\n"
"{\n"
"background: transparent;\n"
"border: none;\n"
"border-bottom: 1px solid steelblue;\n"
"font: 12pt \"Comic Sans MS\";\n"
"}\n"
"QLineEdit:focus {\n"
" outline:none; }\n"
"\n"
"QLabel{\n"
"    color: steelblue;\n"
"    font: 15pt \"Comic Sans MS\";\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: white;\n"
"background: steelblue;\n"
"border-radius: 60px;\n"
"font: 12pt \"Comic Sans MS\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(272, 231))
        self.frame.setMaximumSize(QtCore.QSize(472, 231))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_login = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label_login.setObjectName("label_login")
        self.gridLayout.addWidget(self.label_login, 0, 0, 1, 1)
        self.edit_password = QtWidgets.QLineEdit(self.frame)
        self.edit_password.setText("")
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.gridLayout.addWidget(self.edit_password, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.edit_login = QtWidgets.QLineEdit(self.frame)
        self.edit_login.setStyleSheet("")
        self.edit_login.setText("")
        self.edit_login.setObjectName("edit_login")
        self.gridLayout.addWidget(self.edit_login, 0, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(388, 119))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_patronymic = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_patronymic.setFont(font)
        self.label_patronymic.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label_patronymic.setObjectName("label_patronymic")
        self.gridLayout_2.addWidget(self.label_patronymic, 2, 0, 1, 1)
        self.edit_lastname = QtWidgets.QLineEdit(self.frame_2)
        self.edit_lastname.setStyleSheet("")
        self.edit_lastname.setText("")
        self.edit_lastname.setObjectName("edit_lastname")
        self.gridLayout_2.addWidget(self.edit_lastname, 1, 1, 1, 1)
        self.edit_patronymic = QtWidgets.QLineEdit(self.frame_2)
        self.edit_patronymic.setStyleSheet("")
        self.edit_patronymic.setText("")
        self.edit_patronymic.setObjectName("edit_patronymic")
        self.gridLayout_2.addWidget(self.edit_patronymic, 2, 1, 1, 1)
        self.edit_firstname = QtWidgets.QLineEdit(self.frame_2)
        self.edit_firstname.setStyleSheet("")
        self.edit_firstname.setText("")
        self.edit_firstname.setObjectName("edit_firstname")
        self.gridLayout_2.addWidget(self.edit_firstname, 0, 1, 1, 1)
        self.label_lastname = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_lastname.setFont(font)
        self.label_lastname.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label_lastname.setObjectName("label_lastname")
        self.gridLayout_2.addWidget(self.label_lastname, 1, 0, 1, 1)
        self.label_firstname = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_firstname.setFont(font)
        self.label_firstname.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label_firstname.setObjectName("label_firstname")
        self.gridLayout_2.addWidget(self.label_firstname, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.edit_contacts = ClickableLineEdit(self.frame_4)
        self.edit_contacts.setStyleSheet("")
        self.edit_contacts.setReadOnly(False)
        self.edit_contacts.setObjectName("edit_contacts")
        self.gridLayout_4.addWidget(self.edit_contacts, 4, 1, 1, 1)
        self.label_contacts = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_contacts.setFont(font)
        self.label_contacts.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label_contacts.setObjectName("label_contacts")
        self.gridLayout_4.addWidget(self.label_contacts, 4, 0, 1, 1)
        self.edit_address = ClickableLineEdit(self.frame_4)
        self.edit_address.setStyleSheet("")
        self.edit_address.setReadOnly(False)
        self.edit_address.setObjectName("edit_address")
        self.gridLayout_4.addWidget(self.edit_address, 0, 1, 1, 1)
        self.label_address = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_address.setFont(font)
        self.label_address.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label_address.setObjectName("label_address")
        self.gridLayout_4.addWidget(self.label_address, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(481, 66))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbtn_client = QtWidgets.QRadioButton(self.frame_3)
        self.rbtn_client.setChecked(True)
        self.rbtn_client.setObjectName("rbtn_client")
        self.horizontalLayout.addWidget(self.rbtn_client)
        self.rbtn_driver = QtWidgets.QRadioButton(self.frame_3)
        self.rbtn_driver.setObjectName("rbtn_driver")
        self.horizontalLayout.addWidget(self.rbtn_driver)
        self.btn_passpot = QtWidgets.QPushButton(self.frame_3)
        self.btn_passpot.setMinimumSize(QtCore.QSize(100, 41))
        self.btn_passpot.setStyleSheet("QPushButton{\n"
"color: #1db954;\n"
"background:     #121212;\n"
"border-radius: 60px;\n"
"font: 12pt \"Comic Sans MS\";\n"
"}")
        self.btn_passpot.setObjectName("btn_passpot")
        self.horizontalLayout.addWidget(self.btn_passpot)
        self.verticalLayout.addWidget(self.frame_3)
        self.btn_register = QtWidgets.QPushButton(self.centralwidget)
        self.btn_register.setMinimumSize(QtCore.QSize(181, 41))
        self.btn_register.setStyleSheet("QPushButton{\n"
"color: #1db954;\n"
"background:     #121212;\n"
"border-radius: 60px;\n"
"font: 12pt \"Comic Sans MS\";\n"
"}")
        self.btn_register.setObjectName("btn_register")
        self.verticalLayout.addWidget(self.btn_register)
        RegisterWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Register"))
        self.label_login.setText(_translate("RegisterWindow", "Login"))
        self.label.setText(_translate("RegisterWindow", "Password"))
        self.label_patronymic.setText(_translate("RegisterWindow", "MiddleName"))
        self.label_lastname.setText(_translate("RegisterWindow", "LastName"))
        self.label_firstname.setText(_translate("RegisterWindow", "FirsName"))
        self.edit_contacts.setText(_translate("RegisterWindow", "+375122456798"))
        self.label_contacts.setText(_translate("RegisterWindow", "Contacts"))
        self.edit_address.setText(_translate("RegisterWindow", "ул. Гуляева д.13 кв.19"))
        self.label_address.setText(_translate("RegisterWindow", "Address"))
        self.rbtn_client.setText(_translate("RegisterWindow", "Client"))
        self.rbtn_driver.setText(_translate("RegisterWindow", "Driver"))
        self.btn_passpot.setText(_translate("RegisterWindow", "Passport"))
        self.btn_register.setText(_translate("RegisterWindow", "Register"))
from PyQt.mycomponent.clickablelineedit import ClickableLineEdit
