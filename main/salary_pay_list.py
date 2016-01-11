# -*- coding: utf-8 -*-
from functools import partial

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QPushButton

from .Models import session, Salary
from .salary_pay import salary_pay_event
from .Ui.Ui_salary_pay_list import Ui_Dialog


class salary_pay_list_event(QDialog, Ui_Dialog):
    
    salaries = None
    salary_pay = None
    
    def __init__(self, parent=None):
        super(salary_pay_list_event, self).__init__(parent)
        self.setupUi(self)
        self.salaries = session.query(Salary).filter_by(paied = 0).all()
        for i, salary in enumerate(self.salaries):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem((str)(i + 1)))
            self.table.setItem(i, 1, QTableWidgetItem(salary.name))
            count = 0
            for clerk in salary.clerks:
                count = count + 1
            self.table.setItem(i, 2, QTableWidgetItem((str)(count)))
            totalcost = 0
            for item in salary.item:
                totalcost = totalcost + item.cost
            self.table.setItem(i, 3, QTableWidgetItem((str)(totalcost)))
            button = QPushButton(self.table)
            button.setText('登记')
            button.clicked.connect(partial(self.open_salary_pay, salary, count, totalcost))
            self.table.setCellWidget(i, 4, button)
            
    def open_salary_pay(self, salary, count, totalcost):
        self.salary_pay = salary_pay_event(salary, count, totalcost)
        self.salary_pay.show()
        self.close()
