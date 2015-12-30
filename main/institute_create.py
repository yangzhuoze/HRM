# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QDialog

from .Models import session, Group, Company, Department
from .message import message_event
from .Ui.Ui_institute_create import Ui_Dialog


class institute_create_event(QDialog, Ui_Dialog):
    
    msg = None
    institute = None
    _translate = QCoreApplication.translate
    groups = None
    companies = None
    selected_group = None
    selected_company = None
    
    def __init__(self, institute, parent=None):
        super(institute_create_event, self).__init__(parent)
        self.setupUi(self)
        self.institute = institute
        self.groups = session.query(Group).order_by(Group.id).all()
        if institute == 'group':
            self.label_name.setText('请输入要登记的一级机构名称：')
            self.label_group.close()
            self.input_group.close()
            self.label_company.close()
            self.input_company.close()
        elif institute == 'company':
            self.label_group.setText('请选择一级机构：')
            for group in self.groups:
                self.input_group.addItem("")
                self.input_group.setItemText(group.id - 1, 
                    self._translate('Dialog', group.name))
            self.label_company.close()
            self.input_company.close()
            self.label_name.setText('请输入要登记的二级机构名称：')
        elif institute == 'department':
            self.label_group.setText('请选择一级机构：')
            self.label_company.setText('请选择二级机构：')
            for group in self.groups:
                self.input_group.addItem("")
                self.input_group.setItemText(group.id - 1, 
                    self._translate('Dialog', group.name))
            self.label_name.setText('请输入要登记的三级机构名称：')
    
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
        for company in self.companies:
            if p0 == company.name:
                self.selected_company = company
    
    @pyqtSlot()
    def on_button_clicked(self):
        if self.institute == 'group':
            group = Group(name = self.input_name.text())
            session.add(group)
            session.commit()
            self.msg = message_event(msg = 'Insert Successfully')
            self.msg.show()
            self.close()
        elif self.institute == 'company':
            company = Company(name = self.input_name.text(),
                parent = self.selected_group)
            session.add(company)
            session.commit()
            self.msg = message_event(msg = 'Insert Successfully')
            self.msg.show()
            self.close()
        elif self.institute == 'department':
            department = Department(name = self.input_name.text(),
                parent = self.selected_company)
            session.add(department)
            session.commit()
            self.msg = message_event(msg = 'Insert Successfully')
            self.msg.show()
            self.close()

