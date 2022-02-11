# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conNew.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 463)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 359, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.cmbRegion = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cmbRegion.setFont(font)
        self.cmbRegion.setObjectName("cmbRegion")
        self.gridLayout.addWidget(self.cmbRegion, 3, 1, 1, 1)
        self.btnSaveSettings = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnSaveSettings.setFont(font)
        self.btnSaveSettings.setObjectName("btnSaveSettings")
        self.gridLayout.addWidget(self.btnSaveSettings, 5, 1, 1, 1)
        self.btnGenAtt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnGenAtt.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnGenAtt.setFont(font)
        self.btnGenAtt.setObjectName("btnGenAtt")
        self.gridLayout.addWidget(self.btnGenAtt, 9, 0, 1, 2)
        self.txtIP = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.txtIP.setFont(font)
        self.txtIP.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txtIP.setMaxLength(15)
        self.txtIP.setObjectName("txtIP")
        self.gridLayout.addWidget(self.txtIP, 1, 1, 1, 1)
        self.lblStatus = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout.addWidget(self.lblStatus, 12, 0, 1, 2)
        self.btnSaveToMysql = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSaveToMysql.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnSaveToMysql.setFont(font)
        self.btnSaveToMysql.setObjectName("btnSaveToMysql")
        self.gridLayout.addWidget(self.btnSaveToMysql, 10, 0, 1, 2)
        self.txtPort = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.txtPort.setFont(font)
        self.txtPort.setMaxLength(20)
        self.txtPort.setObjectName("txtPort")
        self.gridLayout.addWidget(self.txtPort, 2, 1, 1, 1)
        self.btnDownload = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnDownload.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnDownload.setFont(font)
        self.btnDownload.setObjectName("btnDownload")
        self.gridLayout.addWidget(self.btnDownload, 11, 0, 1, 2)
        self.txtDateNew = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.txtDateNew.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.txtDateNew.setFont(font)
        self.txtDateNew.setAcceptDrops(False)
        self.txtDateNew.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txtDateNew.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.txtDateNew.setMaximumDate(QtCore.QDate(9999, 12, 31))
        self.txtDateNew.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.txtDateNew.setCalendarPopup(True)
        self.txtDateNew.setObjectName("txtDateNew")
        self.gridLayout.addWidget(self.txtDateNew, 8, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 2)
        self.lblStatus1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus1.setFont(font)
        self.lblStatus1.setText("")
        self.lblStatus1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus1.setObjectName("lblStatus1")
        self.gridLayout.addWidget(self.lblStatus1, 7, 0, 1, 2)
        self.label_39 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)
        self.txtSCName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.txtSCName.setFont(font)
        self.txtSCName.setMaxLength(100)
        self.txtSCName.setObjectName("txtSCName")
        self.gridLayout.addWidget(self.txtSCName, 4, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 8, 0, 1, 1)
        self.lblStatus_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus_2.setFont(font)
        self.lblStatus_2.setText("")
        self.lblStatus_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus_2.setObjectName("lblStatus_2")
        self.gridLayout.addWidget(self.lblStatus_2, 6, 0, 1, 2)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(391, 11, 441, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbltest = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbltest.setFont(font)
        self.lbltest.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbltest.setObjectName("lbltest")
        self.horizontalLayout_5.addWidget(self.lbltest)
        self.lblNoOfRec = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblNoOfRec.setFont(font)
        self.lblNoOfRec.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblNoOfRec.setObjectName("lblNoOfRec")
        self.horizontalLayout_5.addWidget(self.lblNoOfRec)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.lbltest_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbltest_2.setFont(font)
        self.lbltest_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbltest_2.setObjectName("lbltest_2")
        self.horizontalLayout_5.addWidget(self.lbltest_2)
        self.lblSavedRec = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblSavedRec.setFont(font)
        self.lblSavedRec.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblSavedRec.setObjectName("lblSavedRec")
        self.horizontalLayout_5.addWidget(self.lblSavedRec)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 843, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.btnAboutInfo = QtWidgets.QAction(MainWindow)
        self.btnAboutInfo.setObjectName("btnAboutInfo")
        self.menuAbout.addAction(self.btnAboutInfo)
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setAccessibleDescription(_translate("MainWindow", "jkhkjh"))
        self.btnSaveSettings.setText(_translate("MainWindow", "Save Settings"))
        self.btnGenAtt.setText(_translate("MainWindow", "Generate Attendance"))
        self.lblStatus.setText(_translate("MainWindow", "Status"))
        self.btnSaveToMysql.setText(_translate("MainWindow", "Upload Data"))
        self.btnDownload.setText(_translate("MainWindow", "Download File"))
        self.txtDateNew.setDisplayFormat(_translate("MainWindow", "MM/dd/yyyy"))
        self.label_14.setText(_translate("MainWindow", "ZKTeco App Ver. 220210v.2"))
        self.label_39.setText(_translate("MainWindow", "Sale Center Name :"))
        self.label_6.setText(_translate("MainWindow", "Region :"))
        self.label_15.setText(_translate("MainWindow", "Biometric - IP Add. :"))
        self.label_16.setText(_translate("MainWindow", "Port :"))
        self.label_41.setText(_translate("MainWindow", "Date :"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Punch"))
        self.lbltest.setText(_translate("MainWindow", "No. Rec:"))
        self.lblNoOfRec.setText(_translate("MainWindow", "0"))
        self.lbltest_2.setText(_translate("MainWindow", "No. Saved Rec:"))
        self.lblSavedRec.setText(_translate("MainWindow", "0"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.btnAboutInfo.setText(_translate("MainWindow", "Info"))
