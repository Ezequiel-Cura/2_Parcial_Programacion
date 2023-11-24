import pygame, random
from Classes.Characters.Personaje_enemigo import Enemigo
from Classes.Characters.Plataforma import Plataforma
from configuraciones import *

class Boss(Enemigo):
    def __init__(self, posicion, list_animaciones, velocidad, tamaño):
        self.mover_boss = True
        self.superficie = pygame.Surface((300,400))
        


        super().__init__(posicion, list_animaciones, velocidad, tamaño)
    
    def update(self, pantalla,jugador):
        self.animar_movimiento(pantalla)

        self.comportamiento(jugador)


    def comportamiento(self, jugador):
        random_x = random.randint(200, 1600)
        random_y = random.randint(400,800)

        if self.mover_boss:
            self.mover_boss = True
            if self.rectangulos["principal"].x > random_x:
                self.rectangulos["principal"].x -= self.velocidad
            else:
                self.rectangulos["principal"].x += self.velocidad
            if self.rectangulos["principal"].y > random_y:
                self.rectangulos["principal"].y -= self.velocidad
            else:
                self.rectangulos["principal"].y += self.velocidad
            # self.rectangulos["principal"].x = random_x
            # self.rectangulos["principal"].y = random_y
            pygame.time.set_timer(pygame.USEREVENT + 6, 5000,1)
        
        if jugador.rectangulos["principal"].centerx < self.rectangulos["principal"].centerx:
            self.mirando_izq = True
        else:
            self.mirando_izq = False

