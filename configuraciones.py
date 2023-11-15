import pygame


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


# Imagenes personaje principal----------------------------------------------------

dicc_animaciones = {}

# personaje_idle = [pygame.image.load("/Assets/Images/Personajes/Idle/")]
personaje_run = []
personaje_salta = []


# Imagenes enemigos ---------------------------------------------------------------

#goblin
goblin_move = []
goblin_attack = []

#Skeleton
skeleton_move = []
skeleton_attack = []

#boss chuthullu
boss_idle = []
boss_attack1 = []
boss_attack2 = []
boss_fly = []
boss_move = []

#Imagenes de fondo ----------------------------------------------------------------

#lvl 1
bg_demon_forest = [     
    pygame.image.load("Assets/Images/Backgrounds/Forest/parallax-demon-woods-bg-0.png"),
    pygame.image.load("Assets/Images/Backgrounds/Forest/parallax-demon-woods-far-trees-1.png"),
    pygame.image.load("Assets/Images/Backgrounds/Forest/parallax-demon-woods-mid-trees-2.png"),
    pygame.image.load("Assets/Images/Backgrounds/Forest/parallax-demon-woods-close-trees-3.png"),
]

#lvl 2
bg_cave = []

#lvl 3
