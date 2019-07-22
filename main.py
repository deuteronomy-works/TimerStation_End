# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:03:47 2019

@author: Ampofo
"""
import sys
from PyQt5.QtGui import QGuiApplication

from PyQt5.QtQml import QQmlApplicationEngine

from func import SwitchKeys

app = QGuiApplication(sys.argv)
switch = SwitchKeys()
engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty('switcher', switch)
engine.load('UI/qml/main.qml')
engine.quit.connect(app.quit)

sys.exit(app.exec_())
