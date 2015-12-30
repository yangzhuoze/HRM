# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\position_list.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(272, 300)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        self.button_position_create = QtWidgets.QPushButton(Dialog)
        self.button_position_create.setObjectName("button_position_create")
        self.gridLayout.addWidget(self.button_position_create, 5, 1, 1, 1)
        self.button_position_update = QtWidgets.QPushButton(Dialog)
        self.button_position_update.setObjectName("button_position_update")
        self.gridLayout.addWidget(self.button_position_update, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.button_positioncat_update = QtWidgets.QPushButton(Dialog)
        self.button_positioncat_update.setObjectName("button_positioncat_update")
        self.gridLayout.addWidget(self.button_positioncat_update, 4, 1, 1, 1)
        self.button_positioncat_create = QtWidgets.QPushButton(Dialog)
        self.button_positioncat_create.setObjectName("button_positioncat_create")
        self.gridLayout.addWidget(self.button_positioncat_create, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 9, 1, 1, 1)
        self.button_positiontitle_create = QtWidgets.QPushButton(Dialog)
        self.button_positiontitle_create.setObjectName("button_positiontitle_create")
        self.gridLayout.addWidget(self.button_positiontitle_create, 7, 1, 1, 1)
        self.button_positiontitle_update = QtWidgets.QPushButton(Dialog)
        self.button_positiontitle_update.setObjectName("button_positiontitle_update")
        self.gridLayout.addWidget(self.button_positiontitle_update, 8, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_position_create.setText(_translate("Dialog", "职位登记"))
        self.button_position_update.setText(_translate("Dialog", "职位变更"))
        self.button_positioncat_update.setText(_translate("Dialog", "职位分类变更"))
        self.button_positioncat_create.setText(_translate("Dialog", "职位分类登记"))
        self.label.setText(_translate("Dialog", "选择操作："))
        self.button_positiontitle_create.setText(_translate("Dialog", "职称登记"))
        self.button_positiontitle_update.setText(_translate("Dialog", "职称变更"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

