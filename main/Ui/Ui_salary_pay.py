# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\salary_pay.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(684, 487)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 31))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 2, 0, 1, 1)
        self.label_totalcost = QtWidgets.QLabel(Dialog)
        self.label_totalcost.setObjectName("label_totalcost")
        self.gridLayout.addWidget(self.label_totalcost, 4, 0, 1, 1)
        self.label_booktime = QtWidgets.QLabel(Dialog)
        self.label_booktime.setObjectName("label_booktime")
        self.gridLayout.addWidget(self.label_booktime, 5, 0, 1, 1)
        self.label_id = QtWidgets.QLabel(Dialog)
        self.label_id.setObjectName("label_id")
        self.gridLayout.addWidget(self.label_id, 1, 0, 1, 1)
        self.label_count = QtWidgets.QLabel(Dialog)
        self.label_count.setObjectName("label_count")
        self.gridLayout.addWidget(self.label_count, 3, 0, 1, 1)
        self.label_count_data = QtWidgets.QLabel(Dialog)
        self.label_count_data.setObjectName("label_count_data")
        self.gridLayout.addWidget(self.label_count_data, 3, 1, 1, 1)
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.table, 7, 0, 1, 2)
        self.label_booktime_data = QtWidgets.QLabel(Dialog)
        self.label_booktime_data.setObjectName("label_booktime_data")
        self.gridLayout.addWidget(self.label_booktime_data, 5, 1, 1, 1)
        self.label_id_data = QtWidgets.QLabel(Dialog)
        self.label_id_data.setMinimumSize(QtCore.QSize(561, 0))
        self.label_id_data.setObjectName("label_id_data")
        self.gridLayout.addWidget(self.label_id_data, 1, 1, 1, 1)
        self.label_name_data = QtWidgets.QLabel(Dialog)
        self.label_name_data.setObjectName("label_name_data")
        self.gridLayout.addWidget(self.label_name_data, 2, 1, 1, 1)
        self.label_totalcost_data = QtWidgets.QLabel(Dialog)
        self.label_totalcost_data.setObjectName("label_totalcost_data")
        self.gridLayout.addWidget(self.label_totalcost_data, 4, 1, 1, 1)
        self.button = QtWidgets.QPushButton(Dialog)
        self.button.setObjectName("button")
        self.gridLayout.addWidget(self.button, 8, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "你正在做的业务是：人力资源->薪酬发放管理->薪酬发放登记明细"))
        self.label_name.setText(_translate("Dialog", "薪酬标准名称："))
        self.label_totalcost.setText(_translate("Dialog", "薪酬总额："))
        self.label_booktime.setText(_translate("Dialog", "登记时间："))
        self.label_id.setText(_translate("Dialog", "薪酬发放单编号："))
        self.label_count.setText(_translate("Dialog", "总人数"))
        self.label_count_data.setText(_translate("Dialog", "TextLabel"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "档案编号"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "姓名"))
        self.label_booktime_data.setText(_translate("Dialog", "TextLabel"))
        self.label_id_data.setText(_translate("Dialog", "TextLabel"))
        self.label_name_data.setText(_translate("Dialog", "TextLabel"))
        self.label_totalcost_data.setText(_translate("Dialog", "TextLabel"))
        self.button.setText(_translate("Dialog", "提交"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

