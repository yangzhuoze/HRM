# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QLineEdit

from . import app,  session
from .main import main_event
from .Models import Clerk
from .Ui.Ui_login import Ui_Dialog

import currentApp

class login_event(QDialog, Ui_Dialog):
    
    main = None
    
    def __init__(self, parent=None):
        super(login_event, self).__init__(parent)
        self.setupUi(self)
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_username.setText('201501010101')
        self.input_password.setText('000000')
    
    @pyqtSlot()
    def on_button_login_clicked(self):
        global currentApp
        username = self.input_username.text()
        password = self.input_password.text()
        user = session.query(Clerk).filter_by(recordid = username, 
            password = password).first()
        if (user != None):
            currentApp.setCurrentUser(user)
            self.main = main_event()
            self.main.show()
            self.close()
        else:
            self.label_msg.setText('用户名密码不正确')
    
    @pyqtSlot()
    def on_button_quit_clicked(self):
        sys.exit(app.exec_())

