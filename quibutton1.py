#!/usr/bin/python
#encoding=utf-8
# quitbutton.py
import sys
from PyQt4 import QtGui, QtCore
# TODO jfksldjflsjdf
class QuitButton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 250, 150)
		# self.setWindowTitle('Quit button')
        quit = QtGui.QPushButton('Close!', self)
        self.setGeometry(300, 300, 250, 150)
        self.connect(quit, QtCore.SIGNAL('clicked()'),
        QtGui.qApp, QtCore.SLOT('quit()'))
app = QtGui.QApplication(sys.argv)
qb = QuitButton()
qb.show()
sys.exit(app.exec_())
