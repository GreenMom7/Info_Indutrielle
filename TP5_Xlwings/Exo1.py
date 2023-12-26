#-*- coding:Latin-1 -*-
import xlwings as xw
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import names
from random import *
from openpyxl import Workbook

## 2.2 Création d'un fichier Excel à partir de Python
# if __name__ == "__main__":
# 	book = xw.Book() # ouverture d'un nouveau book
# 	sheet0 = book.sheets.add('test') #ajout d'une feuille nommée 'test'
# 	sheet0['A1'].value = 'toto' #ajout d'un texte en case A1 dans la feuille sheet0
# 	texte = sheet0['A1'].value #lecture de la case A1 de la feuille sheet0
# 	print(texte)
# 	sheet0['A2'].value = 10 #ajout d'un entier dans la case A2 de la feuille sheet0
# 	sheet0['A3'].value = np.random.default_rng().uniform(0,20,1)
# 	sheet0['B1'].value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
# 	book.save('test.xlsx') #sauvegarde

# if __name__ == "__main__":
# 	book = xw.Book()
# 	#panda data
# 	df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b']) #création data
# 	sheet0 = book.sheets.add('test')
# 	sheet0['A1'].value = df
# 	df1 = sheet0['A1'].options(pd.DataFrame, expand='table').value
# 	print(df1)
	
# 	#dictionnary
# 	dictionnaire = {'nom':'toto','age':0,'taille':1.2}
# 	sheet0['A5'].value = dictionnaire
	
# 	dictionnaire1 = sheet0['A5:B7'].options(dict).value
# 	print(dictionnaire1)
	
# 	#plot numpy data
# 	fig = plt.figure()
# 	data = sheet0['A2:C3'].options(np.array, ndim=2,transpose=True).value
	
# 	print(data)
# 	plt.plot(data)
# 	sheet0.pictures.add(fig,left=sheet0.range('B8').left, top=sheet0.range('B8').top)

# etudiant0 = {}
# etudiant0 ["nom"] = "akmal"
# etudiant0 ["prenom"] = "hugo"
# etudiant0 ["age"] = 20
# print(etudiant0)

base_donnees = []
for i in range(15):
    etudiant = {"nom": names.get_last_name(),"prenom" : names.get_first_name(), "age" : randint(17,20)}
    base_donnees.append(etudiant)
    
# # Affichage de la base de données
# print("Base de données des étudiants:")
# for i in range (15):
#     print(f"Étudiant {i}: {base_donnees[i]}")
