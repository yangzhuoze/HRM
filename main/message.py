# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui.Ui_message import Ui_Dialog


class message_event(QDialog, Ui_Dialog):
    def __init__(self, parent=None, msg = None):
        super(message_event, self).__init__(parent)
        self.setupUi(self)
        self.message.setText(msg)
    
    @pyqtSlot()
    def on_button_clicked(self):
        self.close()
