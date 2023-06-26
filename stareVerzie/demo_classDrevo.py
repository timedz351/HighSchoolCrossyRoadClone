import tkinter
from random import *
canvas=tkinter.Canvas(width=620,height=850)
canvas.pack()
#   trava=1
#   voda=2
#   cesta=3
#   kamen=4

class ():
    #vytvori drevo s nemennymi vlastnostami, okrem smeru a rychlosti
    def __init__(self,smer,rychlost,y):
        self.x=randrange(0,620)
        self.y=y
        self.sirka=40
        self.vyska=10
        self.smer=smer
        self.rychlost=rychlost
        canvas.create_rectangle(self.x-self.sirka,self.y-self.vyska,self.x+self.sirka,self.y+self.vyska,tags='drevo')

    def posun(self):
        self.x += self.rychlost * self.smer
        if self.smer == -1:
##            canvas.create_image(self.x,self.y,image=drevovlavo,anchor='center',tags='drevo')
            canvas.create_rectangle(self.x-self.sirka,self.y-self.vyska,self.x+self.sirka,self.y+self.vyska,tags='drevo',fill='brown')
##        if self.smer == 1:
##            canvas.create_image(self.x,self.y,image=drevovpravo, anchor='center',tags='drevo')
            
        # posunie drevo na druhu stranu, ak je mimo obrazovky
        if self.smer == 1 and self.x >= screenWidth + self.sirka:
            self.x= 0-self.sirka
        if self.smer ==  -1 and self.x <= 0-self.sirka:
            self.x = screenWidth + self.sirka
            
        
#   skontroluje poziciu kazdeho dreva, a ak sa prekryva,
#   vyzrebuje mu novu nahodnu poziciu
def kontrola(ktoryZoznam2):
    for i in range(0,len(listListovDriev[ktoryZoznam2])):
        for u in range(i+1,len(listListovDriev[ktoryZoznam2])):
            if listListovDriev[ktoryZoznam2][u].x + listListovDriev[ktoryZoznam2][u].sirka*2 > listListovDriev[ktoryZoznam2][i].x > listListovDriev[ktoryZoznam2][u].x:
                listListovDriev[ktoryZoznam2][u].x = randrange(0,620)
            if listListovDriev[ktoryZoznam2][u].x - listListovDriev[ktoryZoznam2][u].sirka*2 < listListovDriev[ktoryZoznam2][i].x < listListovDriev[ktoryZoznam2][u].x:
              listListovDriev[ktoryZoznam2][u].x = randrange(0,620)
#vytvori dreva na Y zistenych pragramom pod tymto
# precita zoznam ydriev a vytvori na tych Y dreva od 1 po 5
listListovDriev=[]
listListovDrievKolizia=[]
def vytvorenieDriev():
    global listListovDriev
    for drevoY in ydriev:
        if drevoY != 0:
            listDriev=[]
            # smer aut na jedej ceste
            spolSmer=1*(-1)**randrange(0,2)
            # rychlost aut na jednej ceste
            spolRychlost=randrange(2,15)
            for i in range(randrange(1,5)):
                drevo = car(spolSmer,spolRychlost,drevoY)
                listDriev.append(drevo)
                canvas.after(300)
                canvas.update()
            #vytvorenie zoznamu zoznamov objektov aut
            listListovDriev.append(listDriev)
            listListovDrievKolizia.append(listDriev)
        else:
            #do zoznamu zoznamov objektov aut, doplni [0],
            #aby sme sa mohli pri kolizi odvolat na rovnaky riadok na akom je hrac
            listListovDrievKolizia.append([0])
# zisti kde je cesta, zapamata si Y ciest do zoznamu
def kdeJeCesta2():
    global ydriev
    naAkomRiadku=None
    ydriev=[]
    for var in range(len(mapa)):
        # ak sa zoznam zacina 3, tak je to cesta a prida Y tohoto zoznamu do zoznamu ydriev
        if mapa[var][0] == 2:
            naAkomRiadku = var*40+30
            ydriev.append(naAkomRiadku)
        else:
            #doplni do zoznamu 0 tam, kde nie je cesta
            ydriev.append(0)
def animaciaDriev():
    canvas.delete('drevo')
    ktoryZoznam2=0
    for listDriev in listListovDriev:
        if listDriev != 0:
            for drevo in listDriev:
                drevo.posun()
            kontrola(ktoryZoznam2)
            ktoryZoznam2+=1

kdeJeCesta2()
vytvorenieDriev()
