# -*- coding: utf-8 -*-
from functools import partial

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView, \
    QPushButton

from .Models import session, Salary
from .salary_query import salary_query_event
from .Ui.Ui_salarylist import Ui_Dialog

class salary_query_list_event(QDialog, Ui_Dialog):
    
    salary_query = None
    
    def __init__(self, parent=None):
        super(salary_query_list_event, self).__init__(parent)
        self.setupUi(self)
        self.label_status.setText('你正在做的业务是：人力资源->薪酬标准管理->薪酬标准查询')
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
            button.clicked.connect(partial(self.open_salary_query, salary))
            self.table.setCellWidget(i, 3, button)
        
    def open_salary_query(self, salary):
        self.salary_query = salary_query_event(salary)
        self.salary_query.show()
