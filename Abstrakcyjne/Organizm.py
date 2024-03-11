from abc import ABC, abstractmethod
import random
class Organizm(ABC):
    sila, inicjatywa, wiek, zyje, pomin, nazwa = 0, 0, 0, True, False, ""

    @abstractmethod
    def akcja(self):
        pass
    @abstractmethod
    def kolizja(self, x, y):
        pass
    def getSila(self):
        return self.sila
    def getInicjatywa(self):
        return self.inicjatywa
    def getNazwa(self):
        return self.nazwa
    def setSila(self, sila):
        self.sila=sila
    def getWiek(self):
        return self.wiek
    def setWiek(self,wiek):
        self.wiek = wiek
    def getPomin(self):
        return self.pomin
    def setPomin(self, pomin):
        self.pomin=pomin
    def getX(self):
        return self.x
    def setX(self, x):
        self.x=x
    def getY(self):
        return self.y
    def setZyje(self, zyje):
        self.zyje=zyje
    def getZyje(self):
        return self.zyje
    def randomPosX(self, x):
        case = random.randint(1,3)
        if case == 1 and x+1 < self.swiat.MAPWIDTH:
            x += 1
            return x
        elif case == 2 and x-1 >= 0:
            x -= 1
            return x
        elif case == 3:
            return x
        return x

    def randomPosY(self, y):
        case = random.randint(1, 3)
        if case == 1 and y+1 < self.swiat.MAPHEIGHT:
            y += 1
            return y
        elif case == 2 and y-1 >= 0:
            y -= 1
            return y
        elif case == 3:
            return y
        return y
    
    
    def rozmnazanie(self, org, nazwa, x, y):
        nX, nY = x, y
        if nazwa == "wilk":
            while nY == y and nX == x:
                nX, nY = org.randomPosX(x), org.randomPosY(y)
            if self.swiat.czyZajete(nX, nY) is False:
                from Zwierzeta.wilk import wilk
                self.swiat.dodajOrganizm(wilk(self.swiat,nX,nY))
                self.swiat.organizmWLokacji(nX, nY).setPomin(True)
        elif nazwa == "owca":
            while nY == y and nX == x:
                nX, nY = org.randomPosX(x), org.randomPosY(y)
            if self.swiat.czyZajete(nX, nY) is False:
                from Zwierzeta.owca import owca
                self.swiat.dodajOrganizm(owca(self.swiat,nX,nY))
                self.swiat.organizmWLokacji(nX, nY).setPomin(True)
        elif nazwa == "lis":
            while nY == y and nX == x:
                nX, nY = org.randomPosX(x), org.randomPosY(y)
            if self.swiat.czyZajete(nX, nY) is False:
                from Zwierzeta.lis import lis
                self.swiat.dodajOrganizm(lis(self.swiat,nX,nY))
                self.swiat.organizmWLokacji(nX, nY).setPomin(True)
        elif nazwa == "antylopa":
            while nY == y and nX == x:
                nX, nY = org.randomPosX(x), org.randomPosY(y)
            if self.swiat.czyZajete(nX, nY) is False:
                from Zwierzeta.antylopa import antylopa
                self.swiat.dodajOrganizm(antylopa(self.swiat,nX,nY))
                self.swiat.organizmWLokacji(nX, nY).setPomin(True)
        elif nazwa == "zolw":
            while nY == y and nX == x:
                nX, nY = org.randomPosX(x), org.randomPosY(y)
            if self.swiat.czyZajete(nX, nY) is False:
                from Zwierzeta.zolw import zolw
                self.swiat.dodajOrganizm(zolw(self.swiat,nX,nY))
                self.swiat.organizmWLokacji(nX, nY).setPomin(True)
        elif nazwa == "cyberowca":
            while nY == y and nX == x:
                nX, nY = org.randomPosX(x), org.randomPosY(y)
            if self.swiat.czyZajete(nX, nY) is False:
                from Zwierzeta.cyberowca import cyberowca
                self.swiat.dodajOrganizm(cyberowca(self.swiat,nX,nY))
                self.swiat.organizmWLokacji(nX, nY).setPomin(True)
        elif nazwa == "trawa":
            while nY == y and nX == x:
                nX, nY = org.randomPosX(x), org.randomPosY(y)
            if self.swiat.czyZajete(nX, nY) is False:
                from Rosliny.trawa import trawa
                self.swiat.dodajOrganizm(trawa(self.swiat,nX,nY))
                self.swiat.organizmWLokacji(nX, nY).setPomin(True)
        elif nazwa == "guarana":
            while nY == y and nX == x:
                nX, nY = org.randomPosX(x), org.randomPosY(y)
            if self.swiat.czyZajete(nX, nY) is False:
                from Rosliny.guarana import guarana
                self.swiat.dodajOrganizm(guarana(self.swiat,nX,nY))
                self.swiat.organizmWLokacji(nX, nY).setPomin(True)
        elif nazwa == "wilcze":
            while nY == y and nX == x:
                nX, nY = org.randomPosX(x), org.randomPosY(y)
            if self.swiat.czyZajete(nX, nY) is False:
                from Rosliny.wilcze import wilcze
                self.swiat.dodajOrganizm(wilcze(self.swiat,nX,nY))
                self.swiat.organizmWLokacji(nX, nY).setPomin(True)
        elif nazwa == "mlecz":
            while nY == y and nX == x:
                nX, nY = org.randomPosX(x), org.randomPosY(y)
            if self.swiat.czyZajete(nX, nY) is False:
                from Rosliny.mlecz import mlecz
                self.swiat.dodajOrganizm(mlecz(self.swiat,nX,nY))
                self.swiat.organizmWLokacji(nX, nY).setPomin(True)
