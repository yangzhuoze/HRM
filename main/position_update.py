# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QDialog

from .Models import session, PositionCat, PositionTitle
from .message import message_event
from .Ui.Ui_position_detail import Ui_Dialog

class position_update_event(QDialog, Ui_Dialog):
    
    msg = None
    operation = None
    _translate = QCoreApplication.translate
    positioncats = None
    positions = None
    positiontitles = None
    selected_positioncat = None
    
    def __init__(self, operation, parent=None):
        super(position_update_event, self).__init__(parent)
        self.setupUi(self)
        self.operation = operation
        self.positioncats = session.query(PositionCat).order_by(PositionCat.id).all()
        self.positiontitles = session.query(PositionTitle).order_by(PositionTitle.id).all()
        if operation != 'positiontitle':
            for positioncat in self.positioncats:
                self.input_positioncat.addItem("")
                self.input_positioncat.setItemText(positioncat.id - 1, 
                    self._translate('Dialog', positioncat.name))
        else:
            for positiontitle in self.positiontitles:
                self.input_positiontitle.addItem("")
                self.input_positiontitle.setItemText(positiontitle.id - 1, 
                    self._translate('Dialog', positiontitle.name))
        if operation == 'positioncat':
            self.label_position.close()
            self.input_position.close()
            self.label_positiontitle.close()
            self.input_positiontitle.close()
            self.label_positioncat.setText('请选择要修改的职位分类：')
            self.label_name.setText('请输入新的职位分类名称：')
        elif operation == 'position':
            self.label_positiontitle.close()
            self.input_positiontitle.close()
            self.label_positioncat.setText('请选择职位分类：')
            self.label_position.setText('请选择要修改的职位：')
            self.label_name.setText('请输入新的职位名称：')
        elif operation == 'positiontitle':
            self.label_positioncat.close()
            self.input_positioncat.close()
            self.label_position.close()
            self.input_position.close()
            self.label_positiontitle.setText('请选择要修改的职称：')
            self.label_name.setText('请输入新的职称名称：')
    
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
                
    @pyqtSlot(int)
    def on_input_positiontitle_currentIndexChanged(self, index):
        positiontitle = self.positiontitles[index]
        self.selected_positiontitle = positiontitle
    
    @pyqtSlot()
    def on_button_clicked(self):
        if self.operation == 'positioncat':
            self.selected_positioncat.name = self.input_name.text()
            session.add(self.selected_positioncat)
        elif self.operation == 'position':
            self.selected_position.name = self.input_name.text()
            session.add(self.selected_position)
        elif self.operation == 'positiontitle':
            self.selected_positiontitle.name = self.input_name.text()
            session.add(self.selected_positiontitle)
        session.commit()
        self.msg = message_event(msg = 'Update Successfully')
        self.msg.show()
        self.close()

