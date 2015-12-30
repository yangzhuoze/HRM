# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QDialog

from .Models import session, PositionCat, Position, PositionTitle
from .message import message_event
from .Ui.Ui_position_detail import Ui_Dialog


class position_create_event(QDialog, Ui_Dialog):

    msg = None
    operation = None
    _translate = QCoreApplication.translate
    positioncats = None
    selected_positioncat = None
    
    def __init__(self, operation, parent=None):
        super(position_create_event, self).__init__(parent)
        self.setupUi(self)
        self.operation = operation
        self.positioncats = session.query(PositionCat).order_by(PositionCat.id).all()
        if operation == 'position':
            for positioncat in self.positioncats:
                self.input_positioncat.addItem("")
                self.input_positioncat.setItemText(positioncat.id - 1, 
                    self._translate('Dialog', positioncat.name))
        if operation == 'positioncat':
            self.label_positioncat.close()
            self.input_positioncat.close()
            self.label_position.close()
            self.input_position.close()
            self.label_positiontitle.close()
            self.input_positiontitle.close()
            self.label_name.setText('请输入要登记的职位分类名称：')
        elif operation == 'position':
            self.label_position.close()
            self.input_position.close()
            self.label_positiontitle.close()
            self.input_positiontitle.close()
            self.label_positioncat.setText('请选择职位分类：')
            self.label_name.setText('请输入要登记的职位名称：')
        elif operation == 'positiontitle':
            self.label_positioncat.close()
            self.input_positioncat.close()
            self.label_position.close()
            self.input_position.close()
            self.label_positiontitle.close()
            self.input_positiontitle.close()
            self.label_name.setText('请输入要登记的职称名称')
    
    @pyqtSlot(int)
    def on_input_positioncat_currentIndexChanged(self, index):
        positioncat = self.positioncats[index]
        self.selected_positioncat = positioncat
        
    @pyqtSlot()
    def on_button_clicked(self):
        if self.operation == 'positioncat':
            positioncat = PositionCat(name = self.input_name.text())
            session.add(positioncat)
        elif self.operation == 'position':
            position = Position(name = self.input_name.text(),
                category = self.selected_positioncat)
            session.add(position)
        elif self.operation == 'positiontitle':
            positiontitle = PositionTitle(name = self.input_name.text())
            session.add(positiontitle)
        session.commit()
        self.msg = message_event(msg = 'Insert Successfully')
        self.msg.show()
        self.close()
