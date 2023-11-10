import pygame as py
from config_game import Config

class Game(Config):
    def __init__(self, size, FPS, caption = "Title", icon = ""):
        super().__init__(size, FPS, caption, icon)

        self.set_background_image()

    def init(self):
        py.init()

        while self.running:
            self.fill_screen()
            
            self.clock.tick(self.FPS)            

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False

       
            py.display.update()
        
        py.quit()


