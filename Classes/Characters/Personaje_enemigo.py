import pygame
from Classes.Characters.Personaje import Personaje

class Enemigo(Personaje):
    def __init__(self, posicion, list_animaciones, velocidad):
        self.direcion_actual = 1

        super().__init__(velocidad, 10, (40, 60),posicion,list_animaciones)



    def comportamiento(self, plataformas, pantalla):
        width_rectangulo = self.rectangulos["principal"].width
        recta_proximidad = pygame.Rect(self.rectangulos["principal"].x - width_rectangulo * 3, 
                                       self.rectangulos["principal"].y,
                                       width_rectangulo * 6,
                                       self.rectangulos["principal"].height)
        # pygame.draw.rect(pantalla, "lightblue", recta_proximidad, 3)
        self.verificar_colision_piso(plataformas)
        nueva_vel = self.velocidad

        if self.esta_saltando == False:

            for rect in self.rectangulos:
                if self.mirando_izq:
                    nueva_vel *= -1
                    
                self.rectangulos[rect].x += nueva_vel
        
            new_x = self.rectangulos["principal"].x + nueva_vel 
            if new_x >= pantalla.get_width() - self.rectangulos["principal"].width:
                self.mirando_izq = True

            if new_x <= 0:
                self.mirando_izq = False






    # def caer_libre(self):
    #     if self.esta_saltando == True:
    #         for rect in self.rectangulos:
    #             self.rectangulos[rect].y += 3