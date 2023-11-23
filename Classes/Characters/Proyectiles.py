import pygame
from Classes.Characters.Items import Items
from configuraciones import *
from Classes.Characters.Entidades import Entidades_Juego
from Classes.Characters.Plataforma import Plataforma

class Proyectiles(Items):
    def __init__(self, tamaño, posicion, direccion):
        self.direccion = direccion
        self.velocidad = 7

        self.pasos_animacion = 0
        self.proyectil_animation = proyectil_animation
        self.animacion_actual = []

        for i in range(len(self.proyectil_animation)):
            self.animacion_actual.append(pygame.transform.scale(self.proyectil_animation[i], tamaño))

        self.rect:pygame.Rect = self.animacion_actual[0].get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.rectangulos: dict[str, pygame.Rect] = Entidades_Juego.obtener_rectangulos(self.rect, self.rect.width, self.rect.height)

        self.eliminar = False

    def update(self, pantalla, lista_plataformas):

        new_vel = self.velocidad

        if self.direccion != 1:
            new_vel *= -1

        self.rectangulos["principal"].x += new_vel
       
        self.animar_movimiento(pantalla)

        self.verificar_limites(lista_plataformas, new_vel, pantalla)

        

    def animar_movimiento(self, pantalla):
        
        if self.pasos_animacion >= len(self.animacion_actual):
            self.pasos_animacion = 0

            pantalla.blit(self.animacion_actual[self.pasos_animacion], self.rectangulos["principal"])
        
        self.pasos_animacion += 0.5

    def verificar_limites(self, lista_plataformas:list[Plataforma], new_vel, pantalla):
        new_x = self.rectangulos["principal"].x + new_vel 

        if new_x <= 0 or new_x >= pantalla.get_width() - self.rectangulos["principal"].width:
            self.eliminar = True

        for plat in lista_plataformas:
           
            if self.rectangulos["principal"].colliderect(plat.rectangulos["principal"]):
                self.eliminar = True
    
    def verificar_colision_enemigos(self, lista_enemigos:list):

        for en in lista_enemigos:
            if self.rectangulos["principal"].colliderect(en.rectangulos["principal"]):
                self.eliminar = True
                ref_en = en
                lista_enemigos.remove(en)
                del ref_en
    
    


    