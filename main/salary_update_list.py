# -*- coding: utf-8 -*-

"""
Module implementing salary_update_list_event.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_salarylist import Ui_Dialog


class salary_update_list_event(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(salary_update_list_event, self).__init__(parent)
        self.setupUi(self)
