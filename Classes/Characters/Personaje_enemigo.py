import pygame
from Classes.Characters.Personaje import Personaje
from Classes.Characters.Plataforma import Plataforma
class Enemigo(Personaje):
    def __init__(self, posicion, list_animaciones, velocidad):
        self.direcion_actual = 1

        super().__init__(velocidad, 10, (40, 60),posicion,list_animaciones)



    def comportamiento(self, plataformas:list[Plataforma], pantalla, jugador):
        width_rectangulo = self.rectangulos["principal"].width
        recta_proximidad = pygame.Rect(self.rectangulos["principal"].x - width_rectangulo * 3, 
                                       self.rectangulos["principal"].y,
                                       width_rectangulo * 6,
                                       self.rectangulos["principal"].height)
        # pygame.draw.rect(pantalla, "lightblue", recta_proximidad, 3)
        # self.verificar_colision_piso(plataformas)
        nueva_vel = self.velocidad

        if self.esta_aire == False:

            for rect in self.rectangulos:
                if self.mirando_izq:
                    # nueva_vel *= -1
                    self.rectangulos[rect].x -= nueva_vel
                else:

                
                # self.rectangulos["left"].x += nueva_vel
                    self.rectangulos[rect].x += nueva_vel

            for plat in plataformas:
                if self.rectangulos["principal"].colliderect(plat.rects_limites["rect_der"]):
                    self.mirando_izq = True
                
                if self.rectangulos["principal"].colliderect(plat.rects_limites["rect_izq"]):
                    self.mirando_izq = False


        if recta_proximidad.colliderect(jugador.rectangulos["principal"]):
            
            if jugador.rectangulos["principal"].x < self.rectangulos["principal"].x:
                self.mirando_izq = True
            else:
                self.mirando_izq = False    
            
            if self.rectangulos["principal"].colliderect(jugador.rectangulos["principal"]):
                self.que_hace = 1
                jugador.vidas -= 3
            
        else:
            self.que_hace = 0





    # def caer_libre(self):
    #     if self.esta_saltando == True:
    #         for rect in self.rectangulos:
    #             self.rectangulos[rect].y += 3