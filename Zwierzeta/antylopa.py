from Abstrakcyjne.Zwierze import Zwierze
import random


class antylopa(Zwierze):
    kolor = (0, 103, 196)

    def __init__(self, swiat, x, y):
        self.swiat = swiat
        self.x = x
        self.y = y
        self.sila = 4
        self.inicjatywa = 4
        self.zyje = True
        self.nazwa = "antylopa"
        self.pomin = False

    def akcja(self):
        if self.zyje is True and self.pomin is False:
            self.wiek += 1
            noweX = self.x
            noweY = self.y
            while noweX == self.x and noweY == self.y:
                noweX = self.randomPosX(noweX)
                noweY = self.randomPosY(noweY)

            if self.kolizja(noweX, noweY) == 1:
                self.x = noweX
                self.y = noweY
            else:
                return

    def randomPosX(self, x):
        case = random.randint(1, 3)
        if case == 1 and x + 2 <= self.swiat.MAPWIDTH - 1:
            x += 2
            return x
        elif case == 2 and x - 2 >= 0:
            x -= 2
            return x
        elif case == 3:
            return x
        return x

    def randomPosY(self, y):
        case = random.randint(1, 3)
        if case == 1 and y + 2 <= self.swiat.MAPHEIGHT - 1:
            y += 2
            return y
        elif case == 2 and y - 2 >= 0:
            y -= 2
            return y
        elif case == 3:
            return y
        return y

    def randomPosXUcieczka(self, x):
        case = random.randint(1, 3)
        if case == 1 and x + 1 <= self.swiat.MAPWIDTH - 1:
            x += 1
            return x
        elif case == 2 and x - 1 >= 0:
            x -= 1
            return x
        elif case == 3:
            return x
        return x

    def randomPosYUcieczka(self, y):
        case = random.randint(1, 3)
        if case == 1 and y + 1 <= self.swiat.MAPHEIGHT - 1:
            y += 1
            return y
        elif case == 2 and y - 1 >= 0:
            y -= 1
            return y
        elif case == 3:
            return y
        return y

    def kolizja(self, x, y):
        case = random.randint(1, 2)
        from Rosliny.wilcze import wilcze
        from Rosliny.guarana import guarana
        from Rosliny.barszcz import barszcz
        from Zwierzeta.zolw import zolw
        if self.zyje is True:
            if self.swiat.czyZajete(x, y) is True and self.swiat.organizmWLokacji(x,
                                                                                      y).nazwa != self.nazwa and isinstance(
                        self.swiat.organizmWLokacji(x, y), zolw) is False and \
                        isinstance(self.swiat.organizmWLokacji(x, y), wilcze) is False and isinstance(
                self.swiat.organizmWLokacji(x, y), guarana) is False:
                if self.getSila() < self.swiat.organizmWLokacji(x, y).getSila():
                    if case == 1:
                        self.swiat.tekst.append(
                            self.nazwa + " zaatakował " + self.swiat.organizmWLokacji(x, y).getNazwa())
                        self.swiat.dodajDoZabicia(self)
                        self.zyje = False
                        self.x = -5
                        return 0
                    else:
                        nX, nY = self.randomPosXUcieczka(x), self.randomPosYUcieczka(y)
                        while self.swiat.czyZajete(nX, nY) is True:
                            nX, nY = self.randomPosXUcieczka(x), self.randomPosYUcieczka(y)
                        self.x = nX
                        self.y = nY
                        self.swiat.tekst.append("Antylopa uciekla")
                        return 0
                elif self.getSila() >= self.swiat.organizmWLokacji(x, y).getSila():
                    if case == 1:
                        self.swiat.tekst.append(
                            self.nazwa + " zaatakował " + self.swiat.organizmWLokacji(x, y).getNazwa())
                        self.swiat.dodajDoZabicia(self.swiat.organizmWLokacji(x, y))
                        self.swiat.organizmWLokacji(x, y).setZyje(False)
                        self.swiat.organizmWLokacji(x, y).x = -3
                        return 1
                    else:
                        nX, nY = self.randomPosXUcieczka(x), self.randomPosYUcieczka(y)
                        while self.swiat.czyZajete(nX, nY) is True:
                            nX, nY = self.randomPosXUcieczka(x), self.randomPosYUcieczka(y)
                        self.x = nX
                        self.y = nY
                        self.swiat.tekst.append("Antylopa uciekla")
                        return 0
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
            elif self.swiat.czyZajete(x, y) is True and self.swiat.organizmWLokacji(x,y).nazwa == self.nazwa and self.swiat.organizmWLokacji(
                        x, y) != self:
                self.rozmnazanie(self, self.nazwa, x, y)
                return 0
            return 1
        else:
            return 0
