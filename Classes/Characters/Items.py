import pygame
from Classes.Characters.Entidades import Entidades_Juego


class Items(Entidades_Juego):
    def __init__(self, tamaño, posicion, list_animaciones, is_health = False):
        self.eliminar = False
        self.is_health = is_health

        super().__init__(tamaño, posicion, list_animaciones)

    def update(self, pantalla):
        self.animar_movimiento(pantalla)

    def animar_movimiento(self, pantalla):
        if self.pasos_animacion >= len(self.animacion_actual):
            self.pasos_animacion = 0

            
        pantalla.blit(self.animacion_actual[int(self.pasos_animacion)], (self.rectangulos["principal"].x , self.rectangulos["principal"].y ))
        # pantalla.blit(self.animacion_actual[self.pasos_animacion], self.rectangulos["principal"])
        
        self.pasos_animacion += 0.10

    def aplicar_efecto(self, puntaje):
        puntaje += 10