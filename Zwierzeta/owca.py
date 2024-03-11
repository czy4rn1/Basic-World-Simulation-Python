from Abstrakcyjne.Zwierze import Zwierze

class owca(Zwierze):
    kolor = (255,255,255)
    def __init__(self, swiat, x, y):
        self.swiat = swiat
        self.x = x
        self.y = y
        self.nazwa = "owca"
        self.zyje = True
        self.sila = 4
        self.inicjatywa = 4
        self.pomin = False

