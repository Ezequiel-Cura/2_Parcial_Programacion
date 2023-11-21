import pygame, random
from DEBUG import *
from Classes.Characters.Personaje_enemigo import Enemigo
from Classes.Characters.Personaje_Principal import PersonajePrincipal
from configuraciones import *
from Classes.Characters.Plataforma import Plataforma
from Classes.Characters.Proyectiles import Proyectiles

class Nivel():
    def __init__(self, pantalla, personaje_principal, lista_plataformas, imagen_fondo ):
        self._slave = pantalla
        self.img_fondo = imagen_fondo

        self.jugador:PersonajePrincipal = personaje_principal
        self.plataformas:list[Plataforma] = lista_plataformas
        
        self.lista_enemigos:list[Enemigo] = []
        self.generar_enemigo_aleatorio(1)
        self.lista_trampas = []

        self.lista_recompensas =[]

        self.lista_bullets:list[Proyectiles] = []

        pygame.font.init()
        self.fuente = pygame.font.SysFont("Arial",30)


        self.time_over = False
        self.vidas = 3
        self._tiempo = 60
        self.vidas_texto = self.fuente.render(f"{self.vidas}", False, "black", None)
        self.tiempo_texto = f"{self._tiempo}"

        # self.set_tiempo(self._slave)
    

    def generar_enemigo_aleatorio(self, nivel:int):

        if nivel == 1:
            for i in range(10):
                random_x = random.randint(20, self._slave.get_width() -20)
                # random_y = random.randint(20, self._slave.get_height())

                enemig = Enemigo((random_x,0), goblin_animations, 3)
                self.lista_enemigos.append(enemig)


    def generar_recompensa_aleatoria(self):
        pass

    def set_tiempo(self, pantalla):
        surface = pygame.Surface((100, 50))
        ticks = round(pygame.time.get_ticks())
   
        pygame.time.set_timer(pygame.USEREVENT + 3, 1000,1)
        # self._slave.blit(ticks, (1000, 0))

    def set_vidas(self, pantalla):
        pass

    def verificar_game_over(self):
        pass
        

    # SE FIJA QUE TECLAS APRETAMOS 
    def update(self, lista_eventos ):
        
        
        
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_m:
                    cambiar_modo()
            elif evento.type == pygame.USEREVENT:
                self.jugador.attack_delay = True
            elif evento.type == pygame.USEREVENT + 1:
                self.jugador.jump_delay = True    
            elif evento.type == pygame.USEREVENT + 2:
                self.jugador.shoot_delay = True
            elif evento.type == pygame.USEREVENT + 3:
                self.time_over = True
                
            

        
        self.leer_inputs()
        self.actualizar_pantalla()

    # ACTUALIZA TODA LA PANTALLA, MOVIMIENTO DE PERSONAJE Y DEMAS
    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0,0))
        self._slave.blit(self.vidas_texto, (700, 0))
        self.set_tiempo(self._slave)

        for plataforma in self.plataformas:
            plataforma.draw(self._slave)

        self.jugador.update(self._slave, self.plataformas, self.lista_enemigos)
        self.jugador.animar_movimiento(self._slave)
        
       
        for bullet in self.lista_bullets:
            if bullet.eliminar:
                ref_bullet = bullet
                self.lista_bullets.remove(bullet)
                del ref_bullet

            bullet.verificar_colision_enemigos(self.lista_enemigos)
            bullet.update(self._slave, self.plataformas)


        for enem in self.lista_enemigos:
            enem.aplicar_gravedad()
            enem.verificar_colision_piso(self.plataformas)
            enem.comportamiento(self.plataformas, self._slave)
            enem.animar_movimiento(self._slave)

        self.dibujar_rectangulos()

    # ACTUALIZAR QUE HACE EL PERSONAJE PRINCIPAL CON LAS TECLAS
    def leer_inputs(self):
        teclas = pygame.key.get_pressed()
        # 0 = Idle_der, 1 = Run_der, 2 = Jump_der, 3 = attack_der
        #   = Idle_izq,-1 = Run_izq, -2 = Jump_izq, -3 attack_izq
        if teclas[pygame.K_a]:
            self.jugador.mirando_izq = True
            self.jugador.que_hace = 1
        elif teclas[pygame.K_d]:

            self.jugador.mirando_izq = False
            self.jugador.que_hace = 1
        else:
            self.jugador.que_hace = 0

        if teclas[pygame.K_SPACE] and self.jugador.attack_delay:
            self.jugador.ataco = True
            pygame.time.set_timer(pygame.USEREVENT, 1000,1)

            self.jugador.attack_delay = False
            self.jugador.que_hace = 3

        if teclas[pygame.K_f] and self.jugador.shoot_delay:
            pygame.time.set_timer(pygame.USEREVENT + 2, 500,1)

            self.jugador.shoot_delay = False
            x = self.jugador.rectangulos["principal"].midtop[0] - 5
            y = self.jugador.rectangulos["principal"].midtop[1] + 5
            
            if self.jugador.mirando_izq:
                nuevo_proyectil = Proyectiles((30,40), (x,y),  -1)
            else:
                nuevo_proyectil = Proyectiles((30,40), (x, y),  1)

            self.lista_bullets.append(nuevo_proyectil)

        if teclas[pygame.K_w] and self.jugador.jump_delay :
            self.jugador.esta_saltando = True
            self.jugador.jump_delay = False
            pygame.time.set_timer(pygame.USEREVENT + 1, 100,1)

            self.jugador.que_hace = 2
            self.jugador.press_tecla_w = True
    
    def dibujar_rectangulos(self):
        if obtener_modo() == True:  

            for rect in self.jugador.rectangulos:
                pygame.draw.rect(self._slave,"Orange", self.jugador.rectangulos[rect],2)

            # if self.jugador.ataco:
            #     pygame.draw.rect(self._slave,"red" ,self.jugador.rect_attack, 2)
            
            for plataforma in self.plataformas:
                for lado in plataforma.rectangulos:
                    pygame.draw.rect(self._slave,"blue", plataforma.rectangulos[lado],2)

            for plataforma in self.plataformas:
                for lado in plataforma.rects_limites:
                    pygame.draw.rect(self._slave,"white", plataforma.rects_limites[lado],2)

            for enemi in self.lista_enemigos:
                for lados in enemi.rectangulos:
                    pygame.draw.rect(self._slave,"red", enemi.rectangulos[lados],2)
 