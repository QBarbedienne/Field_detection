# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Display(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1027, 568)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(930, 100, 61, 20))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(930, 130, 61, 20))
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(850, 210, 113, 20))
        self.lineEdit_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(850, 290, 113, 20))
        self.lineEdit_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(850, 72, 47, 21))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(850, 180, 47, 21))
        self.label_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(850, 260, 111, 21))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(850, 100, 71, 21))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(850, 130, 71, 21))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(850, 340, 111, 41))
        self.pushButton.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 390, 111, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 440, 111, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(850, 500, 111, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 801, 461))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 510, 131, 41))
        self.pushButton_5.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(370, 510, 311, 41))
        self.lineEdit_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "fps"))
        self.label_2.setText(_translate("Dialog", "infos"))
        self.label_3.setText(_translate("Dialog", "field coordinates"))
        self.label_4.setText(_translate("Dialog", "acquisition"))
        self.label_5.setText(_translate("Dialog", "calculation"))
        self.pushButton.setText(_translate("Dialog", "Start"))
        self.pushButton_2.setText(_translate("Dialog", "Pause"))
        self.pushButton_3.setText(_translate("Dialog", "Reboot"))
        self.pushButton_4.setText(_translate("Dialog", "Quit"))
        self.pushButton_5.setText(_translate("Dialog", "Change view"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Display()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())