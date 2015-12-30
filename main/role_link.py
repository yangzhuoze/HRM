# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QDialog

from .Models import session, Role
from .message import message_event
from .Ui.Ui_role_link import Ui_Dialog

class role_link_event(QDialog, Ui_Dialog):
    
    msg = None
    _translate = QCoreApplication.translate
    clerk = None
    roles = None
    selected_role = None
    
    def __init__(self, clerk, parent=None):
        super(role_link_event, self).__init__(parent)
        self.setupUi(self)
        self.clerk = clerk
        self.label_clerk_data.setText(clerk.name)
        self.roles = session.query(Role).order_by(Role.id).all()
        for role in self.roles:
            self.input_role.addItem("")
            self.input_role.setItemText(role.id - 1, 
                self._translate('Dialog', role.name))

    @pyqtSlot(int)
    def on_input_role_currentIndexChanged(self, index):
        role = self.roles[index]
        self.selected_role = role
    
    @pyqtSlot()
    def on_button_clicked(self):
        self.clerk.role = self.selected_role
        session.add(self.clerk)
        session.commit()
        self.msg = message_event(msg = 'Update Successfully')
        self.msg.show()
        self.close()
