# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\role_link.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(279, 202)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_clerk = QtWidgets.QLabel(Dialog)
        self.label_clerk.setMaximumSize(QtCore.QSize(81, 16777215))
        self.label_clerk.setObjectName("label_clerk")
        self.gridLayout.addWidget(self.label_clerk, 1, 0, 1, 1)
        self.label_role = QtWidgets.QLabel(Dialog)
        self.label_role.setObjectName("label_role")
        self.gridLayout.addWidget(self.label_role, 2, 0, 1, 1)
        self.input_role = QtWidgets.QComboBox(Dialog)
        self.input_role.setObjectName("input_role")
        self.gridLayout.addWidget(self.input_role, 2, 1, 1, 1)
        self.label_clerk_data = QtWidgets.QLabel(Dialog)
        self.label_clerk_data.setObjectName("label_clerk_data")
        self.gridLayout.addWidget(self.label_clerk_data, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.button = QtWidgets.QPushButton(Dialog)
        self.button.setObjectName("button")
        self.gridLayout.addWidget(self.button, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_clerk.setText(_translate("Dialog", "员工名："))
        self.label_role.setText(_translate("Dialog", "角色名："))
        self.label_clerk_data.setText(_translate("Dialog", "TextLabel"))
        self.button.setText(_translate("Dialog", "提交"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

