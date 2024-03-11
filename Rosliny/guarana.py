from Abstrakcyjne.Roslina import Roslina

class guarana(Roslina):
    kolor = (146, 255, 243)

    def __init__(self, swiat, x, y):
        self.x = x
        self.y = y
        self.swiat = swiat
        self.zyje = True
        self.nazwa = "guarana"
        self.sila = 0
        self.pomin = False

    def wzmocnij(self, organizm):
        self.swiat.dodajDoZabicia(self)
        organizm.setSila(organizm.getSila() + 3)
        self.zyje = False
        self.x = -2