import pygame
from Classes.Niveles.Nivel import Nivel
from Classes.Characters.Personaje_Principal import PersonajePrincipal
from Classes.Characters.Plataforma import Plataforma
from configuraciones import *

class Nivel_1(Nivel):
    def __init__(self, pantalla:pygame.Surface):
        W = pantalla.get_width()
        H = pantalla.get_height()

        self.count_creacion_vidas = 0
        self.limit_creacione_vidas = 3

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
        piso = Plataforma((W, 100),(0, H * 0.9), True,r"Assets\Images\Backgrounds\Forest\0.png",index=0)

        plat1 = Plataforma((200, 50),(40,500), True,r"Assets\Images\Backgrounds\Forest\0.png",index=1)
        plat2 = Plataforma((200, 50),(800, 250), True,r"Assets\Images\Backgrounds\Forest\0.png",index=2)
        plat3 = Plataforma((300, 50),(700, 600), True,r"Assets\Images\Backgrounds\Forest\0.png",index=3)
        plat4 = Plataforma((300, 50),(1400, 200), True,r"Assets\Images\Backgrounds\Forest\0.png",index=4)
        plat5 = Plataforma((200, 50),(1100,500), True,r"Assets\Images\Backgrounds\Forest\0.png",index=5)
        plat6 = Plataforma((200, 50),(150,200), True,r"Assets\Images\Backgrounds\Forest\0.png",index=6)
        plat7 = Plataforma((200, 50),(1500,650), True,r"Assets\Images\Backgrounds\Forest\0.png",index=7)
        plat8 = Plataforma((200, 50),(460,400), True,r"Assets\Images\Backgrounds\Forest\0.png",index=8)
        plat9 = Plataforma((200, 50),(1500,650), True,r"Assets\Images\Backgrounds\Forest\0.png",index=9)

        plat10 = Plataforma((100, 200),(200, H * 0.8), True,r"Assets\Images\Backgrounds\Forest\0.png",index=10)
        
        lista_plataformas = [piso, plat1, plat2, plat3, plat4, plat5, plat6, plat7, plat8, plat9, plat10]



        # INICIAMOS EL SUPER YA CON TODO LO NECESARIO PARA INICIARLO
        super().__init__(pantalla, mi_personaje, lista_plataformas, self.fondo,1)