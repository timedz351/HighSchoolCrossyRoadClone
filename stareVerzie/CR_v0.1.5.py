import tkinter
from random import *
canvas=tkinter.Canvas(width=620,height=850)
canvas.pack()
#   trava=1
#   voda=2
#   cesta=3

#vytvorenie levelu
travaGif=tkinter.PhotoImage(file='trava.gif')
cesta=tkinter.PhotoImage(file='cesta.png')
voda=tkinter.PhotoImage(file='voda.png')

pocetStlpcov=15
pocetRiadkov=20
mapa=[]

def trava():
    mapa.append([1,]*pocetStlpcov)
def mapaZoznam():
    global mapa
    trava()
    for i in range(pocetRiadkov-2):
        typ=randint(1,3)
        print('tu')
        if typ==1:
            riadok=[1,]*pocetStlpcov
            mapa.append(riadok)

        elif typ==2:
            riadok=[2,]*pocetStlpcov
            mapa.append(riadok)
        else:
            riadok=[3,]*pocetStlpcov
            mapa.append(riadok)
        
    trava()
    level(10,40)
def level(posun,velkostBloku):
    for riadok in range(pocetRiadkov):
        vyberFarby=mapa[riadok][1]
        for stlpec in range(pocetStlpcov):
            if vyberFarby == 1:
                canvas.create_image(stlpec * velkostBloku + posun, riadok * velkostBloku + posun,image=travaGif,anchor='nw')
            elif vyberFarby == 2:
                farba='skyblue'
                canvas.create_image(stlpec * velkostBloku + posun, riadok * velkostBloku + posun,image=voda,anchor='nw')
            else:
                farba='gray'
                canvas.create_image(stlpec * velkostBloku + posun, riadok * velkostBloku + posun,image=cesta,anchor='nw')

mapaZoznam()
tkinter.mainloop()
