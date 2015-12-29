# -*- coding: utf-8 -*-

from functools import partial
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QDialog, QPushButton, QAbstractItemView, \
    QTableWidgetItem

from .Ui.Ui_clerklist import Ui_Dialog
from .Models import session, Clerk
from .clerk_query import clerk_query_event


class clerk_query_list_event(QDialog, Ui_Dialog):
    
    button_filter = None
    _translate = QCoreApplication.translate
    clerk_query = None
    clerk_query_filter = None
    
    def __init__(self, clerks = None, parent=None):
        super(clerk_query_list_event, self).__init__(parent)
        self.setupUi(self)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        if clerks == None:
            clerks = session.query(Clerk).all()
        self.label_status.setText('你正在做的业务是：人力资源->人力资源档案管理->人力资源档案登记查询')
        self.label_total.setText('人力资源档案总数：%s例' % len(clerks))
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
            button.setText('查看明细')
            button.clicked.connect(partial(self.open_clerk_query, clerk))
            self.table.setCellWidget(i, 7, button)
            
    def open_clerk_query(self, clerk):
        self.clerk_query = clerk_query_event(clerk)
        self.clerk_query.show()

    @pyqtSlot()
    def on_button_filter_clicked(self):
        from .clerk_query_filter import clerk_query_filter_event
        self.clerk_query_filter = clerk_query_filter_event()
        self.clerk_query_filter.show()
        self.close()
