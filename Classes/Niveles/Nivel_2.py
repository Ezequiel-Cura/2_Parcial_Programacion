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
        for bg in bg_demon_forest:
            img_escalada = pygame.transform.scale(bg, (W, H))
            self.fondo.blit(img_escalada, (0,0))


        #PERSONAJE
        posicion = (W/2, H/2)
        tamaño = (60, 80)
        list_animaciones = list_animaciones_personaje
        mi_personaje = PersonajePrincipal(tamaño, posicion, list_animaciones)

        #PLATAFORMAS
        piso = Plataforma((W, 100),(0, H * 0.9), False)

        plat1 = Plataforma((200, 50),(W * 0.9, H * 0.7), False)
        plat2 = Plataforma((200, 50),(W * 0.8, H * 0.3), False)
        plat3 = Plataforma((300, 50),(W * 0.2, H * 0.5), False)
        plat4 = Plataforma((300, 50),(W * 0.4, H * 0.7), False)
        plat5 = Plataforma((200, 50),(W * 0.6, H * 0.6), False)
        plat6 = Plataforma((400, 50),(W * 0.5, H * 0.2), False)

        pared = Plataforma((100,100),(W * 0.5, H * 0.2), False)# Pared

        lista_plataformas = [piso, plat1, plat2, plat3, plat4, plat5, plat6, pared]



        super().__init__(pantalla, mi_personaje, lista_plataformas, self.fondo, 2)
