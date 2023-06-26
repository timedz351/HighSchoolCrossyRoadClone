import tkinter
from random import *
canvas=tkinter.Canvas(width=620,height=850)
canvas.pack()
#   trava=1
#   voda=2
#   cesta=3

#vytvorenie levelu
travaGif=tkinter.PhotoImage(file='trava.gif')
framesTrava = [tkinter.PhotoImage(file='trava.gif',format = 'gif -index %i' %(i)) for i in range(3)]
cesta=tkinter.PhotoImage(file='cesta.png')
kamen=tkinter.PhotoImage(file='kamen.gif')
framesKamen= [tkinter.PhotoImage(file='kamen.gif',format = 'gif -index %i' %(i)) for i in range(3)]
vodaGif=tkinter.PhotoImage(file='voda.gif')
framesVoda= [tkinter.PhotoImage(file='voda.gif',format = 'gif -index %i' %(i)) for i in range(3)]

#premenne
pocetStlpcov=15
pocetRiadkov=20
frekvencia=100
mapa=[]
# premenne s globalom
animacia_pocet=0
n=0

#class hraca
class hrac():
    def __init__(self,x,y,sirka,vyska):
        self.x=x
        self.y=y
        self.sirka=sirka
        self.vyska=vyska
    def vykresli(self,x,y):
        canvas.create_rectangle(player.x-self.sirka, player.y-self.vyska, player.x+self.sirka, player.y+self.vyska,fill='yellow',tags='hrac')
    def hore(self,info):
        if mapa[((player.y+10)//40)-2][((player.x+10)//40)-1]!=4:
            self.y -= 40
        
    def vpravo(self,info):
        self.x +=10
    def vlavo(self,info):
        self.x -=10
    def dole(self,info):
        self.y +=10
#zadefinovanie hraca(player)
player=hrac(300,795,10,10)

#vytvorenie riadku s travou, kvoli poslednemu a prvemu riadku
def trava():
    mapa.append([1,]*pocetStlpcov)
    
#vytvorenie zoznamu zoznamov s indexami typu policka
def mapaZoznam():
    global mapa
    trava()
    for i in range(pocetRiadkov-2):
        typ=randint(1,3)
        if typ==1:
            riadok=[]
            for var in range(pocetStlpcov):
                riadok.append(choice((1,1,1,1,4)))
            mapa.append(riadok)
        elif typ==2:
            riadok=[2,]*pocetStlpcov
            mapa.append(riadok)
        else:
            riadok=[3,]*pocetStlpcov
            mapa.append(riadok)
    trava()
    level(10,40,0)
## vytvorenie policok s gifmi
def level(posun,velkostBloku,n):
    for riadok in range(pocetRiadkov):
        for stlpec in range(pocetStlpcov):
            typPolicka=mapa[riadok][stlpec]
            if typPolicka == 1:
                canvas.create_image(stlpec * velkostBloku + posun, riadok * velkostBloku + posun,image=framesTrava[n],anchor='nw',tags='pozadie')
            elif typPolicka == 2:
                canvas.create_image(stlpec * velkostBloku + posun, riadok * velkostBloku + posun,image=framesVoda[n],anchor='nw',tags='pozadie')
            elif typPolicka == 3:
                canvas.create_image(stlpec * velkostBloku + posun, riadok * velkostBloku + posun,image=cesta,anchor='nw',tags='pozadie')
            else:
                canvas.create_image(stlpec * velkostBloku + posun, riadok * velkostBloku + posun,image=framesKamen[n],anchor='nw',tags='pozadie')

#posunutie indexu gifu policka
def animaciaPolicok():
    global n
    canvas.delete('pozadie')
    level(10,40,n)
    n+=1
    if n==3:
        n=0

#### volanie funkcii tlacitkami na zavolanie player classu
##def playerHore(info):
##        player.hore()
##def playerDole(info):
##    player.dole()
##def playerVlavo(info):
##    player.vlavo()
##def playerVpravo(info):
##    player.vpravo()
    
canvas.bind_all('<Up>',player.hore)
canvas.bind_all('<Down>',player.dole)
canvas.bind_all('<Left>',player.vlavo)
canvas.bind_all('<Right>',player.vpravo)

# mainloop
def casomer():
    global animacia_pocet
    canvas.delete('hrac')
    player.vykresli(player.x,player.y)
    if animacia_pocet%5==0:
        animaciaPolicok()
        print(mapa[((player.y+10)//40)-2][((player.x+10)//40)-1])
    animacia_pocet+=1
    canvas.after(frekvencia,casomer)
    canvas.update()
    
mapaZoznam()
casomer()
canvas.mainloop()

