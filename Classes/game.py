import pygame as py
from Classes.config_game import Config
from configuraciones import *
from DEBUG import *

from GUI_form_principal import FormPrincipal


class Game(Config):
    def __init__(self, size, FPS, caption = "Title", icon = ""):
        super().__init__(size, FPS, caption, icon)

        self.form = FormPrincipal(self.SCREEN,
                               500,100,
                               1000,500,
                               "gray",
                               "black",
                               2,
                               True
                               )

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
                # if event.type == py.MOUSEBUTTONDOWN:
                #     print(event.pos)
                
            self.fill_screen()
            
            self.form.update(lista_eventos)

            py.display.update()
        
        py.quit()


