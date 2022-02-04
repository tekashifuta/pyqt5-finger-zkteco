from datetime import datetime
import ipaddress
import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from os.path import exists
from ThreadClerkApp import thdConnZkteco, thdFetchAttendance, thdLoadData, thdSaveSettings, thdSaveToMysql, thdSaveLocalDB
from PyQt5.QtCore import QDate


DURATION_INT = 3
region_list = ["Blank", "CVO1", "CVO2", "CVO3", "EVO1", "EVO2", "EVO3", "NLO1", "NMO1", "NMO2", "OOC1", "SLO1", "SMO1", "SMO2", "WMO1", "WMO2", "WVO1", "WVO2"]

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('conNew.ui', self)
        self.setWindowTitle("Attendance App")
        self.setContentsMargins(10, 10, 10, 10)
        self.setFixedSize(736, 413) # set fixed size of the main window
        self.loadData()
        header = self.tableWidget.horizontalHeader() 
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.myTimer = QtCore.QTimer(self)
        self.cmbRegion.addItems(region_list)
        
        datenoww = datetime.today()
        x = QDate(datenoww)
        self.txtMonth.setDate(x)
        self.txtDay.setDate(x)
        self.txtYear.setDate(x)

        self.btnSaveSettings.clicked.connect(self.strt_wrkr_1)
        self.wkr_thd_1 = thdSaveSettings()
        self.wkr_thd_1.res_to_emit.connect(self.on_j_done_1)

        self.btnGenAtt.clicked.connect(self.strt_wrkr_4)
        self.wkr_thd_4 = thdFetchAttendance()
        self.wkr_thd_4.res_to_emit.connect(self.on_j_done_4)

        self.btnSaveToMysql.clicked.connect(self.strt_wrkr_5)
        self.wkr_thd_5 = thdSaveToMysql()
        self.wkr_thd_5.res_to_emit.connect(self.on_j_done_5)

        self.btnDownload.clicked.connect(self.strt_wrkr_6)
        self.wkr_thd_6 = thdSaveLocalDB()
        self.wkr_thd_6.res_to_emit.connect(self.on_j_done_6)


    def loadData(self):
        file_exists = exists("date.json")
        if not file_exists:
            self.lblStatus.setText("Please set your Settings..")
            self.lblStatus.setStyleSheet('color: red')
        else:
            self.lblStatus.setText("Fetching Data Please wait....")
            self.lblStatus.setStyleSheet('color: orange')
            self.strt_wrkr_2()

    def validate_ip_address(self, address):
        try:
            ip = ipaddress.ip_address(address)
            return True
        except ValueError:
            return False
    
    def checkDate(self):
        date_fmt = self.txtYear.text() + "-" + self.txtMonth.text() + "-" + self.txtDay.text()
        date_fmt_now = datetime.now()
        dateNew = datetime.strptime(date_fmt, "%Y-%m-%d").strftime("%Y-%m-%d")
        dateNow = date_fmt_now.strftime("%Y-%m-%d")
        if dateNew < dateNow:
            return True
        else:
            return False

    def loadDataAndDisable(self, loadData):
        self.txtIP.setText(loadData['set_ip'])
        self.txtPort.setText(loadData['set_port'])
        self.cmbRegion.setCurrentText(loadData['set_region'])
        self.txtSCName.setText(loadData['set_scname'])

    def EnaSetting(self, boolEna):
        self.txtIP.setEnabled(boolEna)
        self.txtPort.setEnabled(boolEna)
        self.cmbRegion.setEnabled(boolEna)
        self.txtSCName.setEnabled(boolEna)
        self.btnSaveSettings.setEnabled(boolEna)

    def EnaQuery(self, boolEna):
        self.txtMonth.setEnabled(boolEna)
        self.txtDay.setEnabled(boolEna)
        self.txtYear.setEnabled(boolEna)
        self.btnGenAtt.setEnabled(boolEna)


# for auto connect timer
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
        if self.time_left_int == 3:
            self.lblStatus.setText('Connecting..')
            self.lblStatus.setStyleSheet('color: green')
            self.strt_wrkr_3()
        else:    
            self.lblStatus.setText(f'Auto Connect into device in {self.time_left_int}')
            self.lblStatus.setStyleSheet('color: green')
# end of auto connect

    def strt_wrkr_1(self):
        if self.cmbRegion.currentText() == 'Blank':
            self.lblStatus.setText("Invalid Region")
            self.lblStatus.setStyleSheet('color: red')
        elif self.txtIP.text() == "" or self.txtPort.text() == "" or self.txtSCName.text() == "":
            self.lblStatus.setText("Please Check Your Inputs")
            self.lblStatus.setStyleSheet('color: red')
        else:
            getReturn = self.validate_ip_address(self.txtIP.text())
            if getReturn:
                self.wkr_thd_1.txt_ip = self.txtIP.text()
                self.wkr_thd_1.txt_port = self.txtPort.text()
                self.wkr_thd_1.txt_region = self.cmbRegion.currentText()
                self.wkr_thd_1.txt_scname = self.txtSCName.text()
                self.wkr_thd_1.start()
            else:
                self.lblStatus.setText("Invalid IP Address")
                self.lblStatus.setStyleSheet('color: red')
    
    def strt_wrkr_2(self):
        self.wkr_thd_2 = thdLoadData()
        self.wkr_thd_2.res_to_emit.connect(self.on_j_done_2)
        self.wkr_thd_2.start()

    def strt_wrkr_3(self):
        self.wkr_thd_3 = thdConnZkteco()
        self.wkr_thd_3.txt_ip = self.txtIP.text()
        self.wkr_thd_3.txt_port = self.txtPort.text()
        self.wkr_thd_3.start()
        self.wkr_thd_3.res_to_emit.connect(self.on_j_done_3)

    def strt_wrkr_4(self):
        chkDate = self.checkDate()
        if chkDate:
            self.wkr_thd_4.txt_ip = self.txtIP.text()
            self.wkr_thd_4.txt_port = self.txtPort.text()
            self.wkr_thd_4.txt_month = self.txtMonth.text()
            self.wkr_thd_4.txt_day = self.txtDay.text()
            self.wkr_thd_4.txt_year = self.txtYear.text()
            self.EnaQuery(False)
            self.btnGenAtt.setEnabled(False)
            self.lblStatus.setText("Generating...")
            self.lblStatus.setStyleSheet("color: orange")
            self.wkr_thd_4.start()
        else:
            self.lblStatus.setText("Date shouldn't above current")
            self.lblStatus.setStyleSheet("color: red")

    def strt_wrkr_5(self):
        self.btnSaveToMysql.setEnabled(False)
        self.btnDownload.setEnabled(False)
        self.lblStatus.setText("Saving Please Wait..")
        self.lblStatus.setStyleSheet("color: orange")
        self.wkr_thd_5.start()

    def strt_wrkr_6(self):
        self.btnSaveToMysql.setEnabled(False)
        self.btnDownload.setEnabled(False)
        self.lblStatus.setText("Saving Local Please Wait..")
        self.lblStatus.setStyleSheet("color: orange")
        self.wkr_thd_6.start()

    def on_j_done_1(self, resDict, resStatus, resStatColor):
        self.lblStatus.setText(resStatus)
        self.lblStatus.setStyleSheet(resStatColor)
        if resDict != {}:
            self.loadDataAndDisable(resDict)
            self.EnaSetting(False)
            self.startTimer_forConnecting()
        self.wkr_thd_1.stop()

    def on_j_done_2(self, resDData, resStatus, resStatColor):
        self.loadDataAndDisable(resDData)
        self.EnaSetting(False)
        self.lblStatus.setText(resStatus)
        self.lblStatus.setStyleSheet(resStatColor)
        self.wkr_thd_2.stop()
        self.startTimer_forConnecting()

    def on_j_done_3(self, resStatus, resStatColor):
        self.EnaQuery(True)
        self.lblStatus.setText(resStatus)
        self.lblStatus.setStyleSheet(resStatColor)
        self.wkr_thd_3.stop()

    def on_j_done_4(self, resList, resStatus, resStatColor, resDate):
        tableRow = 0
        self.tableWidget.setRowCount(len(resList))
        self.lblNoOfRec.setText(str(len(resList)))
        for att in resList:
            self.tableWidget.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(str(att["userID"])))
            self.tableWidget.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(str(att["date"])))
            self.tableWidget.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(str(att["status"])))
            self.tableWidget.setItem(tableRow, 3, QtWidgets.QTableWidgetItem(str(att["punch"])))
            tableRow+=1

        if len(resList) != 0:
            self.lblStatus.setText(resStatus)
            self.lblStatus.setStyleSheet(resStatColor)
            self.btnSaveToMysql.setEnabled(True)
            self.btnDownload.setEnabled(True)
            self.wkr_thd_5.data_to_save = resList
            self.wkr_thd_5.date_query = resDate

            self.wkr_thd_6.data_to_save = resList
            self.wkr_thd_6.date_query = resDate
            self.wkr_thd_6.txt_sc_name = self.txtSCName.text()
            self.wkr_thd_6.txt_region = self.cmbRegion.currentText()
        else:
            self.EnaQuery(True)
            self.lblStatus.setText("No Data Available")
            self.lblStatus.setStyleSheet("color: orange")

        self.wkr_thd_3.stop()

    def on_j_done_5(self, resTxt, resColor):
        self.lblStatus.setText(resTxt)
        self.lblStatus.setStyleSheet(resColor)
        self.EnaQuery(True)
        self.btnSaveToMysql.setEnabled(False)
        self.wkr_thd_5.stop()

    def on_j_done_6(self, resTxt, resColor):
        self.lblStatus.setText(resTxt)
        self.lblStatus.setStyleSheet(resColor)
        self.EnaQuery(True)
        self.wkr_thd_6.stop()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('closing window....')