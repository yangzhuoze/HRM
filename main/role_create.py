# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Models import session, Role
from .message import message_event
from .Ui.Ui_permission import Ui_Dialog

from config import Permission

class role_create_event(QDialog, Ui_Dialog):
    
    msg = None
    permissions = 0x0000
    role = None
    update = False
    
    def __init__(self, role = None, update = False, parent=None):
        super(role_create_event, self).__init__(parent)
        self.setupUi(self)
        self.update = update
        if role != None:
            self.role = role
            self.input_name.setText(role.name)
            self.check_HUMAN_QUERY.setChecked(role.permission &
                Permission.HUMAN_QUERY == Permission.HUMAN_QUERY)
            self.check_HUMAN_CREATE.setChecked(role.permission &
                Permission.HUMAN_CREATE == Permission.HUMAN_CREATE)
            self.check_HUMAN_UPDATE.setChecked(role.permission &
                Permission.HUMAN_UPDATE == Permission.HUMAN_UPDATE)
            self.check_HUMAN_COMFIRM.setChecked(role.permission &
                Permission.HUMAN_COMFIRM == Permission.HUMAN_COMFIRM)
            self.check_HUMAN_DELETE.setChecked(role.permission &
                Permission.HUMAN_DELETE == Permission.HUMAN_DELETE)
            self.check_INSTITUTE_QUERY.setChecked(role.permission &
                Permission.INSTITUTE_QUERY == Permission.INSTITUTE_QUERY)
            self.check_INSTITUTE_CREATE.setChecked(role.permission &
                Permission.INSTITUTE_CREATE == Permission.INSTITUTE_CREATE)
            self.check_INSTITUTE_UPDATE.setChecked(role.permission &
                Permission.INSTITUTE_UPDATE == Permission.INSTITUTE_UPDATE)
            self.check_INSTITUTE_CONFIRM.setChecked(role.permission &
                Permission.INSTITUTE_CONFIRM == Permission.INSTITUTE_CONFIRM)
            self.check_INSTITUTE_DELETE.setChecked(role.permission &
                Permission.INSTITUTE_DELETE == Permission.INSTITUTE_DELETE)
            self.check_SALARY_QUERY.setChecked(role.permission &
                Permission.SALARY_QUERY == Permission.SALARY_QUERY)
            self.check_SALARY_CREATE.setChecked(role.permission &
                Permission.SALARY_CREATE == Permission.SALARY_CREATE)
            self.check_SALARY_UPDATE.setChecked(role.permission &
                Permission.SALARY_UPDATE == Permission.SALARY_UPDATE)
            self.check_SALARY_CONFIRM.setChecked(role.permission &
                Permission.SALARY_CONFIRM == Permission.SALARY_CONFIRM)
            self.check_SALARY_DELETE.setChecked(role.permission &
                Permission.SALARY_DELETE == Permission.SALARY_DELETE)
            self.check_POSITION_QUERY.setChecked(role.permission &
                Permission.POSITION_QUERY == Permission.POSITION_QUERY)
            self.check_POSITION_CREATE.setChecked(role.permission &
                Permission.POSITION_CREATE == Permission.POSITION_CREATE)
            self.check_POSITION_UPDATE.setChecked(role.permission &
                Permission.POSITION_UPDATE == Permission.POSITION_UPDATE)
            self.check_POSITION_CONFIRM.setChecked(role.permission &
                Permission.POSITION_CONFIRM == Permission.POSITION_CONFIRM)
            self.check_POSITION_DELETE.setChecked(role.permission &
                Permission.POSITION_DELETE == Permission.POSITION_DELETE)

    @pyqtSlot()
    def on_button_clicked(self):
        if self.check_HUMAN_QUERY.isChecked():
            self.permissions = self.permissions | Permission.HUMAN_QUERY
        if self.check_HUMAN_CREATE.isChecked():
            self.permissions = self.permissions | Permission.HUMAN_CREATE
        if self.check_HUMAN_UPDATE.isChecked():
            self.permissions = self.permissions | Permission.HUMAN_UPDATE
        if self.check_HUMAN_COMFIRM.isChecked():
            self.permissions = self.permissions | Permission.HUMAN_COMFIRM
        if self.check_HUMAN_DELETE.isChecked():
            self.permissions = self.permissions | Permission.HUMAN_DELETE
        if self.check_INSTITUTE_QUERY.isChecked():
            self.permissions = self.permissions | Permission.INSTITUTE_QUERY
        if self.check_INSTITUTE_CREATE.isChecked():
            self.permissions = self.permissions | Permission.INSTITUTE_CREATE
        if self.check_INSTITUTE_UPDATE.isChecked():
            self.permissions = self.permissions | Permission.INSTITUTE_UPDATE
        if self.check_INSTITUTE_CONFIRM.isChecked():
            self.permissions = self.permissions | Permission.INSTITUTE_CONFIRM
        if self.check_INSTITUTE_DELETE.isChecked():
            self.permissions = self.permissions | Permission.INSTITUTE_DELETE
        if self.check_SALARY_QUERY.isChecked():
            self.permissions = self.permissions | Permission.SALARY_QUERY
        if self.check_SALARY_CREATE.isChecked():
            self.permissions = self.permissions | Permission.SALARY_CREATE
        if self.check_SALARY_UPDATE.isChecked():
            self.permissions = self.permissions | Permission.SALARY_UPDATE
        if self.check_SALARY_CONFIRM.isChecked():
            self.permissions = self.permissions | Permission.SALARY_CONFIRM
        if self.check_SALARY_DELETE.isChecked():
            self.permissions = self.permissions | Permission.SALARY_DELETE
        if self.check_POSITION_QUERY.isChecked():
            self.permissions = self.permissions | Permission.POSITION_QUERY
        if self.check_POSITION_CREATE.isChecked():
            self.permissions = self.permissions | Permission.POSITION_CREATE
        if self.check_POSITION_UPDATE.isChecked():
            self.permissions = self.permissions | Permission.POSITION_UPDATE
        if self.check_POSITION_CONFIRM.isChecked():
            self.permissions = self.permissions | Permission.POSITION_CONFIRM
        if self.check_POSITION_DELETE.isChecked():
            self.permissions = self.permissions | Permission.POSITION_DELETE
        if self.update == False:
            role = Role(name = self.input_name.text(), permission = self.permissions)
            session.add(role)
            session.commit()
            self.msg = message_event(msg = 'Insert Successfully')
            self.msg.show()
            self.close()
        else:
            self.role.name = self.input_name.text()
            self.role.permission = self.permissions
            session.add(self.role)
            session.commit()
            self.msg = message_event(msg = 'Update Successfully')
            self.msg.show()
            self.close()
