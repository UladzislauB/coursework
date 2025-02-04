# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt\ui\Order.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 409)
        MainWindow.setStyleSheet("QLineEdit\n"
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
"    font: 14pt \"Comic Sans MS\";\n"
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
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_to = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_to.setFont(font)
        self.label_to.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label_to.setObjectName("label_to")
        self.gridLayout.addWidget(self.label_to, 1, 0, 1, 1)
        self.edit_from = ClickableLineEdit(self.frame)
        self.edit_from.setStyleSheet("")
        self.edit_from.setText("")
        self.edit_from.setReadOnly(False)
        self.edit_from.setObjectName("edit_from")
        self.gridLayout.addWidget(self.edit_from, 0, 1, 1, 1)
        self.edit_to = ClickableLineEdit(self.frame)
        self.edit_to.setStyleSheet("ClickableLineEdit{\n"
"    color: black;\n"
"}")
        self.edit_to.setText("")
        self.edit_to.setObjectName("edit_to")
        self.gridLayout.addWidget(self.edit_to, 1, 1, 1, 1)
        self.label_from = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_from.setFont(font)
        self.label_from.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.label_from.setObjectName("label_from")
        self.gridLayout.addWidget(self.label_from, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_payment = QtWidgets.QLabel(self.frame_2)
        self.lbl_payment.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.lbl_payment.setObjectName("lbl_payment")
        self.gridLayout_2.addWidget(self.lbl_payment, 0, 0, 1, 2)
        self.comboBox_payment = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_payment.setMaximumSize(QtCore.QSize(500, 30))
        self.comboBox_payment.setStyleSheet("")
        self.comboBox_payment.setObjectName("comboBox_payment")
        self.gridLayout_2.addWidget(self.comboBox_payment, 0, 2, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.frame_2)
        self.btn_add.setMinimumSize(QtCore.QSize(50, 0))
        self.btn_add.setMaximumSize(QtCore.QSize(50, 25))
        self.btn_add.setStyleSheet("QPushButton{\n"
"color: #1db954;\n"
"background:     #121212;\n"
"border-radius: 60px;\n"
"font: 12pt \"Comic Sans MS\";\n"
"}")
        self.btn_add.setObjectName("btn_add")
        self.gridLayout_2.addWidget(self.btn_add, 0, 3, 1, 1)
        self.lbl_tarif = QtWidgets.QLabel(self.frame_2)
        self.lbl_tarif.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.lbl_tarif.setObjectName("lbl_tarif")
        self.gridLayout_2.addWidget(self.lbl_tarif, 1, 0, 1, 2)
        self.lbl_proveder = QtWidgets.QLabel(self.frame_2)
        self.lbl_proveder.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.lbl_proveder.setObjectName("lbl_proveder")
        self.gridLayout_2.addWidget(self.lbl_proveder, 2, 0, 2, 2)
        self.edit_price = QtWidgets.QLineEdit(self.frame_2)
        self.edit_price.setEnabled(False)
        self.edit_price.setStyleSheet("QLineEdit\n"
"{\n"
"background: transparent;\n"
"border: none;\n"
"font: 16pt \"Comic Sans MS\";\n"
"color: steelblue;\n"
"}")
        self.edit_price.setText("")
        self.edit_price.setObjectName("edit_price")
        self.gridLayout_2.addWidget(self.edit_price, 3, 1, 2, 1)
        self.lbl_price = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_price.setFont(font)
        self.lbl_price.setStyleSheet("QLabel{\n"
"    color:    #535353;\n"
"}")
        self.lbl_price.setObjectName("lbl_price")
        self.gridLayout_2.addWidget(self.lbl_price, 4, 0, 1, 1)
        self.comboBox_tarif = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_tarif.setMaximumSize(QtCore.QSize(500, 30))
        self.comboBox_tarif.setStyleSheet("")
        self.comboBox_tarif.setObjectName("comboBox_tarif")
        self.gridLayout_2.addWidget(self.comboBox_tarif, 1, 2, 1, 2)
        self.comboBox_provider = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_provider.setMaximumSize(QtCore.QSize(500, 30))
        self.comboBox_provider.setStyleSheet("")
        self.comboBox_provider.setObjectName("comboBox_provider")
        self.gridLayout_2.addWidget(self.comboBox_provider, 2, 2, 1, 2)
        self.verticalLayout.addWidget(self.frame_2)
        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setMinimumSize(QtCore.QSize(181, 41))
        self.btn_submit.setStyleSheet("QPushButton{\n"
"color: #1db954;\n"
"background:     #121212;\n"
"border-radius: 60px;\n"
"font: 12pt \"Comic Sans MS\";\n"
"}")
        self.btn_submit.setObjectName("btn_submit")
        self.verticalLayout.addWidget(self.btn_submit, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Order Taxi"))
        self.label_to.setText(_translate("MainWindow", "To"))
        self.label_from.setText(_translate("MainWindow", "From"))
        self.lbl_payment.setText(_translate("MainWindow", "Select payment"))
        self.btn_add.setText(_translate("MainWindow", "Add"))
        self.lbl_tarif.setText(_translate("MainWindow", "Select tarif"))
        self.lbl_proveder.setText(_translate("MainWindow", "Select provider"))
        self.lbl_price.setText(_translate("MainWindow", "Price"))
        self.btn_submit.setText(_translate("MainWindow", "Submit"))
from PyQt.mycomponent.clickablelineedit import ClickableLineEdit


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Order = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Order)
    Order.show()
    sys.exit(app.exec_())
