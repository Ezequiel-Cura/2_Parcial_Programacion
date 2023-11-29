import pygame
from Classes.Niveles.Nivel import Nivel
from Classes.Characters.Personaje_Principal import PersonajePrincipal
from Classes.Characters.Plataforma import Plataforma
from configuraciones import *

class Nivel_1(Nivel):
    def __init__(self, pantalla:pygame.Surface):
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
        dicc_animaciones = dicc_animaciones_personaje
        mi_personaje = PersonajePrincipal(tamaño, posicion, dicc_animaciones)

        #PLATAFORMAS
        piso = Plataforma((W, 100),(0, H * 0.9), True,r"Assets\Images\Backgrounds\Forest\0.png")

        plat1 = Plataforma((200, 50),(W * 0.5, H * 0.7), True,r"Assets\Images\Backgrounds\Forest\0.png")
        plat2 = Plataforma((200, 50),(W * 0.7, H * 0.6), True,r"Assets\Images\Backgrounds\Forest\0.png")
        plat3 = Plataforma((300, 50),(100, 200), True,r"Assets\Images\Backgrounds\Forest\0.png")
        plat4 = Plataforma((300, 50),(500, 400), True,r"Assets\Images\Backgrounds\Forest\0.png")
        plat5 = Plataforma((200, 50),(W * 0.1, H * 0.5), True,r"Assets\Images\Backgrounds\Forest\0.png")

        plat6 = Plataforma((100, 200),(200, H * 0.8), True,r"Assets\Images\Backgrounds\Forest\0.png")
        
        lista_plataformas = [piso, plat1, plat2, plat3, plat4, plat5, plat6]



        # INICIAMOS EL SUPER YA CON TODO LO NECESARIO PARA INICIARLO
        super().__init__(pantalla, mi_personaje, lista_plataformas, self.fondo,1)