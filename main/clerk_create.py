# -*- coding: utf-8 -*-

from datetime import datetime

from PyQt5.QtCore import pyqtSlot, QCoreApplication, QDate
from PyQt5.QtWidgets import QDialog

from . import session
from .Models import Group, Clerk, PositionCat, PositionTitle, Salary
from .message import message_event
from .Ui.Ui_clerkdetail import Ui_Dialog

import currentApp

class clerk_create_event(QDialog, Ui_Dialog):
    
    msg = None
    _translate = QCoreApplication.translate
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
    
    salaries = session.query(Salary).order_by(Salary.id).all()
    selected_salary = None
    
    def __init__(self, parent=None):
        super(clerk_create_event, self).__init__(parent)
        self.setupUi(self)
        self.label_booktime_data.setText((str)(datetime.now())[:19])
        self.label_booker_data.setText(currentApp.getCurrentUser().name)
        for group in self.groups:
            self.input_group.addItem("")
            self.input_group.setItemText(group.id - 1, 
                self._translate('Dialog', group.name))
        for positioncat in self.positioncats:
            self.input_positioncat.addItem("")
            self.input_positioncat.setItemText(positioncat.id - 1, 
                self._translate('Dialog', positioncat.name))
        for positiontitle in self.positiontitles:
            self.input_positiontitle.addItem("")
            self.input_positiontitle.setItemText(positiontitle.id - 1, 
                self._translate('Dialog', positiontitle.name))
        for salary in self.salaries:
            self.input_salary.addItem("")
            self.input_salary.setItemText(salary.id - 1, 
                self._translate('Dialog', salary.name))
    
    @pyqtSlot(QDate)
    def on_input_birthday_dateChanged(self, date):
        currentYear = QDate.currentDate().year()
        birthYear = date.year()
        age = (str)(currentYear - birthYear)
        self.label_age_data.setText(age)

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

    @pyqtSlot(int)
    def on_input_positiontitle_currentIndexChanged(self, index):
        self.selected_positiontitle = self.positiontitles[index]

    @pyqtSlot(int)
    def on_input_salary_currentIndexChanged(self, index):
        self.selected_salary = self.salaries[index]

    @pyqtSlot()
    def on_button_submit_clicked(self):
        clerk = Clerk(group = self.selected_group,
            company = self.selected_company,
            department = self.selected_department,
            position = self.selected_position,
            positiontitle = self.selected_positiontitle,
            salary = self.selected_salary,
            name = self.input_name.text(), 
            gender = self.input_gender.currentText(),
            email = self.input_email.text(), 
            phone = self.input_phone.text(),
            qq = self.input_qq.text(), 
            mobilephone = self.input_mobilephone.text(),
            address = self.input_address.text(),
            postcode = self.input_postcode.text(),
            nation = self.input_nation.currentText(),
            birthplace = self.input_birthplace.text(),
            birthday = self.input_birthday.text(),
            ethnicity = self.input_ethnicity.currentText(),
            faith = self.input_faith.currentText(),
            politicalstatus = self.input_politicalstatus.currentText(),
            identification = self.input_identification.text(),
            socialsecurity = self.input_socialsecurity.text(),
            education = self.input_education.currentText(), 
            educationtime = self.input_educationtime.currentText(),
            major = self.input_major.text(), 
            openingbank = self.input_openingbank.text(),
            account = self.input_account.text(), 
            speciality = self.input_speciality.text(),
            hobby = self.input_hobby.text(), 
            vitae = self.input_vitae.toPlainText(),
            relationship = self.input_relationship.toPlainText(), 
            remarks = self.input_remarks.toPlainText())
        clerk.recordid = '%s%02d%02d%02d%02d' % (datetime.now().strftime('%Y'),
            self.selected_group.id, self.selected_company.id, 
            self.selected_department.id, clerk.id)
        session.add(clerk)
        session.commit()
        self.msg = message_event(msg = 'Insert Successfully')
        self.msg.show()
        self.close()
    
    @pyqtSlot()
    def on_button_clear_clicked(self):
        self.close()
