import pygame
from DEBUG import *
from Classes.Characters.Personaje_enemigo import Enemigo
from Classes.Characters.Personaje_Principal import PersonajePrincipal


class Nivel():
    def __init__(self, pantalla, personaje_principal, lista_plataformas, imagen_fondo ):
        self._slave = pantalla
        self.img_fondo = imagen_fondo

        self.jugador:PersonajePrincipal = personaje_principal
        self.plataformas = lista_plataformas
        self.lista_enemigos:list[Enemigo] = self.generar_enemigo_aleatorio()
        self.lista_trampas = []

        self.lista_recompensas =[]
    

    def generar_enemigo_aleatorio(self):
        pass

    def generar_recompensa_aleatoria(self):
        pass

    def set_tiempo(self, pantalla):
        pass

    def set_vias(self, pantalla):
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

        # self.jugador.update(self._slave, self.plataformas)

    # ACTUALIZAR QUE HACE EL PERSONAJE PRINCIPAL
    def leer_inputs(self):
        teclas = pygame.key.get_pressed()

        # if teclas[py.K_a]:
        #     self.jugador.que_hace = 2
        # elif teclas[py.K_d]:
        #     self.jugador.que_hace = 1
        # else:
        #     self.jugador.que_hace = 0

        # if teclas[py.K_w]:
        #     self.jugador.que_hace = 3
        #     self.jugador.press_tecla_w = True
    
    def dibujar_rectangulos(self):
        if obtener_modo() == True:  
            pass
            # for lado in self.jugador.lados:
            #     pygame.draw.rect(self._slave,"Orange", self.jugador.lados[lado],2)

            # for plataforma in self.plataformas:
            #     pygame.draw.rect(self._slave,...)
            
            # for ene_lado in self.enemigos:
            #     pygame.draw.rect