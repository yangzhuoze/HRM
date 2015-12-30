# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\role_link_list.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(509, 407)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 31))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setObjectName("table")
        self.table.setColumnCount(4)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.table, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "你正在做的业务是：人力资源->权限管理->权限关联"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "档案编号"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "姓名"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "权限角色"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "修改权限"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

