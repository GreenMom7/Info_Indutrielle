# -*- coding:Latin-1 -*-
from turtle import *
from math import *

def carre(taille, couleur):

   "fonction qui dessine un carré de taille et de couleur déterminées"
   color(couleur)
   c = 0
   while c < 4:
     forward(taille)
     right(90)
     c = c + 1


def triangle(taillebase, couleur, angle=0):
    color(couleur)
    left(angle)
    taillecote = taillebase * cos(pi/4)
    forward(taillebase)
    left(135)
    forward(taillecote)
    left(90)
    forward(taillecote)
    left(135)
    right(angle)

for j in range (1,8):
    i = 0 
    while i<5:
       down()
       triangle(j*10,'red',0)
       up()
       forward(j*10)
       right(72)
       i = i+1
    forward((j*10)+50)
    

 
g = input() #attente

# down()
# carre(30,'green')
# up()
#forward(60)
# forward(50*3/2)
# i=0
# while i<5:
#    down()
#    triangle(30,'red',0)
#    up()
#    forward(30)
#    right(72)
#    i += 1
   
