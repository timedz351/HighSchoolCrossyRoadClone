import tkinter
from random import *
canvas=tkinter.Canvas(width=620,height=850)
canvas.pack()
sirkaAuta=40
screenWidth=620
screenHeight=850


class car():
    #vytvori auto s nemennymi vlastnostami, okrem smeru a rychlosti
    def __init__(self,smer,rychlost):
        self.x=randrange(0,620)
        self.y=430
        self.sirka=40
        self.vyska=20
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
            
        

def kontrola():
    for i in range(0,len(listAut)-1):
        for u in range(i+1,len(listAut)-1):
            if listAut[u].x + listAut[u].sirka*2 > listAut[i].x > listAut[u].x:
                return True
            elif listAut[u].x - listAut[u].sirka*2 < listAut[i].x < listAut[u].x:
                return True
            else:
                return False
            
            

    
listAut=[]
def vytvorenieAut():   
    spolSmer=1*(-1)**randrange(0,2)
    spolRychlost=randrange(2,9)
    for i in range(6):
        auto = car(spolSmer,spolRychlost)
        while kontrola():
            auto = car(spolSmer,spolRychlost)
        listAut.append(auto)
        canvas.after(1000)
        canvas.update()
    


def hop(info):
    canvas.delete('auto')
    for auto in listAut: 
        auto.posun()
    kontrola()
    
canvas.bind_all('<space>',hop)
vytvorenieAut()
