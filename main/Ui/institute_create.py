# -*- coding: utf-8 -*-

"""
Module implementing institute_create_event.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_institute_create import Ui_Dialog


class institute_create_event(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(institute_create_event, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_button_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
