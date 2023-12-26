from Phidget22.Phidget import *
from Phidget22.Devices.LCD import *
from Phidget22.Devices.VoltageInput import *

import time


def onVoltageChange(voltage):
    global lcd0
    print("Voltage: " + str(voltage))
    
    #Ecriture sur le LCD
    lcd0.clear()
    lcd0.writeText(LCDFont.FONT_5x8, 0, 0, str(voltage) + "V")
    lcd0.flush()


## l'affchage sur l'cran LCD de la tension analogique provenant du potentiomtre 
if __name__ == "__main__":
    lcd0 = LCD()

    lcd0.openWaitForAttachment(5000)
    lcd0.setBacklight(1)
    voltageInput0 = VoltageInput()
    voltageInput0.setOnVoltageChangeHandler(onVoltageChange)
    voltageInput0.openWaitForAttachment(5000)


    try:
        input("Press Enter to Stop\n")
    except (Exception, KeyboardInterrupt):
        pass
    lcd0.close()