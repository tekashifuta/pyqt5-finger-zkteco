from datetime import date, datetime
import errno
import json
import os
import pickle
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QDate, QThread, pyqtSignal
import requests
from HRClientUI import Ui_MainWindow

headers = {
    'Content-Type': 'application/json',
}

# urlSave = "http://localhost/prycegas_att/saveJsonAtt.php"
# urlGetSCNames = "http://attendance.prycegas.com/prycegas_att/selectJsonAtt_SCNames.php"
# urlUpdateStatus = "http://attendance.prycegas.com/prycegas_att/selectJsonAtt_SCNames.php"
urlGetSCNames = "http://attendance.prycegas.com/prycegas_att/selectJsonAtt_SCNames_v1.php"
urlUpdateStatus = "http://attendance.prycegas.com/prycegas_att/updateDL_status_v1.php"

region_list = ["Blank", "CVO1", "CVO2", "CVO3", "EVO1", "EVO2", "EVO3", "NLO1", "NMO1", "NMO2", "OOC1", "SLO1", "SMO1", "SMO2", "WMO1", "WMO2", "WVO1", "WVO2"]

datenoww = datetime.today()
x = QDate(datenoww)

class MyApp(QMainWindow, Ui_MainWindow): # inherit the Ui_MainWindow class from HRClientUI.py HRClient.ui generated via  ----- python -m PyQt5.uic.pyuic youruifile -o yourpyfile -x
    def __init__(self):
        super().__init__()
        self.setupUi(self) #Load the setup ui from converted python ui
        # uic.loadUi('HRClient.ui', self) # para ni e load ang .ui file e erase lng ang Ui_MainWindow sa class
        self.setWindowTitle("HR Client App")
        self.setContentsMargins(10, 10, 10, 10)
        self.setFixedSize(421, 547) # set fixed size of the main window
        self.cmbRegion.addItems(region_list)
        self.progressBar.setProperty("value", 0)

        self.txtDate.setDate(x)
        # self.txtToDate.setDate(x)

        self.btnGetQueryData.clicked.connect(self.strt_wrkr_1)
        self.wrkr_thd_1 = thdFetchDataToMysql()
        self.wrkr_thd_1.res_to_emit.connect(self.on_jb_don_1)
        self.wrkr_thd_1.res_to_emit_timer.connect(self.on_jb_don_PBar)

        self.btnConvertToDAT.clicked.connect(self.strt_wrkr_2)
        self.btnConvertToDAT.clicked.connect(self.strt_wrkr_3)
        self.wrkr_thd_2 = thdConvertData()
        self.wrkr_thd_2.res_to_emit.connect(self.on_jb_don_2)

        self.wrkr_thd_3 = thdUpdateStatus()
        self.wrkr_thd_3.res_to_emit.connect(self.on_jb_don_3)

        self.btnOpenFileD.clicked.connect(self.strt_wrkr_4)
        self.wrkr_thd_4 = thdReadPickle()
        self.wrkr_thd_4.res_to_emit.connect(self.on_jb_don_4)

        self.btnPklToDat.clicked.connect(self.strt_wrkr_5)
        self.wrkr_thd_5 = thdConvPklToDatFile()
        self.wrkr_thd_5.res_to_emit.connect(self.on_jb_don_5)
        self.wrkr_thd_5.res_to_emit_timer.connect(self.on_jb_don_PBar)

        self.btnReset.clicked.connect(self.resetUi)


    def setEna(self, resBool):
        self.cmbRegion.setEnabled(resBool)
        self.txtDate.setEnabled(resBool)
        self.cmbDL_Status.setEnabled(resBool)
        self.btnGetQueryData.setEnabled(resBool)
        self.btnConvertToDAT.setEnabled(not resBool)

    def setEna2(self, resBool):
        self.cmbRegion.setEnabled(resBool)
        self.txtDate.setEnabled(resBool)
        self.cmbDL_Status.setEnabled(resBool)
        self.btnGetQueryData.setEnabled(resBool)
        self.btnConvertToDAT.setEnabled(resBool)

    def resetUi(self):
        self.cmbRegion.setCurrentText("Blank")
        self.txtDate.setDate(x)
        self.cmbDL_Status.setCurrentText("not downloaded")
        self.cmbRegion.setEnabled(True)
        self.txtDate.setEnabled(True)
        self.cmbDL_Status.setEnabled(True)
        self.btnGetQueryData.setEnabled(True)
        self.btnConvertToDAT.setEnabled(False)
        self.btnOpenFileD.setEnabled(True)
        self.btnPklToDat.setEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(""))
        self.progressBar.setValue(0)
        self.lblSCName.setText("...")
        self.lblDateQuery.setText("...")
        self.lblNoRec.setText("...")
        self.lblStatus.setText("GUI Reset")
        self.lblStatus.setStyleSheet('color: green')

    def strt_wrkr_1(self):
        self.lblStatus.setText("Generating...")
        self.lblStatus.setStyleSheet('color: orange')
        self.wrkr_thd_1.txt_date = self.txtDate.text()
        self.wrkr_thd_1.txt_region = self.cmbRegion.currentText()
        self.wrkr_thd_1.txt_dl_status = self.cmbDL_Status.currentText()
        self.wrkr_thd_1.start()

    def strt_wrkr_2(self):
        self.lblStatus.setText("Creating DAT File...")
        self.lblStatus.setStyleSheet('color: orange')
        self.wrkr_thd_3.txt_region = self.cmbRegion.currentText()
        self.wrkr_thd_3.txt_date_query = self.txtDate.text()
        self.wrkr_thd_2.start()

    def strt_wrkr_3(self):
        self.wrkr_thd_3.start()

    def strt_wrkr_4(self):
        filename = QFileDialog.getOpenFileName(self, 'Open a file', '', 'All Files (*.pkl*)')
        path = filename[0]
        if path != '':
            self.wrkr_thd_4.path_to_file = path
            self.wrkr_thd_4.start()

    def strt_wrkr_5(self):
        self.lblStatus.setText("Converting to DAT File")
        self.lblStatus.setStyleSheet("color: red")
        self.wrkr_thd_5.start()


    def on_jb_don_1(self, scList, dataList, resTxt, resColor):
        if resTxt == "Done Query":
            tableRow = 0
            self.tableWidget.setRowCount(len(scList))
            for att in scList:
                self.tableWidget.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(att))
                tableRow+=1
            self.setEna(False)
            self.wrkr_thd_2.txt_data_to_convert = dataList
            self.wrkr_thd_2.txt_region = self.cmbRegion.currentText()
        self.lblStatus.setText(resTxt)
        self.lblStatus.setStyleSheet(resColor)
        self.wrkr_thd_1.stop()

    def on_jb_don_2(self, resTxt, resColor):
        self.lblStatus.setText(resTxt)
        self.lblStatus.setStyleSheet(resColor)
        self.wrkr_thd_2.stop()
        self.setEna(True)

    def on_jb_don_3(self):
        self.wrkr_thd_3.stop()
    
    def on_jb_don_PBar(self, resInt):
        self.progressBar.setValue(resInt)

    def on_jb_don_4(self, resTxt, resColor, resBool, resDict):
        if resBool:
            count = 0
            for _ in resDict['data_json']:
                count = count + 1
            self.lblSCName.setText(resDict['sc_name'])
            self.lblDateQuery.setText(resDict['query_date'])
            self.lblNoRec.setText(str(count))
            self.setEna2(False)
            self.btnOpenFileD.setEnabled(False)
            self.btnPklToDat.setEnabled(True)
            self.wrkr_thd_5.list_of_att = resDict['data_json']
            self.wrkr_thd_5.txt_region = resDict['region_name']
        self.lblStatus.setText(resTxt)
        self.lblStatus.setStyleSheet(resColor)
        self.wrkr_thd_4.stop()

    def on_jb_don_5(self, resTxt, resColor):
        self.lblStatus.setText(resTxt)
        self.lblStatus.setStyleSheet(resColor)
        self.wrkr_thd_5.stop()

class thdFetchDataToMysql(QThread):
    res_to_emit = pyqtSignal(list, list, str, str)
    res_to_emit_timer = pyqtSignal(int)

    def __init__(self, parent=None):
        super(thdFetchDataToMysql, self).__init__(parent)

    def run(self):
        if self.txt_dl_status == 'not downloaded':
            txt_status = ''
        elif self.txt_dl_status == 'downloaded':
            txt_status = 'downloaded'
        else:
            txt_status = 'all'

        payload = json.dumps({
        "data": {
            "region_name": self.txt_region,
            "att_date": self.txt_date,
            "dl_status": txt_status,
        }
        })
        response = requests.request("POST", urlGetSCNames, headers=headers, data=payload)
        if response.text != "empty":
            responses = json.loads(response.text)
            list_sc = []
            list_j_data = []
            for response in responses:
                list_sc.append(response['sc_name'])#combine and store sale center name in a list 
                list_j_data.append(response['data_json'])#combine and store json data name in a list 

            res_list = []
            test12 = 0
            for ilist in list_j_data:
                for item in ilist:
                    if int(item["punch"]) <= 1:
                        resl = '%9s'%str(item["userID"])+'\t'+item["date"]+'\t'+"1"+'\t'+str(item["punch"])+'\t'+"1"+'\t'+"0"
                        res_list.append(resl)
                        test12 += 100 * 1/len(item)
                        self.res_to_emit_timer.emit(int(test12))
            self.res_to_emit.emit(list_sc, res_list, "Done Query", "color: green")
        else:
            self.res_to_emit.emit([], [], "Empty Query", "color: red")
                
    def stop(self):
        self.terminate()

class thdUpdateStatus(QThread):
    res_to_emit = pyqtSignal(str)

    def __init__(self, parent=None):
        super(thdUpdateStatus, self).__init__(parent)

    def run(self):
        url = urlUpdateStatus
        payload = json.dumps({
        "data": {
            "region_name": self.txt_region,
            "att_date": self.txt_date_query,
        }
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        self.res_to_emit.emit(response.text)

    def stop(self):
        self.terminate()

class thdConvertData(QThread):
    res_to_emit = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(thdConvertData, self).__init__(parent)

    def run(self):
        dateNow = date.today()
        filename = f"./SaveFiles/{dateNow.strftime('%m.%d.%Y')}.{self.txt_region}.dat"
        if not os.path.exists(os.path.dirname(filename)):#check if folder exist then creat if not
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(filename, "w") as outfile:
            for items in self.txt_data_to_convert:
                outfile.write("%s\n" % items)

        self.res_to_emit.emit("DAT File Created", "color: green")

    def stop(self):
        self.terminate()

class thdReadPickle(QThread):
    res_to_emit = pyqtSignal(str, str, bool, dict)

    def __init__(self, parent=None):
        super(thdReadPickle, self).__init__(parent)

    def run(self):
        with open(self.path_to_file, "rb") as outfile:
            try:
                loaded_file = pickle.load(outfile)
                self.res_to_emit.emit("Files Loaded", "color: green", True, loaded_file)
            except pickle.UnpicklingError as e:
                self.res_to_emit.emit(f"Error: Check File {e}", "color: red", False, {})

    def stop(self):
        self.terminate()

class thdConvPklToDatFile(QThread):
    res_to_emit = pyqtSignal(str, str)
    res_to_emit_timer = pyqtSignal(int)

    def __init__(self, parent=None):
        super(thdConvPklToDatFile, self).__init__(parent)

    def run(self):
        list_cvrted_dat = []
        countInt = 0
        for item in self.list_of_att:
            if int(item["punch"]) <= 1:
                resl = '%9s'%str(item["userID"])+'\t'+item["date"]+'\t'+"1"+'\t'+str(item["punch"])+'\t'+"1"+'\t'+"0"
                list_cvrted_dat.append(resl)
                countInt += 100 * 1/len(item)
                self.res_to_emit_timer.emit(int(countInt))

        dateNow = date.today()
        filename = f"./ConvertedFiles/{dateNow.strftime('%m.%d.%Y')}.{self.txt_region}.dat"
        if not os.path.exists(os.path.dirname(filename)):#check if folder exist then creat if not
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(filename, "w") as outfile:
            for item in list_cvrted_dat:
                outfile.write("%s\n" % item)

        self.res_to_emit.emit("Converted Succesfully", "color: green")

    def stop(self):
        self.terminate()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('closing window....')