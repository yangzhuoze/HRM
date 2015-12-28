# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui.Ui_main import Ui_MainWindow
from .create import create_event
from .message import message_event

from config import Permission
import currentApp

class main_event(QMainWindow, Ui_MainWindow):
    
    create = None
    message = None
    
    def __init__(self, parent=None):
        super(main_event, self).__init__(parent)
        self.setupUi(self)
        self.label_currentUser_data.setText(currentApp.getCurrentUser().name)

    @pyqtSlot()
    def on_button_human_query_clicked(self):
        self.message = message_event(msg = 'Permission Denied')
        self.message.show()

    @pyqtSlot()
    def on_button_human_create_clicked(self):
        if (currentApp.getCurrentUser().role.permission &
                Permission.HUMAN_REGISTER == Permission.HUMAN_REGISTER):
            self.create = create_event()
            self.create.show()
        else:
            self.message = message_event(msg = 'Permission Denied')
            self.message.show()
