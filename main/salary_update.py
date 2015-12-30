# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from .Models import session, SalaryItem, SalaryItemCost
from .message import message_event
from .Ui.Ui_salary_create import Ui_Dialog


class salary_update_event(QDialog, Ui_Dialog):
    
    salary = None
    msg = None
    
    def __init__(self, salary, parent=None):
        super(salary_update_event, self).__init__(parent)
        self.setupUi(self)
        self.salary = salary
        self.label_status.setText('你正在做的业务是：人力资源->薪酬标准管理->薪酬标准变更')
        items = session.query(SalaryItemCost).filter_by(salary = self.salary).all()
        self.input_name.setText(salary.name)
        self.input_name.setReadOnly(True)
        totalcost = 0
        for i, item in enumerate(items):
            totalcost = totalcost + item.cost
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(item.item.name))
            self.table.setItem(i, 1, QTableWidgetItem((str)(item.cost)))
        self.label_total_data.setText((str)(totalcost))
    
    @pyqtSlot()
    def on_button_submit_clicked(self):
        items = session.query(SalaryItemCost).filter_by(salary = self.salary).all()
        for item in items:
            session.delete(item)
        session.commit()
        for row in range(self.table.rowCount()):
            salaryitem = SalaryItem(name = self.table.item(row, 0).text())
            salaryitemcost = SalaryItemCost(salary = self.salary,
                item = salaryitem, cost = self.table.item(row, 1).text())
            session.add(salaryitemcost)
            session.commit()
        self.msg = message_event(msg = 'Update Successfully')
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
