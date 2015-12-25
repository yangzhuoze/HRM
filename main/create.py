# -*- coding: utf-8 -*-

from datetime import datetime

from PyQt5.QtCore import pyqtSlot,  QCoreApplication,  QDate
from PyQt5.QtWidgets import QDialog

from .Models import Group, Company, Department
from . import session
from .Ui.Ui_clerkdetail import Ui_Dialog

class create_event(QDialog, Ui_Dialog):
    
    _translate = QCoreApplication.translate
    group = session.query(Group).order_by(Group.id).all()
    companies = None
    
    def __init__(self, parent=None):
        super(create_event, self).__init__(parent)
        self.setupUi(self)
        self.label_booktime_data.setText((str)(datetime.now())[:19])
        for i in self.group:
            self.input_group.addItem("")
            self.input_group.setItemText(i.id - 1, self._translate('Dialog', i.name))
    
    @pyqtSlot(QDate)
    def on_input_birthday_dateChanged(self, date):
        currentYear = QDate.currentDate().year()
        birthYear = date.year()
        age = (str)(currentYear - birthYear)
        self.label_age_data.setText(age)
    
    @pyqtSlot(int)
    def on_input_company_currentIndexChanged(self, index):
        self.input_department.clear()
        departments = session.query(Department).order_by(Department.id).filter_by(parent_id = self.companies[index].id)
        for i, department in enumerate(departments):
            self.input_department.addItem("")
            self.input_department.setItemText(i, self._translate('Dialog', department.name))
    
    @pyqtSlot(int)
    def on_input_group_currentIndexChanged(self, index):
        self.input_company.clear()
        self.group_index = index
        self.companies = session.query(Company).order_by(Company.id).filter_by(parent_id = index + 1)
        for i, company in enumerate(self.companies):
            self.input_company.addItem("")
            self.input_company.setItemText(i, self._translate('Dialog', company.name))
    
    @pyqtSlot()
    def on_button_submit_clicked(self):
        pass
    
    @pyqtSlot()
    def on_button_clear_clicked(self):
        pass
