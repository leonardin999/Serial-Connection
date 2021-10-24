# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        MainWindow.setMaximumSize(QtCore.QSize(800, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.port = QtWidgets.QComboBox(self.centralwidget)
        self.port.setGeometry(QtCore.QRect(10, 10, 111, 41))
        self.port.setObjectName("port")
        self.port.addItem("")
        self.btn_connect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_connect.setGeometry(QtCore.QRect(130, 10, 121, 41))
        self.btn_connect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_connect.setAutoFillBackground(False)
        self.btn_connect.setStyleSheet("background-color: rgb(0, 120, 0);\n"
"color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/20x20/icons/20x20/cil-touch-app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_connect.setIcon(icon)
        self.btn_connect.setObjectName("btn_connect")
        self.btn_diconnect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_diconnect.setGeometry(QtCore.QRect(130, 60, 121, 41))
        self.btn_diconnect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_diconnect.setAutoFillBackground(False)
        self.btn_diconnect.setStyleSheet("background-color: rgb(185, 0, 0);\n"
"color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/20x20/icons/20x20/cil-power-standby.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_diconnect.setIcon(icon1)
        self.btn_diconnect.setObjectName("btn_diconnect")
        self.input_val = QtWidgets.QGroupBox(self.centralwidget)
        self.input_val.setGeometry(QtCore.QRect(10, 120, 241, 161))
        self.input_val.setStyleSheet("background-color:rgb(203, 203, 203);")
        self.input_val.setObjectName("input_val")
        self.btn_send = QtWidgets.QPushButton(self.input_val)
        self.btn_send.setGeometry(QtCore.QRect(130, 120, 101, 31))
        self.btn_send.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_send.setObjectName("btn_send")
        self.layoutWidget = QtWidgets.QWidget(self.input_val)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 31, 223, 82))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.inp_angle = QtWidgets.QLineEdit(self.layoutWidget)
        self.inp_angle.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inp_angle.setObjectName("inp_angle")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inp_angle)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.inp_ton = QtWidgets.QLineEdit(self.layoutWidget)
        self.inp_ton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inp_ton.setObjectName("inp_ton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inp_ton)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.inp_toff = QtWidgets.QLineEdit(self.layoutWidget)
        self.inp_toff.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inp_toff.setObjectName("inp_toff")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inp_toff)
        self.output_val = QtWidgets.QGroupBox(self.centralwidget)
        self.output_val.setGeometry(QtCore.QRect(10, 300, 241, 121))
        self.output_val.setStyleSheet("background-color:rgb(203, 203, 203);")
        self.output_val.setObjectName("output_val")
        self.layoutWidget1 = QtWidgets.QWidget(self.output_val)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 31, 223, 82))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.out_angle = QtWidgets.QLineEdit(self.layoutWidget1)
        self.out_angle.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.out_angle.setObjectName("out_angle")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.out_angle)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.out_duty = QtWidgets.QLineEdit(self.layoutWidget1)
        self.out_duty.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.out_duty.setObjectName("out_duty")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.out_duty)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.out_count = QtWidgets.QLineEdit(self.layoutWidget1)
        self.out_count.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.out_count.setObjectName("out_count")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.out_count)
        self.baud = QtWidgets.QComboBox(self.centralwidget)
        self.baud.setGeometry(QtCore.QRect(10, 60, 111, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 29, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 29, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 29, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 29, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 29, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 29, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 29, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 29, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 29, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.baud.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.baud.setFont(font)
        self.baud.setAutoFillBackground(False)
        self.baud.setStyleSheet("")
        self.baud.setIconSize(QtCore.QSize(16, 16))
        self.baud.setFrame(True)
        self.baud.setObjectName("baud")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.txt_output = QtWidgets.QLabel(self.centralwidget)
        self.txt_output.setGeometry(QtCore.QRect(710, 10, 81, 20))
        self.txt_output.setObjectName("txt_output")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 40, 531, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.angle_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.angle_layout.setContentsMargins(0, 0, 0, 0)
        self.angle_layout.setObjectName("angle_layout")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(260, 230, 531, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.duty_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.duty_layout.setContentsMargins(0, 0, 0, 0)
        self.duty_layout.setObjectName("duty_layout")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(670, 419, 121, 31))
        self.status.setObjectName("status")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial GUI"))
        self.port.setItemText(0, _translate("MainWindow", "Arduino Port"))
        self.btn_connect.setText(_translate("MainWindow", "Connect"))
        self.btn_diconnect.setText(_translate("MainWindow", "Disconnected"))
        self.input_val.setTitle(_translate("MainWindow", "Input Value"))
        self.btn_send.setText(_translate("MainWindow", "Sending"))
        self.label.setText(_translate("MainWindow", "Desire Angle:"))
        self.label_2.setText(_translate("MainWindow", "Timing-on: "))
        self.label_3.setText(_translate("MainWindow", "Timing-off: "))
        self.output_val.setTitle(_translate("MainWindow", "Output Value:"))
        self.label_4.setText(_translate("MainWindow", "Current Angle:"))
        self.label_5.setText(_translate("MainWindow", "Duty Cycle(%): "))
        self.label_6.setText(_translate("MainWindow", "Blink Count :"))
        self.baud.setItemText(0, _translate("MainWindow", "Baudrates"))
        self.baud.setItemText(1, _translate("MainWindow", "1200"))
        self.baud.setItemText(2, _translate("MainWindow", "1800"))
        self.baud.setItemText(3, _translate("MainWindow", "2400"))
        self.baud.setItemText(4, _translate("MainWindow", "4800"))
        self.baud.setItemText(5, _translate("MainWindow", "9600"))
        self.baud.setItemText(6, _translate("MainWindow", "38400"))
        self.baud.setItemText(7, _translate("MainWindow", "19200"))
        self.baud.setItemText(8, _translate("MainWindow", "57600"))
        self.baud.setItemText(9, _translate("MainWindow", "115200"))
        self.txt_output.setText(_translate("MainWindow", "Output State"))
        self.status.setText(_translate("MainWindow", "Connecting Status:...."))

import Display.icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

