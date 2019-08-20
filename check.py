import threading
from urllib.request import urlopen
from time import sleep, time
import json
from PyQt5.QtCore import QObject, pyqtSlot as Slot, pyqtSignal as Signal

class Checker(QObject):


    def __init__(self):
        QObject.__init__(self)
        self.ip = "http://localhost"
        self.name = "timer"
        self.curr_time = 0
        self.terminate = False
        self.check_for_time()

    setTime = Signal(str, arguments=["_check_for_time"])
    startSession = Signal(str, arguments=["_set_pause"])

    def registerClient(self):
        reg_thread = threading.Thread(target=self._registerClient)
        reg_thread.daemon = True
        reg_thread.start()

    def _registerClient(self):
        pass

    def check_for_time(self):
        self.terminate = False
        chkTm_thread = threading.Thread(target=self._check_for_time)
        chkTm_thread.daemon = True
        chkTm_thread.start()

    def _check_for_time(self):

        while True and not self.terminate:
            url = self.ip + "/" + self.name + "/" + "777.json"
            resp = urlopen(url)
            data = resp.read()
            info = data.decode('utf-8')

            if info:
                time_info = json.loads(info)
                self.calculate_time(time_info)
                self.set_pause()
                break
            else:
                pass

    def calculate_time(self, times):
        # set time
        today_time = int(times["end_time"]) - time()
        self.curr_time = today_time

        # start thread
        calc_time = threading.Thread(target=self._calculate_time)
        calc_time.daemon = True
        calc_time.start()

    def _calculate_time(self):
        while True and not self.terminate:
            sleep(1)
            self.curr_time -= 1
            sec = self.curr_time
            mins = sec / 60
            hrs = mins / 60
            mini = (hrs - int(hrs)) * 60
            secs = (mini - int(mini)) * 60
            # mSecs = (secs - int(secs)) * 60
            hrs_str = str(int(hrs)) + ":" + str(int(mini)) + ":" + str(int(secs))
            self.setTime.emit(hrs_str)

    def set_pause(self):
        setP_thread = threading.Thread(target=self._set_pause)
        setP_thread.daemon = True
        setP_thread.start()

    def _set_pause(self):
        sleep(2.9)
        self.startSession.emit('')

    def check_for_info(self):
        chkIn_thread = threading.Thread(target=self._check_for_info)
        chkIn_thread.daemon = True
        chkIn_thread.start()

    def _check_for_info(self):
        pass
