import tkinter
from random import *
canvas=tkinter.Canvas(width=620,height=850)
canvas.pack()
screenWidth=620
screenHeight=850

class car():
    #vytvori auto s nemennymi vlastnostami, okrem smeru a rychlosti
    def __init__(self,smer,rychlost,y):
        self.x=randrange(0,620)
        self.y=y
        self.sirka=40
        self.vyska=10
        self.smer=smer
        self.rychlost=rychlost
        canvas.create_rectangle(self.x-self.sirka,self.y-self.vyska,self.x+self.sirka,self.y+self.vyska,tags='auto')

       
    def posun(self):
        self.x += self.rychlost * self.smer
        canvas.create_rectangle(self.x-self.sirka,self.y-self.vyska,self.x+self.sirka,self.y+self.vyska,tags='auto')
        # posunie auto na druhu stranu, ak je mimo obrazovky
        if self.smer == 1 and self.x >= screenWidth + self.sirka:
            self.x= 0-self.sirka
        if self.smer ==  -1 and self.x <= 0-self.sirka:
            self.x = screenWidth + self.sirka
            
        
#   skontroluje poziciu kazdeho auta, a ak sa prekryv,
#   vyzrebuje mu novu nahodnu poziciu
def kontrola(ktoryZoznam):
    for i in range(0,len(listListovAut[ktoryZoznam])):
        for u in range(i+1,len(listListovAut[ktoryZoznam])):
            if listListovAut[ktoryZoznam][u].x + listListovAut[ktoryZoznam][u].sirka*2 > listListovAut[ktoryZoznam][i].x > listListovAut[ktoryZoznam][u].x:
                listListovAut[ktoryZoznam][u].x = randrange(0,620)
            if listListovAut[ktoryZoznam][u].x - listListovAut[ktoryZoznam][u].sirka*2 < listListovAut[ktoryZoznam][i].x < listListovAut[ktoryZoznam][u].x:
              listListovAut[ktoryZoznam][u].x = randrange(0,620)
            
listListovAut=[]
def vytvorenieAut():
    for autoY in range(80,800,80):
        listAut=[]
        spolSmer=1*(-1)**randrange(0,2)
        spolRychlost=randrange(2,15)
        n=1
        for i in range(randrange(6)):
            auto = car(spolSmer,spolRychlost,autoY)
            listAut.append(auto)
            n+=1
        listListovAut.append(listAut)
    
def animaciaPrekazok(info):
    canvas.delete('auto')
    ktoryZoznam=0
    for listAut in listListovAut:
        for auto in listAut:
            auto.posun()
        kontrola(ktoryZoznam)
        ktoryZoznam+=1
    
canvas.bind_all('<space>',hop)
