# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .institute_create import institute_create_event
from .Ui.Ui_institute_create_list import Ui_Dialog


class institute_create_list_event(QDialog, Ui_Dialog):
    
    institute_create = None
    
    def __init__(self, parent=None):
        super(institute_create_list_event, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_button_group_clicked(self):
        self.institute_create = institute_create_event('group')
        self.institute_create.show()
        self.close()
    
    @pyqtSlot()
    def on_button_company_clicked(self):
        self.institute_create = institute_create_event('company')
        self.institute_create.show()
        self.close()
    
    @pyqtSlot()
    def on_button_department_clicked(self):
        self.institute_create = institute_create_event('department')
        self.institute_create.show()
        self.close()
