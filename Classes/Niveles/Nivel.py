import pygame, random
from DEBUG import *
from Classes.Characters.Personaje_enemigo import Enemigo
from Classes.Characters.Necromancer import Necromancer
from Classes.Characters.Boss import Boss
from Classes.Characters.Personaje_Principal import PersonajePrincipal
from configuraciones import *
from Classes.Characters.Plataforma import Plataforma
from Classes.Characters.Proyectiles import Proyectiles
from Classes.Characters.Items import Items

class Nivel():
    def __init__(self, pantalla, personaje_principal, lista_plataformas, imagen_fondo,nivel ):
        self._slave = pantalla
        self.img_fondo = imagen_fondo

        self.jugador:PersonajePrincipal = personaje_principal
        self.plataformas:list[Plataforma] = lista_plataformas
        
        self.necromancer = None
        self.lista_enemigos:list[Enemigo] = []
        self.boss = None
        
        self.generar_enemigo_aleatorio(nivel)
        self.lista_trampas = []

        self.lista_recompensas =[]
        self.generar_recompensa_aleatoria(self.plataformas)
      
        self.lista_bullets:list[Proyectiles] = []

        pygame.font.init()
        self.fuente = pygame.font.SysFont("Assets\font\PixelifySans-VariableFont_wght.ttf",40)

        self.tiempo1 = 0

        self.time_over = False
   
        self._tiempo = 60
        self.vidas_texto = self.fuente.render(f"{self.jugador.vidas}", False, "black", None)
        self.tiempo_texto = f"{self._tiempo}"

        self.inicio_juego = True


        self.puntaje_nivel = 0
        # self.set_tiempo(self._slave)
    

    def generar_enemigo_aleatorio(self, nivel:int):

        if nivel == 1:
            for i in range(10):
                random_x = random.randint(20, self._slave.get_width() -20)
                # random_y = random.randint(20, self._slave.get_height())

                enemig = Enemigo((random_x,0), goblin_animations, 3, (40, 60))
                self.lista_enemigos.append(enemig)
        elif nivel == 2:
            self.necromancer = Necromancer((self._slave.get_height() * 0.5,0),necro_animation, 5, (50,70))
            for i in range(5):
                random_x = random.randint(20, self._slave.get_width() -20)
                enemig = Enemigo((random_x,0), skeleton_animation, 3, (50, 70))
                self.lista_enemigos.append(enemig)
        elif nivel == 3:
            self.boss = Boss((500,500),boss_animation,4,(350, 400))

    def generar_recompensa_aleatoria(self, lista_plataformas):
        for plat in lista_plataformas:
            x = plat.rectangulos["top"].midtop[0]
            y = plat.rectangulos["top"].midtop[1] - 40
            nueva_recompensa = Items((30,30),(x,y),coin_animation)
            self.lista_recompensas.append(nueva_recompensa)
        
    def set_recompensas(self, pantalla):
        self.puntaje_nivel = self.jugador.puntaje
        self.puntaje_nivel_texto = self.fuente.render(f"Points: {self.puntaje_nivel}", False, "white", None)

        pantalla.blit(self.puntaje_nivel_texto, (1000, 0))

    def set_tiempo(self, pantalla):
        surface = pygame.Surface((100, 50))
        tiempo2 = pygame.time.get_ticks()

        if tiempo2 > self.tiempo1 + 1000:
            self.tiempo1 = tiempo2
            # Resto 1, cada 1 segundo
            self._tiempo -= 1
        self.tiempo_texto = self.fuente.render(f"Time:{self._tiempo}", False, "white", None)

        pantalla.blit(self.tiempo_texto, (1500, 0))

    def set_vidas(self, pantalla):
        x = 60
        pantalla.blit(hp_surface,(30,10))
        for i in range(self.jugador.vidas):
            x += 20
            pantalla.blit(heart_img,(x,10))


    def verificar_game_over(self):
        if self.jugador.vidas <= 0 or self.time_over:
            self.time_over = True
    
        
    # SE FIJA QUE TECLAS APRETAMOS 
    def update(self, lista_eventos ):

        if self.time_over:
            return False
        
        if self.inicio_juego:
            pygame.time.set_timer(pygame.USEREVENT + 3, 60000,1)
            self.inicio_juego = False
        
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
            elif evento.type == pygame.USEREVENT + 4:
                self.jugador.inmune = False
            elif evento.type == pygame.USEREVENT + 5:
                if self.necromancer != None:
                    self.necromancer.delay_creacion = True
            elif evento.type == pygame.USEREVENT + 6:
                if self.boss != None:
                    self.boss.mover_boss = True
                
        self.leer_inputs()
        self.actualizar_pantalla()
        self.verificar_game_over()

    # ACTUALIZA TODA LA PANTALLA, MOVIMIENTO DE PERSONAJE Y DEMAS
    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0,0))
        # self._slave.blit(self.vidas_texto, (700, 0))
        self.set_tiempo(self._slave)
        self.set_vidas(self._slave)
        self.set_recompensas(self._slave)

        for plataforma in self.plataformas:
            plataforma.draw(self._slave)

        self.jugador.update(self._slave, self.plataformas, self.lista_enemigos)
        self.jugador.verificar_colision_enemigo(self.lista_enemigos)
        self.jugador.verificar_colision_items(self.lista_recompensas, self.puntaje_nivel)
        self.jugador.animar_movimiento(self._slave)

        for item in self.lista_recompensas:
            item.update(self._slave)
            

        for bullet in self.lista_bullets:
            if bullet.eliminar:
                ref_bullet = bullet
                self.lista_bullets.remove(bullet)
                del ref_bullet

            if self.necromancer != None:
                if bullet.rectangulos["principal"].colliderect(self.necromancer.rectangulos["principal"]):
                    ref_necro = self.necromancer
                    self.necromancer = None
                    del ref_necro
                    bullet.eliminar = True

            bullet.verificar_colision_enemigos(self.lista_enemigos)
            bullet.update(self._slave, self.plataformas)


        if self.necromancer != None:
            self.necromancer.update(self._slave, self.plataformas, self.jugador, self.lista_enemigos)

        if self.boss != None:
            self.boss.update(self._slave, self.jugador, self.plataformas)

        for enem in self.lista_enemigos:
            enem.update(self._slave, self.plataformas, self.jugador)

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
                nuevo_proyectil = Proyectiles((50,50), (x,y),  -1)
            else:
                nuevo_proyectil = Proyectiles((50,50), (x, y),  1)

            self.lista_bullets.append(nuevo_proyectil)

        if teclas[pygame.K_w] and self.jugador.jump_delay:
            self.jugador.esta_saltando = True
            self.jugador.jump_delay = False
            self.jugador.que_hace = 2
            self.jugador.press_tecla_w = True
            pygame.time.set_timer(pygame.USEREVENT + 1, 50,1)
    
    def dibujar_rectangulos(self):
        if obtener_modo() == True:  

            for rect in self.jugador.rectangulos:
                pygame.draw.rect(self._slave,"Orange", self.jugador.rectangulos[rect],2)

            # if self.jugador.ataco:
            #     pygame.draw.rect(self._slave,"red" ,self.jugador.rect_attack, 2)
            for bullet in self.lista_bullets:
                pygame.draw.rect(self._slave,"orange" ,bullet.rect, 2)
            
            if self.necromancer != None:
                for rect in self.necromancer.rectangulos:
                    pygame.draw.rect(self._slave,"Orange", self.necromancer.rectangulos[rect],2)

            if self.boss != None:
                for rect in self.boss.rectangulos:
                    pygame.draw.rect(self._slave,"red", self.boss.rectangulos[rect],2)

            for item in self.lista_recompensas:
                pygame.draw.rect(self._slave,"white", item.rectangulos["principal"],2)



            for plataforma in self.plataformas:
                for lado in plataforma.rectangulos:
                    pygame.draw.rect(self._slave,"blue", plataforma.rectangulos[lado],2)

            for plataforma in self.plataformas:
                for lado in plataforma.rects_limites:
                    pygame.draw.rect(self._slave,"white", plataforma.rects_limites[lado],2)

            for enemi in self.lista_enemigos:
                for lados in enemi.rectangulos:
                    pygame.draw.rect(self._slave,"red", enemi.rectangulos[lados],2)
 