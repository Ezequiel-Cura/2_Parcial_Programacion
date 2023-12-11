import pygame
from Classes.Characters.Items import Items
from configuraciones import *
from Classes.Characters.Entidades import Entidades_Juego
from Classes.Characters.Plataforma import Plataforma
from Classes.Characters.Personaje_enemigo import Enemigo

class Proyectiles(Items):
    def __init__(self, tamaño, posicion, direccion,animacion, angulo = 0):
        self.mirando_izq = direccion
        self.velocidad = 7

        self.pasos_animacion = 0
        self.proyectil_animation = proyectil_animation
        self.animacion_actual = animacion

        self.angulo = angulo
        # for i in range(len(self.proyectil_animation)):
        #     self.animacion_actual.append(pygame.transform.scale(self.proyectil_animation[i], tamaño))

        self.rect:pygame.Rect = self.animacion_actual[0].get_rect()
        self.rect.x = posicion[0] 
        self.rect.y = posicion[1] 
        self.rectangulos: dict[str, pygame.Rect] = Entidades_Juego.obtener_rectangulos(self.rect, self.rect.width, self.rect.height)

        self.eliminar = False

    def update(self, pantalla, lista_plataformas):

        new_vel = self.velocidad

        if self.mirando_izq == True:
            new_vel *= -1

        self.rectangulos["principal"].x += new_vel
       
        self.animar_movimiento(pantalla)

        self.verificar_limites(lista_plataformas, new_vel, pantalla)


    def update_2(self, pantalla, lista_plataformas):
        
        new_vel = self.velocidad

        if self.mirando_izq  == True:
            new_vel *= -1
        
        self.rectangulos["principal"].x += new_vel

        self.animar_movimiento(pantalla)
        self.verificar_limites_boss_bullet(new_vel, pantalla)


    def animar_movimiento(self, pantalla):
        
        if self.pasos_animacion >= len(self.animacion_actual):
            self.pasos_animacion = 0

        if self.mirando_izq == True:
            pantalla.blit( pygame.transform.flip(self.animacion_actual[int(self.pasos_animacion)],True,False), (self.rectangulos["principal"].x , self.rectangulos["principal"].y ))
        else:
            pantalla.blit(self.animacion_actual[int(self.pasos_animacion)], (self.rectangulos["principal"].x , self.rectangulos["principal"].y ))
        # pantalla.blit(self.animacion_actual[self.pasos_animacion], self.rectangulos["principal"])
        
        self.pasos_animacion += 0.10

    def verificar_limites(self, lista_plataformas:list[Plataforma], new_vel, pantalla):
        new_x = self.rectangulos["principal"].x + new_vel 

        if new_x <= 0 or new_x >= pantalla.get_width() - self.rectangulos["principal"].width:
            self.eliminar = True

        for plat in lista_plataformas:
           
            if self.rectangulos["principal"].colliderect(plat.rectangulos["principal"]):
                self.eliminar = True

    def verificar_limites_boss_bullet(self, new_vel, pantalla):
        new_x = self.rectangulos["principal"].x + new_vel 

        if new_x <= 0 or new_x >= pantalla.get_width() - self.rectangulos["principal"].width:
            self.eliminar = True

    
    def verificar_colision_enemigos(self, lista_enemigos:list[Enemigo]):
       
        for en in lista_enemigos:
            if self.rectangulos["principal"].colliderect(en.rectangulos["principal"]):
                self.eliminar = True
                en.eliminar = True
                # ref_en = en
                # lista_enemigos.remove(en)
                # del ref_en
    
    


    