import pygame
from Classes.Characters.Entidades import Entidades_Juego

class Plataforma(Entidades_Juego):
    def __init__(self, tamaño, posicion, es_visible = False, path = "", es_pared = False, index = 0):
        self.es_visible = es_visible
        self.plataforma = Plataforma.crear_plataforma(es_visible, False, tamaño, posicion, path)
        self.rectangulos = Entidades_Juego.obtener_rectangulos(self.plataforma["rectangulo"], self.plataforma["rectangulo"].width, self.plataforma["rectangulo"].height)
        # super().__init__(tamaño, posicion,[])
        self.rects_limites = self.crear_limites_plataformas()
        self.index = index
        self.fuego_rect = self.crear_rect_fuego()

    @staticmethod
    def crear_plataforma(visible,esPremio, tamaño,posicion, path=""):
        plataforma = {}
        if visible:
            img = pygame.image.load(path)
            img_res = pygame.transform.scale(img, (50,tamaño[1]))
            plataforma["superficie"] = pygame.Surface(tamaño)
            repeticiones = int(tamaño[0] / 50)

            for i in range(repeticiones):
                plataforma["superficie"].blit(img_res,(50 * i,0))

        else:
            plataforma["superficie"] = pygame.Surface(tamaño)
        plataforma["rectangulo"] = plataforma["superficie"].get_rect()
        plataforma["rectangulo"].x = posicion[0]
        plataforma["rectangulo"].y = posicion[1]
        plataforma["premio"] = esPremio
        
        return plataforma
    
    def crear_limites_plataformas(self):

        rect_izq = pygame.Rect(self.rectangulos["principal"].topleft[0], 
                               self.rectangulos["principal"].topleft[1] - 10,
                                5,
                                5
                               )
        rect_der = pygame.Rect(self.rectangulos["principal"].topright[0] - 10, 
                               self.rectangulos["principal"].topright[1] - 10,
                                5,
                                5
                               )
        dicc_rects = {
            "rect_izq": rect_izq,
            "rect_der": rect_der
        }
        return dicc_rects
    
    def crear_rect_fuego(self):
        rect_fuego = pygame.Rect(self.rectangulos["principal"].topleft[0], 
                               self.rectangulos["principal"].topleft[1] - 10,
                                self.rectangulos["principal"].width,
                                10)
        return rect_fuego
