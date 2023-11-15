import pygame


class Entidades_Juego:
    def __init__(self,tamaño, posicion, list_animaciones):

        
        self.list_animaciones = list_animaciones
        self.animacion_actual = self.list_animaciones[0]
        self.rect:pygame.Rect = self.animacion_actual[0][0].get_rect()
        self.rectangulos = self.obtener_rectangulos(self.rect, self.rect.width, self.rect.height)

    
    def obtener_rectangulos(rectangulos:pygame.Rect, width:int, height:int):
        diccionario = {}
        if len(rectangulos) > 0 and isinstance(rectangulos, pygame.Rect):

            diccionario["principal"] = rectangulos
            diccionario["bottom"] = pygame.Rect(rectangulos.left, rectangulos.bottom - 12, rectangulos.width, 12)
            diccionario["right"] = pygame.Rect(rectangulos.right - 10, rectangulos.top, 10, rectangulos.height)
            diccionario["left"] = pygame.Rect(rectangulos.left, rectangulos.top, 10, rectangulos.height)
            diccionario["top"] = pygame.Rect(rectangulos.left, rectangulos.top , rectangulos.width, 12)

        return diccionario