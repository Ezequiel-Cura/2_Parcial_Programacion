import pygame
from Classes.Characters.Entidades import Entidades_Juego


class Items(Entidades_Juego):
    def __init__(self, tamaño, posicion, list_animaciones):



        super().__init__(tamaño, posicion, list_animaciones)

    def aplicar_efecto(self):
        pass