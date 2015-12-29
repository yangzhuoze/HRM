# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\clerk_query_filter.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(91, 0))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 2, 1, 1)
        self.input_endtime = QtWidgets.QLineEdit(Dialog)
        self.input_endtime.setObjectName("input_endtime")
        self.gridLayout.addWidget(self.input_endtime, 5, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.input_positioncat = QtWidgets.QComboBox(Dialog)
        self.input_positioncat.setObjectName("input_positioncat")
        self.gridLayout.addWidget(self.input_positioncat, 3, 1, 1, 4)
        self.input_department = QtWidgets.QComboBox(Dialog)
        self.input_department.setObjectName("input_department")
        self.gridLayout.addWidget(self.input_department, 2, 1, 1, 4)
        self.input_starttime = QtWidgets.QLineEdit(Dialog)
        self.input_starttime.setObjectName("input_starttime")
        self.gridLayout.addWidget(self.input_starttime, 5, 1, 1, 1)
        self.input_position = QtWidgets.QComboBox(Dialog)
        self.input_position.setObjectName("input_position")
        self.gridLayout.addWidget(self.input_position, 4, 1, 1, 4)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.input_company = QtWidgets.QComboBox(Dialog)
        self.input_company.setObjectName("input_company")
        self.gridLayout.addWidget(self.input_company, 1, 1, 1, 4)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 4, 1, 1)
        self.input_group = QtWidgets.QComboBox(Dialog)
        self.input_group.setObjectName("input_group")
        self.gridLayout.addWidget(self.input_group, 0, 1, 1, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.button_submit = QtWidgets.QPushButton(Dialog)
        self.button_submit.setMaximumSize(QtCore.QSize(101, 16777215))
        self.button_submit.setObjectName("button_submit")
        self.gridLayout_2.addWidget(self.button_submit, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "职位分类"))
        self.label_6.setText(_translate("Dialog", "建档时间"))
        self.label.setText(_translate("Dialog", "一级机构"))
        self.label_3.setText(_translate("Dialog", "三级机构"))
        self.label_7.setText(_translate("Dialog", "至"))
        self.label_2.setText(_translate("Dialog", "二级机构"))
        self.label_5.setText(_translate("Dialog", "职位名称"))
        self.label_8.setText(_translate("Dialog", "(\'YYYY-mm-dd\')"))
        self.button_submit.setText(_translate("Dialog", "查询"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

