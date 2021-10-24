from serial.tools.list_ports_windows import comports
from app_modules import *
import serial.tools.list_ports


class uiConfig(MainWindown):
    def generated_port(self):
        """
        List all comm port available in devices manager
        """
        ports = serial.tools.list_ports.comports()
        self.comPort = [
            comport.device for comport in serial.tools.list_ports.comports()
        ]
        count = len(self.comPort)
        if count == 0:
            pass
        elif count == 1:
            self.ui.port.addItem(str(self.comPort[0]))
        else:
            self.ui.port.addItem(str(self.commPort[0]))
            self.ui.port.addItem(str(self.commPort[1]))

    def Configuration(self):
        if not self.ui.ser.isOpen():
            self.ui.btn_diconnect.setEnable(False)

        uiConfig.generated_port(self)
        self.ui.inp_angle.setText("0.0")
        self.ui.inp_ton.setText("0.0")
        self.ui.inp_toff.setText("0.0")

