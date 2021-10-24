import sys
import platform
import serial.tools.list_ports
import serial
import matplotlib
from matplotlib import cm

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.animation import FuncAnimation

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (
    QCoreApplication,
    QPropertyAnimation,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
    QEvent,
)
from PyQt5.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot

import warnings

warnings.filterwarnings("ignore")

from app_modules import *


class Display_2D(FigureCanvas):
    def __init__(self, parent=None, width=150, height=100, dpi=75):
        figure = Figure(figsize=(width, height), dpi=dpi)
        style.use("seaborn-notebook")
        figure.tight_layout()
        super(Display_2D, self).__init__(figure)
        self.axes = figure.add_subplot(111)

    def config_display_2D(self, widget):
        widget.axes.grid(True)
        widget.axes.tick_params(axis="x", colors="black")
        widget.axes.tick_params(axis="y", colors="black")


class MainWindow(QMainWindow):
    def __init__(self):
        ## IMPORT MAIN WINDOWN USER INTERFACE ##
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ########################################

        ########## INITIALIZE CONNECTION #######
        self.ui.ser = serial.Serial()
        self.timer = QtCore.QTimer()
        ########################################
        uiConfig.Configuration(self)
        ######### INITIALIZE MATPLOT ###########
        self.plot_1 = Display_2D(self)
        self.plot_1.config_display_2D(self.plot_1)
        self.plot_2 = Display_2D(self)
        self.plot_2.config_display_2D(self.plot_2)
        #######################################

        ########### BUTTON EVENT ###############
        self.ui.btn_connect.clicked.connect(lambda: guiEvent.connectFunction(self))
        self.ui.btn_diconnect.clicked.connect(lambda: guiEvent.disconnectFunction(self))
        self.ui.btn_send.clicked.connect(lambda: guiEvent.sendInformation(self))
        self.timer.timeout.connect(lambda: guiEvent.readInformation(self))
        self.timer.timeout.conenct(lambda: guiEvent.plot_realtime(self))
        self.timer.start(100)


## CODE RUNNING ##
if __name__ == "__main__":
    display = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(display.exec_())
