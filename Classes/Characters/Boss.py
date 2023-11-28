import pygame, random
from Classes.Characters.Entidades import Entidades_Juego
from Classes.Characters.Personaje_enemigo import Enemigo
from Classes.Characters.Plataforma import Plataforma
from configuraciones import *

class Boss(Enemigo):
    def __init__(self, posicion, list_animaciones, velocidad, tamaño):

        super().__init__(posicion, list_animaciones, velocidad, tamaño)
        self.mover_boss = True
        self.llego_pos = False
        self.flag = True
        self.is_flying = False

        self.healt = 30
        self.custom_rect = pygame.Rect((posicion[0], posicion[1]), (150,250))

        self.rectangulos = None
        self.rectangulos = Entidades_Juego.obtener_rectangulos(self.custom_rect, 50,50)


        # tamaño display(1900, 1000)
        self.random_pos = None


    def update(self, pantalla,jugador,lista_plataformas):
        self.animar_movimiento(pantalla)

        # if not self.is_flying:
        #     self.aplicar_gravedad()
        
        # self.verificar_colision_piso(lista_plataformas)

        self.comportamiento(jugador, pantalla)


    def comportamiento(self, jugador, pantalla):
       
        
        # Esto para que siempre este mirando para el lado donde esta el jugador
        if jugador.rectangulos["principal"].centerx < self.rectangulos["principal"].centerx:
            self.movimiento_boss(jugador.rectangulos["principal"].center)
            self.mirando_izq = True
        else:
            self.movimiento_boss(jugador.rectangulos["principal"].center)
            self.mirando_izq = False
       

    def movimiento_boss(self, pos):
        vel_x = self.velocidad
        vel_y = self.velocidad


        if self.rectangulos["principal"].x > pos[0]:
            for lado in self.rectangulos:
                self.rectangulos[lado].x -= vel_x
        else:
            for lado in self.rectangulos:
                self.rectangulos[lado].x += vel_x


            if self.rectangulos["principal"].y > pos[1]:
                for lado in self.rectangulos:
                    self.rectangulos[lado].y -= vel_y
            else:
                for lado in self.rectangulos:
                    self.rectangulos[lado].y += vel_y



    def animar_movimiento(self, pantalla):
        self.animacion_actual = self.list_animaciones[self.que_hace]
        self.count += 1

        if self.count > 5:
            self.pasos_animacion += 1
            self.count = 0

        if self.pasos_animacion >= len(self.animacion_actual):
            self.pasos_animacion = 0


        if self.mirando_izq == True:
            # nueva_lista = Entidades_Juego.rotar_imagen(self.animacion_actual[int(self.pasos_animacion)])
            pantalla.blit( pygame.transform.flip(self.animacion_actual[int(self.pasos_animacion)],True,False), (self.rectangulos["principal"].x  - 100, self.rectangulos["principal"].y - 100))
        else:
            pantalla.blit(self.animacion_actual[int(self.pasos_animacion)], (self.rectangulos["principal"].x - 100 , self.rectangulos["principal"].y -100))
