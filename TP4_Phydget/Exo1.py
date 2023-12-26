from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *
import time

# allumage successivement tous les bits du port de sortie en respectant un intervalle de temps de 0.5 seconde entre chaque bit
# *****************************************************************************************************************************
if __name__ == "__main__":

	digitalOutput0 = DigitalOutput()
	digitalOutput0.setChannel(0)
	digitalOutput0.openWaitForAttachment(5000) #ouvrir le port 

	digitalOutput0.setDutyCycle(1)
	time.sleep(0.50)

	digitalOutput1 = DigitalOutput()
	digitalOutput1.setChannel(1)
	digitalOutput1.openWaitForAttachment(5000)
	
	digitalOutput1.setDutyCycle(1)
	time.sleep(0.50)

	digitalOutput2 = DigitalOutput()
	digitalOutput2.setChannel(2)
	digitalOutput2.openWaitForAttachment(5000)

	digitalOutput2.setDutyCycle(1)
	time.sleep(0.50)

	digitalOutput3 = DigitalOutput()
	digitalOutput3.setChannel(3)
	digitalOutput3.openWaitForAttachment(5000)

	digitalOutput3.setDutyCycle(1)
	time.sleep(0.50)

	digitalOutput4 = DigitalOutput()
	digitalOutput4.setChannel(4)
	digitalOutput4.openWaitForAttachment(5000)

	digitalOutput4.setDutyCycle(1)
	time.sleep(0.50)

	digitalOutput5 = DigitalOutput()
	digitalOutput5.setChannel(5)
	digitalOutput5.openWaitForAttachment(5000)

	digitalOutput5.setDutyCycle(1)
	time.sleep(0.50)

	digitalOutput6 = DigitalOutput()
	digitalOutput6.setChannel(6)
	digitalOutput6.openWaitForAttachment(5000)

	digitalOutput6.setDutyCycle(1)
	time.sleep(0.50)

	digitalOutput7 = DigitalOutput()
	digitalOutput7.setChannel(7)
	digitalOutput7.openWaitForAttachment(5000)

	digitalOutput7.setDutyCycle(1)
	time.sleep(0.50)

	digitalOutput7.setDutyCycle(0)
	time.sleep(0.5)
	digitalOutput7.close()

	digitalOutput6.setDutyCycle(0)
	time.sleep(0.5)
	digitalOutput6.close()

	digitalOutput5.setDutyCycle(0)
	time.sleep(0.5)
	digitalOutput5.close()	

	digitalOutput4.setDutyCycle(0)
	time.sleep(0.5)
	digitalOutput4.close()

	digitalOutput3.setDutyCycle(0)
	time.sleep(0.5)
	digitalOutput3.close()

	digitalOutput2.setDutyCycle(0)
	time.sleep(0.5)
	digitalOutput2.close()
	
	digitalOutput1.setDutyCycle(0)
	time.sleep(0.5)
	digitalOutput1.close()

	digitalOutput0.setDutyCycle(0)
	time.sleep(0.5)
	digitalOutput0.close()
