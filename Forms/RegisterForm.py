import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.uic.properties import QtGui

from Forms import LoginForm
from Forms.ErrorDialog import ErrorDialog
from Models.UserType import UserType
from PyQt.py.Register import Ui_RegisterWindow


class RegisterForm(QtWidgets.QMainWindow, Ui_RegisterWindow):
    def __init__(self, db):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.error_from = None
        self.login_form = None
        self.btn_register.clicked.connect(self.on_register)

    def get_user_type(self):
        if self.rbtn_client.isChecked():
            return UserType.Client.value
        elif self.rbtn_driver.isChecked():
            return UserType.Driver.value
        else:
            return 0

    def on_register(self):
        result = self.db.insert_user(
            self.edit_login.text(),
            self.edit_password.text(),
            self.edit_lastname.text(),
            self.edit_firstname.text(),
            self.edit_patronymic.text(),
            self.get_user_type()
        )
        if result is not None:
            self.error_from = ErrorDialog(result)
            self.error_from.show()
        else:
            self.login_form = LoginForm.LoginWindow(self.db)
            self.login_form.show()
            self.close()
