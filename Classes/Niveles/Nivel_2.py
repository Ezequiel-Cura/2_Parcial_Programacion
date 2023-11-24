import pygame
from Classes.Niveles.Nivel import Nivel
from Classes.Characters.Personaje_Principal import PersonajePrincipal
from Classes.Characters.Plataforma import Plataforma
from configuraciones import *


class Nivel_2(Nivel):
    def __init__(self, pantalla):
        W = pantalla.get_width()
        H = pantalla.get_height()

        #FONDO
        self.fondo = pygame.Surface((W, H))
        for bg in bg_cave:
            img_escalada = pygame.transform.scale(bg, (W, H))
            self.fondo.blit(img_escalada, (0,0))


        #PERSONAJE
        posicion = (W/2, H/2)
        tamaño = (60, 80)
        list_animaciones = list_animaciones_personaje
        mi_personaje = PersonajePrincipal(tamaño, posicion, list_animaciones)

        #PLATAFORMAS
        piso = Plataforma((W, 100),(0, H * 0.9), True,r"Assets\Images\Backgrounds\Cave\0.png" )

        plat1 = Plataforma((200, 50),(W * 0.1, H * 0.67),  True,r"Assets\Images\Backgrounds\Cave\0.png")
        plat2 = Plataforma((300, 50),(W * 0.05, H * 0.3), True,r"Assets\Images\Backgrounds\Cave\0.png")
        plat3 = Plataforma((300, 50),(W * 0.23, H * 0.22), True,r"Assets\Images\Backgrounds\Cave\0.png")
        plat4 = Plataforma((300, 50),(W * 0.3, H * 0.5), True,r"Assets\Images\Backgrounds\Cave\0.png")
        plat5 = Plataforma((200, 50),(W * 0.6, H * 0.6), True,r"Assets\Images\Backgrounds\Cave\0.png")
        plat6 = Plataforma((400, 50),(W * 0.5, H * 0.2), True,r"Assets\Images\Backgrounds\Cave\0.png")

        pared = Plataforma((100,100),(W * 0.5, H * 0.1), False)# Pared

        lista_plataformas = [piso, plat1, plat2, plat3, plat4, plat5, plat6, pared]



        super().__init__(pantalla, mi_personaje, lista_plataformas, self.fondo, 2)
