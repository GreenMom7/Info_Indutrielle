# -*- coding:Latin-1 -*-

from this import d
from tkinter import *
from random import *
from math import *
def start_it():
    "D�marrage de l'animation"
    global flag
    if flag ==0:
        flag =1
    move()
def stop_it():
    "Arr�t de l'animation"
    global flag
    flag =0
def move():
    "Animation du serpent par r�cursivit�"
    global flag
    c = serp[0] # extraction des infos concernant le carr� de queue
    cq = c[0] # r�f. de ce carr� (coordonn�es inutiles ici)
    l =len(serp) # longueur actuelle du serpent (= n. de carr�s)
    c = serp[l-1] #extraction des infos concernant le carr� de t�te
    xt, yt = c[1], c[2] # coordonn�es de ce carr�

    xq, yq = xt+dx*cc, yt+dy*cc # coord. du nouveau carr� de t�te
    # V�rification : a-t-on atteint les limites du canevas ? :
    if xq<0 or xq>canX-cc or yq<0 or yq>canY-cc:
        flag =0 # => arr�t de l'animation
        can.create_text(canX/2, 20, anchor =CENTER, text ="Perdu !!!",fill ="red", font="Arial 14 bold")
    can.coords(cq, xq, yq, xq+cc, yq+cc) # d�placement effectif
    serp.append([cq, xq, yq]) # m�morisation du nouveau carr� de t�te
    
    del(serp[0]) # effacement (retrait de la liste)
    
    # Appel r�cursif de la fonction par elle-m�me (=> boucle d'animation) :
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
dx, dy = 1, 0 # indicateurs pour le sens du d�placement
# Autres variables globales :
canX, canY = 500, 500 # dimensions du canevas
x, y, cc = 100, 100, 15 # coordonn�es et cot� du premier carr�
# Cr�ation de l'espace de jeu (fen�tre, canevas, boutons ...) :
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


# Cr�ation du serpent initial (= ligne de 5 carr�s).
serp =[] # liste vide
# Cr�ation et m�morisation des 5 carr�s : le dernier (� droite) est la t�te.
i =0
j=0
while i <5:
    carre =can.create_rectangle(x, y, x+cc, y+cc, fill="green")
    serp.append([carre, x, y])  
    x =x+cc # le carr� suivant sera un peu plus � droite
    i =i+1

#Cr�ation de la nouritture 
 
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
