import pygame
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


class Swiat:
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
    TILESIZE = 25
    organizmy = []
    doZabicia = []
    kierunek = 0
    superMoc = False
    gatunek = ""
    tekst = []

    def __init__(self, *args):
        if len(args) == 2:
            self.MAPWIDTH = args[0]
            self.MAPHEIGHT = args[1]
            self.plansza = [[None for x in range(self.MAPWIDTH)] for y in range(self.MAPHEIGHT)]
            self.dodajOrganizm(Czlowiek(self, 5, 8))
        else:
            self.wczytajOrganizmy()

        pygame.init()
        pygame.mouse.set_visible(True)
        pygame.display.set_caption('Symulator Świata')
        pygame.mixer.init()
        DISPLAY = pygame.display.set_mode((self.MAPWIDTH * self.TILESIZE + 300, self.MAPHEIGHT * self.TILESIZE + 250))
        DISPLAY.fill(self.czarny)
        pygame.draw.rect(DISPLAY, self.dzwnieb, [5, 5, 240, DISPLAY.get_height() - 10])
        pygame.draw.rect(DISPLAY, self.lekki_red, [250, 5, DISPLAY.get_width() - 255, 90])
        pygame.draw.rect(DISPLAY, self.kolor_przycisku, [250, 100, DISPLAY.get_width() - 255, 45])
        pygame.draw.rect(DISPLAY, self.kolor_tla, [250, 150, DISPLAY.get_width() - 255, DISPLAY.get_height() - 155])
        smallfont = pygame.font.SysFont('Arial Black', 15)
        bigger_font = pygame.font.SysFont('Arial', 20)
        text = smallfont.render('Następna Tura', True, (0, 0, 0), (255, 255, 255))
        text2 = bigger_font.render('Michał Czarnobaj', True, (0,0,0))
        text3 = bigger_font.render('Informatyka, grupa 1', True, (0,0,0))
        text4 = bigger_font.render('Nr indeksu: 188816', True, (0,0,0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.zapiszStanGry()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 250 + self.MAPWIDTH*self.MAPWIDTH*0.5+20 <= pygame.mouse.get_pos()[
                        0] <= 250 + self.MAPWIDTH*self.MAPWIDTH*0.5+20 + 120 and 110 <= \
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
                    pygame.draw.rect(DISPLAY, self.kolory[self.plansza[row][col]],
                                     (col * self.TILESIZE + 275, row * self.TILESIZE + 200, self.TILESIZE - 5,
                                      self.TILESIZE - 5))
            DISPLAY.blit(text, (250 + self.MAPWIDTH*self.MAPWIDTH*0.5+20, 110))
            DISPLAY.blit(text2, (250 + self.MAPWIDTH*self.MAPWIDTH*0.5+8, 15))
            DISPLAY.blit(text3, (250 + self.MAPWIDTH*self.MAPWIDTH*0.5+8, 37))
            DISPLAY.blit(text4, (250 + self.MAPWIDTH*self.MAPWIDTH*0.5+8, 59))
            pygame.display.update()

    def dodajOrganizm(self, organizm: object) -> object:
        self.organizmy.append(organizm)
        for i in range(len(self.organizmy) - 1):
            for j in range(len(self.organizmy) - 1):
                if self.organizmy[j].getInicjatywa() < self.organizmy[j + 1].getInicjatywa():
                    temp = self.organizmy[j]
                    self.organizmy[j] = self.organizmy[j + 1]
                    self.organizmy[j + 1] = temp
                elif self.organizmy[j].getInicjatywa() == self.organizmy[j + 1].getInicjatywa():
                    if self.organizmy[j].getWiek() < self.organizmy[j + 1].getWiek():
                        temp = self.organizmy[j]
                        self.organizmy[j] = self.organizmy[j + 1]
                        self.organizmy[j + 1] = temp
        self.tekst.append("Właśnie powstał "+organizm.getNazwa())
        self.zaaranzujPlansze()

    def zaaranzujPlansze(self):
        self.plansza = [[None for x in range(self.MAPWIDTH)] for y in range(self.MAPHEIGHT)]
        for org in self.organizmy:
            for i in range(self.MAPHEIGHT):
                for j in range(self.MAPWIDTH):
                    if org.getZyje() is True and org.x == j and org.y == i:
                        self.plansza[i][j] = org.nazwa

    def dodajDoZabicia(self, organizm: object) -> object:
        self.doZabicia.append(organizm)
        self.tekst.append("Właśnie umarł "+organizm.getNazwa())

    def nastepnaTura(self, DISPLAY):
        pygame.draw.rect(DISPLAY, self.dzwnieb, [5, 5, 240, DISPLAY.get_height() - 10])
        for k in self.organizmy:
            k.setPomin(False)
        for i in self.organizmy:
            i.akcja()
            if isinstance(i, Czlowiek):
                print(i.getSila())
        for j in self.doZabicia:
            if j in self.organizmy:
                self.organizmy.remove(j)
        self.doZabicia.clear()
        self.zaaranzujPlansze()
        font = pygame.font.SysFont('Arial', 18)
        label = []
        for i in self.tekst:
            label.append(font.render(i, True, (0,0,0)))
        for line in range(len(label)):
            DISPLAY.blit(label[line], (15, 5+15*line))
        self.tekst.clear()
        label.clear()
        pygame.display.update()

    def czyZajete(self, x, y):
        for i in self.organizmy:
            if i.getX() == x and i.getY() == y:
                return True
            else:
                pass
        return False

    def organizmWLokacji(self, x, y):
        for i in self.organizmy:
            if i.getX() == x and i.getY() == y:
                return i
            else:
                pass
        return None

    def getSupermoc(self):
        return self.superMoc

    def setSupermoc(self, supermoc):
        self.superMoc = supermoc

    def getKierunek(self):
        return self.kierunek

    def setKierunek(self, kierunek):
        self.kierunek = kierunek

    def spawnKlik(self, gatunek, x, y):
        spawnX = int((x - 275) / 25)
        spawnY = int((y - 200) / 25)
        if gatunek == "wilk":
            self.dodajOrganizm(wilk(self, spawnX, spawnY))
        elif gatunek == "owca":
            self.dodajOrganizm(owca(self, spawnX, spawnY))
        elif gatunek == "antylopa":
            self.dodajOrganizm(antylopa(self, spawnX, spawnY))
        elif gatunek == "barszcz":
            self.dodajOrganizm(barszcz(self, spawnX, spawnY))
        elif gatunek == "cyberowca":
            self.dodajOrganizm(cyberowca(self, spawnX, spawnY))
        elif gatunek == "guarana":
            self.dodajOrganizm(guarana(self, spawnX, spawnY))
        elif gatunek == "mlecz":
            self.dodajOrganizm(mlecz(self, spawnX, spawnY))
        elif gatunek == "lis":
            self.dodajOrganizm(lis(self, spawnX, spawnY))
        elif gatunek == "trawa":
            self.dodajOrganizm(trawa(self, spawnX, spawnY))
        elif gatunek == "wilcze":
            self.dodajOrganizm(wilcze(self, spawnX, spawnY))
        elif gatunek == "zolw":
            self.dodajOrganizm(zolw(self, spawnX, spawnY))
        else:
            pass

        pygame.display.update()

    def zapiszStanGry(self):
        f = open('C:/Users/micha/Desktop/GraOOP/zapis.txt', 'w') # path to the game directory + 'zapis.txt', the savefile
        f.write(str(self.MAPWIDTH) + " " + str(self.MAPHEIGHT) + "\n")
        for i in self.organizmy:
            if isinstance(i, Czlowiek) is True:
                f.write(
                    str(i.getNazwa()) + " " + str(i.getX()) + " " + str(i.getY()) + " " + str(i.getSila()) + " " + str(
                        i.getInicjatywa()) + " " + str(i.getWiek()) + " " + str(i.getGlownaSila()) + " " + str(
                        i.getCzekaj()) + " " + str(i.getLicznik()) + " " + str(i.getSupermoc()) + "\n")
            else:
                f.write(
                    str(i.getNazwa()) + " " + str(i.getX()) + " " + str(i.getY()) + " " + str(i.getSila()) + " " + str(
                        i.getInicjatywa()) + " " + str(i.getWiek()) + "\n")

    def wczytajOrganizmy(self):
        f = open('C:/Users/micha/Desktop/GraOOP/zapis.txt', 'r') # path to the game directory + 'zapis.txt', the savefile
        lista = f.readlines()
        for i in lista:
            my_data = i.split()
            if len(my_data) == 2:
                self.MAPWIDTH = int(my_data[0])
                self.MAPHEIGHT = int(my_data[1])
                self.plansza = [[None for x in range(self.MAPWIDTH)] for y in range(self.MAPHEIGHT)]
            elif len(my_data) > 2 and my_data[0] == "czlowiek":
                czlowiek = Czlowiek(self, int(my_data[1]), int(my_data[2]))
                self.dodajOrganizm(czlowiek)
                czlowiek.setSila(int(my_data[3]))
                czlowiek.setWiek(int(my_data[5]))
                czlowiek.setGlownaSila(int(my_data[6]))
                czlowiek.setCzekaj(int(my_data[7]))
                czlowiek.setLicznik(int(my_data[8]))
                czlowiek.setSupermoc(bool(my_data[9]))
            else:
                if my_data[0] == "wilk":
                    wilK = wilk(self, int(my_data[1]), int(my_data[2]))
                    self.dodajOrganizm(wilK)
                    wilK.setSila(int(my_data[3]))
                    wilK.setWiek(int(my_data[5]))
                elif my_data[0] == "barszcz":
                    barszcZ = barszcz(self, int(my_data[1]), int(my_data[2]))
                    self.dodajOrganizm(barszcZ)
                    barszcZ.setWiek(int(my_data[5]))
                elif my_data[0] == "cyberowca":
                    cyberowcA = cyberowca(self, int(my_data[1]), int(my_data[2]))
                    self.dodajOrganizm(cyberowcA)
                    cyberowcA.setSila(int(my_data[3]))
                    cyberowcA.setWiek(int(my_data[5]))
                elif my_data[0] == "antylopa":
                    antylopA = antylopa(self, int(my_data[1]), int(my_data[2]))
                    self.dodajOrganizm(antylopA)
                    antylopA.setSila(int(my_data[3]))
                    antylopA.setWiek(int(my_data[5]))
                elif my_data[0] == "guarana":
                    guaranA = guarana(self, int(my_data[1]), int(my_data[2]))
                    self.dodajOrganizm(guaranA)
                    guaranA.setSila(int(my_data[3]))
                    guaranA.setWiek(int(my_data[5]))
                elif my_data[0] == "lis":
                    liS = lis(self, int(my_data[1]), int(my_data[2]))
                    self.dodajOrganizm(liS)
                    liS.setSila(int(my_data[3]))
                    liS.setWiek(int(my_data[5]))
                elif my_data[0] == "mlecz":
                    mlecZ = mlecz(self, int(my_data[1]), int(my_data[2]))
                    self.dodajOrganizm(mlecZ)
                    mlecZ.setSila(int(my_data[3]))
                    mlecZ.setWiek(int(my_data[5]))
                elif my_data[0] == "owca":
                    owcA = owca(self, int(my_data[1]), int(my_data[2]))
                    self.dodajOrganizm(owcA)
                    owcA.setSila(int(my_data[3]))
                    owcA.setWiek(int(my_data[5]))
                elif my_data[0] == "trawa":
                    trawA = trawa(self, int(my_data[1]), int(my_data[2]))
                    self.dodajOrganizm(trawA)
                    trawA.setSila(int(my_data[3]))
                    trawA.setWiek(int(my_data[5]))
                elif my_data[0] == "wilcze":
                    wilczE = wilcze(self, int(my_data[1]), int(my_data[2]))
                    self.dodajOrganizm(wilczE)
                    wilczE.setSila(int(my_data[3]))
                    wilczE.setWiek(int(my_data[5]))
                elif my_data[0] == "zolw":
                    zolW = zolw(self, int(my_data[1]), int(my_data[2]))
                    self.dodajOrganizm(zolW)
                    zolW.setSila(int(my_data[3]))
                    zolW.setWiek(int(my_data[5]))

    def ustaw(self, key):
        if key == pygame.K_UP:
            self.kierunek = 1
        elif key == pygame.K_DOWN:
            self.kierunek = 2
        elif key == pygame.K_LEFT:
            self.kierunek = 3
        elif key == pygame.K_RIGHT:
            self.kierunek = 4
        elif key == pygame.K_w:
            for i in self.organizmy:
                if isinstance(i, Czlowiek) and i.getLicznik() == 5:
                    self.superMoc = True
                    self.tekst.append("Człowiek aktywował moc")
        if key == pygame.K_z:
            self.gatunek = "zolw"
            print(self.gatunek)
        elif key == pygame.K_x:
            self.gatunek = "wilk"
            print(self.gatunek)
        elif key == pygame.K_o:
            self.gatunek = "owca"
            print(self.gatunek)
        elif key == pygame.K_l:
            self.gatunek = "lis"
            print(self.gatunek)
        elif key == pygame.K_c:
            self.gatunek = "cyberowca"
            print(self.gatunek)
        elif key == pygame.K_a:
            self.gatunek = "antylopa"
            print(self.gatunek)
        elif key == pygame.K_b:
            self.gatunek = "barszcz"
            print(self.gatunek)
        elif key == pygame.K_g:
            self.gatunek = "guarana"
            print(self.gatunek)
        elif key == pygame.K_m:
            self.gatunek = "mlecz"
            print(self.gatunek)
        elif key == pygame.K_t:
            self.gatunek = "trawa"
            print(self.gatunek)
        elif key == pygame.K_j:
            self.gatunek = "wilcze"
            print(self.gatunek)
        else:
            pass
