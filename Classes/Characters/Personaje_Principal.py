from Classes.Characters.Personaje import Personaje

class PersonajePrincipal(Personaje):
    def __init__(self, tamaño, posicion, animaciones):
        velocidad = 10
        potencia_salto = 20
        self.score = 0
        
        
        super().__init__(velocidad, potencia_salto, tamaño, posicion, animaciones)


    def verificar_colision_enemigo(self, lista_enemigos):
        pass

    def verificar_accion(self, que_hizo):
        pass

    def verificar_eventos_personaje():
        pass