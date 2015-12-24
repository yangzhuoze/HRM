# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\login.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMaximumSize(QtCore.QSize(400, 16777215))
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 3, 1, 1)
        self.label_username = QtWidgets.QLabel(Dialog)
        self.label_username.setObjectName("label_username")
        self.gridLayout_4.addWidget(self.label_username, 4, 1, 1, 1)
        self.input_username = QtWidgets.QLineEdit(Dialog)
        self.input_username.setMaximumSize(QtCore.QSize(181, 20))
        self.input_username.setObjectName("input_username")
        self.gridLayout_4.addWidget(self.input_username, 4, 2, 1, 3)
        self.button_login = QtWidgets.QPushButton(Dialog)
        self.button_login.setObjectName("button_login")
        self.gridLayout_4.addWidget(self.button_login, 8, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 6, 0, 1, 1)
        self.label_password = QtWidgets.QLabel(Dialog)
        self.label_password.setObjectName("label_password")
        self.gridLayout_4.addWidget(self.label_password, 6, 1, 1, 1)
        self.button_quit = QtWidgets.QPushButton(Dialog)
        self.button_quit.setObjectName("button_quit")
        self.gridLayout_4.addWidget(self.button_quit, 8, 4, 1, 1)
        self.input_password = QtWidgets.QLineEdit(Dialog)
        self.input_password.setMaximumSize(QtCore.QSize(181, 20))
        self.input_password.setObjectName("input_password")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout_4.addWidget(self.input_password, 6, 2, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 6, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 8, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 3, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 1, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 5, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 7, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem8, 9, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem9, 10, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_username.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">员工号：</p></body></html>"))
        self.button_login.setText(_translate("Dialog", "登　陆"))
        self.label_password.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">密　码：</p></body></html>"))
        self.button_quit.setText(_translate("Dialog", "退　出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

