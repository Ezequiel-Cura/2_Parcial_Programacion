from Classes.Characters.Personaje import Personaje
import pygame
from configuraciones import *
class PersonajePrincipal(Personaje):
    def __init__(self, tamaño, posicion, animaciones):
        velocidad = 5
        potencia_salto = 25
        self.score = 0
        
        self.vidas = 3
        self.esta_saltando = False
        self.inmune = False
        self.movimiento_aereo = False
        # animaciones_res = Personaje.reescalar_imagenes(animaciones, tamaño[0], tamaño[1])

        self.list_proyectiles  = [] 
        super().__init__(velocidad, potencia_salto, tamaño, posicion, animaciones)


    def verificar_colision_enemigo(self, lista_enemigos):
        for enemigo in lista_enemigos:
            if self.inmune == False:
                if self.rectangulos["principal"].colliderect(enemigo.rectangulos["principal"]):
                    pygame.time.set_timer(pygame.USEREVENT + 4, 3000, 1)
                    self.inmune = True
                    self.vidas -= 1
        
    def update(self, PANTALLA, plataformas, lista_enemigos, lista_recompensas, puntaje, lista_vidas):
        
        
        if self.que_hace == "idle" and not self.esta_aire:
            if not self.esta_aire:
                self.limit_count = 5
                self.animacion_actual = self.animaciones["idle"]

        if self.que_hace == "run" or self.movimiento_aereo:
                if not self.esta_aire:
                    self.limit_count = 5
                    self.animacion_actual = self.animaciones["run"]
                self.mover(PANTALLA)
                
        if self.que_hace == "jump":
                self.limit_count = 20
                self.animacion_actual = self.animaciones["jump"]
                jump_audio.play(loops=0)
                self.saltar(plataformas)

        if self.que_hace == "attack" or self.ataco :
            if not self.esta_aire:
                self.limit_count = 15
                self.animacion_actual = self.animaciones["attack"]
                self.attack(PANTALLA, lista_enemigos)

        self.animar_movimiento(PANTALLA)
        self.aplicar_gravedad(PANTALLA)
        self.verificar_colision_piso(plataformas)
        self.verificar_colision_pared(plataformas)    
        self.verificar_colision_enemigo(lista_enemigos)
        self.verificar_colision_items(lista_recompensas, puntaje, self)
        self.verificar_colision_items(lista_vidas, puntaje, self)

