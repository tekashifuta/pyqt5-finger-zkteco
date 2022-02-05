from datetime import date, datetime
import errno
import json
import os
import pickle
from PyQt5.QtCore import QThread, pyqtSignal
from zk import ZK
import requests

headers = {
    'Content-Type': 'application/json',
}

# urlSave = "http://localhost/prycegas_att/saveJsonAtt.php"
urlSave = "http://attendance.prycegas.com/prycegas_att/saveJsonAtt_v1.php"

def to_json_get_all_attendance(msg): #convert into json format
    return {
        "userID": int(msg.user_id),
        "date": str(msg.timestamp),
        "status": str(msg.status),
        "punch": str(msg.punch)
    }


class thdSaveSettings(QThread):
    res_to_emit = pyqtSignal(dict, str, str)

    def __init__(self, parent=None):
        super(thdSaveSettings, self).__init__(parent)

    def run(self):
        conn = None
        zk = ZK(self.txt_ip, port=int(self.txt_port), timeout=5, password=0, force_udp=False, ommit_ping=False)
        try:
            conn = zk.connect()
            dictSett = {
                'set_ip': self.txt_ip,
                'set_port': self.txt_port,
                'set_region': self.txt_region,
                'set_scname': self.txt_scname
            }

            # Serializing json 
            json_object = json.dumps(dictSett, indent = 4)
            # Writing to sample.json
            with open("date.json", "w") as outfile:
                outfile.write(json_object)
            self.res_to_emit.emit(dictSett, "Data Saved", "color: green")

        except Exception as e:
            string_pas = "{}".format(e)
            self.res_to_emit.emit({}, string_pas, "color: red")

        finally:
            if conn:
                conn.disconnect()

    def stop(self):
        self.terminate()

class thdLoadData(QThread):
    res_to_emit = pyqtSignal(dict, str, str)

    def __init__(self, parent=None):
        super(thdLoadData, self).__init__(parent)

    def run(self):
        openfile = open('date.json', 'r')
        # Reading from json file
        openfile_obj = json.load(openfile)
        openfile.close()

        self.res_to_emit.emit(openfile_obj, "Data Loaded", "color: green")

    def stop(self):
        self.terminate()

class thdConnZkteco(QThread):
    res_to_emit = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(thdConnZkteco, self).__init__(parent)

    def run(self):
        conn = None
        zk = ZK(self.txt_ip, port=int(self.txt_port), timeout=5, password=0, force_udp=False, ommit_ping=False)
        try:
            conn = zk.connect()
            self.res_to_emit.emit("Connected", "color: green")

        except Exception as e:
            string_pas = "{}".format(e)
            self.res_to_emit.emit(string_pas, "color: red")

        finally:
            if conn:
                conn.disconnect()

    def stop(self):
        self.terminate()

class thdFetchAttendance(QThread):
    res_to_emit = pyqtSignal(list, str, str, str)

    def __init__(self, parent=None):
        super(thdFetchAttendance, self).__init__(parent)

    def run(self):
        conn = None
        zk = ZK(self.txt_ip, port=int(self.txt_port), timeout=5, password=0, force_udp=False, ommit_ping=False)
        try:
            conn = zk.connect()
            date_fmt = str(self.txt_year) + "-" + str(self.txt_month) + "-" + str(self.txt_day)
            date_now = datetime.strptime(date_fmt, "%Y-%m-%d").strftime("%Y-%m-%d")
            attendance = conn.get_attendance()
            res2 = [
                to_json_get_all_attendance(z) for z in attendance if (datetime.strftime(z.timestamp, "%Y-%m-%d") == date_now)
            ]
            # res2 = [
            #     to_json_get_all_attendance(z) for z in attendance if z.user_id == '9671' and datetime.strftime(z.timestamp, "%Y-%m-%d") == datetime.strptime("2022-01-25", "%Y-%m-%d").strftime("%Y-%m-%d")
            # ]
            self.res_to_emit.emit(res2, "Done", "color: green", date_now)

        except Exception as e:
            string_pas = "{}".format(e)
            self.res_to_emit.emit([], string_pas, "color: red", date_now)

        finally:
            if conn:
                conn.disconnect()

    def stop(self):
        self.terminate()

class thdSaveToMysql(QThread):
    res_to_emit = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(thdSaveToMysql, self).__init__(parent)

    def run(self):
        openfile = open('date.json', 'r')
        # Reading from json file
        openfile_obj = json.load(openfile)
        openfile.close()

        url = urlSave
        payload = json.dumps({
        "data": {
            "data_json": json.dumps(self.data_to_save),
            "region_name": openfile_obj['set_region'],
            "sc_name": openfile_obj['set_scname'],
            "att_date": self.date_query
        }
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.text == "existing":
            resTxt = "Existing Data..."
            resColor = "color: red"
        else:
            resTxt = "Done Saving"
            resColor = "color: green"
        
        self.res_to_emit.emit(resTxt, resColor)
    
    def stop(self):
        self.terminate()

class thdSaveLocalDB(QThread):
    res_to_emit = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(thdSaveLocalDB, self).__init__(parent)

    def run(self):
        dictToSave = {
            "region_name": self.txt_region,
            "sc_name": self.txt_sc_name,
            "query_date": self.date_query,
            "data_json": self.data_to_save
        }
        dateNow = date.today()
        filename = f"./DownloadFiles/{dateNow.strftime('%m.%d.%Y')}.{self.txt_region}.pkl"
        if not os.path.exists(os.path.dirname(filename)):#check if folder exist then creat if not
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(filename, "wb") as outfile:
            pickle.dump(dictToSave, outfile)

        self.res_to_emit.emit("OK Check DownloadFiles", "color: green")

    def stop(self):
        self.terminate()