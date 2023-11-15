import pygame


class Entidades_Juego:
    def __init__(self,tamaño, posicion, list_animaciones):

        self.list_animaciones:list = list_animaciones
        self.animacion_actual:list[pygame.Surface] = self.list_animaciones[0]
        self.rect:pygame.Rect = self.animacion_actual[0].get_rect()
        print(self.rect.width)
        self.rectangulos: dict[str, pygame.Rect] = Entidades_Juego.obtener_rectangulos(self.rect, self.rect.width, self.rect.height)
        self.rectangulos["principal"].x = posicion[0]
        self.rectangulos["principal"].y = posicion[1]
    
    def draw(self, pantalla):
        pass

    def mover(self, velocidad):
        pass

    def animar_movimiento(self, pantalla, lista_imagenes):
        pass

    def update(self):
        pass



    @staticmethod
    def obtener_rectangulos(rectangulos:pygame.Rect, width:int, height:int):
        diccionario = {}
        if len(rectangulos) > 0 and isinstance(rectangulos, pygame.Rect):

            diccionario["principal"] = rectangulos
            diccionario["bottom"] = pygame.Rect(rectangulos.left, rectangulos.bottom - 12, rectangulos.width, 12)
            diccionario["right"] = pygame.Rect(rectangulos.right - 10, rectangulos.top, 10, rectangulos.height)
            diccionario["left"] = pygame.Rect(rectangulos.left, rectangulos.top, 10, rectangulos.height)
            diccionario["top"] = pygame.Rect(rectangulos.left, rectangulos.top , rectangulos.width, 12)

        return diccionario
    
    def reescalalar_imagenes(diccionario_animaciones, ancho, alto):
        for clave in diccionario_animaciones:
            for i in range(len(diccionario_animaciones[clave])):
                img = diccionario_animaciones[clave][i]
                diccionario_animaciones[clave][i] = pygame.transform.scale(img, (ancho, alto))

    def rotar_imagen(imagenes:list):
        lista_imagenes = []
        for i in range(len(imagenes)):
            imagen_rotada = pygame.transform.flip(imagenes[i],True,False)
            lista_imagenes.append(imagen_rotada)
        
        return lista_imagenes