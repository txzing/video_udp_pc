# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\TCP_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(643, 515)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_receive = QtWidgets.QTextEdit(Form)
        self.textEdit_receive.setMinimumSize(QtCore.QSize(450, 320))
        self.textEdit_receive.setMaximumSize(QtCore.QSize(460, 16777215))
        self.textEdit_receive.setObjectName("textEdit_receive")
        self.horizontalLayout_2.addWidget(self.textEdit_receive)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox_type = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_type.setObjectName("comboBox_type")
        self.verticalLayout.addWidget(self.comboBox_type)
        self.label_ip = QtWidgets.QLabel(self.groupBox)
        self.label_ip.setObjectName("label_ip")
        self.verticalLayout.addWidget(self.label_ip)
        self.comboBox_ip = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ip.setObjectName("comboBox_ip")
        self.verticalLayout.addWidget(self.comboBox_ip)
        self.label_port = QtWidgets.QLabel(self.groupBox)
        self.label_port.setObjectName("label_port")
        self.verticalLayout.addWidget(self.label_port)
        self.lineEdit_port = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.verticalLayout.addWidget(self.lineEdit_port)
        self.pushButton_Open = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Open.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.verticalLayout.addWidget(self.pushButton_Open)
        self.pushButton_CleanRecevice = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_CleanRecevice.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_CleanRecevice.setObjectName("pushButton_CleanRecevice")
        self.verticalLayout.addWidget(self.pushButton_CleanRecevice)
        self.checkBox_HexRecevive = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_HexRecevive.setObjectName("checkBox_HexRecevive")
        self.verticalLayout.addWidget(self.checkBox_HexRecevive)
        self.checkBox_time = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_time.setObjectName("checkBox_time")
        self.verticalLayout.addWidget(self.checkBox_time)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 49, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.widget_client = QtWidgets.QWidget(Form)
        self.widget_client.setObjectName("widget_client")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_client)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_ipname = QtWidgets.QLabel(self.widget_client)
        self.label_ipname.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_ipname.setObjectName("label_ipname")
        self.gridLayout_2.addWidget(self.label_ipname, 0, 0, 1, 1)
        self.comboBox_ClientIp = QtWidgets.QComboBox(self.widget_client)
        self.comboBox_ClientIp.setMinimumSize(QtCore.QSize(355, 0))
        self.comboBox_ClientIp.setObjectName("comboBox_ClientIp")
        self.gridLayout_2.addWidget(self.comboBox_ClientIp, 0, 1, 1, 1)
        self.pushButton_ClientClose = QtWidgets.QPushButton(self.widget_client)
        self.pushButton_ClientClose.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_ClientClose.setObjectName("pushButton_ClientClose")
        self.gridLayout_2.addWidget(self.pushButton_ClientClose, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(145, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
        self.gridLayout_3.addWidget(self.widget_client, 1, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_Send = QtWidgets.QTextEdit(Form)
        self.textEdit_Send.setObjectName("textEdit_Send")
        self.horizontalLayout.addWidget(self.textEdit_Send)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_Send = QtWidgets.QPushButton(Form)
        self.pushButton_Send.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_Send.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_Send.setObjectName("pushButton_Send")
        self.verticalLayout_2.addWidget(self.pushButton_Send)
        self.pushButton_SendClean = QtWidgets.QPushButton(Form)
        self.pushButton_SendClean.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_SendClean.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_SendClean.setObjectName("pushButton_SendClean")
        self.verticalLayout_2.addWidget(self.pushButton_SendClean)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_TimeSend = QtWidgets.QCheckBox(Form)
        self.checkBox_TimeSend.setObjectName("checkBox_TimeSend")
        self.horizontalLayout_3.addWidget(self.checkBox_TimeSend)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_IntervalTime = QtWidgets.QLineEdit(Form)
        self.lineEdit_IntervalTime.setObjectName("lineEdit_IntervalTime")
        self.horizontalLayout_3.addWidget(self.lineEdit_IntervalTime)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_HexSend = QtWidgets.QCheckBox(Form)
        self.checkBox_HexSend.setObjectName("checkBox_HexSend")
        self.horizontalLayout_4.addWidget(self.checkBox_HexSend)
        self.checkBox_SendEnd = QtWidgets.QCheckBox(Form)
        self.checkBox_SendEnd.setObjectName("checkBox_SendEnd")
        self.horizontalLayout_4.addWidget(self.checkBox_SendEnd)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_ReceviceNum = QtWidgets.QLabel(Form)
        self.label_ReceviceNum.setMinimumSize(QtCore.QSize(70, 0))
        self.label_ReceviceNum.setObjectName("label_ReceviceNum")
        self.verticalLayout_3.addWidget(self.label_ReceviceNum)
        self.label_SendNum = QtWidgets.QLabel(Form)
        self.label_SendNum.setObjectName("label_SendNum")
        self.verticalLayout_3.addWidget(self.label_SendNum)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(306, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 3, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "网络设置"))
        self.label.setText(_translate("Form", "(1)协议类型"))
        self.label_ip.setText(_translate("Form", "(2)本地主机地址"))
        self.label_port.setText(_translate("Form", "(3)本地主机端口"))
        self.pushButton_Open.setText(_translate("Form", "打开"))
        self.pushButton_CleanRecevice.setText(_translate("Form", "清除接收"))
        self.checkBox_HexRecevive.setText(_translate("Form", "16进制显示"))
        self.checkBox_time.setText(_translate("Form", "时间戳"))
        self.label_ipname.setText(_translate("Form", "客户端"))
        self.pushButton_ClientClose.setText(_translate("Form", "断开"))
        self.pushButton_Send.setText(_translate("Form", "发送"))
        self.pushButton_SendClean.setText(_translate("Form", "清除发送"))
        self.checkBox_TimeSend.setText(_translate("Form", "定时发送"))
        self.label_5.setText(_translate("Form", "周期"))
        self.label_6.setText(_translate("Form", "ms"))
        self.checkBox_HexSend.setText(_translate("Form", "16进制发送"))
        self.checkBox_SendEnd.setText(_translate("Form", "发送新行"))
        self.label_ReceviceNum.setText(_translate("Form", "接收:0"))
        self.label_SendNum.setText(_translate("Form", "发送:0"))
