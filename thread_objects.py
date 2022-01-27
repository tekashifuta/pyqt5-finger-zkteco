from datetime import datetime
import json
from PyQt5.QtCore import QThread, pyqtSignal
from zk import ZK
import requests

headers = {
    'Content-Type': 'application/json',
}

urlSave = "http://localhost/Attendance_API/saveJsonAtt.php"

def to_json_get_all_attendance(msg): #convert into json format
    return {
        "userID": int(msg.user_id),
        "date": str(msg.timestamp),
        "status": str(msg.status),
        "punch": str(msg.punch)
    }

class trdLoadIfExist(QThread):
    res_to_emit = pyqtSignal(dict, bool, str, str)

    def __init__(self, parent=None):
        super(trdLoadIfExist, self).__init__(parent)

    def run(self):
        openfile = open('date.json', 'r')
        # Reading from json file
        openfile_obj = json.load(openfile)
        openfile.close()

        if (openfile_obj['date_from_1']['date'] != '' 
            and openfile_obj['date_to_1']['date'] != ''
            and openfile_obj['date_from_2']['date'] != ''
            and openfile_obj['date_to_2']['date'] != ''
            and openfile_obj['IP_add'] != ''
            and openfile_obj['Port_add'] != ''
            and openfile_obj['date_to_1']['month'] != ''
            and openfile_obj['date_to_1']['year'] != ''
            and openfile_obj['region'] != ''
        ):
            self.res_to_emit.emit(openfile_obj, False, 'Fetching data Done', 'color: green')
        else:
            self.res_to_emit.emit(openfile_obj, True, 'Error Fetching data', 'color: red')

    def stop(self):
        self.terminate()

class trdSetSettings(QThread):
    res_to_emit_bool_dict = pyqtSignal(bool, dict, str)
    res_to_emit_dict = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(trdSetSettings, self).__init__(parent)

    def run(self):
            conn = None
            zk = ZK(self.txt_IP, port=int(self.txt_PORT), timeout=5, password=0, force_udp=False, ommit_ping=False)
            try:
                conn = zk.connect()
                txt_year_1_new = int(self.txt_year) - 1 if (int(self.txt_month) == 1) else self.txt_year
                txt_month_1_new = 12 if(int(self.txt_month) == 1) else int(self.txt_month) - 1
                dicSettings = {
                    'IP_add' : str(self.txt_IP),
                    'Port_add' : str(self.txt_PORT),
                    'region' : str(self.txt_region),
                    'cut_off': '1',
                    'date_from_1':{   
                        'year': int(txt_year_1_new),
                        'month' : int(txt_month_1_new),
                        'date' : int(self.txt_from_1),
                    },
                    'date_to_1':{          
                        'year': int(self.txt_year), 
                        'month' : int(self.txt_month),
                        'date' : int(self.txt_to_1),
                    },
                    'date_from_2':{   
                        'year': int(self.txt_year),
                        'month' : int(self.txt_month),
                        'date' : int(self.txt_from_2),
                    },
                    'date_to_2':{          
                        'year': int(self.txt_year), 
                        'month' : int(self.txt_month),
                        'date' : int(self.txt_to_2),
                    },
                }

                # Serializing json 
                json_object = json.dumps(dicSettings, indent = 4)
                
                # Writing to sample.json
                with open("date.json", "w") as outfile:
                    outfile.write(json_object)

                self.res_to_emit_bool_dict.emit(False, dicSettings, 'Successfully Saved')
            except Exception as e:
                string_pas = "Process terminate : {} or can`t connect to device".format(e)
                self.res_to_emit_bool_dict.emit(True, {}, string_pas)

            finally:
                if conn:
                    conn.disconnect()

    def stop(self):
        self.terminate()

class trdAutoConnect(QThread):
    res_to_emit_status = pyqtSignal(bool, str)

    def __init__(self, parent=None):
        super(trdAutoConnect, self).__init__(parent)

    def run(self):
        conn = None
        zk = ZK(self.txt_IP, port=int(self.txt_PORT), timeout=5, password=0, force_udp=False, ommit_ping=False)
        try:
            conn = zk.connect()
            self.res_to_emit_status.emit(True, 'Connected')
        except Exception as e:
            string_pas = "Process terminate : {} or can`t connect to device".format(e)
            self.res_to_emit_status.emit(False, string_pas)

    def stop(self):
        self.terminate()

class trdGenData(QThread):
    res_to_emit_status = pyqtSignal(list, str, str, str, bool)

    def __init__(self, parent=None):
        super(trdGenData, self).__init__(parent)

    def run(self):
        openfile = open('date.json', 'r')
        # Reading from json file
        openfile_obj = json.load(openfile)
        openfile.close()

        if openfile_obj['cut_off'] == '1':
            dateFrom_fmt = str(openfile_obj['date_from_1']["year"]) + "-" + str(openfile_obj['date_from_1']["month"]) + "-" + str(openfile_obj['date_from_1']["date"])
            dateTo_fmt = str(openfile_obj['date_to_1']["year"]) + "-" + str(openfile_obj['date_to_1']["month"]) + "-" + str(openfile_obj['date_to_1']["date"])

            openfile_obj['cut_off'] = '2'
            openfile_obj['date_from_1']['year'] = openfile_obj['date_from_1']['year'] + 1 if (openfile_obj['date_from_1']['month'] == 12) else openfile_obj['date_from_1']['year']
            openfile_obj['date_from_1']['month'] = 1 if (openfile_obj['date_from_1']['month'] == 12) else openfile_obj['date_from_1']['month'] + 1 #edit the value
            
            openfile_obj['date_to_1']['year'] = openfile_obj['date_to_1']['year'] + 1 if (openfile_obj['date_to_1']['month'] == 12) else openfile_obj['date_to_1']['year']
            openfile_obj['date_to_1']['month'] = 1 if (openfile_obj['date_to_1']['month'] == 12) else openfile_obj['date_to_1']['month'] + 1 #edit the value

            # jsonOpen = open("date.json", "w+")
            # jsonOpen.write(json.dumps(openfile_obj, indent = 4)) #update the json
            # jsonOpen.close()

        elif openfile_obj['cut_off'] == '2':
            dateFrom_fmt = str(openfile_obj['date_from_2']["year"]) + "-" + str(openfile_obj['date_from_2']["month"]) + "-" + str(openfile_obj['date_from_2']["date"])
            dateTo_fmt = str(openfile_obj['date_to_2']["year"]) + "-" + str(openfile_obj['date_to_2']["month"]) + "-" + str(openfile_obj['date_to_2']["date"])

            openfile_obj['cut_off'] = '1'
            openfile_obj['date_from_2']['year'] = openfile_obj['date_from_2']['year'] + 1 if (openfile_obj['date_from_2']['month'] == 12) else openfile_obj['date_from_2']['year']
            openfile_obj['date_from_2']['month'] = 1 if (openfile_obj['date_from_2']['month'] == 12) else openfile_obj['date_from_2']['month'] + 1 #edit the value
            
            openfile_obj['date_to_2']['year'] = openfile_obj['date_to_2']['year'] + 1 if (openfile_obj['date_to_2']['month'] == 12) else openfile_obj['date_to_2']['year']
            openfile_obj['date_to_2']['month'] = 1 if (openfile_obj['date_to_2']['month'] == 12) else openfile_obj['date_to_2']['month'] + 1 #edit the value

            # jsonOpen = open("date.json", "w+")
            # jsonOpen.write(json.dumps(openfile_obj, indent = 4)) #update the json
            # jsonOpen.close()

        dateFrom_fmted = datetime.strptime(dateFrom_fmt, "%Y-%m-%d").strftime("%Y-%m-%d")
        dateTo_fmted = datetime.strptime(dateTo_fmt, "%Y-%m-%d").strftime("%Y-%m-%d")
        
        conn = None
        zk = ZK(openfile_obj['IP_add'], port=int(openfile_obj['Port_add']), timeout=5, password=0, force_udp=False, ommit_ping=False)

        try:
            conn = zk.connect()
            attendance = conn.get_attendance()
            res2 = [
                to_json_get_all_attendance(z) for z in attendance 
                if (
                    datetime.strftime(z.timestamp, "%Y-%m-%d") >= datetime.strptime(dateFrom_fmted, "%Y-%m-%d").strftime("%Y-%m-%d") 
                    and 
                    datetime.strftime(z.timestamp, "%Y-%m-%d") <= datetime.strptime(dateTo_fmted, "%Y-%m-%d").strftime("%Y-%m-%d")
                )
            ]

            if res2 != []:#dili ma save ang new date pag blank ang query
                jsonOpen = open("date.json", "w+")
                jsonOpen.write(json.dumps(openfile_obj, indent = 4)) #update the json
                jsonOpen.close()
                genDate = f'Generated Data From {dateFrom_fmt} To {dateTo_fmt}'
                self.res_to_emit_status.emit(res2, 'Succesfully Generated', 'color: green', genDate, True)
            else:
                genDate = f'From {dateFrom_fmt} To {dateTo_fmt}'
                self.res_to_emit_status.emit(res2, 'Succesfully Generated', 'color: green', genDate, False)
            
        except Exception as e:
            string_pas = "Process terminate : {} or can`t connect to device".format(e)
            self.res_to_emit_status.emit([], string_pas, 'color: red', 'Error')
        finally:
            if conn:
                conn.disconnect()

    def stop(self):
        self.terminate()

class trdSaveDataToFB(QThread):
    res_to_emit_status = pyqtSignal(str, str, str, int)

    def __init__(self, parent=None):
        super(trdSaveDataToFB, self).__init__(parent)

    def run(self):
        try:
            openfile = open('date.json', 'r')
            # Reading from json file
            openfile_obj = json.load(openfile)
            openfile.close()

            url = urlSave
            payload = json.dumps({
            "data": {
                "data_json": json.dumps(self.list_of_gen_date),
                "region_id": openfile_obj['region'],
                "sc_id": openfile_obj['region']
            }
            })
            response = requests.request("POST", url, headers=headers, data=payload)

            self.res_to_emit_status.emit(str(response), 'Successfully saved to Firebase', 'color: green', len(self.list_of_gen_date))
        except Exception as e:
            string_pas = "Process terminate : {} or can`t connect to device".format(e)
            # print(string_pas)
            self.res_to_emit_status.emit('Error', string_pas, 'color: red', 0)
            
    def stop(self):
        self.terminate()