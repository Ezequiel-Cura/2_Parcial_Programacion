import pygame


# Imagenes personaje principal----------------------------------------------------

# 0 = Idle_der, 1 = Idle_izq, 2 = Run_der, 3 = Run_izq, 4 = Jump_der, 5 = Jump_izq
list_animaciones_personaje = []

personaje_idle = [       
    pygame.image.load(r"Assets\Images\Personaje\Idle\0.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\1.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\2.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\3.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\4.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\5.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\6.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\7.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\8.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\9.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\10.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\11.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\12.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\13.png"),
    pygame.image.load(r"Assets\Images\Personaje\Idle\14.png"),
]
personaje_run = []
personaje_salta = []


list_animaciones_personaje.append(personaje_idle)
list_animaciones_personaje.append(personaje_run)
list_animaciones_personaje.append(personaje_salta)

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
