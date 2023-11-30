import pygame
from Classes.Niveles.Nivel import Nivel
from Classes.Characters.Personaje_Principal import PersonajePrincipal
from Classes.Characters.Plataforma import Plataforma
from configuraciones import *

class Nivel_3(Nivel):
    def __init__(self, pantalla):
        W = pantalla.get_width()
        H = pantalla.get_height()

        self.count_creacion_vidas = 0
        self.limit_creacione_vidas = 3

        #FONDO
        self.fondo = pygame.Surface((W, H))
        # for bg in bg_space:
        img_escalada = pygame.transform.scale(bg_space[0], (W, H))
        self.fondo.blit(img_escalada, (0,0))
        self.fondo.blit(bg_space[1], (0,0))       
        self.fondo.blit(bg_space[2], (0,0))
        self.fondo.blit(bg_space[3], (0,0))
        self.fondo.blit(bg_space[4], (0,0))


        #PERSONAJE
        posicion = (W/2+ 50, H/2)
        tamaño = (60, 80)
        list_animaciones = dicc_animaciones_personaje
        mi_personaje = PersonajePrincipal(tamaño, posicion, list_animaciones)

        #PLATAFORMAS
        piso = Plataforma((W, 100),(0, H * 0.9), True,r"Assets\Images\Backgrounds\Cave\0.png",index=0 )

        plat1 = Plataforma((200, 50),(100, 300),  True,r"Assets\Images\Backgrounds\Cave\0.png",index=1)
        plat2_5 = Plataforma((200, 50),(70, 600),  True,r"Assets\Images\Backgrounds\Cave\0.png",index=2)
        plat2 = Plataforma((200, 50),(300, 600),  True,r"Assets\Images\Backgrounds\Cave\0.png",index=3)


        plat4 = Plataforma((200, 50),(500,  300),  True,r"Assets\Images\Backgrounds\Cave\0.png",index=4)
        plat5 = Plataforma((200, 50),(700,  600),  True,r"Assets\Images\Backgrounds\Cave\0.png",index=5)


        plat7 = Plataforma((200, 50),(900, 300),  True,r"Assets\Images\Backgrounds\Cave\0.png",index=6)
        plat8 = Plataforma((200, 50),(1100, 600),  True,r"Assets\Images\Backgrounds\Cave\0.png",index=7)

        plat9 = Plataforma((200, 50),(1300, 300),  True,r"Assets\Images\Backgrounds\Cave\0.png",index=8)
        plat10 = Plataforma((200, 50),(1400, 600),  True,r"Assets\Images\Backgrounds\Cave\0.png",index=9)


        lista_plataformas = [piso, plat1, plat2,plat2_5, plat4, plat5, plat7, plat8, plat9, plat10]
        







        super().__init__(pantalla, mi_personaje, lista_plataformas, self.fondo , 3)