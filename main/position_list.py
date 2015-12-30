# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .position_create import position_create_event
from .position_update import position_update_event
from .Ui.Ui_position_list import Ui_Dialog


class position_list_event(QDialog, Ui_Dialog):
    
    position_create = None
    position_update = None
    
    def __init__(self, parent=None):
        super(position_list_event, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_button_position_create_clicked(self):
        self.position_create = position_create_event('position')
        self.position_create.show()
        self.close()
    
    @pyqtSlot()
    def on_button_positioncat_create_clicked(self):
        self.position_create = position_create_event('positioncat')
        self.position_create.show()
        self.close()
    
    @pyqtSlot()
    def on_button_positiontitle_create_clicked(self):
        self.position_create = position_create_event('positiontitle')
        self.position_create.show()
        self.close()
    
    @pyqtSlot()
    def on_button_position_update_clicked(self):
        self.position_update = position_update_event('position')
        self.position_update.show()
        self.close()
    
    @pyqtSlot()
    def on_button_positioncat_update_clicked(self):
        self.position_update = position_update_event('positioncat')
        self.position_update.show()
        self.close()
    
    @pyqtSlot()
    def on_button_positiontitle_update_clicked(self):
        self.position_update = position_update_event('positiontitle')
        self.position_update.show()
        self.close()
