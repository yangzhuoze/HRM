# -*- coding: utf-8 -*-
from functools import partial

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView, \
    QPushButton

from .Models import session, Salary
from .salary_update import salary_update_event
from .Ui.Ui_salarylist import Ui_Dialog


class salary_update_list_event(QDialog, Ui_Dialog):
    
    salary_update = None
    
    def __init__(self, parent=None):
        super(salary_update_list_event, self).__init__(parent)
        self.setupUi(self)
        self.label_status.setText('你正在做的业务是：人力资源->薪酬标准管理->薪酬标准更改')
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        salaries = session.query(Salary).all()
        for i, salary in enumerate(salaries):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem((str)(salary.id)))
            self.table.setItem(i, 1, QTableWidgetItem(salary.name))
            totalcost = 0
            for item in salary.item:
                totalcost = totalcost + item.cost
            self.table.setItem(i, 2, QTableWidgetItem((str)(totalcost)))
            button = QPushButton(self.table)
            button.setText('查看明细')
            button.clicked.connect(partial(self.open_salary_update, salary))
            self.table.setCellWidget(i, 3, button)
            
    def open_salary_update(self, salary):
        self.salary_update = salary_update_event(salary)
        self.salary_update.show()
