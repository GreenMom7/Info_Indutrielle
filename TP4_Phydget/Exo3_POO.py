from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *
import time

class OutputPortPhydget():

	def __init__(self,nbPort):  #self : objet
		"""
		Constructeur de la classe
		"""
		self.__nbPort = nbPort #champ privé correspond au nb de bit : ENCAPSULATION
		self.portOutput = []
		for i in range(self.__nbPort):
			port = DigitalOutput()
			self.portOutput.append(port)
			self.portOutput[i].setChannel(i)
			self.portOutput[i].openWaitForAttachment(5000)

	def setPort(self, value):
		"""
		Methode pour ecrire sur le port de sortie(i.e. allumer des leds en fonction de "value")
		"""
		print(f"value = {hex(value)} : {bin(value)}")  #affichage de la valeur du "value"
		masque = 1									

		for i in range(self.__nbPort):
			res = value & masque                       #operation de masquage ET
			self.portOutput[i].setDutyCycle(res)       #Ecriture sur le port de sortie
			value = value >> 1                         # on regard le bit suivant -> decalage à droite

	def closePort(self): 
		"""
		Methode pour la fermeture des ports de sortie
		"""
		for i in range(self.__nbPort):
			self.portOutput[i].close()

# *---Programme principale---*
if __name__ == "__main__":

	outport8bits = OutputPortPhydget(8) # créationse de l'objet de 8 ports : outport8bits

	for j in range(100):
		for i in range(8):
			outport8bits.setPort(0x55)
			time.sleep(0.25)
			outport8bits.setPort(0xAA)
			time.sleep(0.25)

	for i in range (8):
		outport8bits.closePort()
