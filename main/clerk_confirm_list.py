# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QPushButton, QAbstractItemView, \
    QTableWidgetItem

from .Ui.Ui_clerklist import Ui_Dialog
from .Models import session, Clerk
from .clerk_confirm import clerk_confirm_event

class clerk_confirm_list_event(QDialog, Ui_Dialog):
    
    clerks = session.query(Clerk).filter_by(confirm = 0).\
        order_by(Clerk.id).all()
    
    def __init__(self, parent=None):
        super(clerk_confirm_list_event, self).__init__(parent)
        self.setupUi(self)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i, clerk in enumerate(self.clerks):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(clerk.recordid))
            self.table.setItem(i, 1, QTableWidgetItem(clerk.name))
            self.table.setItem(i, 2, QTableWidgetItem(clerk.gender))
            self.table.setItem(i, 3, QTableWidgetItem(clerk.group.name))
            self.table.setItem(i, 4, QTableWidgetItem(clerk.company.name))
            self.table.setItem(i, 5, QTableWidgetItem(clerk.department.name))
            self.table.setItem(i, 6, QTableWidgetItem(clerk.position.name))
            button = QPushButton(self.table)
            button.setText('复核')
            button.clicked.connect(lambda: self.open_clerk_confirm(clerk))
            self.table.setCellWidget(i, 7, button)

    def open_clerk_confirm(self, clerk):
        self.clerk_confirm = clerk_confirm_event(clerk)
        self.clerk_confirm.show()
