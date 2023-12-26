# -*- coding:Latin-1 -*-

from this import d
from tkinter import *
from random import *
from math import *
def start_it():
    "Démarrage de l'animation"
    global flag
    if flag ==0:
        flag =1
    move()
def stop_it():
    "Arrêt de l'animation"
    global flag
    flag =0
def move():
    "Animation du serpent par récursivité"
    global flag
    c = serp[0] # extraction des infos concernant le carré de queue
    cq = c[0] # réf. de ce carré (coordonnées inutiles ici)
    l =len(serp) # longueur actuelle du serpent (= n. de carrés)
    c = serp[l-1] #extraction des infos concernant le carré de tête
    xt, yt = c[1], c[2] # coordonnées de ce carré

    xq, yq = xt+dx*cc, yt+dy*cc # coord. du nouveau carré de tête
    # Vérification : a-t-on atteint les limites du canevas ? :
    if xq<0 or xq>canX-cc or yq<0 or yq>canY-cc:
        flag =0 # => arrêt de l'animation
        can.create_text(canX/2, 20, anchor =CENTER, text ="Perdu !!!",fill ="red", font="Arial 14 bold")
    can.coords(cq, xq, yq, xq+cc, yq+cc) # déplacement effectif
    serp.append([cq, xq, yq]) # mémorisation du nouveau carré de tête
    
    del(serp[0]) # effacement (retrait de la liste)
    
    # Appel récursif de la fonction par elle-même (=> boucle d'animation) :
    if flag == 1:
        fen.after(200,move)
        
    #Consommer la nourriture
    global cpt
    for food in foods:
        fx = food[1]
        fy = food[2]
        d=sqrt(((yt-fy)**2)+((xt-fx)**2))
        if d<cc:
            can.delete(food[0]) #efface le dessin
            del(food)#enleve de la liste
            cpt=cpt-1
            growth()
            if(cpt == 0):
                flag = 0
                can.create_text(canX/2, 20, anchor =CENTER, text ="Menang!!!",fill ="red", font="Arial 14 bold")  
            
            

def right(event):
    global dx, dy
    dx, dy = 1,0
def left(event):
    global dx, dy
    dx, dy = -1,0
def up(event):
    global dx, dy
    dx, dy = 0,-1
def down(event):
    global dx, dy
    dx, dy = 0,1

def growth():
    global xt, yt, serp, dx, dy
    c = serp[0]
    cq = c[0] 
    l =len(serp)
    c = serp[l-1]
    xt, yt = c[1], c[2]
    carre =can.create_rectangle(xt, yt, xt+cc, yt+cc, fill="red")
    serp.append([carre, xt, yt])
   


# === Programme principal : ========
# Variables globales modifiables par certaines fonctions :
longueur = 5
flag =0 # commutateur pour l'animation
dx, dy = 1, 0 # indicateurs pour le sens du déplacement
# Autres variables globales :
canX, canY = 500, 500 # dimensions du canevas
x, y, cc = 100, 100, 15 # coordonnées et coté du premier carré
# Création de l'espace de jeu (fenêtre, canevas, boutons ...) :
fen =Tk()
can =Canvas(fen, bg ='light blue', height =canX, width =canY)
can.pack(padx =10, pady =10)
bou1 =Button(fen, text="Start", width =10, command =start_it)
bou1.pack(side =LEFT)
bou2 =Button(fen, text="Stop", width =10, command =stop_it)
bou2.pack(side =LEFT)
bou3 =Button(fen, text="Growth", width =10, command =growth)
bou3.pack(side =LEFT)
fen.bind("<Left>", left)
fen.bind("<Right>", right)
fen.bind("<Up>", up)
fen.bind("<Down>", down)


# Création du serpent initial (= ligne de 5 carrés).
serp =[] # liste vide
# Création et mémorisation des 5 carrés : le dernier (à droite) est la tête.
i =0
j=0
while i <5:
    carre =can.create_rectangle(x, y, x+cc, y+cc, fill="green")
    serp.append([carre, x, y])  
    x =x+cc # le carré suivant sera un peu plus à droite
    i =i+1

#Création de la nouritture 
 
global cpt
cpt = 0
foods=[]
while j<10: 
    fx=randint(0,(canX-cc))
    fy=randint(0,(canY-cc))
    food=can.create_oval(fx,fy,fx+cc,fy-cc,fill="yellow")
    foods.append([food,fx,fy])
    j =j+1
    cpt=cpt+1

fen.mainloop()
