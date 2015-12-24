# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from . import app
from .Ui.Ui_login import Ui_Dialog

class login_event(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(login_event, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_button_login_clicked(self):
        print(self.input_username.text())
    
    @pyqtSlot()
    def on_button_quit_clicked(self):
        sys.exit(app.exec_())

