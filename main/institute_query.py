# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView

from .Models import session, Group
from .Ui.Ui_institute_query import Ui_Dialog


class institute_query_event(QDialog, Ui_Dialog):
    
    groups = None
    companies = None
    selected_company = None
    
    def __init__(self, parent=None):
        super(institute_query_event, self).__init__(parent)
        self.setupUi(self)
        self.groups = session.query(Group).order_by(Group.id).all()
        self.table_group.setColumnWidth(1, 200)
        self.table_company.setColumnWidth(1, 200)
        self.table_department.setColumnWidth(1, 200)
        if self.groups is not None:
            for i, group in enumerate(self.groups):
                self.table_group.insertRow(i)
                self.table_group.setItem(i, 0, QTableWidgetItem((str)(i + 1)))
                self.table_group.setItem(i, 1, QTableWidgetItem(group.name))
    
    @pyqtSlot(int, int)
    def on_table_group_cellClicked(self, row, column):
        for rows in range(self.table_company.rowCount()):
            self.table_company.removeRow(0)
        group = self.groups[row]
        self.companies = group.companies
        if self.companies is not None:
            for i, company in enumerate(self.companies):
                self.table_company.insertRow(i)
                self.table_company.setItem(i, 0, QTableWidgetItem((str)(i + 1)))
                self.table_company.setItem(i, 1, QTableWidgetItem(company.name))
    
    @pyqtSlot(int, int)
    def on_table_company_cellClicked(self, row, column):
        for row in range(self.table_department.rowCount()):
            self.table_department.removeRow(0)
        for company in self.companies:
            if self.table_company.item(row, 1).text() == company.name:
                self.selected_company = company
                if company.departments is not None:
                    for i, department in enumerate(company.departments):
                        self.table_department.insertRow(i)
                        self.table_department.setItem(i, 0, QTableWidgetItem((str)(i + 1)))
                        self.table_department.setItem(i, 1, QTableWidgetItem(department.name))
    
    @pyqtSlot()
    def on_button_clicked(self):
        self.close()
