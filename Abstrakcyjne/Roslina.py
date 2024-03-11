from Abstrakcyjne.Organizm import *
from abc import ABC


class Roslina(Organizm, ABC):
    inicjatywa = 0

    def akcja(self):
        if self.zyje is True and self.pomin is False:
            self.rozmnazanie(self, self.nazwa, self.x, self.y)
            self.kolizja(self.x, self.y)


    def kolizja(self, x, y):
        if self.zyje is True:
            if self.swiat.czyZajete(x, y) is True and self.swiat.organizmWLokacji(x, y).nazwa != self.nazwa:
                if (self.getSila() < self.swiat.organizmWLokacji(x, y).getSila()):
                    self.swiat.dodajDoZabicia(self)
                    self.zyje = False
                    self.x = -5
                elif self.getSila() >= self.swiat.organizmWLokacji(x, y).getSila():
                    self.swiat.dodajDoZabicia(self.swiat.organizmWLokacji(x, y))
                    self.swiat.organizmWLokacji(x, y).setZyje(False)
                    self.swiat.organizmWLokacji(x, y).x = -3
