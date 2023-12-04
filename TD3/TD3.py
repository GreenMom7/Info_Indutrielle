# -*- coding:Latin-1 -*-

#from tkinter import *
#fen1 = Tk()
#tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red')
#tex1.pack()
#bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
#bou1.pack()
#fen1.mainloop()

# Petit exercice utilisant la bibliothèque graphique tkinter
#from tkinter import *
#from random import randrange
## --- définition des fonctions gestionnaires d'événements : ---
#def drawline():
#    "Tracé d'une ligne dans le canevas can1"
#    global x1, y1, x2, y2, coul
#    can1.create_rectangle(x1,y1,x2,y2,width=1,fill=coul)
#    # modification des coordonnées pour la ligne suivante :
#    y2, y1 = y2+5, y1-5

#def drawline2():
#    coul = 'red'
#    can1.create_line(0, 325, 500, 325, width=2, fill=coul)
#    can1.create_line(250, 0, 250, 650, width=2, fill=coul)

#def changecolor():
#    "Changement aléatoire de la couleur du tracé"
#    global coul
#    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
#    c = randrange(8) # => génère un nombre aléatoire de 0 à 7
#    #Exo4.1 : modifier le programme pour avoir que les couleurs cyan, maroon, green
#    #c = randrange(1,3,1)
#    coul = pal[c]

##------ Programme principal -------
## les variables suivantes seront utilisées de manière globale :

##Exo4.3 la taille des lignes pour se confonder avec les bords

#x1, y1, x2, y2 = 0, 0, 650, 500 # coordonnées de la ligne

##Exo4.2 x1, y1, x2, y2 = 10, 90, 190, 90

#coul = 'dark green' # couleur de la ligne
## Création du widget principal ("maître") :
#fen1 = Tk()
## création des widgets "esclaves" :
#can1 = Canvas(fen1,bg='dark grey',height=650,width=500)
#can1.pack(side=LEFT)
#bou1 = Button(fen1,text='Quitter',command=fen1.quit)
#bou1.pack(side=BOTTOM)
#bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
#bou2.pack()
#bou3 = Button(fen1,text='Autre couleur',command=changecolor)
#bou3.pack()
#bou4 = Button(fen1,text='Afficher croix',command=drawline2)
#bou4.pack()
#fen1.mainloop() # démarrage du réceptionnaire d'événements
#fen1.destroy() # destruction (fermeture) de la fenêtre

from tkinter import *
from random import randrange

# définition des gestionnaires
# d'événements :
def move():
    "deplacement de la balle"
    global x1, y1, dx, dy, flag
    x1, y1 = x1 +dx, y1 + dy
    if x1 >260:
        x1, dx, dy = 260, -16, -20
    if y1 >260:
        y1, dx, dy = 260, 10, -21
    if x1 <10:
        x1, dx, dy = 10, 19, -5
    if y1 <10:
        y1, dx, dy = 10, 11, 25
    can1.coords(oval1,x1,y1,x1+30,y1+30)
    if flag >0:
        fen1.after(randrange(20,100),move) # => boucler, vitesse aléatoire

def stop_it():
    "arret de l'animation"
    global flag
    flag =0

def start_it():
    "demarrage de l'animation"
    global flag
    if flag ==0: # pour ne lancer qu'une seule boucle
        flag =1
    move()
 
def f(event):
    t=event.keysym
    print("Touche pressée :", t)
    
def g(event):
    x=event.x
    y=event.y
    print("Position :", x, y)
    
def pointeur(event):
    chaine.configure(text = "Clic détecté en X =" + str(event.x) +", Y =" + str(event.y))


#========== Programme principal =============
# les variables suivantes seront utilisées de manière globale :

x1, y1 = randrange(20,210),randrange(40,170) # coordonnées initiales
dx, dy = 15, 0 # 'pas' du déplacement
flag =0 # commutateur

# Création du widget principal ("parent") :
fen1 = Tk()
fen1.title("Main bola")

# création des widgets "enfants" :
can1 = Canvas(fen1,bg='dark grey',height=300, width=300)
can1.pack(side=LEFT, padx =5, pady =5)
can1.bind("<Button-1>", pointeur)
can1.pack()

chaine = Label(fen1)
chaine.pack()

oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
bou1 = Button(fen1,text='Quitter', width =8, command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Demarrer', width =8, command=start_it)
bou2.pack()
bou3 = Button(fen1, text='Arreter', width =8, command=stop_it)
bou3.pack()

# root = Tk()
# root.bind("<Key>", f)
# root.bind("<Motion>",g)
# root.mainloop()

# démarrage du réceptionnaire d'événements (boucle principale) :
fen1.mainloop()
