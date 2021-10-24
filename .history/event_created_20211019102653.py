from app_modules import Ui_MainWindow, MainWindown


class guiEvent(MainWindown):
    def connectInitial(self, port, baudrate):
        self.ui.ser.port = port
        self.ui.ser.baudrate = baudrate
        self.ui.ser.bytesize = serial.EIGHTBITS  # number of bits per bytes
        self.ui.ser.parity = serial.PARITY_NONE  # set parity check: no parity
        self.ui.ser.stopbits = serial.STOPBITS_ONE  # number of stop bits
        self.ui.ser.xonxoff = False  # disable software flow control
        self.ui.ser.rtscts = False  # disable hardware (RTS/CTS) flow control
        self.ui.ser.dsrdtr = False  # disable hardware (DSR/DTR) flow control
        self.ui.ser.writeTimeout = 0  # timeout for write
        self.ui.ser.timeout = 10
        self.ui.ser.open()

    def connectFunction(self):
        port = self.ui.port.currentText()
        baudrate = self.ui.baud.currenText()
        guiEvent.connectInitial(self, port, baudrate)

        if self.ui.ser.isOpen():
            self.ui.status.setText("Connected to " + self.ui.port.currentText())

