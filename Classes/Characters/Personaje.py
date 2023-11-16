import pygame

from Classes.Characters.Entidades import Entidades_Juego


class Personaje(Entidades_Juego):
    def __init__(self,velocidad, potencia_salto, tamaño, posicion, animaciones):
        


        #MOVIMIENTO
        self.velocidad = velocidad
        self.press_tecla_w = False
        self.mirando_izq = False

        #GRAVEDAD
        self.esta_saltando = True # esta saltando o esta en el aire
        self.gravedad = 1
        self.potencia_salto = -25
        self.limite_velocidad_salto = 25
        self.velocidad_y = 0

        super().__init__( tamaño, posicion, animaciones )


    def aplicar_gravedad(self):
        if self.esta_saltando:
            for rect in self.rectangulos:
                self.rectangulos[rect].y += self.velocidad_y

            # self.rectangulos["principal"].y += self.velocidad_y # Hago que suba el rect,
            if self.velocidad_y + self.gravedad < self.limite_velocidad_salto:
                self.velocidad_y += self.gravedad # Al mismo tiempo estoy haciendo que la vel_y vaya reduciendose hasta un limite 

    def verificar_colision_piso(self, lista_pisos):
        for plat in lista_pisos:
            # print(plat["rectangulo"])
            plataforma:pygame.Rect = plat
            if self.rectangulos["bottom"].colliderect(plataforma.plataforma["rectangulo"]):
                self.velocidad_y = 0
                self.esta_saltando = False
                for lado in self.rectangulos:
                    self.rectangulos[lado].bottom = plataforma.plataforma["rectangulo"].top
                    if lado == "top":
                        self.rectangulos[lado].top = self.rectangulos["principal"].top
                # print("COLISION")
                break
            else:
                # print("MAL")
                self.esta_saltando = True

    def saltar(self, plataforma):
        self.velocidad_y = self.potencia_salto


    def verificar_colision_items(self, lista_items):
        pass

    def lanzar_proyectil(self, objetivo):# Objetivo es el personaje?
        pass