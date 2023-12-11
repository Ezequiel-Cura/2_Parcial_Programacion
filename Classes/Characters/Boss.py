import pygame, random
from Classes.Characters.Entidades import Entidades_Juego
from Classes.Characters.Personaje_enemigo import Enemigo
from Classes.Characters.Plataforma import Plataforma
from Classes.Characters.Proyectiles import Proyectiles
from Classes.Characters.Items import Items
from configuraciones import *

class Boss(Enemigo):
    def __init__(self, posicion, list_animaciones, velocidad, tamaño):

        super().__init__(posicion, list_animaciones, velocidad, tamaño)
        self.defeated = False
        self.mover_boss = True
        self.llego_pos = False
        self.flag = True
        self.is_flying = False

        self.limit_count = 6
        self.que_hace = "fly"

        self.health = 30
        self.ratio = self.health / 30
        self.boss_inmune = False
        self.custom_rect = pygame.Rect((posicion[0], posicion[1]), (150,250))

        self.rectangulos = None
        self.rectangulos = Entidades_Juego.obtener_rectangulos(self.custom_rect, 50,50)
        self.mirando_izq = True

        # tamaño display(1900, 1000)


        
        

        self.rect_arriba = pygame.Rect(0, 0, 1600, 300)
        self.rect_medio = pygame.Rect(0, 320,1600, 300)
        self.rect_bajo = pygame.Rect(0, 640, 1600, 300)
        self.lista_rect = [self.rect_arriba,self.rect_medio, self.rect_bajo]

        self.dash_attack = False
        self.fireball_attack = False
        self.fire_attack = False


        self.dash_attack_wait = True
        self.dash_rect = None
        self.dash_limit = False


        self.lista_bullets = []
        self.plat_elegidas = []



    def update(self, pantalla,jugador,lista_plataformas):

        if self.health <= 0:
            self.que_hace = "death"
            self.defeated = True
        else:
        
            if self.que_hace == "fly":
                self.limit_count = 5
                # fly_audio.play(loops=0)
                self.animacion_actual = self.animaciones["fly"]

            if self.que_hace == "dash":
                self.count = 0
                self.limit_count = 60
                self.animacion_actual = self.animaciones["dash"]

            for bullet in self.lista_bullets:
                if bullet.eliminar == True:
                    ref_bul = bullet
                    self.lista_bullets.remove(bullet)
                    del ref_bul

                if bullet.rectangulos["principal"].colliderect(jugador.rectangulos["principal"]):
                    if jugador.inmune == False:
                        bullet.eliminar = True
                        jugador.inmune = True
                        jugador.vidas -= 1
                        pygame.time.set_timer(pygame.USEREVENT + 4, 1000, 1)

                bullet.update_2(pantalla, lista_plataformas)

            self.comportamiento(jugador, pantalla, lista_plataformas)
            self.animar_movimiento(pantalla)

        self.ratio = self.health / 30

        pygame.draw.rect(pantalla, "red", (400,0, 300,30))
        pygame.draw.rect(pantalla, "green", (400,0, 300 * self.ratio,30))


    def comportamiento(self, jugador, pantalla, lista_plataformas):
        rect_arriba = pygame.Rect(0, 0, 1600, 300)
        rect_medio = pygame.Rect(0, 320,1600, 300)
        rect_bajo = pygame.Rect(0, 640, 1600, 300)

        
        # pygame.draw.rect(pantalla,"blue",rect_arriba,3)
        # pygame.draw.rect(pantalla,"blue",rect_medio,3)
        # pygame.draw.rect(pantalla,"blue",rect_bajo,3)

        for rect in self.lista_rect:
            if rect.colliderect(jugador.rectangulos["principal"]) and self.dash_attack_wait:
                self.dash_attack_wait = False
                self.dash_rect = rect
                pygame.time.set_timer(pygame.USEREVENT + 8, 5000,1 )
        

       

        if self.dash_attack:
            fly_audio.stop()

            if self.dash_rect.centery > self.rectangulos["principal"].centery:
                self.rectangulos["principal"].y += 10
            else:
                self.rectangulos["principal"].y -= 10

            #Fijarse que este a la altura del rectangulo a dashear
            if self.rectangulos["principal"].centery > self.dash_rect.top + 50 and self.rectangulos["principal"].centery < self.dash_rect.bottom - 50:
                #que se mueva hacia el jugador
                if self.rectangulos["principal"].x > 100 and self.dash_limit == False:
                    self.que_hace = "dash"
                    self.rectangulos["principal"].x -= 20
                    if self.rectangulos["principal"].colliderect(jugador.rectangulos["principal"]):
                        if jugador.inmune == False:
                            jugador.inmune = True
                            jugador.vidas -= 1
                            pygame.time.set_timer(pygame.USEREVENT + 4, 1000, 1)
                else:
                    self.dash_limit = True

            #Cuando llegue al limite que vuelva
            if self.dash_limit:
                if self.rectangulos["principal"].x < 1700:
                    self.rectangulos["principal"].x += 10
                    self.que_hace = "fly"
                else: # Cuando llegue al limite se acaba el dash
                    self.dash_limit = False
                    self.dash_attack = False
                    self.fireball_attack = True

        if self.fireball_attack:
            
            self.fireball_attack = False

            if len(self.lista_bullets) <= 3 and self.rectangulos["principal"].centerx >= 1600:
                y_bul =  10
                for i in range(3):
                    y_bul = i * 50
                    self.lista_bullets.append(Proyectiles((150,150), (self.rectangulos["principal"].centerx - 50, self.rectangulos["principal"].centery + y_bul) , 1, boss_proyectile))

            if len(self.lista_bullets) <= 0:
                self.fireball_attack = False 
            self.fire_attack = True     

              
           

        if self.fire_attack:
            
            self.fire_attack = False
            self.plat_elegidas = []

            for i in range(3):
                valor = random.randint(0, len(lista_plataformas )-1)
                self.plat_elegidas.append(valor)

        for plat in lista_plataformas:
            for num in self.plat_elegidas:
                if plat.index == num:
                    if plat.fuego_rect.colliderect(jugador.rectangulos["principal"]):
                        if jugador.inmune == False:
                            jugador.inmune = True
                            jugador.vidas -= 1
                            pygame.time.set_timer(pygame.USEREVENT + 4, 2000, 1)

        if len(self.plat_elegidas) > 0:
            self.lava_attack_creation(lista_plataformas,pantalla)

        if not self.dash_attack:
            
            self.que_hace = "fly"



    def animar_movimiento(self, pantalla):
        
        self.count += 1

        if self.count > self.limit_count:
            self.pasos_animacion += 1
            self.count = 0

        if self.pasos_animacion >= len(self.animacion_actual):
            self.pasos_animacion = 0

        if self.mirando_izq == True:
            pantalla.blit( pygame.transform.flip(self.animacion_actual[int(self.pasos_animacion)],True,False), (self.rectangulos["principal"].x  - 100, self.rectangulos["principal"].y - 100))
        else:
            pantalla.blit(self.animacion_actual[int(self.pasos_animacion)], (self.rectangulos["principal"].x - 100 , self.rectangulos["principal"].y -100))


    def lava_attack_creation(self, plataformas, pantalla):
        
        for plat in plataformas:
            for num in self.plat_elegidas:
                if plat.index == num:
                    repeticiones = int(plat.rectangulos["principal"].width / 50)
                    self.animar_fuego(pantalla,repeticiones, plat)


    def animar_fuego(self,pantalla,repeticiones,plat): 
        self.count += 1
        
        if self.count > 20:
            self.pasos_animacion += 1
            self.count = 0
        
        if self.pasos_animacion >= len(self.animacion_actual):
            self.pasos_animacion = 0

        value_x = 0
        for i in range(repeticiones):
            value_x = 50 * i
            pantalla.blit(boss_fire[int(self.pasos_animacion)], (plat.rectangulos["principal"].topleft[0] + value_x , plat.rectangulos["principal"].y -50))

    def shoot_proyectile(self):
        pass

    
    
