import pygame
from Classes.Niveles.Nivel import Nivel
from configuraciones import *

class Nivel_1(Nivel):
    def __init__(self, pantalla:pygame.Surface):
        W = pantalla.get_width()
        H = pantalla.get_height()

        #FONDO
        fondo = pygame.Surface(W, H)
        for bg in bg_demon_forest:
            fondo.blit(bg, (0,0))
        

        #PERSONAJE
        posicion = (W/2, H/2)
        tamaño = (50, 70)




        #PLATAFORMAS




        # ENEMIGOS



    



        # ABAJO DE TODO INICIAMOS EL SUPER YA CON TODO LO NECESARIO PARA INICIARLO
        # super().__init__(pantalla, mi_personaje, lista_plataformas, fondo)