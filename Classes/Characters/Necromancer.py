import pygame, random
from Classes.Characters.Personaje_enemigo import Enemigo
from configuraciones import *

class Necromancer(Enemigo):
    def __init__(self, posicion, list_animaciones, velocidad, tamaño):
        self.delay_creacion = True

        
        super().__init__(posicion, list_animaciones, velocidad, tamaño)

    def update(self, PANTALLA, plataformas, jugador, lista_enemigos):
        self.aplicar_gravedad()
        self.verificar_colision_piso(plataformas)
        self.comportamiento(plataformas,PANTALLA, jugador)
        self.creacion_enemigos(lista_enemigos, PANTALLA)
        self.animar_movimiento(PANTALLA)

    def creacion_enemigos(self, lista_enemigos, pantalla):
        
        if self.delay_creacion:
            pygame.time.set_timer(pygame.USEREVENT + 5 , 15000, 1)
            self.que_hace = 1
            self.delay_creacion = False
            for i in range(5):
                random_x = random.randint(20, pantalla.get_width() -20)
                enemig = Enemigo((random_x,0), skeleton_animation, 3, (50,70))
                lista_enemigos.append(enemig)
        else:
            self.que_hace = 0