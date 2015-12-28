# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui.Ui_main import Ui_MainWindow
from .create import create_event
from .message import message_event
from .clerk_confirm_list import clerk_confirm_list_event
from .clerk_confirm import clerk_confirm_event

from config import Permission
import currentApp

class main_event(QMainWindow, Ui_MainWindow):
    
    create = None
    message = None
    clerk_confirm = None
    
    def __init__(self, parent=None):
        super(main_event, self).__init__(parent)
        self.setupUi(self)
        self.label_currentUser_data.setText(currentApp.getCurrentUser().name)

    @pyqtSlot()
    def on_button_human_query_clicked(self):
        self.clerk_confirm = clerk_confirm_event()
        self.clerk_confirm.show()

    @pyqtSlot()
    def on_button_human_create_clicked(self):
        if (currentApp.getCurrentUser().role.permission &
                Permission.HUMAN_REGISTER == Permission.HUMAN_REGISTER):
            self.create = create_event()
            self.create.show()
        else:
            self.message = message_event(msg = 'Permission Denied')
            self.message.show()
            
    @pyqtSlot()
    def on_button_human_confirm_clicked(self):
        if (currentApp.getCurrentUser().role.permission &
                Permission.HUMAN_COMFIRM == Permission.HUMAN_COMFIRM):
            self.clerk_confirm = clerk_confirm_event(currentApp.getCurrentUser())
            self.clerk_confirm.show()
        else:
            self.message = message_event(msg = 'Permission Denied')
            self.message.show()
