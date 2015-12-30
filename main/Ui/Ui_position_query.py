# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\position_query.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(458, 438)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_positioncat = QtWidgets.QLabel(Dialog)
        self.label_positioncat.setObjectName("label_positioncat")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_positioncat)
        self.table_positioncat = QtWidgets.QTableWidget(Dialog)
        self.table_positioncat.setObjectName("table_positioncat")
        self.table_positioncat.setColumnCount(2)
        self.table_positioncat.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_positioncat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_positioncat.setHorizontalHeaderItem(1, item)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.table_positioncat)
        self.label_position = QtWidgets.QLabel(Dialog)
        self.label_position.setObjectName("label_position")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_position)
        self.table_position = QtWidgets.QTableWidget(Dialog)
        self.table_position.setObjectName("table_position")
        self.table_position.setColumnCount(2)
        self.table_position.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_position.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_position.setHorizontalHeaderItem(1, item)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.table_position)
        self.button = QtWidgets.QPushButton(Dialog)
        self.button.setObjectName("button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.button)
        self.verticalLayout_2.addLayout(self.formLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_positioncat.setText(_translate("Dialog", "职位类别："))
        item = self.table_positioncat.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "分类编号"))
        item = self.table_positioncat.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "分类名称"))
        self.label_position.setText(_translate("Dialog", "职位："))
        item = self.table_position.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "职位编号"))
        item = self.table_position.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "职位名称"))
        self.button.setText(_translate("Dialog", "关闭"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

