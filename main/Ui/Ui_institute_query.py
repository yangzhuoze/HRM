# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\institute_query.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(529, 518)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_group = QtWidgets.QLabel(Dialog)
        self.label_group.setObjectName("label_group")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_group)
        self.label_company = QtWidgets.QLabel(Dialog)
        self.label_company.setObjectName("label_company")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_company)
        self.label_department = QtWidgets.QLabel(Dialog)
        self.label_department.setObjectName("label_department")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_department)
        self.table_group = QtWidgets.QTableWidget(Dialog)
        self.table_group.setObjectName("table_group")
        self.table_group.setColumnCount(2)
        self.table_group.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_group.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_group.setHorizontalHeaderItem(1, item)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.table_group)
        self.table_company = QtWidgets.QTableWidget(Dialog)
        self.table_company.setObjectName("table_company")
        self.table_company.setColumnCount(2)
        self.table_company.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_company.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_company.setHorizontalHeaderItem(1, item)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.table_company)
        self.table_department = QtWidgets.QTableWidget(Dialog)
        self.table_department.setObjectName("table_department")
        self.table_department.setColumnCount(2)
        self.table_department.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_department.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_department.setHorizontalHeaderItem(1, item)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.table_department)
        self.button = QtWidgets.QPushButton(Dialog)
        self.button.setObjectName("button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.button)
        self.verticalLayout_2.addLayout(self.formLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_group.setText(_translate("Dialog", "一级机构："))
        self.label_company.setText(_translate("Dialog", "二级机构："))
        self.label_department.setText(_translate("Dialog", "三级机构："))
        item = self.table_group.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "机构编号"))
        item = self.table_group.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "机构名称"))
        item = self.table_company.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "机构编号"))
        item = self.table_company.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "机构名称"))
        item = self.table_department.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "机构编号"))
        item = self.table_department.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "机构名称"))
        self.button.setText(_translate("Dialog", "关闭"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

