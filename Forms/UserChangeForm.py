from PyQt5 import QtWidgets
from PyQt.py.UserChange import Ui_MainWindow
from PyQt5.QtCore import QDateTime

class UserChangeForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, db, login, parent):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.parent = parent
        self.login = login
        self.lbl_login.setText(f"Login - {login}")
        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.btn_apply.clicked.connect(self.update_user_type)
        self.btn_lock.clicked.connect(self.block_forever)
        self.btn_unlock.clicked.connect(self.unlock)
        self.btn_time_block.clicked.connect(self.block_temporary)
        self.btn_delete.clicked.connect(self.delete)

    def update_user_type(self):
        user_type = self.comboBox_userType.currentText()
        self.db.update_user_type(self.login, user_type)
        self.parent.table_fill()

    def block_forever(self):
        self.db.block_forever(self.login)
        self.parent.table_fill()

    def unlock(self):
        self.db.unlock(self.login)
        self.parent.table_fill()

    def block_temporary(self):
        block_end = self.dateEdit.dateTime().toUTC()
        sec = 100
        self.db.block_temporary(self.login, sec)
        self.parent.table_fill()

    def delete(self):
        self.db.delete(self.login)
        self.parent.table_fill()
        self.close()






