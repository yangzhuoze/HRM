# -*- coding: utf-8 -*-
from datetime import datetime

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from .Models import session
from .message import message_event
from .Ui.Ui_salary_pay import Ui_Dialog


class salary_pay_event(QDialog, Ui_Dialog):
    
    salary = None
    msg = None
    
    def __init__(self, salary, count, totalcost, parent=None):
        super(salary_pay_event, self).__init__(parent)
        self.setupUi(self)
        self.salary = salary
        self.label_id_data.setText((str)(salary.id))
        self.label_name_data.setText(salary.name)
        self.label_count_data.setText((str)(count))
        self.label_totalcost_data.setText((str)(totalcost))
        self.label_booktime_data.setText(datetime.now().strftime('%Y-%m-%d'))
        for i, item in enumerate(salary.item):
            self.table.insertColumn(i + 2)
            self.table.setHorizontalHeaderItem(i + 2, QTableWidgetItem(item.item.name))
        for i, clerk in enumerate(salary.clerks):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem((str)(clerk.id)))
            self.table.setItem(i, 1, QTableWidgetItem(clerk.name))
            for j, item in enumerate(salary.item):
                self.table.setItem(i, j + 2, QTableWidgetItem((str)(item.cost)))
    
    @pyqtSlot()
    def on_button_clicked(self):
        self.salary.paied = 1
        session.add(self.salary)
        session.commit()
        self.msg = message_event(msg = 'Update Successfully')
        self.msg.show()
        self.close()
