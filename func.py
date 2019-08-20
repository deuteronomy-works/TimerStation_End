# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:10:11 2019

@author: Ampofo
"""
import os
import threading

from PyQt5.QtCore import QObject, pyqtSlot as Slot, pyqtSignal as Signal

class SwitchKeys(QObject):


    def __init__(self):
        QObject.__init__(self)
        self.bin_folder = "bin"
        self.status = ""

    @Slot()
    def turnOn(self):
        on_thread = threading.Thread(target=self._turnOn)
        on_thread.daemon = True
        on_thread.start()

    def _turnOn(self):
        # turn on
        self.status = "turning on"
        print(self.status)
        cmd = self.bin_folder + "\\WinKill.exe"
        os.system(cmd)
        self.status = "turned on"

    @Slot()
    def turnOff(self):
        pass

    def _turnOff(self):
        pass
