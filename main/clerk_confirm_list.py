# -*- coding: utf-8 -*-

from functools import partial
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QPushButton, QAbstractItemView, \
    QTableWidgetItem

from .Ui.Ui_clerklist import Ui_Dialog
from .Models import session, Clerk
from .clerk_confirm import clerk_confirm_event

class clerk_confirm_list_event(QDialog, Ui_Dialog):
    
    def __init__(self, parent=None):
        super(clerk_confirm_list_event, self).__init__(parent)
        self.setupUi(self)
        self.button_filter.close()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        clerks = session.query(Clerk).filter_by(confirm = 0).\
            order_by(Clerk.id).all()
        self.label_status.setText('你正在做的业务是：人力资源->人力资源档案管理->人力资源档案登记复核')
        self.label_total.setText('当前等待复核的人力资源档案总数：%s例' % len(clerks))
        for i, clerk in enumerate(clerks):
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
            button.clicked.connect(partial(self.open_clerk_confirm, clerk))
            self.table.setCellWidget(i, 7, button)

    def open_clerk_confirm(self, clerk):
        self.clerk_confirm = clerk_confirm_event(clerk)
        self.clerk_confirm.show()
        self.close()
