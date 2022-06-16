import pygame
import random

class Keraily:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Keräilypeli")
        self.silmukka()

    def silmukka(self):
        self.piirra_naytto()
        self.alkunaytto()

    def piirra_naytto(self):
        self.naytto = pygame.display.set_mode((1200, 650))

    def alkunaytto (self):
        while True:
            naytto = pygame.display.set_mode((1200, 650))
            naytto.fill((0, 0, 0))
            fontti = pygame.font.SysFont("Arial", 24)
            teksti = fontti.render("Keräilypeli", True, (255, 0, 0))
            teksti2 = fontti.render("Kerää robotilla kolikoita, varo hirviöitä!", True, (255, 0, 0))
            teksti3 = fontti.render("Ohjaa robottia nuolinäppäimillä", True, (255, 0, 0))
            teksti4 = fontti.render("Paina F2 aloittaaksesi", True, (255, 0, 0))
            naytto.blit(teksti, (100, 50))
            naytto.blit(teksti2, (100, 100))
            naytto.blit(teksti3, (100, 150))
            naytto.blit(teksti4, (100, 200))
            pygame.display.flip()
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_F2:
                        self.peli()
                if tapahtuma.type == pygame.QUIT:
                    exit()

    def peli(self):
        self.pisteet = 0
        robo = pygame.image.load("robo.png")
        hirvio = pygame.image.load("hirvio.png")
        kolikko = pygame.image.load("kolikko.png")

        #robon aloitupaikka
        x = 0
        y = 480-robo.get_height()

        #hirviön aloituspaikka
        hirvio_x = 0
        hirvio_y = 0

        #hirviö2 aloituspaikka ja nopeus
        h2x = 0
        h2y = 0
        h2xnopeus = 5
        h2ynopeus = 5

        #kolikon aloitupaikka#
        kolikkox= random.randint(0, 1200-robo.get_width())
        kolikkoy= random.randint(0, 650-robo.get_height())

        oikealle = False
        vasemmalle = False
        ylos = False
        alas = False

        kello = pygame.time.Clock()

        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_LEFT:
                        vasemmalle = True
                    if tapahtuma.key == pygame.K_RIGHT:
                        oikealle = True
                    if tapahtuma.key == pygame.K_UP:
                        ylos = True
                    if tapahtuma.key == pygame.K_DOWN:
                        alas = True

                if tapahtuma.type == pygame.KEYUP:
                    if tapahtuma.key == pygame.K_LEFT:
                        vasemmalle = False
                    if tapahtuma.key == pygame.K_RIGHT:
                        oikealle = False
                    if tapahtuma.key == pygame.K_UP:
                        ylos = False
                    if tapahtuma.key == pygame.K_DOWN:
                        alas = False  

                if tapahtuma.type == pygame.QUIT:
                        exit()


            if oikealle and x + robo.get_width()<=1200:
                x += 5
            if vasemmalle and x >=0:
                x -= 5
            if ylos and y >=2 :
                y -= 5
            if alas and y + robo.get_height()<=645:
                y += 5

            #hirviö seuraa roboa            
            if hirvio_x > x:
                hirvio_x -= 2
            if hirvio_x < x:
                hirvio_x += 2
            if hirvio_y > y:
                hirvio_y -= 2
            if hirvio_y < y:
                hirvio_y += 2

            #hirviö2 kimpoilee seinistä
            h2x += h2xnopeus
            h2y += h2ynopeus

            if h2xnopeus > 0 and h2x+robo.get_width() >= 1200:
                h2xnopeus = -h2xnopeus
            if h2xnopeus < 0 and h2x <=0:
                h2xnopeus = -h2xnopeus

            if h2ynopeus > 0 and h2y+robo.get_height() >= 650:
                h2ynopeus = -h2ynopeus

            if h2ynopeus < 0 and h2y <=0:
                h2ynopeus = -h2ynopeus

           #kolikon nappaaminen
            if not x > kolikkox + kolikko.get_width() and not x + kolikko.get_width() < kolikkox:
                if not y > kolikkoy + kolikko.get_height() and not y + kolikko.get_height() < kolikkoy:
                    self.pisteet += 1
                    kolikkox= random.randint(0, 1200-kolikko.get_width())
                    kolikkoy= random.randint(0, 650-kolikko.get_height())

            #hirviöt nappaa robon
            if not x > hirvio_x + hirvio.get_width() and not x + hirvio.get_width() < hirvio_x:
                if not y > hirvio_y + hirvio.get_height() and not y + hirvio.get_height() < hirvio_y:
                    break
            if not x > h2x + hirvio.get_width() and not x + hirvio.get_width() < h2x:
                if not y > h2y + hirvio.get_height() and not y + hirvio.get_height() < h2y:
                    break


            self.naytto.fill((255, 255, 255))
            self.naytto.blit(robo, (x, y))
            self.naytto.blit(hirvio, (hirvio_x, hirvio_y))
            self.naytto.blit(hirvio, (h2x, h2y))
            self.naytto.blit(kolikko, (kolikkox, kolikkoy))
            pygame.display.flip()
            kello.tick(60)
                
        self.peli_ohi()
    
    def peli_ohi(self):
        self.piirra_naytto()
        kello = pygame.time.Clock()
        while True:
            pygame.display.flip()
            kello.tick(60)
            fontti = pygame.font.SysFont("Arial", 24)
            teksti = fontti.render(f"Peli loppui! Pisteet {self.pisteet}", True, (255, 0, 0))
            teksti2 = fontti.render("Paina F2 aloittaaksesi uuden pelin", True, (255, 0, 0))
            self.naytto.blit(teksti, (100, 50))
            self.naytto.blit(teksti2, (100, 100))
            pygame.display.flip()
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    exit()
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_F2:
                        self.peli()


if __name__ == "__main__":
    Keraily()
