from Classes.Characters.Entidades import Entidades_Juego


class Personaje(Entidades_Juego):
    def __init__(self,velocidad, potencia_salto, tamaño, posicion, animaciones):
        self.velocidad = velocidad
        super().__init__( tamaño, posicion, animaciones )

    # no si uso esto
    def saltar(self, plataforma):
        pass

    def verificar_colision_piso(self, lista_pisos):
        pass

    def verificar_colision_items(self, lista_items):
        pass

    def lanzar_proyectil(self, objetivo):# Objetivo es el personaje?
        pass