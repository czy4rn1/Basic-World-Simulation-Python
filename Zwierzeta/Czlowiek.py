from Abstrakcyjne.Zwierze import Zwierze
class Czlowiek(Zwierze):
    kolor = (249, 17, 254)
    def __init__(self, swiat, x, y):
        self.swiat = swiat
        self.x = x
        self.y = y
        self.sila = 5
        self.inicjatywa = 7
        self.zyje = True
        self.supermoc = False
        self.glownaSila = 5
        self.licznik = 5
        self.czekaj = 0
        self.nazwa = "czlowiek"
        self.pomin = False

    def akcja(self):
        if self.zyje is True and self.pomin is False:
            self.wiek += 1
            noweX = self.x
            noweY = self.y
            if self.swiat.getKierunek() == 1:
                noweY -= 1
            elif self.swiat.getKierunek() == 2:
                noweY += 1
            elif self.swiat.getKierunek() == 3:
                noweX -= 1
            elif self.swiat.getKierunek() == 4:
                noweX += 1
            if self.swiat.getSupermoc() is True and self.czekaj == 0 and self.licznik == 5:
                self.supermoc = True
                self.glownaSila = self.sila

            self.swiat.setKierunek(0)
            self.Moc()
            if self.kolizja(noweX, noweY) == 1:
                self.x = noweX
                self.y = noweY
            else:
                return




    def superMoc(self):
        self.sila = self.glownaSila + self.licznik
        if self.sila == 5 or self.licznik == 0:
            self.supermoc = False

    def Moc(self):
        if self.supermoc is True:
            if self.licznik >= 0:
                self.superMoc()
                self.licznik -= 1
                if self.licznik == 0:
                    self.czekaj = 7
                    self.swiat.setSupermoc(False)
        if self.czekaj-1 == 0:
            self.licznik = 5
        self.czekaj -= 1
        if self.czekaj <= 0:
            self.czekaj = 0

    def getGlownaSila(self):
        return self.glownaSila
    def setGlownaSila(self, glownaSila):
        self.glownaSila = glownaSila
    def getCzekaj(self):
        return self.czekaj
    def setCzekaj(self, czekaj):
        self.czekaj = czekaj
    def getLicznik(self):
        return self.licznik
    def setLicznik(self, licznik):
        self.licznik = licznik
    def getSupermoc(self):
        return self.supermoc
    def setSupermoc(self, supermoc):
        self.supermoc = supermoc

