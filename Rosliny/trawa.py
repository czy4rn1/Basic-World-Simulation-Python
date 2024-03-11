from Abstrakcyjne.Roslina import Roslina
class trawa(Roslina):
    kolor = (1, 239, 4)

    def __init__(self, swiat, x, y):
        self.swiat = swiat
        self.x = x
        self.y = y
        self.sila = 0
        self.zyje = True
        self.nazwa = "trawa"
        self.pomin = False
