# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QDialog

from .Models import session, PositionCat
from .message import message_event
from .Ui.Ui_position_detail import Ui_Dialog

class position_update_event(QDialog, Ui_Dialog):
    
    msg = None
    operation = None
    _translate = QCoreApplication.translate
    positioncats = None
    positions = None
    selected_positioncat = None
    selected_company = None
    selected_department = None
    
    def __init__(self, operation, parent=None):
        super(position_update_event, self).__init__(parent)
        self.setupUi(self)
        self.operation = operation
        self.positioncats = session.query(PositionCat).order_by(PositionCat.id).all()
        for positioncat in self.positioncats:
            self.input_positioncat.addItem("")
            self.input_positioncat.setItemText(positioncat.id - 1, 
                self._translate('Dialog', positioncat.name))
        if operation == 'positioncat':
            self.label_position.close()
            self.input_position.close()
            self.label_positioncat.setText('请选择职位分类：')
            self.label_name.setText('请选择要修改的职位分类名称：')
            self.label_name.setText('请输入新的职位分类名称：')
        elif operation == 'position':
            self.label_positioncat.setText('请选择职位分类：')
            self.label_position.setText('请选择要职位：')
            self.label_name.setText('请输入新的职位名称：')
    
    @pyqtSlot(int)
    def on_input_positioncat_currentIndexChanged(self, index):
        positioncat = self.positioncats[index]
        self.selected_positioncat = positioncat
        if self.operation != 'positioncat':
            self.input_position.clear()
            self.selected_position = None
            self.positions = positioncat.position
            for i, position in enumerate(self.positions):
                self.input_position.addItem("")
                self.input_position.setItemText(i, self._translate('Dialog', position.name))
    
    @pyqtSlot(str)
    def on_input_position_currentTextChanged(self, p0):
        for position in self.positions:
            if p0 == position.name:
                self.selected_position = position
    
    @pyqtSlot()
    def on_button_clicked(self):
        if self.operation == 'positioncat':
            self.selected_positioncat.name = self.input_name.text()
            session.add(self.selected_positioncat)
        elif self.operation == 'position':
            self.selected_position.name = self.input_name.text()
            session.add(self.selected_position)
        session.commit()
        self.msg = message_event(msg = 'Update Successfully')
        self.msg.show()
        self.close()

