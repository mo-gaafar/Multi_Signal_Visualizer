import string
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QFileDialog, QScrollBar, QComboBox
from pyparsing import null_debug_action

from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys

from main import MainWindow

# Global Interface Variables
LabelTextBox = "null"


CineSpeed = 1  # from 0.1 to 10x

CurrentChannelProperty = 0
ChannelPropertiesArr = []


class ChannelProperties:

    def __init__(self, Label="Unlabeled", LineColour=0xFFFF00, IsHidden=True, Filename="null"):
        self.Label = Label
        self.LineColour = LineColour
        self.IsHidden = IsHidden
        #self.Filename = Filename


for ForCount in range(3):
    ChannelPropertiesArr.append(ChannelProperties)
    print(ChannelPropertiesArr[ForCount])
# Global plot channel object that contains related attributes


def printbtengan():
    print("brengan")


class SpectrogramProperties:
    def __init__(self, FreqRangeMax=1000, FreqRangeMin=0, SelectedChannel=1, SelectedTheme="Default"):
        self.FreqRangeMax = FreqRangeMax
        self.FreqRangeMin = FreqRangeMin

        self.SelectedChannel = SelectedChannel
        self.SelectedTheme = SelectedTheme

# Initializes all event triggers


def initConnectors(self):

    # Browse button
    self.BrowseButton = self.findChild(QPushButton, "BrowseButton")
    self.BrowseButton.clicked.connect(self.Browse)

    # Export Button
    self.ExportBtn = self.findChild(QPushButton, "ExportBtn")
    self.ExportBtn.clicked.connect(self.ExportPDF)

    # Zoom Buttons
    self.ZoomIn = self.findChild(QPushButton, "ZoomIn")
    self.ZoomIn.clicked.connect(self.ZoomIn)

    self.ZoomOut = self.findChild(QPushButton, "ZoomOut")
    self.ZoomOut.clicked.connect(self.ZoomOut)

    # Current Property Channel Updater (on index change note : channel 1 = 0 )
    self.ChannelsMenu = self.findChild(QComboBox, "ChannelsMenu")
    # self.ChannelsMenu.currentIndexChanged.()

    # Step 1: update CurrentChannelProperty variable with ChannelsMenu CurrentIndex
    # Step 2:
    # Step 3:

    self.ChannelsMenu.currentIndexChanged.connect(lambda: printbtengan())

    # Select Signal Colour Button
    self.SignalColour = self.findChild(QPushButton, "SignalColour")
    self.SignalColour.clicked.connect(lambda: printbtengan())