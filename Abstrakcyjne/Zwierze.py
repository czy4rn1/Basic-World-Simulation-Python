from Abstrakcyjne.Organizm import *
from abc import ABC


class Zwierze(Organizm, ABC):

    def akcja(self):
        if self.zyje is True and self.pomin is False:
            self.wiek += 1
            noweX = self.x
            noweY = self.y
            while noweX == self.x and noweY == self.y:
                noweX = self.randomPosX(self.x)
                noweY = self.randomPosY(self.y)

            rezultat = self.kolizja(noweX, noweY)
            if rezultat == 1:
                self.x = noweX
                self.y = noweY
            else:
                return

    def kolizja(self, x, y):
        from Zwierzeta.zolw import zolw
        from Rosliny.wilcze import wilcze
        from Rosliny.guarana import guarana
        from Rosliny.barszcz import barszcz
        if self.zyje is True:
            if self.swiat.czyZajete(x, y) is True and self.swiat.organizmWLokacji(x,
                                                                                  y).nazwa != self.nazwa and isinstance(
                    self.swiat.organizmWLokacji(x, y), zolw) is False and \
                    isinstance(self.swiat.organizmWLokacji(x, y), wilcze) is False and isinstance(
                self.swiat.organizmWLokacji(x, y), guarana) is False:
                self.swiat.tekst.append(self.nazwa + " zaatakował " + self.swiat.organizmWLokacji(x, y).getNazwa())
                if self.getSila() < self.swiat.organizmWLokacji(x, y).getSila():
                    self.swiat.dodajDoZabicia(self)
                    self.zyje = False
                    self.x = -5
                    return 0
                elif self.getSila() >= self.swiat.organizmWLokacji(x, y).getSila():
                    self.swiat.organizmWLokacji(x, y).setPomin(True)
                    self.swiat.dodajDoZabicia(self.swiat.organizmWLokacji(x, y))
                    self.swiat.organizmWLokacji(x, y).setZyje(False)
                    self.swiat.organizmWLokacji(x, y).x = -3
                    return 1
            elif self.swiat.czyZajete(x, y) is True and self.swiat.organizmWLokacji(x,
                                                                                    y).nazwa != self.nazwa and isinstance(
                    self.swiat.organizmWLokacji(x, y), zolw) is True:
                self.swiat.tekst.append(self.nazwa + " zaatakował " + self.swiat.organizmWLokacji(x, y).getNazwa())
                if self.swiat.organizmWLokacji(x, y).odbilAtak(self) is True:
                    return 0
                else:
                    return 1
            elif self.swiat.czyZajete(x, y) is True and self.swiat.organizmWLokacji(x, y).nazwa != self.nazwa and \
                    isinstance(self.swiat.organizmWLokacji(x, y), guarana) is True:
                self.swiat.tekst.append(self.nazwa + " zaatakował " + self.swiat.organizmWLokacji(x, y).getNazwa())
                self.swiat.organizmWLokacji(x, y).wzmocnij(self)
                return 1
            elif self.swiat.czyZajete(x, y) is True and self.swiat.organizmWLokacji(x, y).nazwa != self.nazwa and \
                    isinstance(self.swiat.organizmWLokacji(x, y), wilcze) is True:
                self.swiat.tekst.append(self.nazwa + " zaatakował " + self.swiat.organizmWLokacji(x, y).getNazwa())
                self.swiat.organizmWLokacji(x, y).zabijSie(self)
                return 0
            elif self.swiat.czyZajete(x, y) is True and self.swiat.organizmWLokacji(x, y).nazwa != self.nazwa and \
                    isinstance(self.swiat.organizmWLokacji(x, y), barszcz) is True:
                self.swiat.tekst.append(self.nazwa + " zaatakował " + self.swiat.organizmWLokacji(x, y).getNazwa())
                self.swiat.organizmWLokacji(x, y).zabijSie(self)
                return 0
            elif self.swiat.czyZajete(x, y) is True and self.swiat.organizmWLokacji(x,
                                                                                    y).nazwa == self.nazwa and self.swiat.organizmWLokacji(
                    x, y) != self:
                self.rozmnazanie(self, self.nazwa, x, y)
                return 0
            return 1
        else:
            return 0
