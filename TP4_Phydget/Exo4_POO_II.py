# -*- coding:Latin-1 -*-
from Phidget22.Phidget import *
from Phidget22.Devices.DigitalInput import *
from Phidget22.Devices.DigitalOutput import *
import time


class InputPortPhydget():

	def __init__(self,nbPort):  #self : objet
		"""
		Constructeur de la classe
		"""
		self.__nbPort = nbPort #champ privé correspond au nb de bit : ENCAPSULATION
		self.portInput = []
		for i in range(self.__nbPort):
			port = DigitalInput()
			self.portInput.append(port)
			self.portInput[i].setChannel(i)
			self.portInput[i].openWaitForAttachment(5000)

	def getPort(self):
		"""
		Methode pour la lecture des ports d'entréé
		"""
		value = 0
		for i in range(self.__nbPort):
			valuebit=self.portInput[i].getState()
			#value = value + valuebit*(2**i)
			value = value + (valuebit<<i)
		return value

	def closePort(self): 
		"""
		Methode pour la fermeture des ports de sortie
		"""
		for i in range(self.__nbPort):
			self.portInput[i].close()

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

if __name__ == "__main__":

    # créationse de l'objet de 8 ports 
	portInput = InputPortPhydget(8)
	portOutput = OutputPortPhydget(8)

	while 1:
		inputvalue = portInput.getPort()
		print(f'i = {inputvalue}')
		portOutput.setPort(inputvalue)
		time.sleep(0.1)
