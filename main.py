# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
from PyQt4 import QtGui, QtCore
from os.path import isfile
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_MainUI import Ui_MainFrom


class MainWindow(QWidget, Ui_MainFrom):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)

    @pyqtSignature("")
    def on_btnImageOpen_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        imageaddressfd = QtGui.QFileDialog(self)
        self.imageaddressfilename = imageaddressfd.getOpenFileName()
        if isfile(self.imageaddressfilename):
            imageaddresstext = open(self.imageaddressfilename).read()
            self.ImageAddressField.setPlainText(imageaddresstext)

    @pyqtSignature("")
    def on_btnImageGenerate_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_btnImageSearch_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_btnWaypointSend_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_btnWaypointAccomplish_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_btnCameraPicture_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_btnCameraVideo_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_btnOpen3d_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        open3dfd = QtGui.QFileDialog(self)
        self.open3dfilename = open3dfd.getOpenFileName()
        if isfile(self.open3dfilename):
            open3dtext = open(self.open3dfilename).read()
            self.ThreedViewField.setGraphicsEffect(open3dtext)

    @pyqtSignature("")
    def on_btnImport_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_btnSetting_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_btnCheck_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
