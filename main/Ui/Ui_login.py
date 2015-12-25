# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\login.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMaximumSize(QtCore.QSize(400, 16777215))
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.layout_msg = QtWidgets.QHBoxLayout()
        self.layout_msg.setObjectName("layout_msg")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_msg.addItem(spacerItem2)
        self.label_msg = QtWidgets.QLabel(Dialog)
        self.label_msg.setObjectName("label_msg")
        self.layout_msg.addWidget(self.label_msg)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_msg.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.layout_msg)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.layout_input = QtWidgets.QGridLayout()
        self.layout_input.setObjectName("layout_input")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_input.addItem(spacerItem5, 0, 0, 1, 1)
        self.input_username = QtWidgets.QLineEdit(Dialog)
        self.input_username.setObjectName("input_username")
        self.layout_input.addWidget(self.input_username, 0, 2, 1, 1)
        self.label_username = QtWidgets.QLabel(Dialog)
        self.label_username.setObjectName("label_username")
        self.layout_input.addWidget(self.label_username, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_input.addItem(spacerItem6, 0, 3, 1, 1)
        self.input_password = QtWidgets.QLineEdit(Dialog)
        self.input_password.setObjectName("input_password")
        self.layout_input.addWidget(self.input_password, 2, 2, 1, 1)
        self.label_password = QtWidgets.QLabel(Dialog)
        self.label_password.setObjectName("label_password")
        self.layout_input.addWidget(self.label_password, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_input.addItem(spacerItem7, 3, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_input.addItem(spacerItem8, 1, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.layout_input)
        self.layout_button = QtWidgets.QHBoxLayout()
        self.layout_button.setObjectName("layout_button")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_button.addItem(spacerItem9)
        self.button_login = QtWidgets.QPushButton(Dialog)
        self.button_login.setObjectName("button_login")
        self.layout_button.addWidget(self.button_login)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_button.addItem(spacerItem10)
        self.button_quit = QtWidgets.QPushButton(Dialog)
        self.button_quit.setObjectName("button_quit")
        self.layout_button.addWidget(self.button_quit)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_button.addItem(spacerItem11)
        self.verticalLayout_4.addLayout(self.layout_button)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 4, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_msg.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_username.setText(_translate("Dialog", "员工号："))
        self.label_password.setText(_translate("Dialog", "密　码："))
        self.button_login.setText(_translate("Dialog", "登陆"))
        self.button_quit.setText(_translate("Dialog", "退出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

