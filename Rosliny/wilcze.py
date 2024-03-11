from Abstrakcyjne.Roslina import Roslina

class wilcze(Roslina):
    kolor = (236, 49, 68)

    def __init__(self, swiat, x, y):
        self.swiat = swiat
        self.x = x
        self.y = y
        self.sila = 99
        self.zyje = True
        self.nazwa = "wilcze"
        self.pomin = False

    def zabijSie(self, organizm):
        self.swiat.dodajDoZabicia(self)
        self.swiat.dodajDoZabicia(organizm)
        self.setZyje(False)
        organizm.setZyje(False)
        organizm.setX(-2)
        self.x = -5