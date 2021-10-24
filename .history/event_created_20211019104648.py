from numpy import angle
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
            self.ui.status.adjustSize()

    def disconnectFunction(self):
        if self.ui.ser.isOpen():
            self.ui.ser.close()
            self.ui.status.setText("Disconnected")
            self.ui.status.adjustSize()
        else:
            self.ui.status.setText("Disconnected")
            self.ui.status.adjustSize()

    def sendInformation(self):
        """
        Encoding messages to send to Serial connected devices
        """
        if self.ui.ser.isOpen():
            ############### FORMAT STRING TO ENCODE ##################
            angle = self.ui.inp_angle.text()
            timing_on = self.ui.inp_ton.text()
            timing_off = self.ui.inp_toff.text()
            messages = str(angle + "," + timing_on + "," + timing_off).strip()
            print(messages)
            ##########################################################

            ################# SENDING MESSAGES ######################
            self.ui.ser.write(messages.encode())
            self.ui.ser.flushInput()
            #########################################################

    def readInformation(self):
        """
        reading messages recives from the device response
        """
        if self.ui.ser.isOpen():
            data = self.ui.ser.readline().decode()
            self.ui.ser.flushInput()

            ############## EXTRACT INFORMATION TO THE LINE EDIT######
            messages = data.strip().split(",")
            self.ui.out_angle.setText(messages[0])
            self.ui.out_duty.setText(messages[1])
            self.ui.out_count.setText(messages[2])

