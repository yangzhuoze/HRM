# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\position_detail.ui'
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
        self.input_name = QtWidgets.QLineEdit(Dialog)
        self.input_name.setObjectName("input_name")
        self.gridLayout.addWidget(self.input_name, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        self.input_positioncat = QtWidgets.QComboBox(Dialog)
        self.input_positioncat.setObjectName("input_positioncat")
        self.gridLayout.addWidget(self.input_positioncat, 0, 3, 1, 1)
        self.label_position = QtWidgets.QLabel(Dialog)
        self.label_position.setObjectName("label_position")
        self.gridLayout.addWidget(self.label_position, 1, 2, 1, 1)
        self.input_position = QtWidgets.QComboBox(Dialog)
        self.input_position.setObjectName("input_position")
        self.gridLayout.addWidget(self.input_position, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.button = QtWidgets.QPushButton(Dialog)
        self.button.setObjectName("button")
        self.gridLayout.addWidget(self.button, 4, 3, 1, 1)
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 2, 2, 1, 1)
        self.label_positioncat = QtWidgets.QLabel(Dialog)
        self.label_positioncat.setObjectName("label_positioncat")
        self.gridLayout.addWidget(self.label_positioncat, 0, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_position.setText(_translate("Dialog", "TextLabel"))
        self.button.setText(_translate("Dialog", "提交"))
        self.label_name.setText(_translate("Dialog", "TextLabel"))
        self.label_positioncat.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

