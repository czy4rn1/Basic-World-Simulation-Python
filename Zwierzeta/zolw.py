import random
from Abstrakcyjne.Zwierze import Zwierze
class zolw(Zwierze):
    kolor = (71,128,0)
    def __init__(self, swiat, x, y):
        self.swiat = swiat
        self.x = x
        self.y = y
        self.zyje = True
        self.sila = 2
        self.inicjatywa = 1
        self.nazwa = "zolw"
        self.pomin = False

    def akcja(self):
        if self.zyje is True and self.pomin is False:
            self.wiek += 1
            case = random.randint(1, 4)
            noweX = self.x
            noweY = self.y
            if case == 1:
                noweX = self.randomPosX(self.x)
                noweY = self.randomPosY(self.y)

            if self.kolizja(noweX, noweY) == 1:
                self.x = noweX
                self.y = noweY
            else:
                return

    def odbilAtak(self, organizm):
        if organizm.getSila() < 5:
            self.swiat.tekst.append("Żółw odbił atak")
            return True
        else:
            self.swiat.dodajDoZabicia(self)
            self.pomin = True
            self.x = -3
            return False