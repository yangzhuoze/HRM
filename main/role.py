# -*- coding: utf-8 -*-
from functools import partial

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QPushButton

from .Models import session, Role
from .role_create import role_create_event
from .Ui.Ui_role import Ui_Dialog

class role_event(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(role_event, self).__init__(parent)
        self.setupUi(self)
        roles = session.query(Role).order_by(Role.id).all()
        for i, role in enumerate(roles):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem((str)(role.id)))
            self.table.setItem(i, 1, QTableWidgetItem(role.name))
            button = QPushButton(self.table)
            button.setText('权限变更')
            button.clicked.connect(partial(self.open_role_update, role))
            self.table.setCellWidget(i, 2, button)
            
    def open_role_update(self, role):
        self.role_create = role_create_event(role, True)
        self.role_create.show()
    
    @pyqtSlot()
    def on_button_clicked(self):
        self.role_create = role_create_event()
        self.role_create.show()
        self.close()
