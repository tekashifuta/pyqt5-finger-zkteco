from datetime import datetime
import ipaddress
import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from os.path import exists
from ThreadClerkApp import thdConnZkteco, thdFetchAttendance, thdLoadData, thdNetChecker, thdSaveSettings, thdSaveToMysql, thdSaveLocalDB
from PyQt5.QtCore import QDate
from ClerkAppUI import Ui_MainWindow #GUI Python File


DURATION_INT = 3
region_list = ["Blank", "CVO1", "CVO2", "CVO3", "EVO1", "EVO2", "EVO3", "NLO1", "NMO1", "NMO2", "OOC1", "SLO1", "SMO1", "SMO2", "WMO1", "WMO2", "WVO1", "WVO2"]


class MyApp(QMainWindow, Ui_MainWindow):# inherit the Ui_MainWindow class from clerkappui generated via  ----- python -m PyQt5.uic.pyuic youruifile -o yourpyfile -x
    def __init__(self):
        super().__init__()
        self.setupUi(self)#Load the setup ui from converted python ui
        # uic.loadUi('conNew.ui', self) # para ni e load ang .ui file e erase lng ang Ui_MainWindow sa class
        self.setWindowTitle("PGIDLA V.1.0.3.220219")
        # self.setContentsMargins(10, 10, 10, 10)
        self.setFixedSize(746, 523) # set fixed size of the main window
        self.loadData()
        header = self.tableWidget.horizontalHeader() 
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.myTimer = QtCore.QTimer(self)
        self.myTimer_net_checker = QtCore.QTimer(self)
        self.cmbRegion.addItems(region_list)

        self.txtIP.setInputMask("000.000.000.000;")
        self.txtIP.setFocus()
        self.txtPort.setInputMask("0000000;")

        self.lblEthernetStatus.setStyleSheet("color: green")


        datenoww = datetime.today()
        x = QDate(datenoww)
        self.txtDateNew.setDate(x)

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

        # self.btnChangeConn.clicked.connect(self.strt_wrkr_7)
        # self.wkr_thd_7 = thdChangeConn()
        # self.wkr_thd_7.res_to_emit.connect(self.on_j_done_7)

        self.btnAboutInfo.triggered.connect(self.show_about)

    
    def show_about(self):
        msg = QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("Designed By: PGI Corporate I.T.<br> Programmed By: DPZea")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def show_message(self, strMessage):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(strMessage)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

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
        date_fmt_now = datetime.now()
        dateNow = date_fmt_now.strftime("%Y-%m-%d")
        date_new = datetime.strptime(self.txtDateNew.text(), "%m/%d/%Y").strftime("%Y-%m-%d")
        if date_new < dateNow:
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
        self.txtDateNew.setEnabled(boolEna)
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

# for auto connect timer
    def startTimer_for_net_checker(self):
        self.time_left_int_net_checker = 5
        self.myTimer_net_checker.timeout.connect(self.timerTimeout_net_checker)
        self.myTimer_net_checker.start(1000)

    def timerTimeout_net_checker(self):
        self.time_left_int_net_checker -= 1

        if self.time_left_int_net_checker == 0:#if humana stop ang timer
            self.time_left_int_net_checker = 5
            self.myTimer_net_checker.stop()#if humana stop ang timer

        self.update_gui_net_checker()

    def update_gui_net_checker(self):
        if self.time_left_int_net_checker == 5:
            self.lblStatus.setText('Connecting..')
            self.lblStatus.setStyleSheet('color: green')
            self.strt_wrkr_net_checker()
        else:    
            self.lblStatus.setText(f'Auto Connect into device in {self.time_left_int_net_checker}')
            self.lblStatus.setStyleSheet('color: green')

    def strt_wrkr_net_checker(self):
        self.wkr_thd_net_checker = thdNetChecker()
        self.wkr_thd_net_checker.start()
        self.wkr_thd_net_checker.res_to_emit.connect(self.on_j_done_net_checker)
        
    def on_j_done_net_checker(self, resTxt, resColor, resBool):
        self.btnSaveToMysql.setEnabled(resBool)
        self.btnDownload.setEnabled(resBool)
        self.lblStatus.setText(resTxt)
        self.lblStatus.setStyleSheet(resColor)
        self.wkr_thd_net_checker.stop()
# end of auto connect


    def strt_wrkr_1(self):
        if self.txtIP.text() == "":
            self.show_message("Invalid Biometrics IP Address")
            self.txtIP.setText("")
            self.txtIP.setFocus()
        elif self.txtPort.text() == "":
            self.show_message("Invalid Port")
        elif self.cmbRegion.currentText() == 'Blank':
            self.show_message("Invalid Region")
            self.cmbRegion.setFocus()
        elif self.txtSCName.text() == "":
            self.show_message("Invalid Sale Center Name")
        else:
            self.lblStatus.setText("Testing Connection...")
            self.lblStatus.setStyleSheet("color: orange")
            self.wkr_thd_1.txt_ip = self.txtIP.text()
            self.wkr_thd_1.txt_port = self.txtPort.text()
            self.wkr_thd_1.txt_region = self.cmbRegion.currentText()
            self.wkr_thd_1.txt_scname = self.txtSCName.text()
            self.wkr_thd_1.start()
    
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
            self.wkr_thd_4.date_new = self.txtDateNew.text()

            self.EnaQuery(False)
            self.btnGenAtt.setEnabled(False)
            self.lblStatus.setText("Generating...")
            self.lblStatus.setStyleSheet("color: orange")
            self.wkr_thd_4.start()
        else:
            self.show_message("Invalid Date <br><br>Date shouldn't equal or above current date")

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

    # def strt_wrkr_7(self):
    #     self.wkr_thd_7.btn_txt = self.btnChangeConn.text()
    #     self.lblStatus.setText("Changing Connections...")
    #     self.lblStatus.setStyleSheet("color: orange")
    #     self.wkr_thd_7.start()

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


    def on_j_done_3(self, resStatus, resStatColor, resbool):
        self.EnaQuery(resbool)
        self.lblStatus.setText(resStatus)
        self.lblStatus.setStyleSheet(resStatColor)
        self.wkr_thd_3.stop()

    def on_j_done_4(self, resList, resStatus, resStatColor, resDate):
        tableRow = 0
        newResList = sorted(resList, key = lambda resList: resList['userID'])
        self.tableWidget.setRowCount(len(resList))
        self.lblNoOfRec.setText(str(len(resList)))
        for att in newResList:
            self.tableWidget.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(str(att["userID"])))
            self.tableWidget.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(str(att["date"])))
            self.tableWidget.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(str(att["status"])))
            self.tableWidget.setItem(tableRow, 3, QtWidgets.QTableWidgetItem("IN" if att["punch"] == "0" else "OUT" if att["punch"] == "1" else att["punch"]))
            tableRow+=1

        if resList:
            self.lblStatus.setText(resStatus)
            self.lblStatus.setStyleSheet(resStatColor)
            self.wkr_thd_5.data_to_save = resList
            self.wkr_thd_5.date_query = resDate

            self.wkr_thd_6.data_to_save = resList
            self.wkr_thd_6.date_query = resDate
            self.wkr_thd_6.txt_sc_name = self.txtSCName.text()
            self.wkr_thd_6.txt_region = self.cmbRegion.currentText()

            self.startTimer_for_net_checker()

        else:
            self.lblStatus.setText("No data Available")
            self.EnaQuery(True)
            self.show_message("Please check your query date")

        self.wkr_thd_3.stop()

    def on_j_done_5(self, resTxt, resColor, resBool):
        if not resBool:
            self.lblStatus.setText("")
            self.show_message(resTxt)
        else:
            self.lblStatus.setText(resTxt)
            self.lblStatus.setStyleSheet(resColor)
        self.EnaQuery(resBool)
        self.btnSaveToMysql.setEnabled(not resBool)
        self.btnDownload.setEnabled(not resBool)
        self.wkr_thd_5.stop()

    def on_j_done_6(self, resTxt, resColor):
        self.lblStatus.setText(resTxt)
        self.lblStatus.setStyleSheet(resColor)
        self.EnaQuery(True)
        self.wkr_thd_6.stop()
        
    # def on_j_done_7(self, resTxt, resColor, resLblStatus, resBtnText):
    #     self.btnChangeConn.setText(resBtnText)
    #     self.lblEthernetStatus.setText(resLblStatus)
    #     self.lblEthernetStatus.setStyleSheet(resColor)
    #     self.lblStatus.setText(resTxt)
    #     self.lblStatus.setStyleSheet(resColor)
    #     self.wkr_thd_7.stop()
    #     self.startTimer_for_net_checker()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        # os.system('netsh interface set interface "Ethernet" enable')
        print('closing window....')