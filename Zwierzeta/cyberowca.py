from Abstrakcyjne.Zwierze import Zwierze
import math
class cyberowca(Zwierze):
    kolor = (233,104,119)
    lista = []
    def __init__(self, swiat, x, y):
        self.swiat = swiat
        self.x = x
        self.y = y
        self.zyje = True
        self.sila = 11
        self.inicjatywa = 4
        self.nazwa = "cyberowca"
        self.pomin = False

    def akcja(self):
        if self.zyje is True and self.pomin is False:
            noweX, noweY = self.x, self.y
            self.wiek += 1
            if self.barszczAlive() is True:
                self.getBarszcz()
                szukanyBarszcz = self.najblizszyBarszcz()
                if szukanyBarszcz.getX() == self.x and szukanyBarszcz.getY() > self.y:
                    noweY += 1
                elif szukanyBarszcz.getX() > self.x and szukanyBarszcz.getY() == self.y:
                    noweX += 1
                elif szukanyBarszcz.getX() > self.x and szukanyBarszcz.getY() > self.y:
                    noweX += 1
                    noweY += 1
                elif szukanyBarszcz.getX() == self.x and szukanyBarszcz.getY() < self.y:
                    noweY -= 1
                elif szukanyBarszcz.getX() < self.x and szukanyBarszcz.getY() == self.y:
                    noweX -= 1
                elif szukanyBarszcz.getX() < self.x and szukanyBarszcz.getY() < self.y:
                    noweX -= 1
                    noweY -= 1
                elif szukanyBarszcz.getX() < self.x and szukanyBarszcz.getY() > self.y:
                    noweX -= 1
                    noweY += 1
                elif szukanyBarszcz.getX() > self.x and szukanyBarszcz.getY() < self.y:
                    noweX += 1
                    noweY -= 1
            else:
                while noweX == self.x and noweY == self.y:
                    noweX = self.randomPosX(self.x)
                    noweY = self.randomPosY(self.y)

            if self.kolizja(noweX, noweY) == 1:
                self.x = noweX
                self.y = noweY
            else:
                return



    def barszczAlive(self):
        from Rosliny.barszcz import barszcz
        for i in self.swiat.organizmy:
            if isinstance(i, barszcz) is True and i.getZyje() is True:
                return True
            else:
                pass
        return False

    def getBarszcz(self):
        from Rosliny.barszcz import barszcz
        for i in self.swiat.organizmy:
            if isinstance(i, barszcz) is True:
                x = abs(self.x - i.getX())
                y = abs(self.y - i.getY())
                i.odleglosc = math.sqrt(x * x + y * y)
                self.lista.append(i)
            else:
                pass

    def najblizszyBarszcz(self):
        for i in range(len(self.lista)-1):
            for j in range(len(self.lista)-1):
                if self.lista[j].odleglosc > self.lista[j+1].odleglosc:
                    temp = self.lista[j]
                    self.lista[j] = self.lista[j+1]
                    self.lista[j+1] = temp
        najblizszy = self.lista[0]
        self.lista.clear()
        return najblizszy




