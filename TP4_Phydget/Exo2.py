from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *
import time

if __name__ == "__main__":
    portOuput = []
    for i in range(8):
        port = DigitalOutput()
        portOuput.append(port)
        portOuput[i].setChannel(i)
        portOuput[i].openWaitForAttachment(5000)

    #TO DO: allumage des leds
    period = 0.5
    for j in range(5):
        for i in range(8):
            portOuput[i].setDutyCycle(1)
            time.sleep(period)

        for i in range(7,-1,-1):
            portOuput[i].setDutyCycle(0)
            time.sleep(period)
    
    try:
        input("Press Enter to Stop\n")
    except (Exception, KeyboardInterrupt):
           pass

    for i in range(8):
        portOuput[i].close()
