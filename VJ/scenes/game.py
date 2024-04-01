'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

import pygame
from elements.bbullet import (RED, GREEN,BLUE,WHITE, bullet, bullet_mask)

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.jorge import Player
from elements.jorge import (mask_image, JorgePNG_mask)

from elements.bug import Enemy
from elements.bbullet import Bullet
pygame.display.set_caption("Jorge The Game")

def StartScene():
    ''' iniciamos los modulos de pygame'''

    pygame.init()
    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''
    SCREEN_WIDTH = 1000  # revisar ancho de la imagen de fondo
    SCREEN_HEIGHT = 700  # revisar alto de la imagen de fondo
    jorge = Player(350,350)
    bullet_game=Bullet()

    jorge_group=pygame.sprite.Group()
    bullet_group=pygame.sprite.Group()

    jorge_group.add(jorge)
    bullet_group.add(bullet_game)
    ''' 2.- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert()

    ''' Preparamos el gameloop '''
    ''' 1.- creamos el reloj del juego'''

    clock = pygame.time.Clock()
    ''' 2.- generador de enemigos'''

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    ''' hora de hacer el gameloop '''
    running = True

    while running: 
        if pygame.sprite.spritecollide(player, bullet_group,False):
            col=BLUE
            if pygame.sprite.spritecollide(player, bullet_group,False,pygame.sprite.collide_mask):
                col=RED
        else:
            col=GREEN
        pos=pygame.mouse.get_pos()
        screen.blit(background_image, [0, 0])
        bullet_group.update(col)
    
        bullet_group.draw(screen)
        pygame.draw.rect(screen, WHITE, jorge.rect,1)
        screen.blit(mask_image, (0,0))
        bullet.fill(col)
        screen.blit(bullet,pos)


        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        for entity in all_sprites:
            if isinstance(entity, Player):
                screen.blit(entity.image, entity.rect)
                pressed_keys = pygame.key.get_pressed()
                entity.update(pressed_keys)  # Actualizar posición del jugador
                entity.mask = pygame.mask.from_surface(entity.image)
            elif isinstance(entity, Enemy):
                screen.blit(entity.image, entity.rect)
                entity.mask = pygame.mask.from_surface(entity.image)
        for enemy in enemies:
            enemy.update()
            enemy.mask = pygame.mask.from_surface(enemy.image)
        if pygame.sprite.spritecollide(player, enemies,False):
            col=BLUE
            if pygame.sprite.spritecollide(player, enemies,False, pygame.sprite.collide_mask):
                player.kill()
                running=False
        
        clock.tick(40)
        enemies.update()
        pygame.display.flip()
        