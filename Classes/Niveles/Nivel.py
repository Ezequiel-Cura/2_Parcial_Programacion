import pygame, random
from DEBUG import *
from Classes.Characters.Personaje_enemigo import Enemigo
from Classes.Characters.Personaje_Principal import PersonajePrincipal
from configuraciones import *

class Nivel():
    def __init__(self, pantalla, personaje_principal, lista_plataformas, imagen_fondo ):
        self._slave = pantalla
        self.img_fondo = imagen_fondo

        self.jugador:PersonajePrincipal = personaje_principal
        self.plataformas = lista_plataformas
        
        self.lista_enemigos:list[Enemigo] = []
        self.generar_enemigo_aleatorio(1)
        self.lista_trampas = []

        self.lista_recompensas =[]


        self.vidas = 3
        self._tiempo = 60
    

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
        pass

    def set_vidas(self, pantalla):
        pass

    def verificar_game_over(self):
        pass
        

    # SE FIJA QUE TECLAS APRETAMOS 
    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_m:
                    cambiar_modo()

        
        self.leer_inputs()
        self.actualizar_pantalla()

    # ACTUALIZA TODA LA PANTALLA, MOVIMIENTO DE PERSONAJE Y DEMAS
    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0,0))

        for plataforma in self.plataformas:
            plataforma.draw(self._slave)

        self.jugador.update(self._slave, self.plataformas)
        self.jugador.animar_movimiento(self._slave)

        for enem in self.lista_enemigos:
            enem.animar_movimiento(self._slave)
            enem.aplicar_gravedad()
            enem.comportamiento(self.plataformas, self._slave)

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

        if teclas[pygame.K_SPACE] :#and self.jugador.ataco == False:
            self.jugador.attack(self._slave, self.lista_enemigos)
            self.jugador.ataco = True

        if teclas[pygame.K_w]:
            self.jugador.que_hace = 2
            self.jugador.press_tecla_w = True
    
    def dibujar_rectangulos(self):
        if obtener_modo() == True:  

            for rect in self.jugador.rectangulos:
                pygame.draw.rect(self._slave,"Orange", self.jugador.rectangulos[rect],2)

            if self.jugador.ataco:
                pygame.draw.rect(self._slave,"red" ,self.jugador.rect_attack)
            
            # for plat in self.plataformas:
            #     pygame.draw.rect(self._slave,"red", plat.rectangulos[rect],2)
            for plataforma in self.plataformas:
                for lado in plataforma.rectangulos:
                    pygame.draw.rect(self._slave,"blue", plataforma.rectangulos[lado],2)

                # self._slave.blit(plataforma.plataforma["superficie"], plataforma.plataforma["rectangulo"])
            pygame.draw.rect(self._slave, "yellow", self.jugador.rectangulos["left"])
            for enemi in self.lista_enemigos:
                for lados in enemi.rectangulos:
                    pygame.draw.rect(self._slave,"red", enemi.rectangulos[lados],2)