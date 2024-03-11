from Abstrakcyjne.Zwierze import Zwierze


class lis(Zwierze):
    kolor = (255,144,4)
    def __init__(self, swiat, x, y):
        self.swiat = swiat
        self.x = x
        self.y = y
        self.zyje = True
        self.nazwa = "lis"
        self.sila= 3
        self.inicjatywa = 7
        self.pomin = False

    def akcja(self):
        if self.zyje is True and self.pomin is False:
            if self.swiat.czyZajete(self.x + 1, self.y) is True \
                    and self.swiat.organizmWLokacji(self.x + 1, self.y).getSila() > self.sila\
                    and self.swiat.czyZajete(self.x - 1, self.y) is True\
                    and self.swiat.organizmWLokacji(self.x - 1, self.y).getSila() > self.sila\
                    and self.swiat.czyZajete(self.x, self.y + 1) is True \
                    and self.swiat.organizmWLokacji(self.x, self.y+1).getSila() > self.sila\
                    and self.swiat.czyZajete(self.x, self.y - 1) is True \
                    and self.swiat.organizmWLokacji(self.x, self.y-1).getSila() > self.sila \
                    and self.swiat.czyZajete(self.x + 1, self.y + 1) is True \
                    and self.swiat.organizmWLokacji(self.x+1, self.y+1).getSila() > self.sila \
                    and self.swiat.czyZajete(self.x - 1, self.y - 1) is True \
                    and self.swiat.organizmWLokacji(self.x-1, self.y-1).getSila() \
                    and self.swiat.czyZajete(self.x - 1, self.y + 1) is True \
                    and self.swiat.organizmWLokacji(self.x-1, self.y+1).getSila() > self.sila\
                    and self.swiat.czyZajete(self.x + 1, self.y - 1) is True \
                    and self.swiat.organizmWLokacji(self.x+1, self.y-1).getSila() > self.sila:
                pass
            else:
                self.wiek += 1
                noweX = self.x
                noweY = self.y
                while True:
                    noweX = self.randomPosX(self.x)
                    noweY = self.randomPosY(self.y)
                    if self.swiat.czyZajete(noweX, noweY) is False or \
                    self.sila >= self.swiat.organizmWLokacji(noweX, noweY).getSila():
                        break
                rezultat = self.kolizja(noweX, noweY)
                if rezultat == 1:
                    self.x = noweX
                    self.y = noweY
                else:
                    return
