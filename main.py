from Classes.game import Game
import pygame

icon_img = pygame.image.load(r"Assets\Images\dragon-icon.png")
# game = Game((2400, 1300), 60, "Fantasy Adventure")
game = Game((1900, 1000), 60, "Fantasy Adventure",icon_img)

game.init() 