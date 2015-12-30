# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QDialog

from .Models import session, Group
from .message import message_event
from .Ui.Ui_institute_create import Ui_Dialog

class institute_update_event(QDialog, Ui_Dialog):
    
    msg = None
    institute = None
    _translate = QCoreApplication.translate
    groups = None
    companies = None
    selected_group = None
    selected_company = None
    selected_department = None
    
    def __init__(self, institute, parent=None):
        super(institute_update_event, self).__init__(parent)
        self.setupUi(self)
        self.institute = institute
        self.groups = session.query(Group).order_by(Group.id).all()
        for group in self.groups:
            self.input_group.addItem("")
            self.input_group.setItemText(group.id - 1, 
                self._translate('Dialog', group.name))
        if institute == 'group':
            self.label_company.close()
            self.input_company.close()
            self.label_department.close()
            self.input_department.close()
            self.label_name.setText('请选择要修改的一级机构名称：')
            self.label_name.setText('请输入新的机构名称：')
        elif institute == 'company':
            self.label_department.close()
            self.input_department.close()
            self.label_group.setText('请选择一级机构：')
            self.label_company.setText('请选择要修改的二级机构：')
            self.label_name.setText('请输入新的机构名称：')
        elif institute == 'department':
            self.label_group.setText('请选择一级机构：')
            self.label_company.setText('请选择二级机构：')
            self.label_department.setText('请选择要修改的三级机构：')
            self.label_name.setText('请输入新的机构名称：')
            
    @pyqtSlot(int)
    def on_input_group_currentIndexChanged(self, index):
        group = self.groups[index]
        self.selected_group = group
        if self.institute != 'group':
            self.input_company.clear()
            self.selected_company = None
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
                if self.institute == 'department':
                    for i, department in enumerate(company.departments):
                        self.input_department.addItem("")
                        self.input_department.setItemText(i, self._translate('Dialog', department.name))
                        

    @pyqtSlot(str)
    def on_input_department_currentTextChanged(self, p0):
        for department in self.selected_company.departments:
            if p0 == department.name:
                self.selected_department = department
                
    @pyqtSlot()
    def on_button_clicked(self):
        if self.institute == 'group':
            self.selected_group.name = self.input_name.text()
            session.add(self.selected_group)
        elif self.institute == 'company':
            self.selected_company.name = self.input_name.text()
            session.add(self.selected_company)
        elif self.institute == 'department':
            self.selected_department.name = self.input_name.text()
            session.add(self.selected_department)
        session.commit()
        self.msg = message_event(msg = 'Update Successfully')
        self.msg.show()
        self.close()
