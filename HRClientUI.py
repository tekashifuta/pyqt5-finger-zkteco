# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HRClient.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.btnPklToDat = QtWidgets.QPushButton(self.centralwidget)
        self.btnPklToDat.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.btnPklToDat.setFont(font)
        self.btnPklToDat.setObjectName("btnPklToDat")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.btnPklToDat)
        self.btnOpenFileD = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.btnOpenFileD.setFont(font)
        self.btnOpenFileD.setObjectName("btnOpenFileD")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.btnOpenFileD)
        self.lblSCName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lblSCName.setFont(font)
        self.lblSCName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSCName.setObjectName("lblSCName")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lblSCName)
        self.lblDateQuery = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lblDateQuery.setFont(font)
        self.lblDateQuery.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDateQuery.setObjectName("lblDateQuery")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lblDateQuery)
        self.lblNoRec = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lblNoRec.setFont(font)
        self.lblNoRec.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNoRec.setObjectName("lblNoRec")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lblNoRec)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_11)
        self.gridLayout_3.addLayout(self.formLayout_2, 4, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txtDate = QtWidgets.QDateEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtDate.setFont(font)
        self.txtDate.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.txtDate.setMaximumDate(QtCore.QDate(9999, 12, 31))
        self.txtDate.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.txtDate.setObjectName("txtDate")
        self.gridLayout.addWidget(self.txtDate, 3, 1, 1, 1)
        self.btnGetQueryData = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetQueryData.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnGetQueryData.setFont(font)
        self.btnGetQueryData.setObjectName("btnGetQueryData")
        self.gridLayout.addWidget(self.btnGetQueryData, 5, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.cmbDL_Status = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cmbDL_Status.setFont(font)
        self.cmbDL_Status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cmbDL_Status.setObjectName("cmbDL_Status")
        self.cmbDL_Status.addItem("")
        self.cmbDL_Status.addItem("")
        self.cmbDL_Status.addItem("")
        self.gridLayout.addWidget(self.cmbDL_Status, 4, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setLineWidth(1)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.cmbRegion = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cmbRegion.setFont(font)
        self.cmbRegion.setObjectName("cmbRegion")
        self.gridLayout.addWidget(self.cmbRegion, 1, 1, 1, 1)
        self.btnConvertToDAT = QtWidgets.QPushButton(self.centralwidget)
        self.btnConvertToDAT.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnConvertToDAT.setFont(font)
        self.btnConvertToDAT.setObjectName("btnConvertToDAT")
        self.gridLayout.addWidget(self.btnConvertToDAT, 7, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.gridLayout_2.addWidget(self.tableWidget, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.lblStatus = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout_3.addWidget(self.lblStatus, 2, 0, 1, 1)
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnReset.setFont(font)
        self.btnReset.setObjectName("btnReset")
        self.gridLayout_3.addWidget(self.btnReset, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "SC NAME"))
        self.label_10.setText(_translate("MainWindow", "# OF RECORDS"))
        self.label_9.setText(_translate("MainWindow", "DATE"))
        self.btnPklToDat.setText(_translate("MainWindow", "Convert to DAT File"))
        self.btnOpenFileD.setText(_translate("MainWindow", "Select File To Convert"))
        self.lblSCName.setText(_translate("MainWindow", "..."))
        self.lblDateQuery.setText(_translate("MainWindow", "..."))
        self.lblNoRec.setText(_translate("MainWindow", "..."))
        self.label_11.setText(_translate("MainWindow", "---------------PKL file Converter---------------"))
        self.txtDate.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.btnGetQueryData.setText(_translate("MainWindow", "Get SC List"))
        self.label_5.setText(_translate("MainWindow", "Format"))
        self.cmbDL_Status.setItemText(0, _translate("MainWindow", "not downloaded"))
        self.cmbDL_Status.setItemText(1, _translate("MainWindow", "downloaded"))
        self.cmbDL_Status.setItemText(2, _translate("MainWindow", "all"))
        self.label_2.setText(_translate("MainWindow", "Region"))
        self.label_4.setText(_translate("MainWindow", "YYYY/MM/DD"))
        self.btnConvertToDAT.setText(_translate("MainWindow", "Create DAT"))
        self.label_3.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SC Names"))
        self.label.setText(_translate("MainWindow", "Ver. 0.0.5"))
        self.label_6.setText(_translate("MainWindow", "List of Uploaded SC"))
        self.label_7.setText(_translate("MainWindow", "Mysql Data Fetcher"))
        self.lblStatus.setText(_translate("MainWindow", "STATUS"))
        self.btnReset.setText(_translate("MainWindow", "Reset GUI"))
