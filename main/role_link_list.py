# -*- coding: utf-8 -*-
from functools import partial

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QAbstractItemView, QTableWidgetItem, \
    QPushButton

from .Models import session, Clerk
from .role_link import role_link_event
from .Ui.Ui_role_link_list import Ui_Dialog


class role_link_list_event(QDialog, Ui_Dialog):
    
    role_link = None
    
    def __init__(self, parent=None):
        super(role_link_list_event, self).__init__(parent)
        self.setupUi(self)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        clerks = session.query(Clerk).all()
        for i, clerk in enumerate(clerks):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(clerk.recordid))
            self.table.setItem(i, 1, QTableWidgetItem(clerk.name))
            self.table.setItem(i, 2, QTableWidgetItem(clerk.role.name))
            button = QPushButton(self.table)
            button.setText('角色变更')
            button.clicked.connect(partial(self.open_role_link, clerk))
            self.table.setCellWidget(i, 3, button)
            
    def open_role_link(self, clerk):
        self.role_link = role_link_event(clerk)
        self.role_link.show()
        self.close()
