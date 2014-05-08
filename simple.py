#!/usr/bin/python
#coding=utf-8
#simple.py

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle(u'中文')
widget.show()

sys.exit(app.exec_())
