# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QLabel

from .Ui.Ui_clerkdetail import Ui_Dialog


class clerk_confirm_event(QDialog, Ui_Dialog):
    def __init__(self, clerk, parent=None):
        super(clerk_confirm_event, self).__init__(parent)
        self.setupUi(self)
        self.input_group.setCurrentText(clerk.group.name)
        self.input_company.setCurrentText(clerk.company.name)
        self.input_department.setCurrentText(clerk.department.name)
        self.input_positioncat.setCurrentText(clerk.position.category.name)
        self.input_position.setCurrentText(clerk.position.name)
        self.input_positiontitle.setCurrentText(clerk.positiontitle.name)
        self.input_name.setText(clerk.name)
        self.input_gender.setCurrentText(clerk.gender)
        self.input_email.setText(clerk.email)
        self.input_phone.setText(clerk.phone)
        self.input_qq.setText(clerk.qq)
        self.input_mobilephone.setText(clerk.mobilephone)
        self.input_address.setText(clerk.address)
        self.input_postcode.setText(clerk.postcode)
        self.input_nation.setCurrentText(clerk.nation)
        self.input_birthplace.setText(clerk.birthplace)
        self.input_birthday.setDate(clerk.birthday)
        self.input_ethnicity.setCurrentText(clerk.ethnicity)
        self.input_faith.setCurrentText(clerk.faith)
        self.input_politicalstatus.setCurrentText(clerk.politicalstatus)
        self.input_identification.setText(clerk.identification)
        self.input_socialsecurity.setText(clerk.socialsecurity)
        self.input_education.setCurrentText(clerk.education)
        self.input_educationtime.setCurrentText(clerk.educationtime)
        self.input_major.setText(clerk.major)
        self.input_openingbank.setText(clerk.openingbank)
        self.input_account.setText(clerk.account)
        self.input_speciality.setText(clerk.speciality)
        self.input_hobby.setText(clerk.hobby)
        self.input_vitae.setText(clerk.vitae)
        self.input_relationship.setText(clerk.relationship)
        self.input_remarks.setText(clerk.remarks)
    
    @pyqtSlot()
    def on_button_submit_clicked(self):
        pass
    
    @pyqtSlot()
    def on_button_clear_clicked(self):
        pass
