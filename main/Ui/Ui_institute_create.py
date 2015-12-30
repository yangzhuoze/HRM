# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\institute_create.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(348, 161)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.input_group = QtWidgets.QComboBox(Dialog)
        self.input_group.setObjectName("input_group")
        self.gridLayout.addWidget(self.input_group, 0, 3, 1, 1)
        self.label_company = QtWidgets.QLabel(Dialog)
        self.label_company.setObjectName("label_company")
        self.gridLayout.addWidget(self.label_company, 1, 2, 1, 1)
        self.input_company = QtWidgets.QComboBox(Dialog)
        self.input_company.setObjectName("input_company")
        self.gridLayout.addWidget(self.input_company, 1, 3, 1, 1)
        self.label_group = QtWidgets.QLabel(Dialog)
        self.label_group.setObjectName("label_group")
        self.gridLayout.addWidget(self.label_group, 0, 2, 1, 1)
        self.button = QtWidgets.QPushButton(Dialog)
        self.button.setObjectName("button")
        self.gridLayout.addWidget(self.button, 5, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 3, 1, 1)
        self.input_name = QtWidgets.QLineEdit(Dialog)
        self.input_name.setObjectName("input_name")
        self.gridLayout.addWidget(self.input_name, 3, 3, 1, 1)
        self.label_department = QtWidgets.QLabel(Dialog)
        self.label_department.setObjectName("label_department")
        self.gridLayout.addWidget(self.label_department, 2, 2, 1, 1)
        self.input_department = QtWidgets.QComboBox(Dialog)
        self.input_department.setObjectName("input_department")
        self.gridLayout.addWidget(self.input_department, 2, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_company.setText(_translate("Dialog", "TextLabel"))
        self.label_group.setText(_translate("Dialog", "TextLabel"))
        self.button.setText(_translate("Dialog", "提交"))
        self.label_name.setText(_translate("Dialog", "TextLabel"))
        self.label_department.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

