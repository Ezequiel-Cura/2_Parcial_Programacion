import pygame


# Imagenes personaje principal----------------------------------------------------

# 0 = Idle_der, 1 = Idle_izq, 2 = Run_der, 3 = Run_izq, 4 = Jump_der, 5 = Jump_izq


# 0 = Idle_der, 1 = Run_der, 2 = Jump_der, 3 = attack_der
#   = Idle_izq,-1 = Run_izq, -2 = Jump_izq, -3 attack_izq

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
]
personaje_ataque = [
    pygame.image.load(r"Assets\Images\Personaje\Attack\0.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\1.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\2.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\3.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\4.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\5.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\6.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\7.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\8.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\9.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\10.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\11.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\12.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\13.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\14.png"),
    pygame.image.load(r"Assets\Images\Personaje\Attack\15.png"),

]

list_animaciones_personaje = [personaje_idle,personaje_run,personaje_salta,personaje_ataque]

# Proyectil


# proyectil_animation = [
#     pygame.image.load(r"Assets\Images\Bullet\02.png")
# ]

proyectil_animation = [
    pygame.image.load(r"Assets\Images\Bullet\bolt\bolt1.png"),
    pygame.image.load(r"Assets\Images\Bullet\bolt\bolt2.png"),
    pygame.image.load(r"Assets\Images\Bullet\bolt\bolt3.png"),
    pygame.image.load(r"Assets\Images\Bullet\bolt\bolt4.png"),
]



# Imagenes enemigos ---------------------------------------------------------------

#goblin

goblin_move = [
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Run\0.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Run\1.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Run\2.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Run\3.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Run\4.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Run\5.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Run\6.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Run\7.png"),
]
goblin_attack = [
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Attack\0.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Attack\1.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Attack\2.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Attack\3.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Attack\4.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Attack\5.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Attack\6.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Attack\7.png"),
]
goblin_animations = [goblin_move,goblin_attack]

#Skeleton
skeleton_move = [
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Run\0.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Run\1.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Run\2.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Run\3.png"),
]
skeleton_attack = [
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Attack\0.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Attack\1.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Attack\2.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Attack\3.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Attack\4.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Attack\5.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Attack\6.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Attack\7.png"),
]

skeleton_animation = [skeleton_move, skeleton_attack]

#mini boss necromancer
necro_walk = [
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Walk\0.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Walk\1.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Walk\2.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Walk\3.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Walk\4.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Walk\5.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Walk\6.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Walk\7.png"),
]

necro_revive = [
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\0.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\1.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\2.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\3.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\4.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\5.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\6.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\7.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\8.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\9.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\10.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\11.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Resurection\12.png"),
]

necro_animation = [necro_walk, necro_revive]


#boss chuthullu
boss_idle = []
boss_attack1 = []
boss_attack2 = []
boss_fly = []
boss_move = []

# Items ----------------------------------------------------------------
coin_animation = [
    pygame.image.load(r"Assets\Images\Items\Coin\1.png"),
    pygame.image.load(r"Assets\Images\Items\Coin\2.png"),
    pygame.image.load(r"Assets\Images\Items\Coin\3.png"),
    pygame.image.load(r"Assets\Images\Items\Coin\4.png"),
    pygame.image.load(r"Assets\Images\Items\Coin\5.png"),
    pygame.image.load(r"Assets\Images\Items\Coin\6.png"),
]

hp_surface = pygame.image.load(r"Assets\Images\Items\0.png")
hp_surface = pygame.transform.scale(hp_surface, ( 50,50))
heart_img = pygame.image.load(r"Assets\Images\Items\1.png")
heart_img = pygame.transform.scale(heart_img, ( 50,50))

#Imagenes de fondo ----------------------------------------------------------------

#lvl 1
bg_demon_forest = [     
    pygame.image.load("Assets/Images/Backgrounds/Forest/parallax-demon-woods-bg-0.png"),
    pygame.image.load("Assets/Images/Backgrounds/Forest/parallax-demon-woods-far-trees-1.png"),
    pygame.image.load("Assets/Images/Backgrounds/Forest/parallax-demon-woods-mid-trees-2.png"),
    pygame.image.load("Assets/Images/Backgrounds/Forest/parallax-demon-woods-close-trees-3.png"),
]

#lvl 2
bg_cave = [
    pygame.image.load(r"Assets\Images\Backgrounds\Cave\background1.png"),
    pygame.image.load(r"Assets\Images\Backgrounds\Cave\background2.png"),
    pygame.image.load(r"Assets\Images\Backgrounds\Cave\background3.png"),
    pygame.image.load(r"Assets\Images\Backgrounds\Cave\background4a.png"),
    pygame.image.load(r"Assets\Images\Backgrounds\Cave\background4b.png"),
]


#lvl 3
bg_space = [
    pygame.image.load(r"Assets\Images\Backgrounds\Space\parallax-space-backgound.png"),
    pygame.image.load(r"Assets\Images\Backgrounds\Space\parallax-space-stars.png"),
    pygame.image.load(r"Assets\Images\Backgrounds\Space\parallax-space-far-planets.png"),
    pygame.image.load(r"Assets\Images\Backgrounds\Space\parallax-space-big-planet.png"),
    pygame.image.load(r"Assets\Images\Backgrounds\Space\parallax-space-ring-planet.png"),
]
