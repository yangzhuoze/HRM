# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView

from .Ui.Ui_salary import Ui_Dialog

class salary_query_event(QDialog, Ui_Dialog):
    def __init__(self, salary, parent=None):
        super(salary_query_event, self).__init__(parent)
        self.setupUi(self)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label_status.setText('你正在做的业务是：人力资源->薪酬标准管理->薪酬标准查询')
        self.label_id_data.setText((str)(salary.id))
        self.label_name_data.setText(salary.name)
        self.label_booker_data.setText(salary.booker)
        self.label_booktime_data.setText(salary.booktime.strftime('%Y-%m-%d'))
        totalcost = 0
        for i, item in enumerate(salary.item):
            totalcost = totalcost + item.cost
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem((str)(i + 1)))
            self.table.setItem(i, 1, QTableWidgetItem(item.item.name))
            self.table.setItem(i, 2, QTableWidgetItem((str)(item.cost)))
        self.label_total_data.setText((str)(totalcost))
