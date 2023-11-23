import pygame as py
from Classes.config_game import Config
from configuraciones import *
from Classes.Niveles.Nivel_1 import Nivel_1
from Classes.Niveles.Nivel_2 import Nivel_2
from DEBUG import *

class Game(Config):
    def __init__(self, size, FPS, caption = "Title", icon = ""):
        super().__init__(size, FPS, caption, icon)
        self.nivel_1 = Nivel_2(self.SCREEN)

    def init(self):
        py.init()

        

        while self.running:
            
            self.clock.tick(self.FPS) 

            lista_eventos = py.event.get()
            for event in lista_eventos:
                if event.type == py.QUIT:
                    self.running = False
                if event.type == py.K_m:
                    cambiar_modo()
                
            

            self.fill_screen()
            
            res = self.nivel_1.update(lista_eventos)

            if res == False:
                self.running = False
            py.display.update()
        
        py.quit()


