# -*- coding:Latin-1 -*-
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageInput import *
import time

def onVoltageChange(self, voltage):
    print("Voltage: " + str(voltage))

if __name__ == "__main__":
    #lcd0 = LCD()

    #lcd0.setBacklight(1)
    voltageInput0 = VoltageInput()
    voltageInput0.setOnVoltageChangeHandler(onVoltageChange)
    voltageInput0.openWaitForAttachment(5000)
    try:
        input("Press Enter to Stop\n")
    except (Exception, KeyboardInterrupt):
        pass
    voltageInput0.close()

