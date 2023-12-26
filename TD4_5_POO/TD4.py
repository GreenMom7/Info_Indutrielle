# # -*- coding:Latin-1 -*-
# from random import *
# from math import *


# class Matrice2D():
#    #Exo1.1
#    #nbLignes = 0
#    #nbColonnes = 0
#    #Matrice = []

#    #Exo1.2
#    def __init__(self, nblignes, nbcolonnes):
#        self.nblignes=nblignes
#        self.nbcolonnes=nbcolonnes
#        self.Matrice=[]

#        for i in range (self.nblignes):
#           ligne = []
#           for j in range (self.nbcolonnes):
#               ligne.append(0)
#           self.Matrice.append(ligne)
#    #Exo1.3
#    def affiche(self):
#        for i in range(self.nblignes):
#            for j in range(self.nbcolonnes):
#                 print(f'{self.Matrice[i][j]:.2f}', end=' ')
#            print('')
#    #Exo1.4
#    def randomInit(self, etendue):
#        for i in range(self.nblignes):
#            for j in range(self.nbcolonnes):
#                self.Matrice[i][j] = random()*etendue
# #Exo2.1
# class MatriceRotation(Matrice2D):
#     def __init__(self,angle):
#         Matrice2D.__init__(self,2,2) #terus bagi parametres
#         #super().__init__(2,2) tk perlu self
#         self.angle = angle
#         self.Matrice[0][0] = cos(angle)
#         self.Matrice[0][1] = -sin(angle)
#         self.Matrice[1][0] = sin(angle)
#         self.Matrice[1][1] = cos(angle)
#     #Exo2.2
#     def affiche(self):
#         print('Matrice de rotation')
#         Matrice2D.affiche(self)
        
#    #Exo 2.4  
#     def transformation(self,pi):
#        p=Point(0,0)
#        p.x= self.Matrice[0][0]*pi.x + self.Matrice[0][1]*pi.y
#        p.y= self.Matrice[1][0]*pi.x + self.Matrice[1][1]*pi.y    
#        return p
       
# class Point():
#    global x, y
#    """Point Gomtrique"""
#    def __init__(self,x,y):
#        self.x = x
#        self.y = y

#    def affiche1(self):
#        print(f"Le point initial : ({self.x:.2f},{self.y:.2f})")

#    def affiche2(self): #definition d'une mthode affiche
#        print(f"L'image de point par la rotation est ({self.x:.2f},{self.y:.2f})")
       
# # M = Matrice2D(3,3)
# # M.randomInit(9)
# # M.affiche()
# #print(f'M = {M.Matrice} avec nombre de ligne = {M.nblignes} et nombre de colonnes = {M.nbcolonnes}')

# # #Exo2.3
# # R1 = MatriceRotation(pi/4)
# # R1.affiche()
# # print('')
# # R2 = MatriceRotation(pi/3)
# # R2.affiche()
# # print('')
# # R3 = MatriceRotation(pi/2)
# # R3.affiche()
# # print('')

# # P = Point(1,1)
# # P.affiche()
# Pin = Point(2,-2)
# Pin.affiche1()
# R3  = MatriceRotation(pi)

# R3.affiche()
# Pout = R3.transformation(Pin)
# print('')
# Pout.affiche2()


from tkinter import *
from math import *

def draw(canvas,listPoint,coul='black',h=480/2,w=480/2):
    l = len(listPoint)
    for i in range(l-1):
        canvas.create_line(listPoint[i].x+w,listPoint[i].y+h,listPoint[i+1].x+w,listPoint[i+1].y+h,width=2,fill=coul)
        canvas.create_line(listPoint[l-1].x+w,listPoint[l-1].y+h,listPoint[0].x+w,listPoint[0].y+h,width=2,fill=coul)

def rotate():
    global theta,LR
    P1 = Point(-100,-100)
    P2 = Point(-100,100)
    P3 = Point(100,100)
    P4 = Point(100,-100)
    listePointsStart = [P1,P2,P3,P4]
    draw(can1,listePointsStart)
    theta= theta+dtheta
    LRX.config(text='angle'+str(theta))
        # rajoutez votre code pour transformer les 4 points et faire le dessin
    R = MatriceRotation(theta)
    P1n=R.transformation(P1)
    P2n=R.transformation(P2)
    P3n=R.transformation(P3)
    P4n=R.transformation(P4)
    listePointsStart = [P1n,P2n,P3n,P4n]
    draw(can1,listePointsStart)

class Point():
    global x, y
    """Point Geometrique"""
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Matrice2D():
   def __init__(self, nblignes, nbcolonnes):
       self.nblignes=nblignes
       self.nbcolonnes=nbcolonnes
       self.Matrice=[]

       for i in range (self.nblignes):
          ligne = []
          for j in range (self.nbcolonnes):
              ligne.append(0)
          self.Matrice.append(ligne)
 
   def affiche(self):
       for i in range(self.nblignes):
           for j in range(self.nbcolonnes):
                print(f'{self.Matrice[i][j]:.2f}', end=' ')
           print('')

class MatriceRotation(Matrice2D):
    def __init__(self,angle):
        #Matrice2D.__init__(self,2,2) #terus bagi parametres
        super().__init__(2,2) #tk perlu self
        self.angle = angle
        self.Matrice[0][0] = cos(angle)
        self.Matrice[0][1] = -sin(angle)
        self.Matrice[1][0] = sin(angle)
        self.Matrice[1][1] = cos(angle)
    
    def affiche(self):
        print('Matrice de rotation')
        Matrice2D.affiche(self)
       
    def transformation(self,pi):
        p=Point(0,0)
        p.x= self.Matrice[0][0]*pi.x + self.Matrice[0][1]*pi.y
        p.y= self.Matrice[1][0]*pi.x + self.Matrice[1][1]*pi.y   
        return p


theta = 0 #angle courant
dtheta= 10 #increment d'angle
#animation---------------------------------------------
fen1 = Tk()
fen1.title("Animation 2D")

can1 = Canvas(fen1,bg='dark grey',height=500,width=500)
can1.pack(side=LEFT,padx = 5,pady=5)

BQuad = Button(fen1,text='GO',command = rotate)
BQuad.pack(side = BOTTOM)

LRX = Label(fen1,text='angle = '+str(theta))
LRX.pack(side=TOP)

fen1.mainloop()
