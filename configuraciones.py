import pygame
from Classes.Characters.Entidades import Entidades_Juego

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
]

dicc_animaciones_personaje = {
    "idle": personaje_idle,
    "run":personaje_run,
    "jump": personaje_salta,
    "attack":personaje_ataque
}

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
goblin_death = [
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Death\0.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Death\1.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Death\2.png"),
    pygame.image.load(r"Assets\Images\Enemys\Goblin\Death\3.png"),
    
]
dicc_animations_goblin = {
    "run": goblin_move,
    "attack": goblin_attack,
    "death": goblin_death
}
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

skeleton_death = [
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Death\0.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Death\1.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Death\2.png"),
    pygame.image.load(r"Assets\Images\Enemys\Skeleton\Death\3.png"),
]

dicc_animations_skeleton = {
    "run": skeleton_move,
    "attack": skeleton_attack,
    "death": skeleton_death
}

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

necro_death = [
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Death\0.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Death\1.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Death\2.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Death\3.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Death\4.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Death\5.png"),
    pygame.image.load(r"Assets\Images\Enemys\Necromancer\Death\6.png"),
]


dicc_animations_necro = {
    "run": necro_walk,
    "revive": necro_revive,
    "death": necro_death
    
}

necro_animation = [necro_walk, necro_revive]


#boss chuthullu
boss_idle = [
    pygame.image.load(r"Assets\Images\Boss\idle\idle_1.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_2.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_3.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_4.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_5.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_6.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_7.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_8.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_9.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_10.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_11.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_12.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_13.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_14.png"),
    pygame.image.load(r"Assets\Images\Boss\idle\idle_15.png"),
]
boss_move = [
    pygame.image.load(r"Assets\Images\Boss\walk\walk_1.png"),
    pygame.image.load(r"Assets\Images\Boss\walk\walk_2.png"),
    pygame.image.load(r"Assets\Images\Boss\walk\walk_3.png"),
    pygame.image.load(r"Assets\Images\Boss\walk\walk_4.png"),
    pygame.image.load(r"Assets\Images\Boss\walk\walk_5.png"),
    pygame.image.load(r"Assets\Images\Boss\walk\walk_6.png"),
    pygame.image.load(r"Assets\Images\Boss\walk\walk_7.png"),
    pygame.image.load(r"Assets\Images\Boss\walk\walk_8.png"),
    pygame.image.load(r"Assets\Images\Boss\walk\walk_9.png"),
    pygame.image.load(r"Assets\Images\Boss\walk\walk_10.png"),
    pygame.image.load(r"Assets\Images\Boss\walk\walk_11.png"),
    pygame.image.load(r"Assets\Images\Boss\walk\walk_12.png"),
]
boss_fly = [
    pygame.image.load(r"Assets\Images\Boss\fly\fly_1.png"),
    pygame.image.load(r"Assets\Images\Boss\fly\fly_2.png"),
    pygame.image.load(r"Assets\Images\Boss\fly\fly_3.png"),
    pygame.image.load(r"Assets\Images\Boss\fly\fly_4.png"),
    pygame.image.load(r"Assets\Images\Boss\fly\fly_5.png"),
    pygame.image.load(r"Assets\Images\Boss\fly\fly_6.png"),
]
boss_attack1 = [
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_1.png"),
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_2.png"),
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_3.png"),
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_4.png"),
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_5.png"),
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_6.png"),
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_7.png"),
]
boss_attack2 = [
    pygame.image.load(r"Assets\Images\Boss\2atk\2atk_1.png"),
    pygame.image.load(r"Assets\Images\Boss\2atk\2atk_2.png"),
    pygame.image.load(r"Assets\Images\Boss\2atk\2atk_3.png"),
    pygame.image.load(r"Assets\Images\Boss\2atk\2atk_4.png"),
    pygame.image.load(r"Assets\Images\Boss\2atk\2atk_5.png"),
    pygame.image.load(r"Assets\Images\Boss\2atk\2atk_6.png"),
    pygame.image.load(r"Assets\Images\Boss\2atk\2atk_7.png"),
    pygame.image.load(r"Assets\Images\Boss\2atk\2atk_8.png"),
    pygame.image.load(r"Assets\Images\Boss\2atk\2atk_9.png"),
]
boss_hurt = [
    pygame.image.load(r"Assets\Images\Boss\hurt\hurt_1.png"),
    pygame.image.load(r"Assets\Images\Boss\hurt\hurt_2.png"),
    pygame.image.load(r"Assets\Images\Boss\hurt\hurt_3.png"),
    pygame.image.load(r"Assets\Images\Boss\hurt\hurt_4.png"),
    pygame.image.load(r"Assets\Images\Boss\hurt\hurt_5.png"),

]
boss_death = [
    pygame.image.load(r"Assets\Images\Boss\death\death_1.png"),
    pygame.image.load(r"Assets\Images\Boss\death\death_2.png"),
    pygame.image.load(r"Assets\Images\Boss\death\death_3.png"),
    pygame.image.load(r"Assets\Images\Boss\death\death_4.png"),
    pygame.image.load(r"Assets\Images\Boss\death\death_5.png"),
    pygame.image.load(r"Assets\Images\Boss\death\death_6.png"),
    pygame.image.load(r"Assets\Images\Boss\death\death_7.png"),
    pygame.image.load(r"Assets\Images\Boss\death\death_8.png"),
    pygame.image.load(r"Assets\Images\Boss\death\death_9.png"),
    pygame.image.load(r"Assets\Images\Boss\death\death_10.png"),
    pygame.image.load(r"Assets\Images\Boss\death\death_11.png"),
]
boss_dash = [
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_1.png"),
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_2.png"),
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_3.png"),
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_4.png"),
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_5.png"),
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_6.png"),
    pygame.image.load(r"Assets\Images\Boss\1atk\1atk_7.png"),
]

dicc_animations_boss = {
    "idle": boss_idle,
    "run": boss_move,
    "fly": boss_fly,
    "dash": boss_dash,
    "death": boss_death
}

boss_animation = [boss_idle, boss_move, boss_fly, boss_attack1, boss_attack2]

boss_proyectile = [
    pygame.image.load(r"Assets\Images\Bullet\Boss bullet\PixelartFireBall-13.png"),
    pygame.image.load(r"Assets\Images\Bullet\Boss bullet\PixelartFireBall-14.png"),
    pygame.image.load(r"Assets\Images\Bullet\Boss bullet\PixelartFireBall-15.png"),
    pygame.image.load(r"Assets\Images\Bullet\Boss bullet\PixelartFireBall-16.png"),
    pygame.image.load(r"Assets\Images\Bullet\Boss bullet\PixelartFireBall-17.png"),
    pygame.image.load(r"Assets\Images\Bullet\Boss bullet\PixelartFireBall-18.png"),
]

boss_fire = [
    pygame.image.load(r"Assets\Images\Items\Fire\burning_loop_1.png"),
    pygame.image.load(r"Assets\Images\Items\Fire\burning_loop_2.png"),
    pygame.image.load(r"Assets\Images\Items\Fire\burning_loop_3.png"),
    pygame.image.load(r"Assets\Images\Items\Fire\burning_loop_4.png"),
    pygame.image.load(r"Assets\Images\Items\Fire\burning_loop_5.png"),
    pygame.image.load(r"Assets\Images\Items\Fire\burning_loop_6.png"),
    pygame.image.load(r"Assets\Images\Items\Fire\burning_loop_7.png"),

]

boss_fire = Entidades_Juego.reescalalar_imagenesa(boss_fire, 50,60)

# Items ----------------------------------------------------------------
coin_animation = [
    pygame.image.load(r"Assets\Images\Items\Coin\1.png"),
    pygame.image.load(r"Assets\Images\Items\Coin\2.png"),
    pygame.image.load(r"Assets\Images\Items\Coin\3.png"),
    pygame.image.load(r"Assets\Images\Items\Coin\4.png"),
    pygame.image.load(r"Assets\Images\Items\Coin\5.png"),
    pygame.image.load(r"Assets\Images\Items\Coin\6.png"),
]

heart_item = [
    pygame.image.load(r"Assets\Images\Items\Heart.png"),
    pygame.image.load(r"Assets\Images\Items\Heart.png"),
    pygame.image.load(r"Assets\Images\Items\Heart.png"),
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


# -------------------- AUDIO --------------------------------------------
pygame.mixer.init()

lose_audio = pygame.mixer.Sound(r"Assets\Music\Death.ogg")

victory_audio = pygame.mixer.Sound(r"Assets\Music\Victory.ogg")

music_ambiental_menu = pygame.mixer.Sound(r"Assets\Music\Ambient 1.mp3")

jump_audio = pygame.mixer.Sound(r"Assets\Music\30_Jump_03.wav")
attack_audio = pygame.mixer.Sound(r"Assets\Music\slash.mp3")
heal_audio = pygame.mixer.Sound(r"Assets\Music\02_Heal_02.wav")
fire_explosion_audio = pygame.mixer.Sound(r"Assets\Music\04_Fire_explosion_04_medium.wav")
coin_audio = pygame.mixer.Sound(r"Assets\Music\coin.mp3")
fly_audio = pygame.mixer.Sound(r"Assets\Music\flying.mp3")

level_3_music = pygame.mixer.Sound(r"Assets\Music\lvl3music.mp3")






sonido_off = pygame.image.load(r"Assets\UI\sonido_off.png")
sonido_on = pygame.image.load(r"Assets\UI\sonido_on.png")