# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from .Models import session, Salary, SalaryItem, SalaryItemCost
from .message import message_event
from .Ui.Ui_salary_create import Ui_Dialog

import currentApp

class salary_create_event(QDialog, Ui_Dialog):
    
    item = None
    msg = None
    
    def __init__(self, parent=None):
        super(salary_create_event, self).__init__(parent)
        self.setupUi(self)
        self.label_status.setText('你正在做的业务是：人力资源->薪酬标准管理->薪酬标准登记')
        session.query(SalaryItem).all()
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(0, 0, QTableWidgetItem('基本工资'))
    
    @pyqtSlot()
    def on_button_submit_clicked(self):
        salary = Salary(name = self.input_name.text(),
            booker = currentApp.getCurrentUser().name)
        for row in range(self.table.rowCount()):
            salaryitem = SalaryItem(name = self.table.item(row, 0).text())
            salaryitemcost = SalaryItemCost(salary = salary,
                item = salaryitem, cost = self.table.item(row, 1).text())
            session.add(salaryitemcost)
            session.commit()
        self.msg = message_event(msg = 'Insert Successfully')
        self.msg.show()
        self.close()
    
    @pyqtSlot()
    def on_button_create_clicked(self):
        self.table.insertRow(self.table.rowCount())
    
    @pyqtSlot()
    def on_button_delete_clicked(self):
        self.table.removeRow(self.table.currentRow())

    @pyqtSlot(int, int)
    def on_table_cellChanged(self, row, column):
        total = 0
        for i in range(self.table.rowCount()):
            self.item = self.table.item(i, 1)
            if self.item is not None:
                total = (int)(self.item.text()) + total
        self.label_total_data.setText((str)(total))
