import pygame
from Classes.Niveles.Nivel import Nivel
from Classes.Characters.Personaje_Principal import PersonajePrincipal
from configuraciones import *

class Nivel_1(Nivel):
    def __init__(self, pantalla:pygame.Surface):
        W = pantalla.get_width()
        H = pantalla.get_height()
        print(type(W))
        #FONDO
        self.fondo = pygame.Surface((W, H))
        for bg in bg_demon_forest:
            img_escalada = pygame.transform.scale(bg, (W, H))
            self.fondo.blit(img_escalada, (0,0))
        

        #PERSONAJE
        posicion = (W/2, H/2)
        tamaño = (50, 70)
        list_animaciones = list_animaciones_personaje
        mi_personaje = PersonajePrincipal(tamaño, posicion, list_animaciones)



        #PLATAFORMAS



        lista_plataformas = []



        # ABAJO DE TODO INICIAMOS EL SUPER YA CON TODO LO NECESARIO PARA INICIARLO
        super().__init__(pantalla, mi_personaje, lista_plataformas, self.fondo)