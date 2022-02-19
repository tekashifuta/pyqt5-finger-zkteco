from datetime import date, datetime
import errno
import json
from operator import truediv
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

import http.client as httplib
import wmi
c=wmi.WMI()
o=c.query("select * from Win32_NetworkAdapter")

def have_internet():
    conn = httplib.HTTPSConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        return True
    except Exception:
        return False
    finally:
        conn.close()


class thdSaveSettings(QThread):
    res_to_emit = pyqtSignal(dict, str, str)

    def __init__(self, parent=None):
        super(thdSaveSettings, self).__init__(parent)

    def run(self):
        conn = None
        zk = ZK(self.txt_ip, port=int(self.txt_port), timeout=5, password=0, force_udp=False, ommit_ping=False)
        # if self.txt_mode == 'Default':
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
            os.system(f"attrib +h date.json")
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
        with open('date.json', 'r') as openfile:
            openfile_obj = json.load(openfile)

        self.res_to_emit.emit(openfile_obj, "Data Paired", "color: green")

    def stop(self):
        self.terminate()

class thdConnZkteco(QThread):
    res_to_emit = pyqtSignal(str, str, bool)

    def __init__(self, parent=None):
        super(thdConnZkteco, self).__init__(parent)

    def run(self):
        conn = None
        zk = ZK(self.txt_ip, port=int(self.txt_port), timeout=5, password=0, force_udp=False, ommit_ping=False)
        try:
            conn = zk.connect()
            self.res_to_emit.emit("Connected", "color: green", True)

        except Exception as e:
            string_pas = "{}".format(e)
            self.res_to_emit.emit(string_pas, "color: red", False)

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
        date_now = datetime.strptime(self.date_new, "%m/%d/%Y").strftime("%Y-%m-%d")
        try:
            conn = zk.connect()
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
    res_to_emit = pyqtSignal(str, str, bool)

    def __init__(self, parent=None):
        super(thdSaveToMysql, self).__init__(parent)

    def run(self):
        with open('date.json', 'r') as openfile:
            openfile_obj = json.load(openfile)

        url = urlSave
        payload = json.dumps({
            "data": {
                "data_json": json.dumps(self.data_to_save),
                "region_name": openfile_obj['set_region'],
                "sc_name": openfile_obj['set_scname'],
                "att_date": self.date_query
            }
            })

        # if self.txt_mode == 'Tether':
        #     os.system(f'netsh interface set interface "Ethernet" disable')
        #     os.system(f'netsh interface set interface "Ethernet 2" Enable')
        #     os.system(f'netsh interface ip set address "Ethernet 2" dhcp')
        #     if have_internet():
        #         response = requests.request("POST", url, headers=headers, data=payload)
        #     else:
        #         resTxt = "Can't Connect To Internet"
        #         resColor = "color: red"
        # else:
        if have_internet():
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.text == "existing":
                resTxt = "Existing Data..."
                resColor = "color: red"
            else:
                resTxt = "Done Saving"
                resColor = "color: green"
            self.res_to_emit.emit(resTxt, resColor, True)    
        else:
            resTxt = "Check your Internet or Tether connection"
            resColor = "color: red"
            self.res_to_emit.emit(resTxt, resColor, False)
        
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
        dateNew = datetime.strptime(self.date_query, '%Y-%m-%d').strftime('%Y.%m.%d')
        filename = f"./DownloadFiles/{dateNew}_{self.txt_region}.pkl"
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

# class thdChangeConn(QThread):
#     res_to_emit = pyqtSignal(str, str, str, str)

#     def __init__(self, parent=None):
#         super(thdChangeConn, self).__init__(parent)

#     def run(self):
#         networksNames = [x for x in o if x.PhysicalAdapter and x.NetConnectionID.startswith("Ethernet")]
#         for netConn in networksNames:
#             if netConn.NetConnectionID == 'Ethernet':
#                 if self.btn_txt == "Disable":
#                     os.system(f'netsh interface set interface "{netConn.NetConnectionID}" disable')
#                     self.res_to_emit.emit("Ethernet Disabled", "color: orange", "Ethernet Disabled", "Enable")
#                 else:
#                     os.system(f'netsh interface set interface "{netConn.NetConnectionID}" enable')
#                     self.res_to_emit.emit("Ethernet Enabled", "color: green", "Ethernet Enabled", "Disable")
#         # getoutput = self.txt_ip.split('.')[2:]
#         # new_ip = '.'.join(self.txt_ip.split('.')[:-1]+[str(int(getoutput[1])+1)])#change the 4th octet
#         # new_subnet = '255.255.255.0'
#         # new_gateway = '.'.join(self.txt_ip.split('.')[:-2]+[getoutput[0], "1"])#change the 3rd and 4th octet
#         # disableNet = [x.NetConnectionID for x in o if x.PhysicalAdapter and not x.NetEnabled and x.NetConnectionID.startswith("Ethernet")]
#         # os.system(f'netsh interface ip set address Ethernet static {new_ip} {new_subnet} {new_gateway}')
        
#     def stop(self):
#         self.terminate()

class thdNetChecker(QThread):
    res_to_emit = pyqtSignal(str, str, bool)

    def __init__(self, parent=None):
        super(thdNetChecker, self).__init__(parent)

    def run(self):
        if have_internet():
            self.res_to_emit.emit("Connected to Internet", "color: green", True)
        else:
            self.res_to_emit.emit("Unreachable Connection", "color: red", True)

    def stop(self):
        self.terminate()