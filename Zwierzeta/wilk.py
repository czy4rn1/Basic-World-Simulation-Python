from Abstrakcyjne.Zwierze import Zwierze


class wilk(Zwierze):
    kolor = (65, 66, 72)
    def __init__(self, swiat, x, y):
        self.swiat = swiat
        self.x = x
        self.y = y
        self.zyje = True
        self.nazwa = "wilk"
        self.sila = 9
        self.inicjatywa = 5
        self.pomin = False
