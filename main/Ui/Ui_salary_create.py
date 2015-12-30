# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\salary_create.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(627, 392)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_delete = QtWidgets.QPushButton(Dialog)
        self.button_delete.setObjectName("button_delete")
        self.gridLayout_2.addWidget(self.button_delete, 7, 4, 1, 1)
        self.label_status = QtWidgets.QLabel(Dialog)
        self.label_status.setMinimumSize(QtCore.QSize(0, 31))
        self.label_status.setObjectName("label_status")
        self.gridLayout_2.addWidget(self.label_status, 1, 2, 1, 3)
        self.button_submit = QtWidgets.QPushButton(Dialog)
        self.button_submit.setObjectName("button_submit")
        self.gridLayout_2.addWidget(self.button_submit, 7, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        self.button_create = QtWidgets.QPushButton(Dialog)
        self.button_create.setObjectName("button_create")
        self.gridLayout_2.addWidget(self.button_create, 7, 3, 1, 1)
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.gridLayout_2.addWidget(self.table, 6, 2, 1, 3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.input_name = QtWidgets.QLineEdit(Dialog)
        self.input_name.setObjectName("input_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_name)
        self.label_total = QtWidgets.QLabel(Dialog)
        self.label_total.setObjectName("label_total")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_total)
        self.label_total_data = QtWidgets.QLabel(Dialog)
        self.label_total_data.setObjectName("label_total_data")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_total_data)
        self.gridLayout_2.addLayout(self.formLayout, 3, 2, 2, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_delete.setText(_translate("Dialog", "删除项目"))
        self.label_status.setText(_translate("Dialog", "你正在做的业务是：人力资源->薪酬标准管理->薪酬标准登记"))
        self.button_submit.setText(_translate("Dialog", "提交"))
        self.button_create.setText(_translate("Dialog", "新增项目"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "薪酬项目名称"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "金额"))
        self.label_name.setText(_translate("Dialog", "薪酬标准名称："))
        self.label_total.setText(_translate("Dialog", "薪酬总额："))
        self.label_total_data.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

