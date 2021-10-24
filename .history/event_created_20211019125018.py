import numpy as np
from main import MainWindow
import serial


class guiEvent(MainWindow):
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
        if (
            self.ui.port.currentText() != "Arduino Port"
            and self.ui.port.currentText() != ""
        ):
            port = self.ui.port.currentText()
            baudrate = self.ui.baud.currentText()
            guiEvent.connectInitial(self, port, baudrate)

            if self.ui.ser.isOpen():
                self.ui.status.setText("Connected to " + self.ui.port.currentText())
                self.ui.status.adjustSize()

    def disconnectFunction(self):
        if self.ui.ser.isOpen():
            self.ui.ser.close()
            self.ui.status.setText("Disconnected")
            self.ui.status.adjustSize()
            self.ui.btn_diconnect.setEnabled(False)
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
            ############## EXTRACT INFORMATION TO THE LINE EDIT######
            messages = data.strip().split(",")
            self.ui.out_angle.setText(messages[0])
            self.ui.out_duty.setText(messages[1])
            self.ui.out_count.setText(messages[2])

    def generated_plot_angle(self):
        """
        Function to plot Data from Actual Angle and Duty Cycle Changing on 2D visualization....
        """
        self.y = float(self.ui.out_angle.text())
        self.x = float(self.ui.out_count.text())
        self.plot_1.axes.plot(self.x, self.y, color=(0, 1, 0.29))
        self.plot_1.axes.yaxis.grid(True, linestyle="--")
        self.plot_1.axes.set_ylim(ymin=0, ymax=360)
        self.plot_1.draw()

    def generated_plot_duty(self):
        """
        Function to plot Data from Actual Angle and Duty Cycle Changing on 2D visualization....
        """
        try:
            self.y = float(self.ui.out_duty.text())
            self.x = float(self.ui.out_count.text())
            if not np.nan(self.ydata):

                self.plot_2.axes.plot(self.x, self.y, color=(0, 1, 0.29))
                self.plot_2.axes.yaxis.grid(True, linestyle="--")
                self.plot_2.axes.set_ylim(ymin=0, ymax=100)
                self.plot_2.draw()
        except:
            pass

    def plot_realtime(self):
        if self.ui.ser.isOpen():
            guiEvent.generated_plot_angle(self)
            guiEvent.generated_plot_duty(self)

