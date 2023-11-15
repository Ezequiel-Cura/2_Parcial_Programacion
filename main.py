from Classes.game import Game
import ctypes
import math

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(round(ancho,1), round(alto,1))

game = Game((2400, 1300), 60, "Fantasy Adventure")


game.init()


