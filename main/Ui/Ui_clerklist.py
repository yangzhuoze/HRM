# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\clerklist.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(828, 412)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_status = QtWidgets.QLabel(Dialog)
        self.label_status.setMinimumSize(QtCore.QSize(0, 31))
        self.label_status.setMaximumSize(QtCore.QSize(16777215, 31))
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 0, 0, 1, 2)
        self.label_total = QtWidgets.QLabel(Dialog)
        self.label_total.setMinimumSize(QtCore.QSize(0, 16))
        self.label_total.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label_total.setObjectName("label_total")
        self.gridLayout.addWidget(self.label_total, 1, 0, 1, 2)
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setObjectName("table")
        self.table.setColumnCount(8)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.table, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_status.setText(_translate("Dialog", "TextLabel"))
        self.label_total.setText(_translate("Dialog", "TextLabel"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "档案编号"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "姓名"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "性别"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "一级机构"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "二级机构"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "三级机构"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "职位名称"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "复核"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

