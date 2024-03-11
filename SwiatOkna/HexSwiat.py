from Swiat import *
import sys
from Zwierzeta.wilk import *
from Zwierzeta.zolw import *
from Zwierzeta.cyberowca import *
from Zwierzeta.Czlowiek import *
from Zwierzeta.lis import *
from Zwierzeta.owca import *
from Zwierzeta.antylopa import *
from Rosliny.trawa import *
from Rosliny.wilcze import *
from Rosliny.mlecz import *
from Rosliny.guarana import *
from Rosliny.barszcz import *

class HexSwiat(Swiat):
    dzwnieb = (150, 222, 230)
    lekki_red = (196, 113, 143)
    kolor_przycisku = (165, 222, 108)
    kolor_tla = (64,38,35)
    czarny = (0, 0, 0)
    kolory = {"wilk": wilk.kolor,
              "zolw": zolw.kolor,
              "cyberowca": cyberowca.kolor,
              "czlowiek": Czlowiek.kolor,
              "lis": lis.kolor,
              "owca": owca.kolor,
              "antylopa": antylopa.kolor,
              "trawa": trawa.kolor,
              "wilcze": wilcze.kolor,
              "barszcz": barszcz.kolor,
              "mlecz": mlecz.kolor,
              "guarana": guarana.kolor,
              None: (167, 85, 2)}
    TILESIZE = 35
    organizmy = []
    doZabicia = []
    kierunek = 0
    superMoc = False
    gatunek = ""

    def __init__(self, *args):
        if len(args) == 2:
            self.MAPWIDTH = args[0]
            self.MAPHEIGHT = args[1]
            self.plansza = [[None for x in range(self.MAPWIDTH)] for y in range(self.MAPHEIGHT)]
            self.dodajOrganizm(Czlowiek(self, 8, 5))
        else:
            self.wczytajOrganizmy()

        pygame.init()
        pygame.mouse.set_visible(True)
        pygame.display.set_caption('Symulator Świata')
        pygame.mixer.init()
        DISPLAY = pygame.display.set_mode((self.MAPWIDTH * self.TILESIZE + 300, self.MAPHEIGHT * self.TILESIZE + 400))
        DISPLAY.fill(self.czarny)
        pygame.draw.rect(DISPLAY, self.dzwnieb, [5, 5, 240, DISPLAY.get_height() - 10])
        pygame.draw.rect(DISPLAY, self.lekki_red, [250, 5, DISPLAY.get_width() - 255, 90])
        pygame.draw.rect(DISPLAY, self.kolor_przycisku, [250, 100, DISPLAY.get_width() - 255, 45])
        pygame.draw.rect(DISPLAY, self.kolor_tla, [250, 150, DISPLAY.get_width() - 255, DISPLAY.get_height() - 155])
        smallfont = pygame.font.SysFont('Arial Black', 15)
        bigger_font = pygame.font.SysFont('Arial', 20)
        text = smallfont.render('Następna Tura', True, (0, 0, 0), (255, 255, 255))
        text2 = bigger_font.render('Michał Czarnobaj', True, (0, 0, 0))
        text3 = bigger_font.render('Informatyka, grupa 1', True, (0, 0, 0))
        text4 = bigger_font.render('Nr indeksu: 188816', True, (0, 0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.zapiszStanGry()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 250 + self.MAPWIDTH * self.MAPWIDTH * 0.8 + 20 <= pygame.mouse.get_pos()[0] <= 250 + self.MAPWIDTH * self.MAPWIDTH * 0.8 + 20 + 120 and 110 <= \
                            pygame.mouse.get_pos()[1] <= 132:
                        self.nastepnaTura(DISPLAY)
                        print(pygame.mouse.get_pos())
                    elif 200 <= pygame.mouse.get_pos()[0] <= DISPLAY.get_width() and \
                            150 <= pygame.mouse.get_pos()[1] <= DISPLAY.get_height():
                        self.spawnKlik(self.gatunek, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                        print(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    self.ustaw(event.key)
            for row in range(self.MAPHEIGHT):
                for col in range(self.MAPWIDTH):
                    points = [(col * self.TILESIZE + 280, row * self.TILESIZE + 375 - 15*col),
                              (col * self.TILESIZE + 266, row * self.TILESIZE + 389 - 15*col),
                              (col * self.TILESIZE + 280, row * self.TILESIZE + 404 - 15*col),
                              (col * self.TILESIZE + 294, row * self.TILESIZE + 404 - 15*col),
                              (col * self.TILESIZE + 309, row * self.TILESIZE + 389 - 15*col),
                              (col * self.TILESIZE + 294, row * self.TILESIZE + 375 - 15*col)]
                    pygame.draw.polygon(DISPLAY, self.kolory[self.plansza[row][col]], points)
            DISPLAY.blit(text, (250 + self.MAPWIDTH * self.MAPWIDTH * 0.8 + 20, 110))
            DISPLAY.blit(text2, (250 + self.MAPWIDTH * self.MAPWIDTH * 0.8 + 8, 15))
            DISPLAY.blit(text3, (250 + self.MAPWIDTH * self.MAPWIDTH * 0.8 + 8, 37))
            DISPLAY.blit(text4, (250 + self.MAPWIDTH * self.MAPWIDTH * 0.8 + 8, 59))
            pygame.display.update()

    def spawnKlik(self, gatunek, x, y):
        spawnX = int((x-280)/35)
        spawnY = int((y-370+15*spawnX)/35)
        if gatunek == "wilk" and self.czyZajete(spawnX, spawnY) is False:
            self.dodajOrganizm(wilk(self,spawnX, spawnY))
        elif gatunek == "owca" and self.czyZajete(spawnX, spawnY) is False:
            self.dodajOrganizm(owca(self, spawnX, spawnY))
        elif gatunek == "antylopa" and self.czyZajete(spawnX, spawnY) is False:
            self.dodajOrganizm(antylopa(self, spawnX, spawnY))
        elif gatunek == "barszcz" and self.czyZajete(spawnX, spawnY) is False:
            self.dodajOrganizm(barszcz(self, spawnX, spawnY))
        elif gatunek == "cyberowca" and self.czyZajete(spawnX, spawnY) is False:
            self.dodajOrganizm(cyberowca(self, spawnX, spawnY))
        elif gatunek == "guarana" and self.czyZajete(spawnX, spawnY) is False:
            self.dodajOrganizm(guarana(self, spawnX, spawnY))
        elif gatunek == "mlecz" and self.czyZajete(spawnX, spawnY) is False:
            self.dodajOrganizm(mlecz(self, spawnX, spawnY))
        elif gatunek == "lis" and self.czyZajete(spawnX, spawnY) is False:
            self.dodajOrganizm(lis(self, spawnX, spawnY))
        elif gatunek == "trawa" and self.czyZajete(spawnX, spawnY) is False:
            self.dodajOrganizm(trawa(self, spawnX, spawnY))
        elif gatunek == "wilcze" and self.czyZajete(spawnX, spawnY) is False:
            self.dodajOrganizm(wilcze(self, spawnX, spawnY))
        elif gatunek == "zolw" and self.czyZajete(spawnX, spawnY) is False:
            self.dodajOrganizm(zolw(self, spawnX, spawnY))
        else:
            pass

        pygame.display.update()