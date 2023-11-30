import pygame
from Classes.Niveles.Nivel import Nivel
from Classes.Characters.Personaje_Principal import PersonajePrincipal
from Classes.Characters.Plataforma import Plataforma
from configuraciones import *


class Nivel_2(Nivel):
    def __init__(self, pantalla):
        W = pantalla.get_width()
        H = pantalla.get_height()

        self.count_creacion_vidas = 0
        self.limit_creacione_vidas = 3
        
        #FONDO
        self.fondo = pygame.Surface((W, H))
        for bg in bg_cave:
            img_escalada = pygame.transform.scale(bg, (W, H))
            self.fondo.blit(img_escalada, (0,0))

    
        #PERSONAJE
        posicion = (W/2, H/2)
        tamaño = (60, 80)
        list_animaciones = dicc_animaciones_personaje
        mi_personaje = PersonajePrincipal(tamaño, posicion, list_animaciones)

        #PLATAFORMAS
        piso = Plataforma((W, 100),(0, H * 0.9), True,r"Assets\Images\Backgrounds\Cave\0.png" ,index=0)

        plat1 = Plataforma((200, 50),(100,350),  True,r"Assets\Images\Backgrounds\Cave\0.png",index=1)
        plat2 = Plataforma((300, 50),(600,400), True,r"Assets\Images\Backgrounds\Cave\0.png",index=2)
        plat3 = Plataforma((300, 50),(950,200), True,r"Assets\Images\Backgrounds\Cave\0.png",index=3)
        plat4 = Plataforma((300, 50),(1000,500), True,r"Assets\Images\Backgrounds\Cave\0.png",index=4)
        plat5 = Plataforma((200, 50),(1500,300), True,r"Assets\Images\Backgrounds\Cave\0.png",index=5)
        plat6 = Plataforma((400, 50),(350,650), True,r"Assets\Images\Backgrounds\Cave\0.png",index=6)
        plat7 = Plataforma((400, 50),(1300,650), True,r"Assets\Images\Backgrounds\Cave\0.png",index=7)

        pared = Plataforma((100,100),(940, 100), True,r"Assets\Images\Backgrounds\Cave\0.png", True,index=8)# Pared

        lista_plataformas = [piso, plat1, plat2, plat3, plat4, plat5, plat6,plat7, pared]



        super().__init__(pantalla, mi_personaje, lista_plataformas, self.fondo, 2)
