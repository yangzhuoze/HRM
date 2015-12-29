# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\salary.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(628, 391)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_status = QtWidgets.QLabel(Dialog)
        self.label_status.setMinimumSize(QtCore.QSize(0, 31))
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_booker_data = QtWidgets.QLabel(Dialog)
        self.label_booker_data.setObjectName("label_booker_data")
        self.gridLayout_3.addWidget(self.label_booker_data, 1, 1, 1, 1)
        self.label_booker = QtWidgets.QLabel(Dialog)
        self.label_booker.setObjectName("label_booker")
        self.gridLayout_3.addWidget(self.label_booker, 1, 0, 1, 1)
        self.label_id_data = QtWidgets.QLabel(Dialog)
        self.label_id_data.setObjectName("label_id_data")
        self.gridLayout_3.addWidget(self.label_id_data, 0, 1, 1, 1)
        self.label_id = QtWidgets.QLabel(Dialog)
        self.label_id.setObjectName("label_id")
        self.gridLayout_3.addWidget(self.label_id, 0, 0, 1, 1)
        self.label_booktime = QtWidgets.QLabel(Dialog)
        self.label_booktime.setObjectName("label_booktime")
        self.gridLayout_3.addWidget(self.label_booktime, 1, 2, 1, 1)
        self.label_booktime_data = QtWidgets.QLabel(Dialog)
        self.label_booktime_data.setObjectName("label_booktime_data")
        self.gridLayout_3.addWidget(self.label_booktime_data, 1, 3, 1, 1)
        self.label_total = QtWidgets.QLabel(Dialog)
        self.label_total.setObjectName("label_total")
        self.gridLayout_3.addWidget(self.label_total, 0, 4, 1, 1)
        self.label_total_data = QtWidgets.QLabel(Dialog)
        self.label_total_data.setObjectName("label_total_data")
        self.gridLayout_3.addWidget(self.label_total_data, 0, 5, 1, 1)
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setObjectName("label_name")
        self.gridLayout_3.addWidget(self.label_name, 0, 2, 1, 1)
        self.label_name_data = QtWidgets.QLabel(Dialog)
        self.label_name_data.setObjectName("label_name_data")
        self.gridLayout_3.addWidget(self.label_name_data, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.table, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_status.setText(_translate("Dialog", "TextLabel"))
        self.label_booker_data.setText(_translate("Dialog", "TextLabel"))
        self.label_booker.setText(_translate("Dialog", "制定人"))
        self.label_id_data.setText(_translate("Dialog", "TextLabel"))
        self.label_id.setText(_translate("Dialog", "薪酬标准编号"))
        self.label_booktime.setText(_translate("Dialog", "登记时间"))
        self.label_booktime_data.setText(_translate("Dialog", "TextLabel"))
        self.label_total.setText(_translate("Dialog", "薪酬总额"))
        self.label_total_data.setText(_translate("Dialog", "TextLabel"))
        self.label_name.setText(_translate("Dialog", "薪酬标准名称"))
        self.label_name_data.setText(_translate("Dialog", "TextLabel"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "序号"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "薪酬项目名称"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "金额"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

