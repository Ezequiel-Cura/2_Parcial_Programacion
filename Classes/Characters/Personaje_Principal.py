from Classes.Characters.Personaje import Personaje
import pygame

class PersonajePrincipal(Personaje):
    def __init__(self, tamaño, posicion, animaciones):
        velocidad = 5
        potencia_salto = 25
        self.score = 0
        
        self.vidas = 3
        self.esta_saltando = False
        self.inmune = False
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
        
        


    def verificar_accion(self, que_hizo):
        pass

    def verificar_eventos_personaje():
        pass