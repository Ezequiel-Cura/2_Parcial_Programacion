import pygame
from Classes.Niveles.Nivel_1 import Nivel_1
from Classes.Niveles.Nivel_2 import Nivel_2
from Classes.Niveles.Nivel_3 import Nivel_3



class Manejador_niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {
            "nivel_uno": Nivel_1,
            "nivel_dos": Nivel_2,
            "nivel_tres": Nivel_3
        }

    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)