import tkinter,time,pygame
from random import *

r=tkinter.Tk()
r.title('The other side')
canvas=tkinter.Canvas(r,width=600,height=850)
canvas.pack()

#   trava=1
#   voda=2
#   cesta=3
#   kamen=4
#premenne
screenWidth=620
screenHeight=850
pocetStlpcov=15
pocetRiadkov=20
frekvencia=100
mapa=[]
mozem=False
sumCas=0
casy=[100,100,100,100]
#############################################################################################################################################
#HRAC#
#############################################################################################################################################
#class hraca
class hrac():
    def __init__(self,x,y,sirka,vyska):
        self.x=x
        self.y=y
        self.sirka=sirka
        self.vyska=vyska
    def vykresli(self,x,y):
##        canvas.create_rectangle(player.x-self.sirka, player.y-self.vyska, player.x+self.sirka, player.y+self.vyska,fill='yellow',tags='hrac')
        canvas.create_image(player.x,player.y-20,image=hracPNG,anchor='center',tags='hrac')
    
    def hore(self,info):
        #kontrola ci na policku nad hracom nieje kamen, zisti poziciu hraca a posunie o policko hore
        if mapa[((player.y)//40)-1][((player.x)//40)]!=4 and mozem:
            self.y -= 40
            canvas.delete('hrac')
            player.vykresli(player.x,player.y)
        
    def vpravo(self,info):
        if  not ((player.x)//40) ==14:#ak nie som na kraji
            if mapa[((player.y)//40)][((player.x)//40)+1]!=4 and mozem:#ak nie je vedla mna kamen
                self.x +=40
                canvas.delete('hrac')
                player.vykresli(player.x,player.y)
    def vlavo(self,info):
        if mapa[((player.y)//40)][((player.x)//40)-1]!=4 and not ((player.x)//40) ==0 and mozem:
            self.x -=40
            canvas.delete('hrac')
            player.vykresli(player.x,player.y)
    def dole(self,info):
        if not ((player.y)//40) == 19:
            if mapa[((player.y)//40)+1][((player.x)//40)]!=4 and mozem:
                self.y +=40
                canvas.delete('hrac')
                player.vykresli(player.x,player.y)
#zadefinovanie hraca(player)
player=hrac(300,785,13,25)


#############################################################################################################################################
#LEVEL#
#############################################################################################################################################
#vytvorenie riadku s travou, kvoli poslednemu a prvemu riadku
def trava():
    mapa.append([1,]*pocetStlpcov)
    
#vytvorenie zoznamu zoznamov s indexami typu policka
def mapaZoznam():
    global mapa
    trava()
    for i in range(pocetRiadkov-2):
        if lvl==1:
            typ=randint(1,3)
            # typ=1
        elif lvl==2:
            typ=randint(2,3)
            # typ=1
        elif lvl==3:
            typ=3
            # typ=1
        else:
            typ=2
            # typ=1
        # if lvl==1:
        #     typ=randint(1,3)
        #     # typ=1
        # elif lvl==2:
        #     typ=randint(1,3)
        #     # typ=1
        # elif lvl==3:
        #     typ=randint(1,3)
            
        # else:
        #     typ=randint(1,3)
            
        if typ==1:
            riadok=[]
            #vytvori riadok s travou s par kamenmi
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
    level(0,40,0)
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

#############################################################################################################################################
#AUTO#
#############################################################################################################################################
class car():
    #vytvori auto s nemennymi vlastnostami, okrem smeru a rychlosti
    def __init__(self,smer,rychlost,y):
        self.x=randrange(0,620)
        self.y=y
        self.sirka=30
        self.vyska=10
        self.smer=smer
        self.rychlost=rychlost
        canvas.create_rectangle(self.x-self.sirka,self.y-self.vyska,self.x+self.sirka,self.y+self.vyska,tags='auto')

    def posun(self):
        self.x += self.rychlost * self.smer
        if self.smer == -1:
            canvas.create_image(self.x,self.y,image=autovlavo,anchor='center',tags='auto')
##            canvas.create_rectangle(self.x-self.sirka,self.y-self.vyska,self.x+self.sirka,self.y+self.vyska,tags='auto',fill='yellow')
        if self.smer == 1:
            canvas.create_image(self.x,self.y,image=autovpravo, anchor='center',tags='auto')
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
#vytvori auta na Y zistenych pragramom pod tymto
# precita zoznam yaut a vytvori na tych Y auta od 1 po 5

def vytvorenieAut():
    global listListovAut
    for autoY in yaut:
        if autoY != 0:
            listAut=[]
            # smer aut na jedej ceste
            spolSmer=1*(-1)**randrange(0,2)
            # rychlost aut na jednej ceste
            spolRychlost=randrange(2,15)
            for i in range(randrange(1,5)):
                auto = car(spolSmer,spolRychlost,autoY)
                listAut.append(auto)
            #vytvorenie zoznamu zoznamov objektov aut
            listListovAut.append(listAut)
            listListovAutKolizia.append(listAut)
        else:
            #do zoznamu zoznamov objektov aut, doplni [0],
            #aby sme sa mohli pri kolizi odvolat na rovnaky riadok na akom je hrac
            listListovAutKolizia.append([0])
# zisti kde je cesta, zapamata si Y ciest do zoznamu
def kdeJeCesta():
    global yaut
    naAkomRiadku=None
    yaut=[]
    for var in range(len(mapa)):
        # ak sa zoznam zacina 3, tak je to cesta a prida Y tohoto zoznamu do zoznamu yaut
        if mapa[var][0] == 3:
            naAkomRiadku = var*40+20
            yaut.append(naAkomRiadku)
        else:
            #doplni do zoznamu 0 tam, kde nie je cesta
            yaut.append(0)
def animaciaAut():
    canvas.delete('auto')
    ktoryZoznam=0
    for listAut in listListovAut:
        if listAut != 0:
            for auto in listAut:
                auto.posun()
            kontrola(ktoryZoznam)
            ktoryZoznam+=1

#############################################################################################################################################
#DREVO#
#############################################################################################################################################

class log():
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
            canvas.create_image(self.x,self.y,image=drevovlavo,anchor='center',tags='drevovlavo')
        if self.smer == 1:
            canvas.create_image(self.x,self.y,image=drevovpravo, anchor='center',tags='drevovpravo')
            
        # posunie drevo na druhu stranu, ak je mimo obrazovky
        if self.smer == 1 and self.x >= screenWidth + self.sirka:
            self.x= 0-self.sirka
        if self.smer ==  -1 and self.x <= 0-self.sirka:
            self.x = screenWidth + self.sirka
            
        
#   skontroluje poziciu kazdeho dreva, a ak sa prekryva,
#   vyzrebuje mu novu nahodnu poziciu
def kontrola2(ktoryZoznam2):
    for i in range(0,len(listListovDriev[ktoryZoznam2])):
        for u in range(i+1,len(listListovDriev[ktoryZoznam2])):
            if listListovDriev[ktoryZoznam2][u].x + listListovDriev[ktoryZoznam2][u].sirka*2 > listListovDriev[ktoryZoznam2][i].x > listListovDriev[ktoryZoznam2][u].x:
                listListovDriev[ktoryZoznam2][u].x = randrange(0,620)
            if listListovDriev[ktoryZoznam2][u].x - listListovDriev[ktoryZoznam2][u].sirka*2 < listListovDriev[ktoryZoznam2][i].x < listListovDriev[ktoryZoznam2][u].x:
              listListovDriev[ktoryZoznam2][u].x = randrange(0,620)
#vytvori dreva na Y zistenych pragramom pod tymto
# precita zoznam ydriev a vytvori na tych Y dreva od 1 po 5

def vytvorenieDriev():
    global listListovDriev
    kolkatyRiadok=0
    for drevoY in ydriev:
        if drevoY != 0:
            listDriev=[]
            # smer driev na jedej ceste
            spolSmer=1*(-1)**randrange(0,2)
            # rychlost driev na jednej ceste
            spolRychlost=randrange(2,12)
            #skontroluje rychlost dreva nad drevom, ktore vytvaram, ak je v dolnej polovici prida 2, inak ubere 2
            if kolkatyRiadok >= 1:
                if spolRychlost ==  listListovDriev[kolkatyRiadok-1][0].rychlost:
                    if listListovDriev[kolkatyRiadok-1][0].rychlost <7:
                        spolRychlost+=3
                    else:
                        spolRychlost-=3
            for i in range(randrange(1,5)):
                drevo = log(spolSmer,spolRychlost,drevoY)
                listDriev.append(drevo)
##                canvas.after(300)
##                canvas.update()
            #vytvorenie zoznamu zoznamov objektov aut
            listListovDriev.append(listDriev)
            listListovDrievKolizia.append(listDriev)
            kolkatyRiadok+=1
        else:
            #do zoznamu zoznamov objektov aut, doplni [0],
            #aby sme sa mohli pri kolizi odvolat na rovnaky riadok na akom je hrac
            listListovDrievKolizia.append([0])
        
# zisti kde je cesta, zapamata si Y ciest do zoznamu
def kdeJeVoda():
    global ydriev
    naAkomRiadku=None
    ydriev=[]
    for var in range(len(mapa)):
        # ak sa zoznam zacina 3, tak je to cesta a prida Y tohoto zoznamu do zoznamu ydriev
        if mapa[var][0] == 2:
            naAkomRiadku = var*40+20
            ydriev.append(naAkomRiadku)
        else:
            #doplni do zoznamu 0 tam, kde nie je cesta
            ydriev.append(0)
def animaciaDriev():
    canvas.delete('drevovlavo','drevovpravo')
    ktoryZoznam2=0
    for listDriev in listListovDriev:
        if listDriev != 0:
            for drevo in listDriev:
                drevo.posun()
            kontrola2(ktoryZoznam2)
            ktoryZoznam2+=1

#############################################################################################################################################
#ANIMACIE#
#############################################################################################################################################
def bum():
    m=0
    for i in range(7):
        canvas.delete('bum')
        canvas.create_image(player.x,player.y,anchor='center',image=bumbumFrames[m],tags='bum')
        m+=1
        canvas.update()
        canvas.after(300)
def Plac():
    m=0
    for i in range(21):
        canvas.delete('plac')
        canvas.create_image(player.x,player.y-40,anchor='center',image=placFrames[m],tags='plac')
        m+=1
        canvas.update()
        canvas.after(30)
#posunutie indexu gifu policka
def animaciaPolicok():
    global n
    canvas.delete('pozadie')
    level(0,40,n)
    n+=1
    if n==3:
        n=0 
#############################################################################################################################################
#KOLIZIE#
#############################################################################################################################################
def koliziaAuto():
    global mozem
    # pre vsetky objekty aut v zozname aut na rovnakom riadku ako je hrac
    # skontroluje koliziu
    for auto in listListovAutKolizia[riadokHraca-1]:
        if auto != 0:
            if  auto.x - auto.sirka < player.x + player.sirka < auto.x + auto.sirka or auto.x - auto.sirka < player.x - player.sirka < auto.x + auto.sirka:
                mozem=False
                bum()
                Menu(False,True,False)
                
def koliziaDrevo():
    global mozem, koliziaStymto
    if 0>player.x or player.x>600:#ak som na dreve, a som mimo hracej plochy, prehram
        mozem=False
        Menu(False,True,False)        
    niesomNa=[]
    for drevo in listListovDrievKolizia[riadokHraca-1]:
##        if drevo != 0:
        if not (drevo.x - drevo.sirka < player.x - player.sirka  < drevo.x + drevo.sirka or drevo.x - drevo.sirka < player.x + player.sirka  < drevo.x + drevo.sirka) :
            niesomNa.append(drevo)
    if len(niesomNa) == len(listListovDrievKolizia[riadokHraca-1]):
        mozem=False
        Plac()
        Menu(False,True,False)
    else:
        player.x += listListovDrievKolizia[riadokHraca-1][0].rychlost*listListovDrievKolizia[riadokHraca-1][0].smer
        
def posunDostredu():# zisti kam dopadne hrac ked vyjde z vody, a posunie ho na najblizsi stred policka
    kdeSom=(player.x)//40
    player.x=(kdeSom+1)*40-20
    
#############################################################################################################################################
#SPUSTANIE#
#############################################################################################################################################          
# premenne s globalom
def citanieSkore():
    global lvlbest
    suborCit=open('lvlskore.txt','r')
    for i in suborCit:
        lvlbest.append(int((i).strip()))
    suborCit.close()

def zapisSkore():
    global lvlbest
    suborZap=open('lvlskore.txt','w')
    for i in range(len(lvlbest)-1):
        if casy[i] < lvlbest[i]:
            lvlbest[i]=casy[i]
        suborZap.write(str(lvlbest[i])+'\n')
    if sumCas < lvlbest[4]:
        lvlbest[4]=sumCas
        suborZap.write(str(lvlbest[4])+'\n')

    # for i in range(len(lvlbest)):
        
    suborZap.close()

def globPremRestart():
    global animacia_pocet,n,somNaVode,mozem,listListovAut,listListovAutKolizia,listListovDriev, listListovDrievKolizia,mapa,start_sek,basetime
    start_sek=0
    animacia_pocet=0
    mapa=[]
    n=0 #pocitanie na animaciu gifov
    somNaVode= False #kontrola ci som na vode a ked z nej vyjdem,prepocet na stred policka, posunie panacika 
    mozem=True
    listListovAut=[]
    listListovAutKolizia=[]
    listListovDriev=[]
    listListovDrievKolizia=[]
    basetime=time.time() #pociatocny cas

def start():#restart vsetkeho na novy level
    canvas.delete('menu')
    globPremRestart()
    mapaZoznam()
    kdeJeCesta()
    vytvorenieAut()
    kdeJeVoda()
    vytvorenieDriev()
    casomer()
    player.vykresli(player.x,player.y)
    canvas.create_text(50,820,text='Level:'+str(lvl),tags=('butStart','pozadiee'),font=('LLPixel','15'))

def Menu(nextlevel,prehra,vyhra):#spusti sa na zaciatku, pri prehrati a pri vyhre,nextlevel=True/False
    global lvl,sumCas,casy,animaciaMenu
    player.x=300
    player.y=785
    if nextlevel: #ak sa dostanem na prvy riadok, nextlevel=True
        # canvas.delete('all')
        casy[lvl-1]=int(cas)
        sumCas+=int(cas)
        if vyhra: # koniec hry
            pygame.mixer.music.pause()
            Text='Play again!'
            canvas.create_rectangle([200, 200, 400, 650],fill='white',tags='butStart',width=4)
            canvas.create_rectangle([200, 600, 400, 650],fill='white',tags='butStart',width=4)
            canvas.create_text(300,620,text=Text,tags='butStart',font=('LLPixel','26'))
            canvas.create_text(300,300,text='Best total time:'+str(lvlbest[4])+'s',tags='butStart',font=('LLPixel','10'))
            canvas.create_text(300,400,text='Total time:'+str(sumCas)+'s',tags='butStart',font=('LLPixel','10'))
            sumCas=0
            lvl=1
        else:#next level
            pygame.mixer.music.pause()
            canvas.create_image(0,0,image=menu,tags='menu',anchor='nw')
            Text='Next Level'
            canvas.create_rectangle([70, 578, 260, 640],fill='white',tags='butStart',width=4)
            canvas.create_text(164.5,609,text=Text,tags='butStart',font=('LLPixel','26'))
            lvl+=1
            canvas.create_text(164.5,661,text='Time:'+str(int(cas))+'s',tags='butStart',font=('LLPixel','26'),fill='white')  
            canvas.create_text(164.5,659,text='Time:'+str(int(cas))+'s',tags='butStart',font=('LLPixel','26'))
            canvas.create_text(164.5,711,text='Total time:'+str(sumCas)+'s',tags='butStart',font=('LLPixel','26'),fill='white')
            canvas.create_text(164.5,709,text='Total time:'+str(sumCas)+'s',tags='butStart',font=('LLPixel','26'))
            canvas.create_text(164.5,761,text='Lvl'+str(lvl)+' best time:'+str(lvlbest[lvl-1])+'s',tags='butStart',font=('LLPixel','26'),fill='white') 
            canvas.create_text(164.5,759,text='Lvl'+str(lvl)+' best time:'+str(lvlbest[lvl-1])+'s',tags='butStart',font=('LLPixel','26'))   
    else:#pri kolizii = prehra
        if prehra:
            pygame.mixer.music.pause()
            canvas.delete('hrac')
            Text='Play again!'
            canvas.create_rectangle([200, 400, 400, 450],fill='white',tags='butStart',width=4)
            canvas.create_text(300,375,text='GAME OVER',tags='butStart',font=('LLPixel','26'),fill='black')
            canvas.create_text(300,370,text='GAME OVER',tags='butStart',font=('LLPixel','26'),fill='white')
            canvas.create_text(300,425,text=Text,tags='butStart',font=('LLPixel','26'),fill='black')
        else:#uplny zaciatok hry
            animaciaMenu=True
            canvas.delete('all')
            canvas.create_image(0,0,image=menu,tags='menu',anchor='nw')
            Text='Play'
            canvas.create_rectangle([70, 578, 260, 640],fill='white',tags='butStart',width=4)
            canvas.create_text(164.5,609,text=Text,tags='butStart',font=('LLPixel','26'))#text v tlacidle, podla toho ci som prehal alebo nie
        lvl=1
        sumCas=0
    
    
def timer(basetime):#casomiera
    global start_sek,cas
    now= time.time()
    cas=now-basetime
    if cas>start_sek+1 and mozem:
        start_sek=int(cas)-1
        canvas.delete('cas')
        canvas.create_text(130,820,text='Time:'+str(int(cas)),tags='cas',font=('LLPixel','15'))


def casomer():
    global riadokHraca, somNaVode,animacia_pocet,mozem,basetime
    riadokHraca=(player.y)//40+1  #zisitim na akom riadku je hrac, pouzivam v koliziach
    if mozem:
        timer(basetime)
        canvas.delete('hrac')
        if animacia_pocet%5==0:
            animaciaPolicok()
            print(casy,lvlbest)
        animacia_pocet+=1
        animaciaAut()
        animaciaDriev()
        player.vykresli(player.x,player.y)
        if mapa[riadokHraca-1][0] == 1:
            if somNaVode==True:
                posunDostredu()
                somNaVode=False
        elif mapa[riadokHraca-1][0] == 2:
            koliziaDrevo()
            somNaVode=True
        else:
            mapa[riadokHraca-1][0] == 3
            koliziaAuto()
            if somNaVode==True:
                posunDostredu()
                somNaVode=False
        #vyhra, zastavi hru, vsetko vzmaze, resetne globalne premenne
        if riadokHraca==1:
            mozem=False
            if lvl !=4:
                Menu(True,False,False)              
            else:
                zapisSkore()
                Menu(True,False,True)
        canvas.after(frekvencia,casomer)
        canvas.update()
#############################################################################################################################################
#INE#
#############################################################################################################################################
def klik(s):
    global animaciaMenu
    #ak je zastavena hra, mozem kliknut na tlacitko  nextlevel,prehra,vyhra
    if not mozem:
        if 70<s.x<260 and 578<s.y<640 or 200 < s.x < 400 and 400 <s.y < 450 or 200 < s.x < 400 and 600 < s.y < 650:
            canvas.delete('butStart')
            #animacia odletenia menu
            pygame.mixer.music.play(-1)
            if animaciaMenu:
                for i in range(120):
                    canvas.move('menu',5,0)
                    canvas.after(7)
                    canvas.update()
                animaciaMenu= False
            
            start()
            
def pauza(s):
    global mozem
    if mozem:
        mozem=False
    else:
        mozem = True
        casomer()

def debug():
##    canvas.create_line(player.x-1000,player.y,player.x+1000,player.y,tags='pozadie',fill='red')
##    canvas.create_line(player.x,player.y-1000,player.x,player.y+1000,tags='pozadie',fill='red')
    for riadok in range(pocetRiadkov):
            for stlpec in range(pocetStlpcov):
                canvas.create_rectangle(stlpec * 40, riadok * 40,(stlpec+1) * 40, (riadok+1) * 40,tags='pozadie')
canvas.bind_all('<Up>',player.hore)
canvas.bind_all('<Down>',player.dole)
canvas.bind_all('<Left>',player.vlavo)
canvas.bind_all('<Right>',player.vpravo)
canvas.bind_all('<space>',pauza)
canvas.bind('<Button-1>',klik)

# import obrazkov
framesTrava = [tkinter.PhotoImage(file='files/trava.gif',format = 'gif -index %i' %(i)) for i in range(3)]
cesta=tkinter.PhotoImage(file='files/cesta.png')
kamen=tkinter.PhotoImage(file='files/kamen.gif')
framesKamen= [tkinter.PhotoImage(file='files/kamen.gif',format = 'gif -index %i' %(i)) for i in range(3)]
vodaGif=tkinter.PhotoImage(file='files/voda.gif')
framesVoda= [tkinter.PhotoImage(file='files/voda.gif',format = 'gif -index %i' %(i)) for i in range(3)]
hracPNG=tkinter.PhotoImage(file='files/player3.png')
autovpravo=tkinter.PhotoImage(file='files/autovpravo.png')
autovlavo=tkinter.PhotoImage(file='files/autovlavo.png')
drevovpravo=tkinter.PhotoImage(file='files/drevovpravo.png')
drevovlavo=tkinter.PhotoImage(file='files/drevovlavo.png')
menu=tkinter.PhotoImage(file='files/menu.png')
bumbum=tkinter.PhotoImage(file='files/bumbum.gif')
bumbumFrames= [tkinter.PhotoImage(file='files/bumbum.gif',format = 'gif -index %i' %(i)) for i in range(7)]
plac=tkinter.PhotoImage(file='files/splash.gif')
placFrames= [tkinter.PhotoImage(file='files/splash.gif',format = 'gif -index %i' %(i)) for i in range(21)]
pygame.init()
pygame.mixer.music.load('files/menu_hudba.mp3')

lvlbest=[]
citanieSkore()
print(lvlbest)
Menu(False,False,False)
r.mainloop()
