import pygame


# Imagenes personaje principal----------------------------------------------------

# 0 = Idle_der, 1 = Idle_izq, 2 = Run_der, 3 = Run_izq, 4 = Jump_der, 5 = Jump_izq


# 0 = Idle_der, 1 = Run_der, 2 = Jump_der, 3 = attack_der
#   = Idle_izq,-1 = Run_izq, -2 = Jump_izq, -3 attack_izq
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
personaje_run = [
    pygame.image.load(r"Assets\Images\Personaje\Run\0.png"),
    pygame.image.load(r"Assets\Images\Personaje\Run\1.png"),
    pygame.image.load(r"Assets\Images\Personaje\Run\2.png"),
    pygame.image.load(r"Assets\Images\Personaje\Run\3.png"),
    pygame.image.load(r"Assets\Images\Personaje\Run\4.png"),
    pygame.image.load(r"Assets\Images\Personaje\Run\5.png"),
    pygame.image.load(r"Assets\Images\Personaje\Run\6.png"),
    pygame.image.load(r"Assets\Images\Personaje\Run\7.png"),
]
personaje_salta = [
    pygame.image.load(r"Assets\Images\Personaje\Jump\0.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\1.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\2.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\3.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\4.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\5.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\6.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\7.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\8.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\9.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\10.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\11.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\12.png"),
    pygame.image.load(r"Assets\Images\Personaje\Jump\13.png"),
]


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
