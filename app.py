import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow
from thread_objects import trdLoadIfExist, trdSetSettings, trdAutoConnect, trdGenData, trdSaveDataToFB
from os.path import exists
import ipaddress 

region_list = ["Blank", "CVO1", "CVO2", "CVO3", "EVO1", "EVO2", "EVO3", "NLO1", "NMO1", "NMO2", "OOC1", "SLO1", "SMO1", "SMO2", "WMO1", "WMO2", "WVO1", "WVO2"]

DURATION_INT = 4

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('connect2.ui', self)
        self.setWindowTitle("Test App")
        self.setContentsMargins(10, 10, 10, 10)
        self.setFixedSize(550, 898) # set fixe size of the main window
        self.myTimer = QtCore.QTimer(self)
        self.cmbRegion.addItems(region_list)
        self.loadData()
        self.defaultText()

        #Resize Header of the Table
        header = self.tableWidget.horizontalHeader() 
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        #only int in textbox
        self.onlyInt = QIntValidator()
        self.txtPort.setValidator(self.onlyInt)

        self.btnSaveSettings.clicked.connect(self.strt_wrkr_2)
        self.worker_thread_2 = trdSetSettings()
        self.worker_thread_2.res_to_emit_bool_dict.connect(self.onJobDone2)

        self.worker_thread_4 = trdAutoConnect()
        self.worker_thread_4.res_to_emit_status.connect(self.onJobDone4)

        self.btnAutoGen.clicked.connect(self.strt_wrkr_5)
        self.worker_thread_5 = trdGenData()
        self.worker_thread_5.res_to_emit_status.connect(self.onJobDone5)

        self.btnSaveToFirebase.clicked.connect(self.strt_wrkr_6)
        self.worker_thread_6 = trdSaveDataToFB()
        self.worker_thread_6.res_to_emit_status.connect(self.onJobDone6)
        

    def loadData(self):
        file_exists = exists("date.json")
        if not file_exists:
            self.lblStatus.setText("Please set your Settings..")
            self.lblStatus.setStyleSheet('color: red')
        else:
            self.lblStatus.setText("Fetching Data Please wait....")
            self.lblStatus.setStyleSheet('color: orange')
            self.strt_wrkr_3()

    def enableObjects(self, enaBool):
        self.txtFrom1.setEnabled(enaBool)
        self.txtTo1.setEnabled(enaBool)
        self.txtFrom2.setEnabled(enaBool)
        self.txtTo2.setEnabled(enaBool)
        self.txtIP.setEnabled(enaBool)
        self.txtPort.setEnabled(enaBool)
        self.txtMonth.setEnabled(enaBool)
        self.txtYear.setEnabled(enaBool)
        self.txtSCName.setEnabled(enaBool)
        self.cmbRegion.setEnabled(enaBool)
        self.btnSaveSettings.setEnabled(enaBool)

        # self.btnAutoGen.setEnabled(not enaBool)
        # self.btnGetAll.setEnabled(not enaBool)

    def enableSetTxt(self, enaStr):
        self.txtFrom1.setDate(QDate.fromString(str(enaStr['date_from_1']['date']), 'dd'))
        self.txtTo1.setDate(QDate.fromString(str(enaStr['date_to_1']['date']), 'dd'))
        self.txtFrom2.setDate(QDate.fromString(str(enaStr['date_from_2']['date']), 'dd'))
        self.txtTo2.setDate(QDate.fromString(str(enaStr['date_to_2']['date']), 'dd'))
        self.txtIP.setText(enaStr['IP_add'])
        self.txtPort.setText(enaStr['Port_add'])
        self.txtMonth.setDate(QDate.fromString(str(enaStr['date_to_1']['month']), 'MM'))
        self.txtYear.setDate(QDate.fromString(str(enaStr['date_to_1']['year']), 'yyyy'))
        self.txtSCName.setText(enaStr['SCName'])
        self.cmbRegion.setCurrentText(enaStr['region'])
    
    def defaultText(self):
        self.txtFrom1.setDate(QDate.fromString('23', 'dd'))
        self.txtTo1.setDate(QDate.fromString('09', 'dd'))
        self.txtFrom2.setDate(QDate.fromString('10', 'dd'))
        self.txtTo2.setDate(QDate.fromString('24', 'dd'))
        self.txtIP.setText('')
        self.txtPort.setText('')

    def validate_ip_address(self, address):
        try:
            ip = ipaddress.ip_address(address)
            return True
        except ValueError:
            return False

    def strt_wrkr_2(self):
        if (self.txtYear.text() == "" and self.txtMonth.text() == "" 
            and self.txtFrom1.text() == "" and self.txtTo1.text() == "" and self.txtFrom2.text() == "" and self.txtTo2.text() == ""):
            self.lblStatus.setText('Kulang ang Entry')
            self.lblStatus.setStyleSheet('color: red')
        elif self.txtPort.text() == "":
            self.txtPort.setFocus()
            self.lblStatus.setText('Not a valid PORT')
            self.lblStatus.setStyleSheet('color: red')
        elif self.cmbRegion.currentText() == "Blank":
            self.cmbRegion.setFocus()
            self.lblStatus.setText('Please Select Region')
            self.lblStatus.setStyleSheet('color: red')
        elif self.txtSCName.text() == "":
            self.txtSCName.setFocus()
            self.lblStatus.setText('Please Input SC Name')
            self.lblStatus.setStyleSheet('color: red')
        else:
            getReturn = self.validate_ip_address(self.txtIP.text())
            if getReturn:
                self.lblStatus.setText('Saving settings please wait....')
                self.lblStatus.setStyleSheet('color: orange')
                self.enableObjects(False)
                self.worker_thread_2.txt_from_1 = self.txtFrom1.text()
                self.worker_thread_2.txt_to_1 = self.txtTo1.text()
                self.worker_thread_2.txt_from_2 = self.txtFrom2.text()
                self.worker_thread_2.txt_to_2 = self.txtTo2.text()
                self.worker_thread_2.txt_IP = self.txtIP.text()
                self.worker_thread_2.txt_PORT = self.txtPort.text()
                self.worker_thread_2.txt_month = self.txtMonth.text()
                self.worker_thread_2.txt_year = self.txtYear.text()
                self.worker_thread_2.txt_SCName = self.txtSCName.text()
                self.worker_thread_2.txt_region = self.cmbRegion.currentText()
                self.worker_thread_2.start()
            else:
                self.lblStatus.setText('Not a valid address')
                self.lblStatus.setStyleSheet('color: red')

    def strt_wrkr_3(self):
        self.worker_thread_3 = trdLoadIfExist()
        self.worker_thread_3.start()
        self.worker_thread_3.res_to_emit.connect(self.onJobDone3)

    def strt_wrkr_4(self):
        self.worker_thread_4.txt_IP = self.txtIP.text()
        self.worker_thread_4.txt_PORT = self.txtPort.text()
        self.worker_thread_4.start()
        # self.worker_thread_4.res_to_emit.connect(self.onJobDone3)

    def strt_wrkr_5(self):
        self.lblStatus.setText('Generating Attendance')
        self.lblStatus.setStyleSheet('color: orange')
        self.btnAutoGen.setEnabled(False)
        self.worker_thread_5.start()

    def strt_wrkr_6(self):
        self.btnSaveToFirebase.setEnabled(False)
        self.lblStatus.setText('Saving to firebase....')
        self.lblStatus.setStyleSheet('color: green')
        self.worker_thread_6.start()

    def onJobDone2(self, boolRes, dictRes, strRes):
        if dictRes != {}:
            self.enableObjects(boolRes)
            self.lblStatus.setText(strRes)
            self.lblStatus.setStyleSheet('color: green')
            self.worker_thread_2.stop()
            self.startTimer_forConnecting()
        else:
            self.lblStatus.setText(strRes)
            self.lblStatus.setStyleSheet('color: red')
            self.enableObjects(boolRes)
            self.worker_thread_2.stop()

    def onJobDone3(self, recivedObj, setBool, lblText, styleColor):
        self.enableObjects(setBool)
        self.enableSetTxt(recivedObj)
        self.lblStatus.setText(lblText)
        self.lblStatus.setStyleSheet(styleColor)
        self.worker_thread_3.stop()
        self.startTimer_forConnecting()

    def onJobDone4(self, bool_res, status_res):
        self.btnAutoGen.setEnabled(bool_res)
        self.lblStatus.setText(status_res)
        self.lblStatus.setStyleSheet('color: green')
        self.worker_thread_4.stop()

    def onJobDone5(self, listRes, listGenInfo, strRes, strResColor, strLblRes, boolEnaRes):
        self.lblStatus.setText(strRes)
        self.lblStatus.setStyleSheet(strResColor)

        tableRow = 0
        self.tableWidget.setRowCount(len(listRes))
        self.lblNoOfRec.setText(str(len(listRes)))
        self.lblDateStatus.setText(strLblRes)
        for att in listRes:
            self.tableWidget.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(str(att["userID"])))
            self.tableWidget.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(str(att["date"])))
            self.tableWidget.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(str(att["status"])))
            self.tableWidget.setItem(tableRow, 3, QtWidgets.QTableWidgetItem(str(att["punch"])))
            tableRow+=1

        self.btnSaveToFirebase.setEnabled(boolEnaRes)
        self.worker_thread_5.stop()
        self.worker_thread_6.list_of_gen_date = listRes
        self.worker_thread_6.list_gen_info = listGenInfo

    def onJobDone6(self, dataIDRes, lblStrRes, strResColor, savedNum):
        self.lblSaveStatus.setText(dataIDRes)
        self.lblStatus.setText(lblStrRes)
        self.lblStatus.setStyleSheet(strResColor)
        self.lblSavedRec.setText(str(savedNum))
        self.worker_thread_6.stop()

    def startTimer_forConnecting(self):
        self.time_left_int = DURATION_INT

        self.myTimer.timeout.connect(self.timerTimeout)
        self.myTimer.start(1000)

    def timerTimeout(self):
        self.time_left_int -= 1

        if self.time_left_int == 0:#if humana stop ang timer
            self.time_left_int = DURATION_INT
            self.myTimer.stop()#if humana stop ang timer

        self.update_gui()

    def update_gui(self):
        if self.time_left_int == 4:
            self.lblStatus.setText('Connecting..')
            self.lblStatus.setStyleSheet('color: green')
            self.strt_wrkr_4()
        else:    
            self.lblStatus.setText(f'Auto Connect into device in {self.time_left_int}')
            self.lblStatus.setStyleSheet('color: green')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('closing window....')