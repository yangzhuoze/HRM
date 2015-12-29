# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QDialog

from . import session
from .Models import Group, Clerk, PositionCat, PositionTitle
from .Ui.Ui_clerk_query_filter import Ui_Dialog


class clerk_query_filter_event(QDialog, Ui_Dialog):
    
    _translate = QCoreApplication.translate
    query_list = None
    groups = session.query(Group).order_by(Group.id).all()
    companies = None
    selected_group = None
    selected_company = None
    selected_department = None
    
    positioncats = session.query(PositionCat).order_by(PositionCat.id).all()
    selected_positioncat = None
    selected_position = None
    
    positiontitles = session.query(PositionTitle).order_by(PositionTitle.id).all()
    selected_positiontitle = None
    
    def __init__(self, parent=None):
        super(clerk_query_filter_event, self).__init__(parent)
        self.setupUi(self)
        for group in self.groups:
            self.input_group.addItem("")
            self.input_group.setItemText(group.id - 1, 
                self._translate('Dialog', group.name))
        for positioncat in self.positioncats:
            self.input_positioncat.addItem("")
            self.input_positioncat.setItemText(positioncat.id - 1, 
                self._translate('Dialog', positioncat.name))
    
    @pyqtSlot(int)
    def on_input_group_currentIndexChanged(self, index):
        self.input_company.clear()
        self.selected_company = None
        group = self.groups[index]
        self.selected_group = group
        self.companies = group.companies
        for i, company in enumerate(self.companies):
            self.input_company.addItem("")
            self.input_company.setItemText(i, self._translate('Dialog', company.name))
                
    @pyqtSlot(str)
    def on_input_company_currentTextChanged(self, p0):
        self.input_department.clear()
        self.selected_department = None
        for company in self.companies:
            if p0 == company.name:
                self.selected_company = company
                for i, department in enumerate(company.departments):
                    self.input_department.addItem("")
                    self.input_department.setItemText(i, self._translate('Dialog', department.name))
        
    @pyqtSlot(str)
    def on_input_department_currentTextChanged(self, p0):
        for department in self.selected_company.departments:
            if p0 == department.name:
                self.selected_department = department


    @pyqtSlot(int)
    def on_input_positioncat_currentIndexChanged(self, index):
        self.input_position.clear()
        self.selected_position = None
        positioncat = self.positioncats[index]
        self.selected_positioncat = positioncat
        for i, position in enumerate(positioncat.position):
            self.input_position.addItem("")
            self.input_position.setItemText(i, self._translate('Dialog', position.name))
    
    @pyqtSlot(str)
    def on_input_position_currentTextChanged(self, p0):
        for position in self.selected_positioncat.position:
            if p0 == position.name:
                self.selected_position = position
    
    @pyqtSlot()
    def on_button_submit_clicked(self):
        clerks = session.query(Clerk).filter_by(
            group = self.selected_group,
            company = self.selected_company,
            department = self.selected_department,
            position = self.selected_position).all()
        from .clerk_query_list import clerk_query_list_event
        self.query_list = clerk_query_list_event(clerks = clerks)
        self.query_list.show()
        self.close()
