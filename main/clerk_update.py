# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Models import session
from .message import message_event
from .Ui.Ui_clerkdetail import Ui_Dialog


class clerk_update_event(QDialog, Ui_Dialog):
    
    clerk = None
    msg = None
    
    def __init__(self, clerk, parent=None):
        self.clerk = clerk
        super(clerk_update_event, self).__init__(parent)
        self.setupUi(self)
        self.label_status.setText('你正在做的业务是：人力资源->人力资源档案管理->人力资源档案变更')
        self.input_group.addItem(clerk.group.name)
        self.input_company.addItem(clerk.company.name)
        self.input_department.addItem(clerk.department.name)
        self.input_positioncat.addItem(clerk.position.category.name)
        self.input_position.addItem(clerk.position.name)
        self.input_positiontitle.addItem(clerk.positiontitle.name)
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
        self.clerk.name = self.input_name.text()
        self.clerk.gender = self.input_gender.currentText()
        self.clerk.email = self.input_email.text()
        self.clerk.phone = self.input_phone.text()
        self.clerk.qq = self.input_qq.text()
        self.clerk.mobilephone = self.input_mobilephone.text()
        self.clerk.address = self.input_address.text()
        self.clerk.postcode = self.input_postcode.text()
        self.clerk.nation = self.input_nation.currentText()
        self.clerk.birthplace = self.input_birthplace.text()
        self.clerk.birthday = self.input_birthday.text()
        self.clerk.ethnicity = self.input_ethnicity.currentText()
        self.clerk.faith = self.input_faith.currentText()
        self.clerk.politicalstatus = self.input_politicalstatus.currentText()
        self.clerk.identification = self.input_identification.text()
        self.clerk.socialsecurity = self.input_socialsecurity.text()
        self.clerk.education = self.input_education.currentText()
        self.clerk.educationtime = self.input_educationtime.currentText()
        self.clerk.major = self.input_major.text()
        self.clerk.openingbank = self.input_openingbank.text()
        self.clerk.account = self.input_account.text()
        self.clerk.speciality = self.input_speciality.text()
        self.clerk.hobby = self.input_hobby.text()
        self.clerk.vitae = self.input_vitae.toPlainText()
        self.clerk.relationship = self.input_relationship.toPlainText()
        self.clerk.remarks = self.input_remarks.toPlainText()
        session.add(self.clerk)
        session.commit()
        self.msg = message_event(msg = 'Update Successfully')
        self.msg.show()
        self.close()
        
    @pyqtSlot()
    def on_button_clear_clicked(self):
        self.close()
