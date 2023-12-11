import pygame
from Classes.Characters.Personaje import Personaje
from Classes.Characters.Plataforma import Plataforma

class Enemigo(Personaje):
    def __init__(self, posicion, list_animaciones, velocidad, tamaño):
        self.direcion_actual = 1

        self.eliminar = False
        super().__init__(velocidad, 10,tamaño ,posicion,list_animaciones)
        self.que_hace = "run"
        self.flag_death = True


    def update(self, PANTALLA, plataformas, jugador):
        self.aplicar_gravedad(PANTALLA)
        self.verificar_colision_piso(plataformas)
        self.verificar_colision_pared(plataformas)
        self.comportamiento(plataformas, PANTALLA, jugador)
        self.animar_movimiento(PANTALLA)

    def comportamiento(self, plataformas:list[Plataforma], pantalla, jugador):
        if self.eliminar == False:
            width_rectangulo = self.rectangulos["principal"].width
            recta_proximidad = pygame.Rect(self.rectangulos["principal"].x - width_rectangulo * 3, 
                                        self.rectangulos["principal"].y,
                                        width_rectangulo * 10,
                                        self.rectangulos["principal"].height)
            # pygame.draw.rect(pantalla, "lightblue", recta_proximidad, 3)
            # self.verificar_colision_piso(plataformas)
            nueva_vel = self.velocidad

            if self.esta_aire == False:

                for rect in self.rectangulos:
                    if self.mirando_izq:
                        self.rectangulos[rect].x -= nueva_vel
                    else:
                        self.rectangulos[rect].x += nueva_vel

                for plat in plataformas:
                    #colision limites de plataforma
                    if self.rectangulos["principal"].colliderect(plat.rects_limites["rect_der"]):
                        self.mirando_izq = True
                    if self.rectangulos["principal"].colliderect(plat.rects_limites["rect_izq"]):
                        self.mirando_izq = False

                    #colision paredes
                    if self.rectangulos["principal"].colliderect(plat.rectangulos["left"]):
                        self.mirando_izq = True
                    if self.rectangulos["principal"].colliderect(plat.rectangulos["right"]):
                        self.mirando_izq = False


            if recta_proximidad.colliderect(jugador.rectangulos["principal"]):
                
                if jugador.rectangulos["principal"].x < self.rectangulos["principal"].x:
                    self.mirando_izq = True
                else:
                    self.mirando_izq = False    
                
                if self.rectangulos["principal"].colliderect(jugador.rectangulos["principal"]):
                    self.que_hace = "attack"
                    
            else:
                self.que_hace = "run"
        else:
            print(self.que_hace)
            self.que_hace = "death"
            self.animacion_actual = self.animaciones["death"]
            self.limit_count = 30
            if self.flag_death:
                pygame.time.set_timer(pygame.USEREVENT + 10, 1000)
                self.flag_death = False
