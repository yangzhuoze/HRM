# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot,  QDate
from PyQt5.QtWidgets import QDialog

from .Models import Group
from . import session
from .Ui.Ui_create import Ui_Dialog

class create_event(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(create_event, self).__init__(parent)
        self.setupUi(self)
        for i in session.query(Group).all():
            self.input_group.addItem(i.name)
    
    @pyqtSlot(QDate)
    def on_input_birthday_dateChanged(self, date):
        currentYear = QDate.currentDate().year()
        birthYear = date.year()
        age = (str)(currentYear - birthYear)
        self.label_age_data.setText(age)
    
    @pyqtSlot(int)
    def on_input_company_currentIndexChanged(self, index):
        pass
    
    @pyqtSlot(int)
    def on_input_group_currentIndexChanged(self, index):
        pass
    
    @pyqtSlot()
    def on_button_submit_clicked(self):
        pass
    
    @pyqtSlot()
    def on_button_clear_clicked(self):
        pass
