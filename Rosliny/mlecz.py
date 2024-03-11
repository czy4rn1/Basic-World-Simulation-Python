from Abstrakcyjne.Roslina import Roslina
import random


class mlecz(Roslina):
    kolor = (239, 150, 214)

    def __init__(self, swiat, x, y):
        self.swiat = swiat
        self.x = x
        self.y = y
        self.zyje = True
        self.nazwa = "mlecz"
        self.sila = 0
        self.pomin = False

    def akcja(self):
        if self.zyje is True and self.pomin is False:
            self.wiek += 1
            for i in range(3):
                if random.randint(1, 2) == 1:
                    self.rozmnazanie(self, self.nazwa, self.x, self.y)
            self.kolizja(self.x, self.y)
