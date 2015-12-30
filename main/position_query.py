# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from .Models import session, PositionCat
from .Ui.Ui_position_query import Ui_Dialog


class position_query_event(QDialog, Ui_Dialog):
    
    positioncats = None
    positions = None
    
    def __init__(self, parent=None):
        super(position_query_event, self).__init__(parent)
        self.setupUi(self)
        self.positioncats = session.query(PositionCat).order_by(PositionCat.id).all()
        self.table_positioncat.setColumnWidth(1, 200)
        self.table_position.setColumnWidth(1, 200)
        if self.positioncats is not None:
            for i, positioncat in enumerate(self.positioncats):
                self.table_positioncat.insertRow(i)
                self.table_positioncat.setItem(i, 0, QTableWidgetItem((str)(i + 1)))
                self.table_positioncat.setItem(i, 1, QTableWidgetItem(positioncat.name))
    
    @pyqtSlot(int, int)
    def on_table_positioncat_cellClicked(self, row, column):
        for rows in range(self.table_position.rowCount()):
            self.table_position.removeRow(0)
        positioncat = self.positioncats[row]
        self.positions = positioncat.position
        if self.positions is not None:
            for i, position in enumerate(self.positions):
                self.table_position.insertRow(i)
                self.table_position.setItem(i, 0, QTableWidgetItem((str)(i + 1)))
                self.table_position.setItem(i, 1, QTableWidgetItem(position.name))
    
    @pyqtSlot()
    def on_button_clicked(self):
        self.close()
