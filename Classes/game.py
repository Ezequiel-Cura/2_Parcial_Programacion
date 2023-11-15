import pygame as py
from Classes.config_game import Config
from configuraciones import *
from Classes.Niveles.Nivel_1 import Nivel_1


class Game(Config):
    def __init__(self, size, FPS, caption = "Title", icon = ""):
        super().__init__(size, FPS, caption, icon)
        self.nivel_1 = Nivel_1(self.SCREEN)

    def init(self):
        py.init()

        while self.running:
            
            self.clock.tick(self.FPS) 

            lista_eventos = py.event.get()
            for event in lista_eventos:
                if event.type == py.QUIT:
                    self.running = False

            self.fill_screen()
            
            self.nivel_1.update(lista_eventos)

            py.display.update()
        
        py.quit()


