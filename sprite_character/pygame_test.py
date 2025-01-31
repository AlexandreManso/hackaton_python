import time
import pygame as pg
from pygame.locals import *

pg.init()

#Ouverture de la fenêtre Pygame
fenetre = pg.display.set_mode((320, 240))
clock=pg.time.Clock()

#Chargement et collage du fond
fond = pg.image.load("gts.png").convert()
fenetre.blit(fond, (0,0))

#perso
perso = pg.image.load("001_0.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pg.display.flip()

#BOUCLE INFINIE
continuer = 1
deplacement=None
step=0
state_d=-1
state_u=-1
state_l=-1
state_r=-1
state=[state_d, state_r, state_l, state_u]

sprite_d=["001_0.png","001_1.png","001_2.png","001_3.png"]
sprite_r=["001_8.png","001_9.png","001_10.png","001_11.png"]
sprite_l=["001_4.png","001_5.png","001_6.png","001_7.png"]
sprite_u=["001_12.png","001_13.png","001_14.png","001_15.png"]


while continuer:
    clock.tick(10)
    print('boucle')
    deplacement=None
    step=0
    for event in pg.event.get():
        if event.type == QUIT:
            continuer=0
        if event.type == KEYDOWN:
            if event.key == K_SPACE: 
                print('aaa')
            if event.key == K_DOWN:
                state_d=3
            if event.key == K_UP:
                state_u=3
            if event.key == K_LEFT:
                state_l=3
            if event.key == K_RIGHT:
                state_r=3

    if state_l>-1:
        position_perso = position_perso.move(-3,0)           
        fenetre.blit(fond, (0,0))
        perso = pg.image.load(sprite_l[state_l]).convert_alpha()
        fenetre.blit(perso, position_perso)
        pg.display.flip()
        state_l=state_l-1
        
    elif state_u>-1:
        position_perso = position_perso.move(0,-3)           
        fenetre.blit(fond, (0,0))
        perso = pg.image.load(sprite_u[state_u]).convert_alpha()
        fenetre.blit(perso, position_perso)
        pg.display.flip()
        state_u=state_u-1
        
    elif state_d>-1:
        position_perso = position_perso.move(0,3)           
        fenetre.blit(fond, (0,0))
        perso = pg.image.load(sprite_d[state_d]).convert_alpha()
        fenetre.blit(perso, position_perso)
        pg.display.flip()
        state_d=state_d-1
        
    elif state_r>-1:
        position_perso = position_perso.move(3,0)           
        fenetre.blit(fond, (0,0))
        perso = pg.image.load(sprite_r[state_r]).convert_alpha()
        fenetre.blit(perso, position_perso)
        pg.display.flip()
        state_r=state_r-1
    
    pg.key.set_repeat(400, 30)
    
    # pg.key.set_repeat(400, 30)            
    # fenetre.blit(fond, (0,0))
    # fenetre.blit(perso, position_perso)
    # pg.display.flip()