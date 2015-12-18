# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_update import Ui_Dialog
from datetime import date


class Ui_update(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Ui_update, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_button_submit_clicked(self):
        pass
    
    @pyqtSlot()
    def on_button_clear_clicked(self):
        pass
    
    @pyqtSlot(int)
    def on_input_company_currentIndexChanged(self, index):
        pass
    
    @pyqtSlot(int)
    def on_input_positioncat_currentIndexChanged(self, index):
        pass
    
    @pyqtSlot(int)
    def on_input_group_currentIndexChanged(self, index):
        pass
    
    @pyqtSlot(date)
    def on_input_birthday_dateChanged(self, date):
        self.label_age_data.setText = '2222'

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = Ui_update()
    dialog.show()
    sys.exit(app.exec_())
