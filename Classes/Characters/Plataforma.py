import pygame
from Classes.Characters.Entidades import Entidades_Juego

class Plataforma(Entidades_Juego):
    def __init__(self, tamaño, posicion, es_visible = False):
        self.es_visible = es_visible
        self.plataforma = Plataforma.crear_plataforma(es_visible, False, tamaño, posicion)


    @staticmethod
    def crear_plataforma(visible,esPremio, tamaño,posicion, path=""):
        plataforma = {}
        if visible:
            plataforma["superficie"] = pygame.image.load(path)
            plataforma["superficie"] = pygame.transform.scale(plataforma["superficie"],tamaño)
        else:
            plataforma["superficie"] = pygame.Surface(tamaño)
        plataforma["rectangulo"] = plataforma["superficie"].get_rect()
        plataforma["rectangulo"].x = posicion[0]
        plataforma["rectangulo"].y = posicion[1]
        plataforma["premio"] = esPremio
        
        return plataforma