from Abstrakcyjne.Roslina import Roslina
from Abstrakcyjne.Zwierze import Zwierze
class barszcz(Roslina):
    kolor = (250,242,15)
    odleglosc = 0
    def __init__(self, swiat, x, y):
        self.swiat = swiat
        self.x = x
        self.y = y
        self.sila = 10
        self.zyje = True
        self.nazwa = "barszcz"
        self.pomin = False

    def akcja(self):
        if self.zyje is True and self.pomin is False:
            self.wiek += 1
            from Zwierzeta.cyberowca import cyberowca
            if self.swiat.czyZajete(self.x+1, self.y) is True and  \
                    isinstance(self.swiat.organizmWLokacji(self.x+1, self.y), Zwierze) is True and \
                    isinstance(self.swiat.organizmWLokacji(self.x+1, self.y), cyberowca) is False:
                self.swiat.dodajDoZabicia(self.swiat.organizmWLokacji(self.x+1, self.y))
                self.swiat.organizmWLokacji(self.x + 1, self.y).setZyje(False)
                self.swiat.organizmWLokacji(self.x + 1, self.y).setX = -5
            if self.swiat.czyZajete(self.x+1, self.y+1) is True and  \
                    isinstance(self.swiat.organizmWLokacji(self.x+1, self.y+1), Zwierze) is True and \
                    isinstance(self.swiat.organizmWLokacji(self.x+1, self.y+1), cyberowca) is False:
                self.swiat.dodajDoZabicia(self.swiat.organizmWLokacji(self.x+1, self.y+1))
                self.swiat.organizmWLokacji(self.x + 1, self.y + 1).setZyje(False)
                self.swiat.organizmWLokacji(self.x + 1, self.y + 1).setX = -5
            if self.swiat.czyZajete(self.x+1, self.y-1) is True and  \
                    isinstance(self.swiat.organizmWLokacji(self.x+1, self.y-1), Zwierze) is True and \
                    isinstance(self.swiat.organizmWLokacji(self.x+1, self.y-1), cyberowca) is False:
                self.swiat.dodajDoZabicia(self.swiat.organizmWLokacji(self.x+1, self.y-1))
                self.swiat.organizmWLokacji(self.x + 1, self.y - 1).setZyje(False)
                self.swiat.organizmWLokacji(self.x + 1, self.y - 1).setX = -5
            if self.swiat.czyZajete(self.x-1, self.y) is True and \
                    isinstance(self.swiat.organizmWLokacji(self.x-1, self.y), Zwierze) is True and \
                    isinstance(self.swiat.organizmWLokacji(self.x-1, self.y), cyberowca) is False:
                self.swiat.dodajDoZabicia(self.swiat.organizmWLokacji(self.x-1, self.y))
                self.swiat.organizmWLokacji(self.x - 1, self.y).setZyje(False)
                self.swiat.organizmWLokacji(self.x - 1, self.y).setX = -5
            if self.swiat.czyZajete(self.x-1, self.y + 1) is True and \
                    isinstance(self.swiat.organizmWLokacji(self.x-1, self.y+1), Zwierze) is True and \
                    isinstance(self.swiat.organizmWLokacji(self.x-1, self.y+1), cyberowca) is False:
                self.swiat.dodajDoZabicia(self.swiat.organizmWLokacji(self.x-1, self.y + 1))
                self.swiat.organizmWLokacji(self.x-1, self.y + 1).setZyje(False)
                self.swiat.organizmWLokacji(self.x-1, self.y + 1).setX = -5
            if self.swiat.czyZajete(self.x-1, self.y-1) is True and \
                    isinstance(self.swiat.organizmWLokacji(self.x-1, self.y-1), Zwierze) is True and \
                    isinstance(self.swiat.organizmWLokacji(self.x-1, self.y-1), cyberowca) is False:
                self.swiat.dodajDoZabicia(self.swiat.organizmWLokacji(self.x-1, self.y-1))
                self.swiat.organizmWLokacji(self.x-1, self.y-1).setZyje(False)
                self.swiat.organizmWLokacji(self.x-1, self.y-1).setX = -5
            if self.swiat.czyZajete(self.x, self.y + 1) is True and \
                    isinstance(self.swiat.organizmWLokacji(self.x, self.y+1), Zwierze) is True and \
                    isinstance(self.swiat.organizmWLokacji(self.x, self.y+1), cyberowca) is False:
                self.swiat.dodajDoZabicia(self.swiat.organizmWLokacji(self.x, self.y + 1))
                self.swiat.organizmWLokacji(self.x, self.y + 1).setZyje(False)
                self.swiat.organizmWLokacji(self.x, self.y + 1).setX = -5
            if self.swiat.czyZajete(self.x, self.y - 1) is True and  \
                    isinstance(self.swiat.organizmWLokacji(self.x, self.y-1), Zwierze) is True and \
                    isinstance(self.swiat.organizmWLokacji(self.x, self.y-1), cyberowca) is False:
                self.swiat.dodajDoZabicia(self.swiat.organizmWLokacji(self.x, self.y - 1))
                self.swiat.organizmWLokacji(self.x, self.y - 1).setZyje(False)
                self.swiat.organizmWLokacji(self.x, self.y - 1).setX = -5

    def zabijSie(self, organizm):
        self.swiat.dodajDoZabicia(self)
        self.swiat.dodajDoZabicia(organizm)
        self.zyje = False
        organizm.setZyje(False)
        organizm.setX(-2)
        self.x = -5
