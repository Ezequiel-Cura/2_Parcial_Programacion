import pygame as py
from Classes.config_game import Config
from configuraciones import *

class Game(Config):
    def __init__(self, size, FPS, caption = "Title", icon = ""):
        super().__init__(size, FPS, caption, icon)
        

    def init(self):
        py.init()

        while self.running:
            
            self.clock.tick(self.FPS) 

            lista_eventos = py.event.get()
            for event in lista_eventos:
                if event.type == py.QUIT:
                    self.running = False

            self.fill_screen()

            for bg in bg_demon_forest:
                bg = pygame.transform.scale(bg, (self.size))
                self.SCREEN.blit(bg,(0,0))
       
            py.display.update()
        
        py.quit()


