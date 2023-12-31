import pygame

from Classes.Characters.Entidades import Entidades_Juego
from Classes.Characters.Items import Items
from configuraciones import *

class Personaje(Entidades_Juego):
    def __init__(self,velocidad, potencia_salto, tamaño, posicion, animaciones):
        
        self.puntaje = 0
        #attack
        self.ataco = False
        self.rect_attack = None

        #MOVIMIENTO
        self.velocidad = velocidad
        self.press_tecla_w = False
        self.mirando_izq = False

        #GRAVEDAD
        self.esta_aire = True # esta saltando o esta en el aire
        self.gravedad = 1
        self.potencia_salto = -25
        self.limite_velocidad_salto = 25
        self.velocidad_y = 0

        super().__init__( tamaño, posicion, animaciones )


    def aplicar_gravedad(self, PANTALLA):
        if self.esta_aire:
            self.animar_movimiento(PANTALLA)
            
            for rect in self.rectangulos:
                self.rectangulos[rect].y += self.velocidad_y

            # Hago que suba el rect,
            if self.velocidad_y + self.gravedad < self.limite_velocidad_salto:
                self.velocidad_y += self.gravedad # Al mismo tiempo estoy haciendo que la vel_y vaya reduciendose hasta un limite 

    def verificar_colision_piso(self, lista_pisos):
        for plat in lista_pisos:

            plataforma:pygame.Rect = plat
            if self.rectangulos["bottom"].colliderect(plataforma.rectangulos["top"]):
                self.esta_saltando = False
                self.velocidad_y = 0
                self.esta_aire = False
                for lado in self.rectangulos:
                    self.rectangulos[lado].bottom = plataforma.rectangulos["top"].top
                    if lado == "top":
                        self.rectangulos[lado].top = self.rectangulos["principal"].top

                break
            elif self.rectangulos["top"].colliderect(plat.rectangulos["bottom"]):
                self.velocidad_y = 25
                for lado in self.rectangulos:
                    self.rectangulos[lado].top = plataforma.rectangulos["bottom"].bottom
                    if lado == "bottom":
                        self.rectangulos[lado].top = self.rectangulos["principal"].bottom
                break
            else:

                self.esta_aire = True

    
    def verificar_colision_pared(self, lista_plataformas):
        for plat in lista_plataformas:
            plataforma:pygame.Rect = plat
            if self.rectangulos["right"].colliderect(plataforma.rectangulos["left"]):
                
                for lado in self.rectangulos:
                    self.rectangulos[lado].right = plataforma.rectangulos["left"].left
                    if lado == "left" or lado == "top":
                        self.rectangulos[lado].left = self.rectangulos["principal"].left
                break
            elif self.rectangulos["left"].colliderect(plataforma.rectangulos["right"]):
                for lado in self.rectangulos:
                    self.rectangulos[lado].left = plataforma.rectangulos["right"].right
                    if lado == "right":
                        self.rectangulos[lado].right = self.rectangulos["principal"].right
                break


    def saltar(self, plataformas):
        self.velocidad_y = self.potencia_salto

    def attack(self, pantalla,lista_objetivo):
        # self.ataco = True
        if self.mirando_izq:
            self.rect_attack = pygame.Rect(self.rectangulos["principal"].midtop[0] -self.rectangulos["principal"].width ,self.rectangulos["principal"].topleft[1], self.rectangulos["principal"].width, self.rectangulos["principal"].height)
        else:
            self.rect_attack = pygame.Rect(self.rectangulos["principal"].midtop[0],self.rectangulos["principal"].midtop[1], self.rectangulos["principal"].width, self.rectangulos["principal"].height)


        for ene in lista_objetivo:
            if self.rect_attack.colliderect(ene.rectangulos["principal"]):
                ene.eliminar = True
                # ref_ene = ene 
                # lista_objetivo.remove(ene)
                # del ref_ene
        # pygame.draw.rect(pantalla,"red" ,self.rect_attack)

    def verificar_colision_items(self, lista_items:list[Items], puntaje,jugador):

        for item in lista_items:
            if self.rectangulos["principal"].colliderect(item.rectangulos["principal"]):
                if item.is_health == True:  
                    heal_audio.play(loops=0)
                    jugador.vidas += 1
                    ref_item = item
                    lista_items.remove(item)
                    del ref_item
                else:
                    coin_audio.play(loops=0)
                    self.puntaje += 10
                    ref_item = item
                    lista_items.remove(item)
                    del ref_item
       