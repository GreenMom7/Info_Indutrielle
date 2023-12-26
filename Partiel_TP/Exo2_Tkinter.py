# -*- coding:Latin-1 -*-
from tkinter import *

def drawCercle():
    h,w = can1.winfo_height(),can1.winfo_width()
    rayon = 25
    can1.create_oval(w/2-rayon,h/2-rayon,w/2+rayon,h/2+rayon)
    
def drawCible():
    h,w = can1.winfo_height(),can1.winfo_width()
    can1.create_line(h/2,0,h/2,w,fill = 'red')
    can1.create_line(0,w/2,h,w/2, fill ='red')
    ray = 10
    for i in range(9):
        can1.create_oval(w/2-ray,h/2-ray,w/2+ray,h/2+ray)
        ray = ray + 10
    
fen1=Tk()

can1=Canvas(fen1, bg='dark grey', height=200, width=200)

can1.pack(side=LEFT)

bou1=Button(fen1, text='Quitter', command = fen1.quit)
bou1.pack(side=BOTTOM)

bou2=Button(fen1, text='Cercle', command = drawCercle)
bou2.pack(side=BOTTOM)

bou3=Button(fen1, text='Cible', command = drawCible)
bou3.pack(side=BOTTOM)
fen1.mainloop()