from datetime import date
import errno
import json
import os
import sys
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from os.path import exists
import requests

headers = {
    'Content-Type': 'application/json',
}
urlGetData = "http://localhost/Attendance_API/selectJsonAtt.php"

region_list = ["Blank", "CVO1", "CVO2", "CVO3", "EVO1", "EVO2", "EVO3", "NLO1", "NMO1", "NMO2", "OOC1", "SLO1", "SMO1", "SMO2", "WMO1", "WMO2", "WVO1", "WVO2"]

def to_json_get_all_attendance(msg): #convert into json format
    return {msg.userID+" "+msg.date+" "+"1"+" "+"0"+" "+msg.punch+" "+"0"}

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('fetching.ui', self)
        self.setWindowTitle("Test App")
        self.setContentsMargins(10, 10, 10, 10)
        self.setFixedSize(351, 176) # set fixed size of the main window
        self.progressBar.setProperty("value", 0)
        self.cmbRegion.addItems(region_list)

        self.btnGetData.clicked.connect(self.strt_wrkr_1)
        self.worker_thread_1 = thdGetDataFromMysql()
        self.worker_thread_1.res_to_emit_status.connect(self.onJobDone1)
        self.worker_thread_1.res_to_emit_timer.connect(self.onJobDone1Timer)

        self.worker_thread_2 = thdConvertData()
        self.worker_thread_2.res_to_emit_status.connect(self.onJobDone2)
        

    def strt_wrkr_1(self):
        self.lblStatus.setText('Fetching Data into Mysql')
        self.cmbRegion.setEnabled(False)
        self.btnGetData.setEnabled(False)
        self.worker_thread_1.txt_region = self.cmbRegion.currentText()
        self.worker_thread_1.start()
    
    def onJobDone1(self, resDict, resStatus, resStatColor, resRegion, resBool):
        if resBool:#Check if it has data
            self.worker_thread_2.txt_data_to_convert = resDict
            self.worker_thread_2.txt_region = resRegion
            self.worker_thread_2.start()#start the second thread to make convert data
        self.cmbRegion.setEnabled(True)
        self.btnGetData.setEnabled(True)    
        self.lblStatus.setText(resStatus)
        self.lblStatus.setStyleSheet(resStatColor)    
        self.worker_thread_1.stop()


    def onJobDone2(self, resData):
        self.worker_thread_2.stop()

    def onJobDone1Timer(self, resInt):
        # print(resInt)
        self.progressBar.setValue(resInt)

class thdGetDataFromMysql(QThread):
    res_to_emit_status = pyqtSignal(list, str, str, str, bool)
    res_to_emit_timer = pyqtSignal(int)

    def __init__(self, parent=None):
        super(thdGetDataFromMysql, self).__init__(parent)

    def run(self):
        url = urlGetData
        payload = json.dumps({
        "data": {
            "region_id": self.txt_region
        }
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        
        res_list = []
        test12 = 0
        if response.text != "empty":
            items = json.loads(response.text)
            for item1 in items:
                for item in item1:
                    # resl = "{0:>9s} {1:>15s} {2:>1} {3:>1} {4:>1} {5:>1}".format(str(item["userID"]), str(item["date"]), item["status"], 0, (item["punch"] if (item["punch"] == 1) else 1), 0)
                    resl = '%9s'%str(item["userID"])+'\t'+item["date"]+'\t'+"1"+'\t'+str(item["punch"])+'\t'+"1"+'\t'+"0"
                    res_list.append(resl)
                    test12 += 100 * 1/100
                    self.res_to_emit_timer.emit(test12)
            # print(test12)
            self.res_to_emit_status.emit(res_list, 'Done Fetching Data...', 'color: green', self.txt_region, True) 
        else:
            self.res_to_emit_status.emit(res_list, 'No data Exists', 'color: red', self.txt_region, False)

    def stop(self):
        self.terminate()

class thdConvertData(QThread):
    res_to_emit_status = pyqtSignal(str)

    def __init__(self, parent=None):
        super(thdConvertData, self).__init__(parent)

    def run(self):
        dateNow = date.today()
        filename = f"../SaveFiles/{dateNow.strftime('%m.%d.%Y')}.{self.txt_region}.dat"
        if not os.path.exists(os.path.dirname(filename)):#check if folder exist then creat if not
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(filename, "w") as outfile:
            for items in self.txt_data_to_convert:
                outfile.write("%s\n" % items)

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