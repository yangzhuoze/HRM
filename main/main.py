# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui.Ui_main import Ui_MainWindow
from .message import message_event
from .clerk_query_list import clerk_query_list_event
from .clerk_create import clerk_create_event
from .clerk_update_list import clerk_update_list_event
from .clerk_confirm_list import clerk_confirm_list_event
from .position_query import position_query_event
from .position_list import position_list_event
from .role import role_event
from .role_link_list import role_link_list_event
from .institute_query import institute_query_event
from .institute_create_list import institute_create_list_event
from .institute_update_list import institute_update_list_event
from .salary_query_list import salary_query_list_event
from .salary_create import salary_create_event
from .salary_update_list import salary_update_list_event
from .salary_confirm_list import salary_confirm_list_event
from .salary_pay_list import salary_pay_list_event

from config import Permission
import currentApp

class main_event(QMainWindow, Ui_MainWindow):
    
    message = None
    clerk_query = None
    clerk_create = None
    clerk_update = None
    clerk_confirm = None
    position_query = None
    position_list = None
    role = None
    role_link_list = None
    institute_query = None
    institute_create = None
    institute_update = None
    salary_query = None
    salary_create = None
    salary_update = None
    salary_confirm = None
    salary_pay = None
    
    def __init__(self, parent=None):
        super(main_event, self).__init__(parent)
        self.setupUi(self)
        self.label_currentUser_data.setText(currentApp.getCurrentUser().name)

    @pyqtSlot()
    def on_button_human_query_clicked(self):
        self.clerk_query = clerk_query_list_event()
        self.clerk_query.show()

    @pyqtSlot()
    def on_button_human_create_clicked(self):
        if (currentApp.getCurrentUser().role.permission &
                Permission.HUMAN_CREATE == Permission.HUMAN_CREATE):
            self.clerk_ = clerk_create_event()
            self.clerk_.show()
        else:
            self.message = message_event(msg = 'Permission Denied')
            self.message.show()
            
    @pyqtSlot()
    def on_button_human_update_clicked(self):
        if (currentApp.getCurrentUser().role.permission &
                Permission.HUMAN_UPDATE == Permission.HUMAN_UPDATE):
            self.clerk_update = clerk_update_list_event()
            self.clerk_update.show()
        else:
            self.message = message_event(msg = 'Permission Denied')
            self.message.show()
            
    @pyqtSlot()
    def on_button_human_confirm_clicked(self):
        if (currentApp.getCurrentUser().role.permission &
                Permission.HUMAN_COMFIRM == Permission.HUMAN_COMFIRM):
            self.clerk_confirm = clerk_confirm_list_event()
            self.clerk_confirm.show()
        else:
            self.message = message_event(msg = 'Permission Denied')
            self.message.show()
            
    @pyqtSlot()
    def on_button_position_query_clicked(self):
        self.position_query = position_query_event()
        self.position_query.show()
            
    @pyqtSlot()
    def on_button_position_list_clicked(self):
        self.position_list = position_list_event()
        self.position_list.show()
            
    @pyqtSlot()
    def on_button_role_clicked(self):
        self.role = role_event()
        self.role.show()
            
    @pyqtSlot()
    def on_button_role_link_list_clicked(self):
        self.role_link_list = role_link_list_event()
        self.role_link_list.show()
            
    @pyqtSlot()
    def on_button_institute_query_clicked(self):
        self.institute_query = institute_query_event()
        self.institute_query.show()
        
    @pyqtSlot()
    def on_button_institute_create_clicked(self):
        self.institute_create = institute_create_list_event()
        self.institute_create.show()
        
    @pyqtSlot()
    def on_button_institute_update_clicked(self):
        self.institute_update = institute_update_list_event()
        self.institute_update.show()

    @pyqtSlot()
    def on_button_salary_query_clicked(self):
        self.salary_query = salary_query_list_event()
        self.salary_query.show()
            
    @pyqtSlot()
    def on_button_salary_create_clicked(self):
        self.salary_create = salary_create_event()
        self.salary_create.show()
        
    @pyqtSlot()
    def on_button_salary_update_clicked(self):
        self.salary_update = salary_update_list_event()
        self.salary_update.show()
        
    @pyqtSlot()
    def on_button_salary_confirm_clicked(self):
        self.salary_confirm = salary_confirm_list_event()
        self.salary_confirm.show()
        
    @pyqtSlot()
    def on_button_salary_pay_clicked(self):
        self.salary_pay = salary_pay_list_event()
        self.salary_pay.show()
