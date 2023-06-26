import tkinter
from random import *
canvas=tkinter.Canvas(width=620,height=850)
canvas.pack()
#   trava=1
#   voda=2
#   cesta=3

#vytvorenie levelu
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
        if vyberFarby == 1:
            farba='green'
        elif vyberFarby == 2:
            farba='skyblue'
        else:
            farba='gray'
        for stlpec in range(pocetStlpcov):
            canvas.create_rectangle(stlpec * velkostBloku + posun, riadok * velkostBloku + posun,(stlpec + 1) * velkostBloku + posun, (riadok+1) * velkostBloku + posun,
                                                        fill=farba)
mapaZoznam()
