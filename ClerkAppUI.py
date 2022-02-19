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
        MainWindow.resize(746, 523)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 341, 421))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txtPort = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txtPort.setFont(font)
        self.txtPort.setMaxLength(20)
        self.txtPort.setObjectName("txtPort")
        self.gridLayout.addWidget(self.txtPort, 1, 1, 1, 1)
        self.btnGenAtt = QtWidgets.QPushButton(self.groupBox)
        self.btnGenAtt.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnGenAtt.setFont(font)
        self.btnGenAtt.setObjectName("btnGenAtt")
        self.gridLayout.addWidget(self.btnGenAtt, 10, 1, 1, 1)
        self.txtSCName = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txtSCName.setFont(font)
        self.txtSCName.setMaxLength(100)
        self.txtSCName.setObjectName("txtSCName")
        self.gridLayout.addWidget(self.txtSCName, 3, 1, 1, 1)
        self.lblStatus = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout.addWidget(self.lblStatus, 14, 0, 1, 2)
        self.btnDownload = QtWidgets.QPushButton(self.groupBox)
        self.btnDownload.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnDownload.setFont(font)
        self.btnDownload.setObjectName("btnDownload")
        self.gridLayout.addWidget(self.btnDownload, 13, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 3, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.txtIP = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txtIP.setFont(font)
        self.txtIP.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txtIP.setMaxLength(15)
        self.txtIP.setObjectName("txtIP")
        self.gridLayout.addWidget(self.txtIP, 0, 1, 1, 1)
        self.btnSaveSettings = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnSaveSettings.setFont(font)
        self.btnSaveSettings.setObjectName("btnSaveSettings")
        self.gridLayout.addWidget(self.btnSaveSettings, 4, 1, 1, 1)
        self.cmbRegion = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.cmbRegion.setFont(font)
        self.cmbRegion.setObjectName("cmbRegion")
        self.gridLayout.addWidget(self.cmbRegion, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.btnSaveToMysql = QtWidgets.QPushButton(self.groupBox)
        self.btnSaveToMysql.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnSaveToMysql.setFont(font)
        self.btnSaveToMysql.setObjectName("btnSaveToMysql")
        self.gridLayout.addWidget(self.btnSaveToMysql, 12, 1, 1, 1)
        self.lblEthernetStatus = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblEthernetStatus.setFont(font)
        self.lblEthernetStatus.setText("")
        self.lblEthernetStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEthernetStatus.setObjectName("lblEthernetStatus")
        self.gridLayout.addWidget(self.lblEthernetStatus, 11, 1, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 8, 0, 2, 1)
        self.txtDateNew = QtWidgets.QDateEdit(self.groupBox)
        self.txtDateNew.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
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
        self.gridLayout.addWidget(self.txtDateNew, 8, 1, 2, 1)
        self.lblStatus1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus1.setFont(font)
        self.lblStatus1.setText("")
        self.lblStatus1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus1.setObjectName("lblStatus1")
        self.gridLayout.addWidget(self.lblStatus1, 5, 0, 1, 2)
        self.lblStatus1_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus1_2.setFont(font)
        self.lblStatus1_2.setText("")
        self.lblStatus1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus1_2.setObjectName("lblStatus1_2")
        self.gridLayout.addWidget(self.lblStatus1_2, 6, 0, 2, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 10, 320, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 40, 371, 421))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
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
        self.lbltest = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbltest.setFont(font)
        self.lbltest.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbltest.setObjectName("lbltest")
        self.horizontalLayout_5.addWidget(self.lbltest)
        self.lblNoOfRec = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblNoOfRec.setFont(font)
        self.lblNoOfRec.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblNoOfRec.setObjectName("lblNoOfRec")
        self.horizontalLayout_5.addWidget(self.lblNoOfRec)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.lbltest_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbltest_2.setFont(font)
        self.lbltest_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbltest_2.setObjectName("lbltest_2")
        self.horizontalLayout_5.addWidget(self.lbltest_2)
        self.lblSavedRec = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblSavedRec.setFont(font)
        self.lblSavedRec.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblSavedRec.setObjectName("lblSavedRec")
        self.horizontalLayout_5.addWidget(self.lblSavedRec)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 746, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.btnAboutInfo = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.btnAboutInfo.setFont(font)
        self.btnAboutInfo.setObjectName("btnAboutInfo")
        self.actionasdfasd = QtWidgets.QAction(MainWindow)
        self.actionasdfasd.setObjectName("actionasdfasd")
        self.menuAbout.addAction(self.btnAboutInfo)
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtIP, self.txtPort)
        MainWindow.setTabOrder(self.txtPort, self.cmbRegion)
        MainWindow.setTabOrder(self.cmbRegion, self.txtSCName)
        MainWindow.setTabOrder(self.txtSCName, self.txtDateNew)
        MainWindow.setTabOrder(self.txtDateNew, self.btnGenAtt)
        MainWindow.setTabOrder(self.btnGenAtt, self.btnDownload)
        MainWindow.setTabOrder(self.btnDownload, self.tableWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setAccessibleDescription(_translate("MainWindow", "jkhkjh"))
        self.groupBox.setTitle(_translate("MainWindow", "Data Logs Information"))
        self.btnGenAtt.setText(_translate("MainWindow", "Generate Attendance"))
        self.lblStatus.setText(_translate("MainWindow", "Status"))
        self.btnDownload.setText(_translate("MainWindow", "Download File"))
        self.label_39.setText(_translate("MainWindow", "Sale Center Name :"))
        self.label_16.setText(_translate("MainWindow", "Port :"))
        self.label_15.setText(_translate("MainWindow", "           Biometric - IP Add. :"))
        self.btnSaveSettings.setText(_translate("MainWindow", "Save Settings"))
        self.label_6.setText(_translate("MainWindow", "Region :"))
        self.btnSaveToMysql.setText(_translate("MainWindow", "Upload Data"))
        self.label_41.setText(_translate("MainWindow", "Date :"))
        self.txtDateNew.setDisplayFormat(_translate("MainWindow", "MM/dd/yyyy"))
        self.label_14.setText(_translate("MainWindow", "PGI Data Logs App Ver1.0.3.220219 - Clerk"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Employee Data Information"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Punch"))
        self.lbltest.setText(_translate("MainWindow", "No. Records :"))
        self.lblNoOfRec.setText(_translate("MainWindow", "0"))
        self.lbltest_2.setText(_translate("MainWindow", "No. Saved Records :"))
        self.lblSavedRec.setText(_translate("MainWindow", "0"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.btnAboutInfo.setText(_translate("MainWindow", "Info"))
        self.actionasdfasd.setText(_translate("MainWindow", "asdfasd"))
