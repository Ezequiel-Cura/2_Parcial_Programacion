from Classes.Characters.Personaje import Personaje

class PersonajePrincipal(Personaje):
    def __init__(self, tamaño, posicion, animaciones):
        velocidad = 5
        potencia_salto = 25
        self.score = 0
        animaciones_res = Personaje.reescalar_imagenes(animaciones, tamaño[0], tamaño[1])

        super().__init__(velocidad, potencia_salto, tamaño, posicion, animaciones_res)


    def verificar_colision_enemigo(self, lista_enemigos):
        pass

    def verificar_accion(self, que_hizo):
        pass

    def verificar_eventos_personaje():
        pass